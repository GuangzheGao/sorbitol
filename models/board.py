
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Table,  ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from utils.db import mysql_engine, mysql_session
from datetime import datetime
from models.base import Base
from models.list import List
from models.user import User


user_board_table = Table('user_board', Base.metadata,
                            Column('board_id', Integer, ForeignKey('boards.id')),
                            Column('user_id', Integer, ForeignKey('users.id')))

class Board(Base):
    __tablename__ = 'boards'
    lists = relationship(List, backref="boards") #one to many

    id = Column(Integer, primary_key = True)
    title = Column(String(512))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    visibility = Column(String(1))
    users = relationship(User,
                           backref="boards",
                           secondary=user_board_table) #many to many

    @classmethod
    def add(cls, title, visibility):
        board = cls(title = title, visibility = visibility)
        try:
            mysql_session.add(board)
            mysql_session.commit()
        except Exception as e:
            mysql_session.flush()
            print "error in mysql commit:", e

        return list.id

    @classmethod
    def get(cls, board_id):
        board_id = long(board_id)
        board = mysql_session.query(cls).filter_by(id = board_id).first()
        return board

    @classmethod
    def get_all(cls, user_id):
        #need to use intermediate table
        return None

    def get_users(self):
        '''return a list of user objs'''
        #print mysql_session.query(self.users).filter_by(board_id = self.id).all()
        user_id_list =  mysql_session.query(user_board_table).filter_by(board_id = self.id).all()
        ret_id_name_pair = []
        for row_user in user_id_list:
            dict_pair = dict()
            user_row = mysql_session.query(User).filter_by(id = row_user.user_id).first()
            dict_pair["id"] = user_row.id
            dict_pair["name"] = user_row.username
            ret_id_name_pair.append(dict_pair)
        return ret_id_name_pair #list of id, name pairs

    def add_user(self, user):
        self.users.append(user)
        try:
            mysql_session.add(user)
            mysql_session.commit()
        except Exception as e:
            mysql_session.flush()
            print "error in mysql commit:", e
