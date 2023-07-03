from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    title = db.Colum(db.String(100), nullable=False)
    intro = db.Colum(db.String(300), nullable=False)
    text = db.Colum(db.Text(300), nullable=False)
    date = db.Colum(db.DateTime(300), defolt=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' %self.id

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>>/<int:id>')
def user(name, id):
    return 'User page: ' + name + "-" + str(id)


if __name__ == '__main__':
    app.run(debug=True)
