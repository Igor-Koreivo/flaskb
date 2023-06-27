from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return 'Hello World'


@app.route('/abaut')
def abaut():
    return 'Abaut Us'


@app.route('/page')
def page():
    return 'Page Us'


@app.route('/user/<string:name>>/<int:id>')
def user(name, id):
    return 'User page' + name + "-" + id


if __name__ == '__main__':
    app.run(debug=True)
