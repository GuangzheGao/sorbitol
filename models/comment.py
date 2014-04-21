
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Table,  ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from utils.db import mysql_engine, mysql_session
from datetime import datetime
from models.base import Base
from models.user import User


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey('cards.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String(512))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    @classmethod
    def add(cls, card_id, user_id, content):
        comment = cls(card_id = card_id, user_id = user_id, content = content)
        try:
            mysql_session.add(comment)
            mysql_session.commit()
        except Exception as e:
            mysql_session.flush()
            print "error in mysql commit:", e

        return comment.id

    @classmethod
    def get(cls, comment_id):
        comment_id = long(comment_id)
        comment = mysql_session.query(cls).filter_by(id = comment_id).first()
        return comment

    @classmethod
    def get_all(cls, card_id):
        card_id = long(card_id)
        comments = mysql_session.query(cls).filter_by(card_id = card_id)
        return comments
