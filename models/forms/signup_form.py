# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField
from wtforms.validators import Email, DataRequired, Length
from models.user import User

class SignupForm(Form):
    username = TextField('Name',
                      [DataRequired(), Length(min = 6, max = 20)])
    email = TextField('Email', 
                      [Email(), DataRequired(), Length(min = 6, max = 20)])
    password = PasswordField('Password', 
                             [DataRequired(), Length(min = 6, max = 20)])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        return Form.validate(self)
