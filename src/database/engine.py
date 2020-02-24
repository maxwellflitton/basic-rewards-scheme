"""
taken from:
https://leportella.com/english/2019/01/10/sqlalchemy-basics-tutorial.html
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import GlobalParams

params = GlobalParams()
# this creates the connection for the database
engine = create_engine(params.get("DB_URL"), echo=True)

# this creates the middle ground between python objects we deal with in python and the engine that communicates
# with the database
Session = sessionmaker(bind=engine)

# sessions will talk to tables but the engine will be implementing things on the DB
session = Session()

Base = declarative_base()


if __name__ == "__main__":
    pass
