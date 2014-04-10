#-*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField
from wtforms.validators import Email, DataRequired, Length
from models.user import User

class LoginForm(Form):
    email = TextField('email', [Email(), DataRequired(), Length(min=6, max=120)])
    password = PasswordField('password', [DataRequired(), Length(min=6, max=20)])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        if not User.check_password_format(self.password.data):
            self.password.errors.append("Invalid Password")
            return False

        user = User.get_validate_user(self.email.data, self.password.data)

        if user is None:
            self.email.errors.append('Unknown email/password')
            return False

        self.user = user
        return True    

