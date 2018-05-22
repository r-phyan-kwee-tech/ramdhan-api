#! usr/bin/python
# -*- coding: utf-8 -*-
import os
from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_basicauth import BasicAuth
from flask_cors import CORS
from flask_graphql import GraphQLView
from werkzeug.routing import BaseConverter
from werkzeug.utils import redirect

from database import db_session, Base as model_base, engine
from schema import schema
from seeds import gen_seeds
from sheet_fetch import SheetFetch

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OR, the same with increased verbosity:
load_dotenv(dotenv_path, verbose=True)

app = Flask(__name__)
CORS(app)

app.config['BASIC_AUTH_USERNAME'] = os.environ['BASIC_AUTH_USER_NAME']
app.config['BASIC_AUTH_PASSWORD'] = os.environ['BASIC_AUTH_PASSWORD']
basic_auth = BasicAuth(app)

if os.environ["ENV"] != 'production':
    app.debug = True
    app.add_url_rule('/api', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True,
                                                           context={'session': db_session}))
else:
    app.debug = False
    app.add_url_rule('/api', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=False,
                                                           context={'session': db_session}))

    app.add_url_rule('/sandbox', view_func=GraphQLView.as_view('sandbox', schema=schema, graphiql=True,
                                                               context={'session': db_session}))


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def index():
    return redirect('notfound.html')
    # return "Click here to to go to <a href='/api'> /api</a>"


@app.route('/fetch/<country_id>')
@basic_auth.required
def fetch(country_id):
    status = SheetFetch().fetch(country_id)
    return jsonify({"fetch_status": status})


@app.route('/scrap/<source_id>/<issuenumber>')
def scrap(source_id, issuenumber, context=db_session):
    return jsonify({"status": 200, "msg": "issue already exists"})


if __name__ == "__main__":
    exists = engine.dialect.has_table(engine.connect(), "country")

    if exists is False:
        model_base.metadata.create_all(engine)
        gen_seeds()
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
