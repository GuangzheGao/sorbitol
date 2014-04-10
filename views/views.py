# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
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

    return render_template('signup.html', form = fro)
