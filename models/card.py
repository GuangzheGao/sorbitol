# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Table,  ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from utils.db import mysql_engine, mysql_session, r_server
from datetime import datetime
from models.base import Base
from models.user import User
from models.comment import Comment

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key = True)
    list_id = Column(Integer)
    title = Column(String(512))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    #helper to jsonify when called
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id' : self.id,
           'list_id' : self.list_id,
           'title' : self.title,
           'created_at' : self.created_at,
           'labels' : self.get_labels(),
           'users' : self.get_users()
       }

    @classmethod
    def add(cls, title, list_id, user_id):
        card = cls(title = title, list_id = list_id)
        try:
            mysql_session.add(card)
            mysql_session.commit()
        except Exception as e:
            mysql_session.rollback()
            print "error in mysql commit:", e
            raise
        finally:
            mysql_session.close()
        
        user = User.get(user_id)
        card.add_user(user)
        return card.id

    @classmethod
    def get(cls, card_id):
        card_id = long(card_id)
        card = mysql_session.query(cls).filter_by(id = card_id).first()
        return card

    @classmethod
    def get_cards_by_list_id(cls, list_id):
        list_id = long(list_id)
        cards = mysql_session.query(cls).filter_by(list_id = list_id).all()
        return cards

    def get_user_ids(self):
        '''return a list of user objs'''
        return r_server.lrange('/card/%d/users' % self.id, 0, -1)

    def add_user(self, user):
        r_server.rpush('/card/%d/users' % self.id, user.id)

    def get_labels(self):
        '''return a list of label string'''
        return r_server.lrange('/card/%d/labels' % self.id, 0, -1)

    def add_label(self, label_id, label_str):
        r_server.rpush('/card/%d/labels/%d' % (self.id, label_id), label_str)
    
    @classmethod
    def incr_comment(cls, card_id):
        r_server.incr('/card/%d/comment/count' % (card_id))

    @classmethod
    def decr_comment(cls, card_id):
        r_server.decr('/card/%d/comment/count' % (card_id))

    def get_comment_count(self):
        count = r_server.get('/card/%d/comment/count' % self.id)
        if count == None:
            return 0
        else:
            return count

    def get_description(self):
        return r_server.get('/card/%d/desc' % self.id)

    def set_description(self, desc):
        r_server.set('/card/%d/desc' % self.id, desc)
