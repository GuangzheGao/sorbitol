# -*- coding: utf-8 -*-
from flask import request, redirect, url_for, Blueprint, render_template, jsonify
from models.user import User
from models.forms.login_form import LoginForm
from models.forms.signup_form import SignupForm
from models.forms.ajax.add_card_form import AddCardForm
from models.forms.ajax.add_list_form import AddListForm
from models.forms.ajax.edit_card_desc_form import EditCardDescForm
from models.forms.ajax.add_comment_form import AddCommentForm
from models.forms.ajax.add_board_form import AddBoardForm
from models.forms.ajax.upload_photo_form import UploadPhoto
from models.board import Board
from models.list import List
from models.card import Card
from models.group import Group
from models.comment import Comment

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

@main_app.route('/u/<path:user_id>')
@login_required
def render_user(user_id = None):
    '''user page'''
    user = User.get(long(user_id))
    if not user:
        return jsonify({'code':404, 'message':'Page Not Found'})
    return render_template('profile.html', 
                            tag = 'profile',
                            user = current_user,
                            profile_owner = user,
                            avatar_image = None,
                            add_board_form = AddBoardForm())

@main_app.route('/u/<path:user_id>/cards')
@login_required
def render_user_cards(user_id = None):
    if long(user_id) != current_user.id:
        return redirect(url_for('index'))

    user = User.get(long(user_id))
    cards = user.get_cards()
    return render_template('profile.html',
                            tag = 'cards',
                            user = current_user,
                            profile_owner = user,
                            add_board_form = AddBoardForm(),
                            avatar_image = None,
                            cards = user.get_cards())

@main_app.route('/u/<user_id>/account')
@login_required
def render_user_settings(user_id = None):
    if long(user_id) != current_user.id:
        return redirect(url_for('index'))

    user = User.get(long(user_id))
    if not user:
        abort(404)

    avatar_image = user.get_avatar()

    return render_template('profile.html',
                            tag = 'settings',
                            user = current_user,
                            profile_owner = user,
                            upload_photo_form = UploadPhoto(),
                            avatar_image = avatar_image,
                            add_board_form = AddBoardForm())

@main_app.route('/b', methods=['POST', ])
@login_required
def api_board(board_id=None):
    print "=======", request.form
    try:
        title = request.form['title']
    except:
        return jsonify({'code':400, 'message':'Invalid Request'})

    board_id = Board.add(title,'A')
    board = Board.get(board_id)
    board.add_user(current_user)
    current_user.add_board(board)
    List.add("To Do", board_id)
    List.add("Doing", board_id)
    List.add("Done", board_id)
    return jsonify({'board_id':board_id})

@main_app.route('/b/<path:board_id>')
@login_required
def render_board(board_id = None):
    '''board page'''
    board=Board.get(board_id)
    try:
        show_card_id = request.args['show_card']
    except:
        show_card_id = -1

    if board == None:
        return render_template('404.html');
    else:
        return render_template('board.html', 
                                user=current_user, 
                                board=board, 
                                show_card_id=show_card_id,
                                lists = board.get_lists(),
                                add_card_form = AddCardForm(),
                                add_list_form = AddListForm(),
                                edit_card_desc_form = EditCardDescForm(),
                                add_comment_form = AddCommentForm(),
                                add_board_form = AddBoardForm())

''' AJAX endpoints, retrieve kids using parent '''
@main_app.route('/l', methods=['GET', 'POST'])
def api_list(board_id = None):
    if request.method == 'GET':
        board_id = request.args.get('board_id')
        lists = List.get_all(board_id)
        if lists != None:
            return jsonify(json_list=[i.serialize() for i in lists])
        else:
            return jsonify({'code': 404, 'message': 'List ID not valid.'})
    else:
        try:
            board_id = long(request.form['board_id'])
            title = request.form['title']
        except KeyError:
            return jsonify({'code': 400, 'message': 'Bad Request'})
        else:
            return jsonify({"list_id": List.add(title, board_id)})

@main_app.route('/c', methods=['GET', 'POST'])
@login_required
def api_card(list_id = None):
    if request.method == 'GET':
        list_id = request.args.get('list_id')
        if list_id != None:
            cards = Card.get_cards_by_list_id(list_id)
            return jsonify(json_list=[card.serialize() for card in cards])
        else:
            return jsonify({'code': 404, 'message': 'Card ID not valid.'})
    else:
        try:
            list_id = long(request.form['list_id'])
            title = request.form['title']
        except KeyError:
            return jsonify({'code': 400, 'message': 'Bad Request'})

        return jsonify({"card_id": Card.add(title, list_id, current_user.id)})

@main_app.route('/c/<path:card_id>', methods=['POST',])
@login_required
def api_edit_card(card_id = None):
    if card_id == None:
        return jsonify({'code': 400, 'message': 'Bad Request'})
    else:
        card = Card.get(long(card_id))
        if card == None:
            return jsonify({'code': 404, 'message': 'Page Not Found'})

    try:
        desc = request.form['desc']
        card.set_description(desc)
    except KeyError:
        return jsonify({'code': 400, 'message': 'Bad Request'})
    return jsonify({'code': 200, 'card_id':card_id}) 

@main_app.route('/c/<path:card_id>/comments', methods=['POST',])
@login_required
def api_add_comment(card_id=None):
    if card_id == None:
        return jsonify({'code': 400, 'message': 'Bad Request'})
    else:
        card = Card.get(long(card_id))
        if card == None:
            return jsonify({'code': 404, 'message': 'Page Not Found'})
    
    try:
        content = request.form['comment']
    except:
        return jsonify({'code': 400, 'message': 'Bad Request'})

    comment = Comment.add(long(card_id), current_user.id, content)
    return jsonify({'card_id': card_id})

