from flask import Flask

app = Flask(__name__)


def index():
    return "This is a flask app."


def hello_world():
    return "Hello World!"


def hello_to(name):
    return f"Hello, {name}!"


app.add_url_rule('/', 'index', index)
app.add_url_rule('/hello', 'hello', hello_world)
app.add_url_rule('/hello/<name>', 'hello_to', hello_to)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
