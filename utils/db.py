# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

mongo_client = MongoClient()
mysql_engine = create_engine(
                 'mysql://root:password@localhost/sorbitol?charset=utf8',
                 echo=False)
mysql_session = sessionmaker(bind=mysql_engine)()

