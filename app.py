from flask import Flask

app = Flask(__name__)


def index():
    return "This is a flask app."


def hello_world():
    return "Hello World!"


app.add_url_rule('/', 'index', index)
app.add_url_rule('/hello', 'hello', hello_world)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
