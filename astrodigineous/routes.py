from flask import render_template
from astrodigineous import app

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/q', methods=['POST'])
def process_search():
    # query from params
    # content_type = request.form['contentType']
    search_text = request.form['searchText']
    # labels = request.form['labels']

    # pass results to render_template along with template file
    # pseudo-code:
    # resorces = Resources.where(labels: labels)
    search = "%{}%".format(search_text)
    results = Resource.query.filter(Resource.name.like(search)).all()
    return render_template("results.html", results=results)

@app.route('/tags', methods=['GET'])
def list_tags():
    # See https://stackoverflow.com/a/3325497 for searching example
    return ""
