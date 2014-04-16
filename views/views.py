# -*- coding: utf-8 -*-
from flask import request, redirect, url_for, Blueprint, render_template, jsonify
from models.user import User
from models.forms.login_form import LoginForm
from models.forms.signup_form import SignupForm
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

    return render_template('login.html', form = form)

@main_app.route('/logout')
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
            if username_exist or email_exist:
                # any of them exist, redraw signup page
                return render_template('signup.html', form = form)
            else:
                # add new user to database, redirect to login
                user_id = User.signup(form.username.data,
                                      form.password.data,
                                      form.email.data)
                return redirect(url_for('.render_login'), code=303)
        else:
            # if the form is not valid, redraw signup page
            return render_template('signup.html', form = form)
    
    return render_template('signup.html', form = SignupForm())

@main_app.route('/group')
@login_required
def render_groups():
    '''page listing groups for a user'''
    return render_template('groups.html', user = current_user)

@main_app.route('/group/<path:group_id>')
@login_required
def render_singe_group(group_id = None):
    '''page for one single group'''
    return render_template('single_group.html', user = current_user)

@main_app.route('/group/<path:group_id>/members')
@login_required
def render_group_members(group_id = None):
    '''page for all members in a group'''
    return render_template('group_members.html', user = current_user)

@main_app.route('/user/<path:user_id>')
@login_required
def render_user(user_id = None):
    '''user page'''
    return render_template('group_members.html', user = current_user)

@main_app.route('/b/<path:board_id>')
@login_required
def render_board(board_id = None):
    '''board page'''
    return render_template('board.html', user = current_user)

@main_app.route('/l/<path:list_id>')
def api_list(list_id = None):
    return jsonify(None)

@main_app.route('/c/<path:card_id>')
def api_card(card_id = None):
    return jsonify(None)
