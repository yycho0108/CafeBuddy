from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/kate')
def kate_page():
    import pandas as pd
    # df = pd.read_csv('people')
    table = pd.read_csv("C:/Users/murta/PycharmProjects/caffebuddy/people")
    return render_template("kate.html", data=table.to_html())
    # user_details = {
    #     'name': 'Murtaza',
    #     'table': '2'
    # }
    # return render_template('kate.html', user=user_details)
    # return df.to_html()

if __name__ == '__main__':
    app.run()
