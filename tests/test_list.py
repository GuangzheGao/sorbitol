# -*- coding: utf-8 -*-

from models.board import Board
from models.user import User
from models.list import List
from models.card import Card

from unittest import TestCase
from utils.db import mysql_session, mysql_engine, r_server

class TestList(TestCase):
    def setUp(self):
        mysql_session.flush()
        mysql_session.close()
        r_server.flushdb()

        List.__table__.drop(mysql_engine, checkfirst=True)
        List.__table__.create(mysql_engine, checkfirst=True)
        
        Board.__table__.drop(mysql_engine, checkfirst=True)
        Board.__table__.create(mysql_engine, checkfirst=True)
        
        Card.__table__.drop(mysql_engine, checkfirst=True)
        Card.__table__.create(mysql_engine, checkfirst=True)
        
        User.__table__.drop(mysql_engine, checkfirst=True)
        User.__table__.create(mysql_engine, checkfirst=True)


    def test_set_and_get_list(self):
        bid0 = Board.add("board1", "A")
        lid0 = List.add("List0", bid0)
        list0 = List.get(lid0)
        assert list0.title == "List0", True
        assert list0.board_id == lid0

    def test_get_lists_by_board_id(self):
        bid0 = Board.add("board1", "A")
        bid1 = Board.add("board2", "A")
        lid0 = List.add("List0", bid0)
        list0 = List.get(lid0)
        lid1 = List.add("List1", bid1)
        list1 = List.get(lid1)
        assert lid0 in [_list.id for _list in List.get_lists_by_board_id(bid0)]
        assert lid1 not in [_list.id for _list in List.get_lists_by_board_id(bid0)]
        
    def test_get_cards(self):
        bid0 = Board.add("board1", "A")
        lid0 = List.add("List0", bid0) 
        list0 = List.get(lid0)
        lid1 = List.add("List1", bid0) 
        list1 = List.get(lid1)

        uid0 = User.add("test1", "password", "test1@test.com")
        
        caid0 = Card.add("card1", lid0, uid0)
        caid1 = Card.add("card2", lid1, uid0)

        assert caid0 in [card.id for card in list0.get_cards()]
        assert caid1 not in [card.id for card in list0.get_cards()]
        
  
