# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Table, ForeignKey
from sqlalchemy.orm import relationship, backref
from utils.db import mysql_engine, mysql_session
from datetime import datetime
from models.base import Base
from models.user import User

group_member_table = Table('group_member', Base.metadata,
                            Column('group_id', Integer, ForeignKey('groups.id')),
                            Column('member_id', Integer, ForeignKey('users.id')))

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key = True)
    name = Column(String(512))
    created_at = Column(TIMESTAMP, default = datetime.utcnow)
    members = relationship(User, 
                           backref="groups", 
                           secondary=group_member_table)

    @classmethod
    def add(cls, name):
        group = cls(name = name)
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
    
    def get_members(self):
        '''return a list of user objs'''
        return self.members

    def add_member(self, user):
        self.members.append(user)
        try:
            mysql_session.add(user)
            mysql_session.commit()
        except Exception as e:
            mysql_session.flush()
            print "error in mysql commit:", e

