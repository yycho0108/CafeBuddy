from flask import Flask, render_template, request
import json
import sqlite3
app = Flask(__name__)

table_no = 0

@app.route('/table')
def new_table():
    pass

@app.route('/open_table')
def open_table():
    conn = sqlite3.connect("cafebuddy.db")
    cur = conn.cursor()
    query = "DELETE FROM people WHERE table_no = {}".format(table_no)
    print(query)
    cur.execute(query)

    conn.commit()

    cur.execute("select * from people")

    rows = cur.fetchall();
    for row in rows:
        print(row)

    cur.close()
    conn.close()
    return render_template('table_free.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)

@app.route('/exit',methods = ['POST', 'GET'])
def exit():
    if request.method == 'POST':
        result = request.form
        conn = sqlite3.connect("cafebuddy.db")
        cur = conn.cursor()
        people = []
        for key, value in result.items():
            if key.startswith("Name") and len(value) > 0:
                fn, ln = value.split(" ")
                people.append("('{}', '{}', {})".format(fn, ln, table_no))

        entries = ",".join(people)
        query = "INSERT INTO people (first_name,last_name, table_no) VALUES {}".format(entries)
        print(query)
        cur.execute(query)
        conn.commit()

        cur.execute("select * from people")

        rows = cur.fetchall();
        for row in rows:
            print(row)

        cur.close()
        conn.close()
        return render_template("exit.html",exit = exit)


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
   app.run(debug = True)

