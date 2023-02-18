from flask import Flask

app = Flask(__name__)


def index():
    return "This is a flask app."


def hello_world():
    return "Hello World!"


def hello_to(name):
    return f"Hello, {name}!"


def blog():
    return f"Welcome to the Blog!"


def blog_details(bid):
    return f"Blog number {bid}"


def version(ver):
    return f"Blog number {ver}."


def path_to(path):
    return f"You are at {path}."


app.add_url_rule('/', 'index', index)
app.add_url_rule('/hello', 'hello', hello_world)
app.add_url_rule('/hello/<name>', 'hello_to', hello_to)

app.add_url_rule('/blog', 'blog', blog)
app.add_url_rule('/blog/<int:bid>', 'blog_details', blog_details)
app.add_url_rule('/version/<float:ver>', 'version', version)
app.add_url_rule('/to/<path:path>', 'path_to', path_to)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
