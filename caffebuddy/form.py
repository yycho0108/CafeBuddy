from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
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
      return render_template("exit.html",exit = exit)


if __name__ == '__main__':
   app.run(debug = True) 