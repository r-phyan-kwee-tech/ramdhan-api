import calendar
import datetime
from time import strftime, gmtime

import os
from dotenv import load_dotenv
from os.path import join, dirname
from sqlalchemy import Column, Integer, Text, String, ForeignKey, BIGINT, VARCHAR, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

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
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=True,
#                                          bind=engine))


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


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)
    username = Column(String(255))


class Country(Base):
    __tablename__ = 'country'
    id = Column(String(50), primary_key=True, index=True)
    object_id = Column(String(50), unique=True, index=True)
    name = Column(VARCHAR(100), unique=True)
    state = relationship("State", uselist=True)
    # article = relationship("Article", back_populates="source")

    created_date = Column(BIGINT(), default=calendar.timegm(datetime.datetime.utcnow().utctimetuple()))
    updated_date = Column(BIGINT(), default=calendar.timegm(datetime.datetime.utcnow().utctimetuple()))


class State(Base):
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


class Day(Base):
    __tablename__ = 'day'
    id = Column(String(50), primary_key=True, index=True)
    object_id = Column(String(50), unique=True, index=True)
    day = Column(Integer())
    if os.environ["ENV"] == 'production':
        day_mm = Column(String(10, collation="utf8mb4_myanmar_ci", convert_unicode=True))
    else:
        day_mm = Column(String(10))

    calendar_day = Column(String(30), default=str(strftime("%a, %d %b %Y %X +0000", gmtime())))
    hijari_day = Column(String(30), default=str(strftime("%a, %d %b %Y %X +0000", gmtime())))

    sehri_time_desc = Column(String(30))
    iftari_time_desc = Column(String(30))
    sehri_time_desc_mm_uni = Column(String(30,collation="utf8mb4_myanmar_ci",convert_unicode=True))
    sehri_time_desc_mm_zawgyi = Column(String(30,collation="utf8mb4_myanmar_ci",convert_unicode=True))
    iftari_time_desc_mm_zawgyi = Column(String(30,collation="utf8mb4_myanmar_ci",convert_unicode=True))
    iftari_time_desc_mm_uni = Column(String(30,collation="utf8mb4_myanmar_ci",convert_unicode=True))

    sehri_time = Column(String(30), default=str("4:30 am"))
    iftari_time = Column(String(30), default=str("7:30 pm"))

    is_kadir = Column(Boolean, default=False)

    country_id = Column(String(255), ForeignKey("country.object_id"))
    state_id = Column(String(255), ForeignKey("state.object_id"))
    created_date = Column(BIGINT(), default=calendar.timegm(datetime.datetime.utcnow().utctimetuple()))
    # updated_date = Column(String(50), default=str(strftime("%a, %d %b %Y %X +0000", gmtime())))
    updated_date = Column(BIGINT(), default=calendar.timegm(datetime.datetime.utcnow().utctimetuple()))
