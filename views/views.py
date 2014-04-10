# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify
from models.forms import SignupForm, LoginForm
from flask.ext.login import login_user, logout_user, current_user, login_required
main_app = Blueprint('main_app', __name__)

@main_app.route('/')
def index():
    return render_template('index.html')

@main_app.route('/login',  methods=['GET', 'POST'])
def render_login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            return redirect(url_for('index'))

    return render_template('login.html', form = form)
            
@main_app.route('/signup', methods=['GET', 'POST'])
def render_signup():
    form = SignupForm(request.form)
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('signup.html', form = from)

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
    return render_template('board.html')

@main_app.route('/l/<path:list_id>')
def api_list(list_id = None):
    return jsonify(None)

@main_app.route('/c/<path:card_id>')
def api_card(card_id = None):
    return jsonify(None)


