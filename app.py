from flask import Flask, redirect, url_for, request, render_template
from utils import generate_sitemap


app = Flask(__name__)


def index():
    return "This is a flask app."


def hello_world():
    return "Hello Admin!"


def hello_to(name):
    return render_template('hello.html', name=name)


@app.route('/success/<name>')
def success(name):
    return f"Welcome {name}!"


def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


def blog():
    return f"Welcome to the Blog!"


def blog_details(bid):
    return f"Blog number {bid}"


def version(ver):
    return f"Blog number {ver}."


def path_to(path):
    return f"You are at {path}."


app.add_url_rule('/', 'index', index)
app.add_url_rule('/hello/', 'hello', hello_world)
app.add_url_rule('/hello/<name>/', 'hello_to', hello_to)
app.add_url_rule('/login/', 'login', login, methods=['POST', 'GET'])


app.add_url_rule('/blog/', 'blog', blog)
app.add_url_rule('/blog/<int:bid>/', 'blog_details', blog_details)
app.add_url_rule('/version/<float:ver>/', 'version', version)
app.add_url_rule('/to/<path:path>/', 'path_to', path_to)


@app.route("/site-map")
def site_map():
    return generate_sitemap(app.url_map)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
