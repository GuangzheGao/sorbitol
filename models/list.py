
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Table, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from utils.db import mysql_engine, mysql_session
from datetime import datetime
from models.base import Base
from models.card import Card

class List(Base):
    __tablename__ = 'lists'
    cards = relationship(Card, backref="lists") #one to many

    id = Column(Integer, primary_key = True)
    board_id = Column(Integer, ForeignKey('boards.id'))
    title = Column(String(512))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

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
        list = cls(board_id = board_id, title = title)
        try:
            mysql_session.add(list)
            mysql_session.commit()
        except Exception as e:
            mysql_session.flush()
            print "error in mysql commit:", e

        print "!!!~+~++~++~+~+~:"
        print list.id
        return list.id

    @classmethod
    def get(cls, list_id):
        list_id = long(list_id)
        list = mysql_session.query(cls).filter_by(id = list_id).first()
        return list

    @classmethod
    def get_all(cls, board_id):
        board_id = long(board_id)
        lists = mysql_session.query(cls).filter_by(board_id = board_id).all()
        return lists