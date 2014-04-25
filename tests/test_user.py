# -*- coding: utf-8 -*-
from models.user import User
from models.board import Board
from models.card import Card
from models.list import List

from unittest import TestCase
from utils.db import mysql_session, mysql_engine, r_server
class TestUser(TestCase):
    def setUp(self):
        mysql_session.flush()
        mysql_session.close()
        r_server.flushdb()

        User.__table__.drop(mysql_engine, checkfirst=True)
        User.__table__.create(mysql_engine, checkfirst=True)
        
        Board.__table__.drop(mysql_engine, checkfirst=True)
        Board.__table__.create(mysql_engine, checkfirst=True)

    def test_set_and_get_user(self):
        cid = User.signup("test_user1", "password", "test_user1@gmail.com")
        user = User.get(cid)
        assert cid == user.id
        assert user.username == "test_user1"
        assert user.email == "test_user1@gmail.com"
        assert user.check_password("password") == True
        assert user.check_password("random123") == False

    def test_add_and_get_boards(self):
        cid = User.add("test_user1", "password", "test_user1@gmail.com")
        user = User.get(cid)

        bid0 = Board.add("board1", "A")
        bid1 = Board.add("board2", "A")
        board0 = Board.get(bid0)
        board1 = Board.get(bid1)
        user.add_board(board0)

        assert str(bid0) in user.get_board_ids()
        assert str(bid1) not in user.get_board_ids()

    def test_add_and_get_cards(self):
        uid0 = User.add("test_user1", "password", "test_user1@gmail.com")
        user0 = User.get(uid0)
        uid1 = User.add("test_user2", "password", "test_user2@gmail.com")
        user1 = User.get(uid1)
        bid0 = Board.add("board1", "A")
        lid0 = List.add("List0", bid0)

        caid0 = Card.add("card1", lid0, uid0)
        caid1 = Card.add("card2", lid0, uid1)
        card0 = Card.get(caid0)


        print caid0, user0.get_card_ids()
        assert str(caid0) in user0.get_card_ids()
        assert str(caid1) not in user0.get_card_ids()
