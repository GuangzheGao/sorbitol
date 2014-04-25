# -*- coding: utf-8 -*-
import os

from werkzeug import secure_filename
from flask import Flask, Blueprint, render_template, redirect, url_for, request, jsonify, flash
from flask.ext.login import LoginManager, current_user, login_required
from flaskext.uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf.csrf import CsrfProtect

from views.views import main_app
from models.user import User
from models.board import Board
from models.forms.ajax.add_board_form import AddBoardForm
from models.forms.ajax.upload_photo_form import UploadPhoto

from utils.utils import timesince, initial

csrf = CsrfProtect()
app = Flask(__name__)
csrf.init_app(app)

app.register_blueprint(main_app)
app.secret_key = 's3cr3t'
login_manager = LoginManager()
login_manager.init_app(app)

UPLOADS_DEFAULT_DEST = os.getcwd()+os.sep+'uploads'

app.config.from_object(__name__)
app.config.from_envvar('PHOTOLOG_SETTINGS', silent=True)

images = UploadSet('images', IMAGES)
configure_uploads(app, (images,))

app.jinja_env.filters['timesince'] = timesince
app.jinja_env.filters['initial'] = initial

@login_manager.user_loader
def get_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    if not current_user or current_user.is_anonymous():
        return redirect(url_for('main_app.render_login'))

    #return render_template('index.html', user=current_user)
    return render_template('index.html', user=current_user, boards=current_user.get_boards(), add_board_form = AddBoardForm())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/upload', methods=['POST',])
@login_required
def upload():
    form = UploadPhoto()
    if 'upload' in request.files:
        if form.validate_on_submit():
            image = request.files.get('upload')
            filename = 'avatar_' + form.user_id.data + '.png'

            try:
                # remove duplicate if exist
                os.remove(images.config.destination + '/' + filename)
            except:
                pass
            filename = images.save(image, 
                                   name=filename,)
            user = User.get(form.user_id.data)
            if not user:
                abort(404)
            user.set_avatar(images.url(filename))
            return redirect(url_for('main_app.render_user_settings', user_id=current_user.id))
            

    return jsonify({'code':400, 'message':'Bad Request'})
if __name__ == '__main__':
    app.debug = True
    app.run()

