from utils.db import mysql_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(bind=mysql_engine)
