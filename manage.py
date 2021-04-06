import calendar
import datetime
import os
from os.path import join, dirname
from time import strftime, gmtime

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, BIGINT, VARCHAR, Boolean, Text
from sqlalchemy.orm import relationship

from seeds import gen_seeds

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
# OR, the same with increased verbosity:
from database import engine

app.config['SQLALCHEMY_DATABASE_URI'] = str(engine.url)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)





class Country(db.Model):
    __tablename__ = 'country'
    id = Column(String(50), primary_key=True, index=True)
    object_id = Column(String(50), unique=True, index=True)
    name = Column(VARCHAR(100), unique=True)
    state = relationship("State", uselist=True)
    # article = relationship("Article", back_populates="source")
    remark = Column(String(50))
    created_date = Column(BIGINT(), default=calendar.timegm(datetime.datetime.utcnow().utctimetuple()))
    updated_date = Column(BIGINT(), default=calendar.timegm(datetime.datetime.utcnow().utctimetuple()))


class State(db.Model):
    __tablename__ = 'state'
    id = Column(String(50), primary_key=True, index=True)
    object_id = Column(String(50), unique=True, index=True)
    if os.environ["ENV"] == 'production':
        name_mm_uni = Column(String(50, collation='utf8mb4_myanmar_ci', convert_unicode=True))
        name_mm_zawgyi = Column(String(50, collation='utf8mb4_myanmar_ci', convert_unicode=True))
    else:
        name_mm_uni = Column(String(50))
        name_mm_zawgyi = Column(String(50))

    country_id = Column(String(255), ForeignKey("country.object_id"))

    day = relationship("Day", uselist=True)
    created_date = Column(BIGINT(), default=calendar.timegm(datetime.datetime.utcnow().utctimetuple()))
    updated_date = Column(BIGINT(), default=calendar.timegm(datetime.datetime.utcnow().utctimetuple()))


class Day(db.Model):
    __tablename__ = 'day'
    id = Column(String(50), primary_key=True, index=True)
    object_id = Column(String(50), unique=True, index=True)
    day = Column(Integer())
    if os.environ["ENV"] == 'production':
        day_mm = Column(String(10, collation="utf8mb4_myanmar_ci", convert_unicode=True))
        sehri_time_desc_mm_uni = Column(String(30, collation="utf8mb4_myanmar_ci", convert_unicode=True))
        sehri_time_desc_mm_zawgyi = Column(String(30, collation="utf8mb4_myanmar_ci", convert_unicode=True))
        iftari_time_desc_mm_zawgyi = Column(String(30, collation="utf8mb4_myanmar_ci", convert_unicode=True))
        iftari_time_desc_mm_uni = Column(String(30, collation="utf8mb4_myanmar_ci", convert_unicode=True))
        dua_mm_uni = Column(String(2000, collation="utf8mb4_myanmar_ci", convert_unicode=True))
        dua_mm_zawgyi = Column(String(2000, collation="utf8mb4_myanmar_ci", convert_unicode=True))
        dua_ar = Column(String(1000, collation="utf8_general_ci", convert_unicode=True))

    else:
        day_mm = Column(String(10))
        sehri_time_desc_mm_uni = Column(String(30))
        sehri_time_desc_mm_zawgyi = Column(String(30))
        iftari_time_desc_mm_zawgyi = Column(String(30))
        iftari_time_desc_mm_uni = Column(String(30))
        dua_ar = Column(String(1000))
        dua_mm_uni = Column(String(2000))
        dua_mm_zawgyi = Column(String(2000))

    calendar_day = Column(String(30), default=str(strftime("%a, %d %b %Y %X +0000", gmtime())))
    hijari_day = Column(String(30), default=str(strftime("%a, %d %b %Y %X +0000", gmtime())))

    sehri_time_desc = Column(String(30))
    iftari_time_desc = Column(String(30))

    dua_en = Column(String(1000))

    sehri_time = Column(String(30), default=str("4:30 am"))
    iftari_time = Column(String(30), default=str("7:30 pm"))

    is_kadir = Column(Boolean, default=False)

    country_id = Column(String(255), ForeignKey("country.object_id"),index=True)
    state_id = Column(String(255), ForeignKey("state.object_id"),index=True)
    created_date = Column(BIGINT(), default=calendar.timegm(datetime.datetime.utcnow().utctimetuple()))
    # updated_date = Column(String(50), default=str(strftime("%a, %d %b %Y %X +0000", gmtime())))
    updated_date = Column(BIGINT(), default=calendar.timegm(datetime.datetime.utcnow().utctimetuple()))


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
