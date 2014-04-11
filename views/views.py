# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

main_app = Blueprint('main_app', __name__)

@main_app.route('/')
def index():
    return render_template('index.html') #show groups and boards inside

@main_app.route('/group/<groupname>')
def group_main(groupname):
    return render_template('group.html') #show boards and members of group

@main_app.route('/b/<boardID>')
def board(boardID):
    return render_template('board.html') #show lists(AJAX), card(AJAX), members of board

@main_app.route('/l/<listID>')
def list(listID):
    pass; #show lists(AJAX), card(AJAX), members of board

@main_app.route('/c/<cardID>')
def card(cardID):
    pass; #show things inside card

@main_app.route('/login', methods=['GET', 'POST'])
def route():
    return render_template('login_sign_up.html');