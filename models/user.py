# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from utils.db import mysql_engine, mysql_session
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import re

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    username = Column(String(200))
    password = Column(String(200))
    email = Column(String(200))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    @classmethod
    def get(cls, user_id):
        '''warning: unsafe method, get user obj deirectly without checking password'''
        user_id = int(user_id)
        user = mysql_session.query(cls).filter_by(id = user_id).first()
        return user

    @classmethod
    def get_validate_user(cls, user_email, user_unsafe_password):
        user = mysql_session.query(cls).filter_by(email = user_email).first()
        user.id = int(user.id)
        
        if not user:
            return None
        
        if user.check_password(user_unsafe_password):
            return user
        else:
            return None

    @classmethod
    def check_password_format(cls, password):
        return len(password) in range(6, 121) and re.match(r'[\w]*$', password)

    @classmethod
    def register(cls, username, unsafe_password, user_email):
        safe_password = generate_password_hash(unsafe_password)
        user = User(username = username,
                    password = safe_password, 
                    email = user_email)
        mysql_session.add(user)
        try:
            mysql_session.commit()
        except Exception as e:
            mysql_session.flush()
            print e

        return user.id
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anoymous(self):
        return False

    def get_id(self):
        return int(self.id)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

User.query = mysql_session.query(User)
