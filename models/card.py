
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Table,  ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from utils.db import mysql_engine, mysql_session
from datetime import datetime
from models.base import Base
from models.user import User
from models.comment import Comment

user_card_table = Table('user_card', Base.metadata,
                            Column('card_id', Integer, ForeignKey('cards.id')),
                            Column('user_id', Integer, ForeignKey('users.id')))

class Card(Base):
    __tablename__ = 'cards'
    comments = relationship(Comment, backref="Cards") #one to many

    id = Column(Integer, primary_key = True)
    list_id = Column(Integer, ForeignKey('lists.id'))
    title = Column(String(512))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    labels = Column(Integer)
    users = relationship(User,
                           backref="cards",
                           secondary=user_card_table)

    #helper to jsonify when called
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id' : self.id,
           'list_id' : self.list_id,
           'title' : self.title,
           'created_at' : self.created_at,
            'labels' : self.labels
       }

    @classmethod
    def add(cls, name,  list_id, labels):
        card = cls(title = name, list_id = list_id, labels = labels)
        try:
            mysql_session.add(card)
            mysql_session.commit()
        except Exception as e:
            mysql_session.flush()
            print "error in mysql commit:", e

        return card.id

    @classmethod
    def get(cls, card_id):
        card_id = long(card_id)
        card = mysql_session.query(cls).filter_by(id = card_id).first()
        return card

    @classmethod
    def get_all(cls, list_id):
        list_id = long(list_id)
        cards = mysql_session.query(cls).filter_by(list_id = list_id).all()
        return cards

    def get_users(self):
        '''return a list of user objs'''
        return self.users

    def add_user(self, user):
        self.users.append(user)
        try:
            mysql_session.add(user)
            mysql_session.commit()
        except Exception as e:
            mysql_session.flush()
            print "error in mysql commit:", e