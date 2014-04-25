# -*- coding: utf-8 -*-

from models.board import Board
from models.user import User
from models.list import List

from unittest import TestCase
from utils.db import mysql_session, mysql_engine, r_server

class TestBoard(TestCase):
    def setUp(self):
        mysql_session.flush()
        mysql_session.close()
        r_server.flushdb()
        Board.__table__.drop(mysql_engine, checkfirst=True)
        Board.__table__.create(mysql_engine, checkfirst=True)

    def test_set_and_get_board(self):
        bid0 = Board.add("board0", "A")
        board0 = Board.get(bid0)
        assert board0.title == "board0", True
        assert board0.visibility == "A", True

    def test_add_and_get_users(self):
        bid0 = Board.add("board0", "A")
        board0 = Board.get(bid0)
        uid0 = User.add("test1", "password", "test1@test.com")
        user0 = User.get(uid0)
        uid1 = User.add("test2", "password", "test2@test.com")
        user1 = User.get(uid0)
        board0.add_user(user0)
        assert str(uid0) in board0.get_user_ids()
        assert str(uid1) not in board0.get_user_ids()

    def test_add_and_get_lists(self):
        bid0 = Board.add("board0", "A")
        board0 = Board.get(bid0)
        bid1 = Board.add("board1", "A")

        lid0 = List.add("list0", bid0)
        lid1 = List.add("list1", bid1)
        assert lid0 in [_list.id for _list in board0.get_lists()]
        assert lid1 not in [_list.id for _list in board0.get_lists()]



