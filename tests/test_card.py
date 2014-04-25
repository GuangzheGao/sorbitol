# -*- coding: utf-8 -*-

from models.user import User
from models.list import List
from models.card import Card
from models.board import Board
from unittest import TestCase
from utils.db import mysql_session, mysql_engine, r_server

class TestCard(TestCase):
    def setUp(self):
        mysql_session.flush()
        mysql_session.close()
        r_server.flushdb()        
        Card.__table__.drop(mysql_engine, checkfirst=True)
        Card.__table__.create(mysql_engine, checkfirst=True)
        Board.__table__.drop(mysql_engine, checkfirst=True)
        Board.__table__.create(mysql_engine, checkfirst=True)
        List.__table__.drop(mysql_engine, checkfirst=True)
        List.__table__.create(mysql_engine, checkfirst=True)

    def test_set_and_get_card(self):
        uid0 = User.add("test1", "password", "test1@test.com")
        bid0 = Board.add("board1", "A")
        lid0 = List.add("To Do", bid0)
        card_id = Card.add("card0", lid0, uid0)
        card = Card.get(card_id)
        assert card.title == 'card0'
        assert card.list_id == lid0

    def test_get_cards_by_list_id(self):
        uid0 = User.add("test1", "password", "test1@test.com")
        bid0 = Board.add("board1", "A")
        lid0 = List.add("To Do", bid0)
        card_id = Card.add("card0", lid0, uid0)
        card = Card.get(card_id)
        assert card_id in [card.id for card in Card.get_cards_by_list_id(lid0)]

    def test_get_user_ids(self):
        uid0 = User.add("test1", "password", "test1@test.com")
        bid0 = Board.add("board1", "A")
        lid0 = List.add("To Do", bid0)
        card_id = Card.add("card0", lid0, uid0)
        card = Card.get(card_id)
        assert str(uid0) in [user_id for user_id in card.get_user_ids()]

    def test_get_and_test_description(self):
        uid0 = User.add("test1", "password", "test1@test.com")
        bid0 = Board.add("board1", "A")
        lid0 = List.add("To Do", bid0)
        card_id = Card.add("card0", lid0, uid0)
        card = Card.get(card_id)
        card.set_description('desc')
        assert 'desc' in card.get_description()

    def incr_decr_get_comment(self):
        uid0 = User.add("test1", "password", "test1@test.com")
        bid0 = Board.add("board1", "A")
        lid0 = List.add("To Do", bid0)
        card_id = Card.add("card0", lid0, uid0)
        card = Card.get(card_id)
        Card.incr_comment(card_id)
        assert 1 == card.get_comment_count()
        Card.desc_comment(card_id)
        assert 0 == card.get_comment_count()
