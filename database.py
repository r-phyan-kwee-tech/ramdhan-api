import os
from os.path import join, dirname

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OR, the same with increased verbosity:
load_dotenv(dotenv_path, verbose=True)

url = os.environ["DB_URL_FORMAT"]
url = url.format(os.environ["DB_USER_NAME"], os.environ["DB_PASSWORD"], os.environ["DB_HOST"], os.environ["DB_PORT"],
                 os.environ["DB_NAME"])

# Replace 'sqlite:///rfg.db' with your path to database
if os.environ["ENV"] != 'production':
    engine = create_engine('sqlite:///ramdan.db', convert_unicode=True)
else:
    engine = create_engine(url)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def gen_offset_from_page(page, limit):
    page = int(page)
    limit = int(limit)
    if page is 0:
        page = 1
    return (page * limit) - limit


def generate_meta(limit, page, total_items):
    """
    This method help to generate links and metadata object
    :param table_view_name:
    :param limit:
    :param page:
    :param page_count:
    :return:
    """
    meta_object = {}
    total_count = len(total_items) if len(total_items) is not 0 else 0
    total_pages = total_count / limit
    modulus = total_count % limit
    import re
    total_pages = int(re.sub(r"\.\d+$", '', str(total_pages))) + 1 if modulus is not 0 else total_pages
    meta_object["current"] = page
    meta_object["total_page"] = total_pages
    if total_pages > page:
        meta_object["next_page"] = page + 1
        meta_object["prev_page"] = None if page - 1 is 0 else page - 1
    else:
        meta_object["next_page"] = None
        meta_object["prev_page"] = page - 1

    return meta_object
