# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify
from models.forms import SignupForm, LoginForm
from flask.ext.login import login_user, logout_user, current_user, login_required

main_app = Blueprint('main_app', __name__)

@main_app.route('/')
def index():
<<<<<<< HEAD
    return render_template('index.html')

@main_app.route('/login',  methods=['GET', 'POST'])
def render_login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            return redirect(url_for('index'))

    return render_template('login.html', form = form)

@main_app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@main_app.route('/signup', methods=['GET', 'POST'])
def render_signup():
    # if current user, redirect to index
    if current_user:
        return redirect(url_for('index'))

    form = SignupForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            username_exist = 
                User.query.filter_by(username = form.username.data).first()
            email_exist = User.query.filter_by(email = form.email.data).first()

        # check if the username or email is exist
        if user_exist:
            form.username.errors.append('Username is already in use.')
        if email_exist:
            form.email.errors.append('Email is already in use.')
        if user_exist or email_exist:
            # any of them exist, redraw signup page
            return render_template('signup.html', form = form)
        else:
            # add new user to database, redirect to login
            user_id = User.signup(form.username.data,
                                  form.password.data,
                                  form.email.data)
            return redirect(url_for('login'))
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
    return render_template('board.html')

@main_app.route('/l/<path:list_id>')
def api_list(list_id = None):
    return jsonify(None)

@main_app.route('/c/<path:card_id>')
def api_card(card_id = None):
    return jsonify(None)


=======
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
def login():
    return render_template('login.html');

@main_app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html');
>>>>>>> 994b81ec2092995c04f579916547eafeae727286
