# Author: Gouthaman Balaraman
# http://gouthamanbalaraman.com/minimal-flask-login-example.html

from flask import Flask, Response
from flask.ext.login import LoginManager, UserMixin, login_required
from flask import Flask
app = Flask(__name__)
from flask import render_template
from flask import request

@app.route('/')
def menu():
    return render_template('test.html')