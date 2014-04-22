# -*- coding: utf-8 -*-
from __future__ import absolute_import
from models.user import User
from models.board import Board
from models.list import List
from models.card import Card
from models.comment import Comment
from utils.db import mysql_engine, r_server

r_server.flushdb()
Board.__table__.drop(mysql_engine, checkfirst=True)
Board.__table__.create(mysql_engine, checkfirst=True)
User.__table__.drop(mysql_engine, checkfirst=True)
User.__table__.create(mysql_engine, checkfirst=True)
List.__table__.drop(mysql_engine, checkfirst=True)
List.__table__.create(mysql_engine, checkfirst=True)
Card.__table__.drop(mysql_engine, checkfirst=True)
Card.__table__.create(mysql_engine, checkfirst=True)

uid0 = User.add("test1", "password", "test1@test.com")
uid1 = User.add("test2", "password", "test2@test.com")
uid2 = User.add("test3", "password", "test3@test.com")

user0 = User.get(uid0)
user1 = User.get(uid1)
user2 = User.get(uid2)

bid0 = Board.add("board1", "A")
bid1 = Board.add("board2", "A")

board0 = Board.get(bid0)
board1 = Board.get(bid1)

board0.add_user(user0)
board0.add_user(user1)
board0.add_user(user2)

board1.add_user(user0)
board1.add_user(user1)

user0.add_board(board0)
user0.add_board(board1)
user1.add_board(board0)
user1.add_board(board1)
user2.add_board(board0)


lid0 = List.add(bid0, "To Do")
lid1 = List.add(bid0, "Doing")
lid2 = List.add(bid0, "Done")

caid0 = Card.add("card1", lid0)
caid1 = Card.add("card2", lid0)
caid2 = Card.add("card3", lid1)

coid0 = Comment.add(caid0, uid0, "comment1")
coid1 = Comment.add(caid0, uid1, "comment2")
coid2 = Comment.add(caid0, uid2, "comment3")
