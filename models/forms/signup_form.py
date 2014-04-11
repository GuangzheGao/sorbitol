# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField
from wtforms.validators import Email, DataRequired, Length

class SignupForm(Form):
    username = TextField('email',
                      [Email(), DataRequired(), Length(min = 6, max = 120)])
    email = TextField('email', 
                      [Email(), DataRequired(), Length(min = 6, max = 120)])
    password = PasswordField('password', 
                             [DataRequired(), Length(min = 6, max = 20)])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

