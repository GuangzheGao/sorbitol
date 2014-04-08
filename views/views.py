# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

main_app = Blueprint('main_app', __name__)

@main_app.route('/')
def index():
    return render_template('index.html')
