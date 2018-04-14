from flask import Flask, render_template
#import pandas as pd
import sqlite3
from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

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
