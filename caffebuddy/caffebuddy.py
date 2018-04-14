from flask import Flask, render_template

#import pandas as pd
import sqlite3
from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler
import psycopg2

#import pandas as pd
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ipbifgmvvhliav:4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e@ec2-107-20-151-189.compute-1.amazonaws.com:5432/d2mo1re4fcqlhr'
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

@app.route('/kate', methods=['POST', 'GET'])
def kate_page():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
    con = psycopg2.connect(dbname='d2mo1re4fcqlhr', user='ipbifgmvvhliav', host='ec2-107-20-151'
                                                                                '-189.compute-1.amazonaws.com',
                           password='4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e')
    # conn.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM seating")


    people = cur.fetchall()
    people_friendlevel = []
    for p in people:
        cur.execute("SELECT type_people FROM people WHERE name LIKE '%{}%'".format(p[1]))
        people_friendlevel.append((*p, *cur.fetchone()))


    cur.close()
    con.close()
    print(people_friendlevel)
    return render_template("kate.html", items=people_friendlevel)


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
        conn = psycopg2.connect(dbname='d2mo1re4fcqlhr', host='ec2-107-20-151-189.compute-1.amazonaws.com', 
            user='ipbifgmvvhliav', password='4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e')
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
        conn = psycopg2.connect(dbname='d2mo1re4fcqlhr', host='ec2-107-20-151-189.compute-1.amazonaws.com', 
            user='ipbifgmvvhliav', password='4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e')
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
    if request.method == 'POST':
        if request.form['submit'] == "Remove":
            # remove_from_database()
            print(request.form['category'])
            print(request.form['person'])
        elif request.form['submit'] == "Add":
            #add_to_database()
            print(request.form['category'])
            print(request.form['new_person'])
        # TODO : commit data to database

    # TODO : load data from database
    data = json.dumps({
        'friend' : ['f1', 'f2'],
        'acquaintance' : ['a1', 'a2'],
        'enemy' : ['e1', 'e2']
        })
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

if __name__ == '__main__':
    app.run()
