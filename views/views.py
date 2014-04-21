# -*- coding: utf-8 -*-
from flask import request, redirect, url_for, Blueprint, render_template, jsonify
from models.user import User
from models.forms.login_form import LoginForm
from models.forms.signup_form import SignupForm

from models.board import Board
from models.list import List
from models.card import Card

from flask.ext.login import login_user, logout_user, current_user, login_required

main_app = Blueprint('main_app', __name__)

@main_app.route('/login',  methods=['GET', 'POST'])
def render_login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        print "POST"
        if form.validate_on_submit():
            login_user(form.user)
            return redirect(url_for('index'))

    return render_template('login.html', form = form, user=None)

@main_app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@main_app.route('/signup', methods=['GET', 'POST'])
def render_signup():
    # if current user, redirect to index
    if not current_user.is_anonymous():
        return redirect(url_for('index'))

    form = SignupForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            username_exist = User.query.filter_by(username = form.username.data).first()
            email_exist = User.query.filter_by(email = form.email.data).first()

            # check if the username or email is exist
            if username_exist:
                form.username.errors.append('Username is already in use.')
            if email_exist:
                form.email.errors.append('Email is already in use.')
            if user_exist or email_exist:
                # any of them exist, redraw signup page
                return render_template('signup.html', form = form)
        else:
            # add new user to database, redirect to login
            print "username", form.username.data
            print "password", form.password.data
            print "email", form.email.data
            user_id = User.signup(form.username.data,
                                  form.password.data,
                                  form.email.data)
            return redirect(url_for('.render_login'), code=303)
    else:
        # if the form is not valid, redraw signup page
        return render_template('signup.html', form = form)

    return render_template('signup.html', form = SignupForm())

@main_app.route('/group')
def render_groups():
    '''page listing groups for a user'''
    return render_template('groups.html')

@main_app.route('/group/<path:group_id>')
def render_singe_group(group_id = None):
    '''page for one single group'''
    return render_template('single_group.html')

@main_app.route('/group/<path:group_id>/members')
def render_group_members(group_id = None):
    '''page for all members in a group'''
    return render_template('group_members.html')

@main_app.route('/user/<path:user_id>')
def render_user(user_id = None):
    '''user page'''
    return render_template('group_members.html')

@main_app.route('/b/<path:board_id>')
def render_board(board_id = None):
    '''board page'''
    board=Board.get(board_id)
    if board == None:
        return render_template('404.html');
    else:
        return render_template('board.html', user=current_user, board=board)

''' AJAX endpoints, retrieve kids using parent '''
@main_app.route('/l', methods=['GET', 'POST'])
def api_list(board_id = None):
    if request.method == 'GET':
        board_id = request.args.get('board_id')
        lists = List.get_all(board_id)
        if lists != None:
            return jsonify(json_list=[i.serialize() for i in lists])
        else:
            return jsonify(None)
    else:
        board_id = request.json['board_id']
        title = request.json['title']
        if board_id == None or title == None:
            return -1
        else:
            return jsonify({"list_id": List.add(board_id, title)})

@main_app.route('/c', methods=['GET', 'POST'])
def api_card(list_id = None):
    if request.method == 'GET':
        list_id = request.args.get('list_id')
        if list_id != None:
            cards = Card.get_all(list_id)
            return jsonify(json_list=[i.serialize() for i in cards])
        else:
            return jsonify(None)
    else:
        list_id = request.json['list_id']
        title = request.json['title']
        label = request.json['label']
        if list_id == None or title == None or label == None:
            return -1
        else:
            return jsonify({"card_id": Card.add(title, list_id, label)})

