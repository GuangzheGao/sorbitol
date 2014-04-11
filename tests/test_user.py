# -*- coding: utf-8 -*-

from models.user import User

from unittest import TestCase
from utils.db import mysql_session, mysql_engine

class TestUser(TestCase):
    def setUp(self):
        mysql_session.flush()
        mysql_session.close()

        User.__table__.drop(mysql_engine, checkfirst=True)
        User.__table__.create(mysql_engine, checkfirst=True)

    def test_set_and_get_user(self):
        cid = User.signup("test_user1", "password", "test_user1@gmail.com")
        user = User.get(cid)
        assert cid == user.id
        assert user.username == "test_user1"
        assert user.email == "test_user1@gmail.com"
        assert user.check_password("password") == True
        assert user.check_password("random123") == False
    
    def tearDown(self):
        User.__table__.drop(mysql_engine, checkfirst=True)
        User.__table__.create(mysql_engine, checkfirst=True)
