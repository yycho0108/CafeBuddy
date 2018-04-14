from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/kate')
def kate_page():
    return "kate's page"

if __name__ == '__main__':
    app.run()
