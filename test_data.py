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
Comment.__table__.drop(mysql_engine, checkfirst=True)
Comment.__table__.create(mysql_engine, checkfirst=True)
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

user0.set_avatar('http://127.0.0.1:5000/_uploads/images/avatar_1.png')
user1.set_avatar('http://127.0.0.1:5000/_uploads/images/avatar_2.png')

lid0 = List.add("To Do", bid0)
lid1 = List.add("Doing", bid0)
lid2 = List.add("Done", bid0)

caid0 = Card.add("card1", lid0, uid0)
caid1 = Card.add("card2", lid0, uid0)
caid2 = Card.add("card3", lid1, uid0)

card0 = Card.get(caid0)
card0.add_user(user1)
card0.add_user(user2)

coid0 = Comment.add(caid0, uid0, "comment1")
coid1 = Comment.add(caid0, uid1, "comment2")
coid2 = Comment.add(caid0, uid2, "comment3")



'''
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from models.user import User
from models.board import Board
from models.list import List
from models.card import Card
from models.comment import Comment
from models.group import Group
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
Group.__table__.drop(mysql_engine, checkfirst=True)
Group.__table__.create(mysql_engine, checkfirst=True)

uid0 = User.add("test1", "password", "test1@test.com")
uid1 = User.add("test2", "password", "test2@test.com")
uid2 = User.add("test3", "password", "test3@test.com")

user0 = User.get(uid0)
user1 = User.get(uid1)
user2 = User.get(uid2)

gid0 = Group.add("MUSABLA", "this group is good")
bid0 = Board.add("board1", "A", gid0)
bid1 = Board.add("board2", "A", gid0)

group0 = Group.get(gid0)
board0 = Board.get(bid0)
board1 = Board.get(bid1)

group0.add_user(user0)  #useful in group information page, boards and members
board0.add_user(user0)  #useful in main board page
board0.add_user(user1)
board0.add_user(user2)

board1.add_user(user0)
board1.add_user(user1)

user0.add_group(group0) #index page
user1.add_group(group0) #index page
user2.add_group(group0) #index page

user0.add_board(board1)
user1.add_board(board0)
user1.add_board(board1)
user2.add_board(board0)


lid0 = List.add("To Do", bid0)
lid1 = List.add("Doing", bid0)
lid2 = List.add("Done", bid0)

caid0 = Card.add("card1", lid0, uid0)
caid1 = Card.add("card2", lid0, uid0)
caid2 = Card.add("card3", lid1, uid0)

coid0 = Comment.add(caid0, uid0, "comment1")
coid1 = Comment.add(caid0, uid1, "comment2")
coid2 = Comment.add(caid0, uid2, "comment3")
'''



