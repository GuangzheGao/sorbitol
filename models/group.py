# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Table, ForeignKey
from sqlalchemy.orm import relationship, backref
from utils.db import mysql_engine, mysql_session, r_server
from datetime import datetime
from models.base import Base
from models.user import User
from models.board import Board

'''
group_member_table = Table('group_member', Base.metadata,
                            Column('group_id', Integer, ForeignKey('groups.id')),
                            Column('member_id', Integer, ForeignKey('users.id')))
'''

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key = True)
    title = Column(String(512))
    description = Column(String(512))
    created_at = Column(TIMESTAMP, default = datetime.utcnow)

    '''
    members = relationship(User,
                           backref="groups",
                           secondary=group_member_table)
    '''

    @classmethod
    def add(cls, title, description):
        group = cls(title = title, description = description)
        try:
            mysql_session.add(group)
            mysql_session.commit()
        except Exception as e:
            mysql_session.flush()
            print "error in mysql commit:", e

        return group.id

    @classmethod
    def get(cls, group_id):
        group_id = long(group_id)
        group = mysql_session.query(cls).filter_by(id = group_id).first()
        return group



    @classmethod
    def get_multi(cls, ids):
        return [cls.get(id) for id in ids]

    def get_user_ids(self):
        print "users for group %d" % self.id, r_server.lrange('/group/%d/users' % self.id, 0, -1)
        return r_server.lrange('/group/%d/users' % self.id, 0, -1)

    def get_users(self):
        '''return a list of user objs'''
        return User.get_multi(self.get_user_ids())

    def add_user(self, user):
        r_server.rpush('/group/%d/users' % self.id, user.id)

    def get_boards(self):
        '''return a list of board objs'''
        return Board.get_boards_by_group_id(self.id)

    '''
    def get_members(self):
        #return a list of user objs
        return self.members

    def add_member(self, user):
        self.members.append(user)
        try:
            mysql_session.add(user)
            mysql_session.commit()
        except Exception as e:
            mysql_session.flush()
            print "error in mysql commit:", e
    '''