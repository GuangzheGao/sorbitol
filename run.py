# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, render_template, redirect, url_for
from flask.ext.login import LoginManager, current_user
from views.views import main_app

from models.user import User

app = Flask(__name__)
app.register_blueprint(main_app)
app.secret_key = 's3cr3t'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def get_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    if not current_user or current_user.is_anonymous():
        return redirect(url_for('main_app.render_login'))
    return render_template('index.html', user=current_user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

