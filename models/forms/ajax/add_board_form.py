# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextAreaField, TextField
from wtforms.validators import DataRequired, Length

class AddBoardForm(Form):
    title = TextField('title', [DataRequired(), Length(min=1, max=512)])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        
    def validate(self):
        return Form.validate(self)

