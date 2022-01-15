from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import enum
import json

app = Flask(__name__)

# Consider format improvements via https://stackoverflow.com/a/48316009
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://astrodigenous:lilith31@mysql.heidiwhite.net/astrodigenous' # '?charset=utf8'

db = SQLAlchemy(app)

class ContentType(enum.Enum):
    audio = 1
    video = 2
    image = 3
    text = 4


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(127), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag: %r>' % self.label


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), unique=True, nullable=False)
    reference_url = db.Column(db.String(256), unique=True, nullable=False)
    content_type = db.Column(db.Enum(ContentType), nullable=False)

    def __repr__(self):
        return '<Resource: %r>' % self.name

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/q', methods=['POST'])
def process_search():
    # query from params
    content_type = request.form.get('contentType')
    search_text = request.form.get('searchText')
    # labels = request.form['labels']

    # pass results to render_template along with template file
    # pseudo-code:
    search = "%{}%".format(search_text)
    results = Resource.query.filter(Resource.name.like(search)).all()
    return render_template("results.html", results=results, search_text=search_text)

@app.route('/tags', methods=['GET'])
def list_tags():
    # See https://stackoverflow.com/a/3325497 for searching example
    return ""
