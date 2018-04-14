from flask import Flask, render_template

#import pandas as pd
import os
import sqlite3
from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler
import psycopg2

from collections import defaultdict
import json

#import pandas as pd
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ipbifgmvvhliav:4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e@ec2-107-20-151-189.compute-1.amazonaws.com:5432/d2mo1re4fcqlhr'
DATABASE_URL = os.environ['DATABASE_URL']

#conn = psycopg2.connect(dbname='d2mo1re4fcqlhr', user='ipbifgmvvhliav', host='ec2-107-20-151'
#        '-189.compute-1.amazonaws.com',
#        password='4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e')

# ^^NO NEED TO, AND SHOULD AVOID, HARDCODING URL IN CODE:
# check with heroku config

db = SQLAlchemy(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(80))

    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_
    
    def __repr__(self):
        return'<User %r' % self.name
# ^^ Deprecated

@app.route('/list_of_tables', methods=['POST', 'GET'])
def kate_page():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
    # conn.row_factory = sql.Row
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT * FROM seating")


    people = cur.fetchall()
    table_map = {}
    for p in people:
        cur.execute("SELECT relationship, class_year, major, misc FROM people_attr WHERE name LIKE '%{}%'".format(p[1]))
        people_list = table_map.get(p[2], [])
        people_list.append((p[1], cur.fetchone()))
        table_map[p[2]] = people_list


    cur.close()
    conn.close()
    print(table_map)
    empty_tables = [i for i in range(10) if i not in table_map]
    return render_template("list_tables.html", all_tables=table_map, empty_tables=empty_tables)


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

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
        return render_template('index.html', users=users)

    else:
        return render_template('index.html')

# table_no = 0

@app.route('/table')
def new_table():
    return render_template('table.html')

@app.route('/open_table/<int:table_no>',methods = ['POST', 'GET'])
def open_table(table_no):
    if request.method == 'POST':
        result = request.form
        # global table_no
        # table_no=result["TableNumber"]
        # print("table no set",table_no)

    else: 
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        #conn = psycopg2.connect(dbname='d2mo1re4fcqlhr', host='ec2-107-20-151-189.compute-1.amazonaws.com', 
        #    user='ipbifgmvvhliav', password='4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e')
        cur = conn.cursor()
        query = "DELETE FROM seating WHERE table_no = {}".format(table_no)
        print(query)
        cur.execute(query)

        conn.commit()

        cur.close()
        conn.close()
    return render_template('table_free.html', table_no=table_no)

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)

@app.route('/exit/<int:table_no>',methods = ['POST', 'GET'])
def exit(table_no):
    if request.method == 'POST':
        result = request.form
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        #conn = psycopg2.connect(dbname='d2mo1re4fcqlhr', host='ec2-107-20-151-189.compute-1.amazonaws.com', 
        #    user='ipbifgmvvhliav', password='4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e')
        cur = conn.cursor()
        people = []
        for key, value in result.items():
            if key.startswith("Name") and len(value) > 0:
                people.append("('{}', {})".format(value, table_no))

        entries = ",".join(people)
        query = "INSERT INTO seating (name, table_no) VALUES {}".format(entries)
        print(query)
        cur.execute(query)
        conn.commit()

        cur.close()
        conn.close()
        return render_template("exit.html",table_no=table_no)


@app.route('/preferences',methods = ['POST', 'GET'])
def preferences():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT name, relationship FROM people_attr")
    res = cur.fetchall()

    if request.method == 'POST':
        form = request.form
        if form['submit'] == "Remove":
            query = "DELETE FROM people_attr WHERE name = '{}'".format(form['person'])
            cur.execute(query)
            conn.commit()
        elif form['submit'] == "Add":
            query = 'INSERT INTO people_attr (name, relationship) values (\'{}\', \'{}\') ON CONFLICT (name) DO UPDATE SET relationship = EXCLUDED.relationship;'\
                .format(form['new_person'], form['category'])
            cur.execute(query)
            conn.commit()
        elif form['submit'] == "Weight":
            # TODO : handle weight modifications
            pass

    # most recent data
    data = {
            'friend' : [],
            'acquaintance' : [],
            'enemy' : []
            }
    for name, rel in res:
        rel = rel.lower()
        if rel in data.keys():
            data[rel].append(name)
    data = json.dumps(data)

    cur.close()
    conn.close()

    return render_template('preferences.html',
        data=data,
        weight={
            'friend' : 2,
            'acquaintance' : 1,
            'empty'  : 0,
            'stranger' : -1,
            'enemy' : -2
            }
        )

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/pancakes')
def pancakes():
    return render_template("Pancakes.html")

@app.route('/bacon')
def bacon():
	return render_template("bacon.html")

@app.route('/fruit')
def fruit():
    return render_template("fruit.html")

@app.route('/tenders')
def tenders():
    return render_template("tenders.html")

@app.route('/vegburg')
def vegburg():
    return render_template("vegburg.html")

@app.route('/pizza')
def pizza():
    return render_template("pizza.html")

@app.route('/pasta')
def pasta():
    return render_template("pasta.html")

if __name__ == '__main__':
    app.run()
