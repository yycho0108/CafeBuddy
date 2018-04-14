from flask import Flask, render_template
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ipbifgmvvhliav:4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e@ec2-107-20-151-189.compute-1.amazonaws.com:5432/d2mo1re4fcqlhr'
db = SQLAlchemy(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(80))

    def __init__(self,name,type):
        self.name = name
        self.type = type
    
    def __repr__(self):
        return'<User %r' % self.name


@app.route('/')
def hello_world():
    return 'Hello World!'

#

if __name__ == '__main__':
    app.run()
