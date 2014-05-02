# -*- coding: utf-8 -*-
from models.board import Board
from models.user import User
from models.activity import Activity

from unittest import TestCase
from utils.db import mysql_session, mysql_engine, r_server

class TestActivity(TestCase):
    def setUp(self):
        mysql_session.flush()
        mysql_session.close()
        r_server.flushdb()

        Activity.__table__.drop(mysql_engine, checkfirst=True)
        Activity.__table__.create(mysql_engine, checkfirst=True)

        Board.__table__.drop(mysql_engine, checkfirst=True)
        Board.__table__.create(mysql_engine, checkfirst=True)

    def test_add_and_get(self):
        uid0 = User.add("test1", "password", "test1@test.com")
        bid0 = Board.add("board1", "A")
        aid0 = Activity.add(bid0, uid0, "BLABLA")
        activity0 = Activity.get(aid0)
        assert bid0 == activity0.board_id
        assert uid0 == activity0.user_id
        assert "BLABLA" == activity0.content

    def test_get_comments_by_card_id(self):
        uid0 = User.add("test1", "password", "test1@test.com")
        bid0 = Board.add("board1", "A")
        bid1 = Board.add("board2", "A")
        aid0 = Activity.add(bid0, uid0, "BLABLA")
        aid1 = Activity.add(bid0, uid0, "LA")
        aid2 = Activity.add(bid1, uid0, "HULA")

        activity0 = Activity.get(aid0)
        activity1 = Activity.get(aid1)
        activity2 = Activity.get(aid2)

        assert aid0 in [activity.id for activity in Activity.get_all(bid0)]
        assert aid1 in [activity.id for activity in Activity.get_all(bid0)]
        assert aid2 not in [activity.id for activity in Activity.get_all(bid0)]
        assert aid2 in [activity.id for activity in Activity.get_all(bid1)]