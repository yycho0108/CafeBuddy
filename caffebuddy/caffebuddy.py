from flask import Flask, render_template

#import pandas as pd
import sqlite3
from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

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

class 


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/kate', methods=['POST', 'GET'])
def kate_page():
    conn = sqlite3.connect("cafebuddy.db")
    # conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM people")

    return render_template("kate.html", items = cur.fetchall())
    # cur.close()
    # conn.close()
    # df = pd.read_csv('people')
    # table = pd.read_csv("C:/Users/murta/PycharmProjects/caffebuddy/people")
    # return render_template("kate.html", data=table.to_html())
    # user_details = {
    #     'name': 'Murtaza',
    #     'table': '2'
    # }
    # return render_template('kate.html', user=user_details)
    # return df.to_html()
    # return "kates page"

# @app.route('/post_user', methods=['POST'])
# def post_user():
#     user = User(request.form[''])

@app.route('/login', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
        return render_template('index.html', users=users)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()