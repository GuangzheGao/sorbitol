# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, TIMESTAMP
from utils.db import mysql_engine, mysql_session, r_server
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import re
from models.base import Base

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
        user_id = long(user_id)
        user = mysql_session.query(cls).filter_by(id=user_id).first()
        return user

    @classmethod
    def get_multi(cls, ids):
        return [cls.get(id) for id in ids]

    @classmethod
    def get_validate_user(cls, user_email, user_unsafe_password):
        user = mysql_session.query(cls).filter_by(email=user_email).first()
        
        if not user:
            return None
        
        user.id = long(user.id)
        if user.check_password(user_unsafe_password):
            return user
        else:
            return None

    @classmethod
    def check_password_format(cls, password):
        return len(password) in range(6, 121) and re.match(r'[\w]*$', password)

    @classmethod
    def signup(cls, username, unsafe_password, user_email):
        return cls.add(username, unsafe_password, user_email)

    @classmethod
    def add(cls, username, unsafe_password, user_email):
        safe_password = generate_password_hash(unsafe_password)
        user = User(username=username,
                    password=safe_password, 
                    email=user_email)
        try:
            mysql_session.add(user)
            mysql_session.commit()
        except Exception as e:
            mysql_session.rollback()
            print e
            raise
        finally:
            mysql_session.close()

        return user.id
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
   
    def get_board_ids(self):
        return r_server.lrange('/user/%d/boards' % self.id, 0 , -1)
    
    def get_boards(self):
        from models.board import Board
        return Board.get_multi(self.get_board_ids())

    def add_board(self, board):
        return r_server.rpush('/user/%d/boards' % self.id, board.id)
    
    def get_card_ids(self):
        return r_server.lrange('/user/%d/cards' % self.id, 0, -1)

    def get_cards(self):
        from models.card import Card
        return Card.get_multi(self.get_card_ids())

    def add_card(self, card):
        r_server.rpush('/user/%d/cards' % self.id, card.id)

User.query = mysql_session.query(User)
