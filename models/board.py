# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Table,  ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from utils.db import mysql_engine, mysql_session, r_server
from datetime import datetime
from models.base import Base
from models.list import List
from models.user import User

class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key = True)
    #group_id = Column(Integer, primary_key = True)
    title = Column(String(512))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    visibility = Column(String(1))

    @classmethod
    def add(cls, title, visibility, ): #no group_id for now
        board = cls(title = title, visibility = visibility) #no group_id = group_id
        try:
            mysql_session.add(board)
            mysql_session.commit()
        except Exception as e:
            mysql_session.rollback()
            print "error in mysql commit:", e
            raise
        finally:
            mysql_session.close()

        return board.id

    @classmethod
    def get(cls, board_id):
        board_id = long(board_id)
        board = mysql_session.query(cls).filter_by(id = board_id).first()
        return board

    '''
    @classmethod
    def get_boards_by_group_id(cls, group_id):
        group_id = long(group_id)
        boards = mysql_session.query(cls).filter_by(group_id = group_id).all()
        return boards
    '''

    @classmethod
    def get_multi(cls, ids):
        return [cls.get(id) for id in ids]

    def get_user_ids(self):
        #print "users for board %d" % self.id, r_server.lrange('/board/%d/users' % self.id, 0, -1)
        #return r_server.lrange('/board/%d/users' % self.id, 0, -1)
        return r_server.smembers('/board/%d/users' % self.id)

    def get_users(self):
        '''return a list of user objs'''
        return User.get_multi(self.get_user_ids())       

    def add_user(self, user):
        #r_server.rpush('/board/%d/users' % self.id, user.id)
        return r_server.sadd('/board/%d/users' % self.id, user.id)

    def get_lists(self):
        '''return a list of user objs'''
        return List.get_lists_by_board_id(self.id)
