# -*- coding: utf-8 -*-

from flask_wtf import Form
from flask.ext.uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length
from wtforms import TextField

images = UploadSet('images', IMAGES)

class UploadPhoto(Form):
    upload = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, 'Unrecognizable Data Format!')
    ])
    user_id = TextField('user_id', [DataRequired(), Length(min=1, max=12)]) 
