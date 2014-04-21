# -*- coding: utf-8 -*-

from models.user import User
from models.group import Group
from models.card import Card
from unittest import TestCase
from utils.db import mysql_session, mysql_engine

class TestCard(TestCase):
    def setUp(self):
        mysql_session.flush()
        mysql_session.close()
        
        Card.__table__.drop(mysql_engine, checkfirst=True)
        Card.__table__.create(mysql_engine, checkfirst=True)


    def test_set_and_get_card(self):
        card_id = Card.add("wwww", 122222, -1)
        card = Card.get(card_id)
        assert Card.title == 'wwww'
  
