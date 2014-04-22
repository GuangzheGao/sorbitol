# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextAreaField, TextField
from wtforms.validators import DataRequired, Length

class AddCardForm(Form):
    title = TextAreaField('title', [DataRequired(), Length(min=1, max=512)])
    list_id = TextField('list_id', [DataRequired(), Length(min=1, max=12)]) 

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        
    def validate(self):
        return Form.validate(self)

