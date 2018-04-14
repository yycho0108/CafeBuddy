from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('table_free.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

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
