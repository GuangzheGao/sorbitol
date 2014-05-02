# -*- coding: utf-8 -*-

'''
from models.user import User
from models.group import Group
from unittest import TestCase
from utils.db import mysql_session, mysql_engine
class TestGroup(TestCase):
    def setUp(self):
        mysql_session.flush()
        mysql_session.close()
        
        User.__table__.drop(mysql_engine, checkfirst=True)
        User.__table__.create(mysql_engine, checkfirst=True)
        
        Group.__table__.drop(mysql_engine, checkfirst=True)
        Group.__table__.create(mysql_engine, checkfirst=True)

    def test_set_and_get_group(self):
        group_id = Group.add('test_group')
        group = Group.get(group_id)
        assert group.name == 'test_group'
   
    def test_add_member(self):
        cid = User.signup("test_user1", "password", "test_user1@gmail.com")
        user = User.get(cid)
        group_id = Group.add("test_group")
        group = Group.get(group_id)
        group.add_member(user)
        assert user in group.get_members()
        assert group in user.get_groups()
'''