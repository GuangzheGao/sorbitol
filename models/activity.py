
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Table,  ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from utils.db import mysql_engine, mysql_session
from datetime import datetime
from models.base import Base
from models.user import User


class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer) #who conducted the activity
    board_id = Column(Integer)
    content = Column(String(512))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    @classmethod
    def add(cls, board_id, user_id, content):
        activity = cls(board_id = board_id, user_id = user_id, content = content)
        try:
            mysql_session.add(activity)
            mysql_session.commit()
        except Exception as e:
            mysql_session.rollback()
            print "error in mysql commit:", e
            raise
        finally:
            mysql_session.close()

        return activity.id
        #return activity.created_at #note for activity we don't care id, but time!

    @classmethod
    def get(cls, activity_id):
        activity_id = long(activity_id)
        activity = mysql_session.query(cls).filter_by(id = activity_id).first()
        return activity

    @classmethod
    def get_all(cls, board_id):
        activities = mysql_session.query(cls).filter_by(board_id = board_id)
        return activities

    @classmethod
    def get_all_by_user(cls,user_id):
        activities = mysql_session.query(cls).filter_by(user_id = user_id)
        return activities