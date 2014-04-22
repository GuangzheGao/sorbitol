# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Table, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from utils.db import mysql_engine, mysql_session
from datetime import datetime
from models.base import Base
from models.card import Card

class List(Base):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key = True)
    title = Column(String(512))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    board_id = Column(Integer)

    #helper to jsonify when called
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id' : self.id,
           'board_id' : self.board_id,
           'title' : self.title
           #'created_at' : self.created_at
       }

    @classmethod
    def add(cls, board_id, title):
        _list = cls(board_id = board_id, title = title)
        try:
            mysql_session.add(_list)
            mysql_session.commit()
        except Exception as e:
            mysql_session.rollback()
            raise
            print "error in mysql commit:", e
        finally:
            mysql_session.close()
        return _list.id

    @classmethod
    def get(cls, list_id):
        list_id = long(list_id)
        _list = mysql_session.query(cls).filter_by(id = list_id).first()
        return _list

    @classmethod
    def get_lists_by_board_id(cls, board_id):
        board_id = long(board_id)
        lists = mysql_session.query(cls).filter_by(board_id = board_id).all()
        return lists

    @classmethod
    def get_multi(cls, ids):
        return [cls.get(id) for id in ids]

    def get_cards(self):
        return Card.get_cards_by_list_id(self.id)
