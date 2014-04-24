# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextAreaField, TextField
from wtforms.validators import DataRequired, Length

class AddCommentForm(Form):
    comment = TextAreaField('description', [DataRequired(), Length(min=1, max=4096)])
    card_id = TextField('card_id', [DataRequired(), Length(min=1, max=12)]) 

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        
    def validate(self):
        return Form.validate(self)
