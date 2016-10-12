#!/usr/bin/env python
# -*- coding=utf-8 -*-


from datetime import datetime

from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment


app = Flask(__name__)
app.debug = True
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

@app.errorhandler
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
