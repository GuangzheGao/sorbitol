# -*- coding: utf-8 -*-

from flask import Flask, Blueprint
from views.views import main_app

app = Flask(__name__)
app.register_blueprint(main_app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run()

