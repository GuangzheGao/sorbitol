# -*- coding: utf-8 -*-
from models.board import Board
from models.user import User
from models.list import List
from models.card import Card
from models.comment import Comment

from unittest import TestCase
from utils.db import mysql_session, mysql_engine, r_server

class TestComment(TestCase):
    def setUp(self):
        mysql_session.flush()
        mysql_session.close()
        r_server.flushdb()

        Comment.__table__.drop(mysql_engine, checkfirst=True)
        Comment.__table__.create(mysql_engine, checkfirst=True)
        
        Board.__table__.drop(mysql_engine, checkfirst=True)
        Board.__table__.create(mysql_engine, checkfirst=True)

    def test_add_and_get(self):
        uid0 = User.add("test1", "password", "test1@test.com")
        bid0 = Board.add("board1", "A")
        lid0 = List.add("To Do", bid0)
        caid0 = Card.add("card1", lid0, uid0)
        coid0 = Comment.add(caid0, uid0, "comment1")
        comment0 = Comment.get(coid0)
        assert caid0 == comment0.card_id
        assert uid0 == comment0.user_id
        assert "comment1" == comment0.content

    def test_get_comments_by_card_id(self):
        uid0 = User.add("test1", "password", "test1@test.com")
        bid0 = Board.add("board1", "A")
        lid0 = List.add("To Do", bid0)

        caid0 = Card.add("card1", lid0, uid0)
        caid1 = Card.add("card2", lid0, uid0)

        coid0 = Comment.add(caid0, uid0, "comment1")
        coid1 = Comment.add(caid1, uid0, "comment2")

        comment0 = Comment.get(coid0)
        comment1 = Comment.get(coid1)

        assert coid0 in [comment.id for comment in Comment.get_comments_by_card_id(caid0)]
        assert coid1 not in [comment.id for comment in Comment.get_comments_by_card_id(caid0)]
