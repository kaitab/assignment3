
from flask import request, render_template

from . import app
from .notes import NoteBook


notebook = NoteBook()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'delete' in request.form:
            notebook.delete(request.form['title'])
        else:
            notebook.add(request.form['title'], request.form['content'])
    notes = None
    term = None
    if request.method == 'GET':
        if 'term' in request.args:
            term = request.args['term']
            notes = notebook.find(request.args['term'])
    if notes is None:
        notes = notebook.note_names()
    return render_template('index.html', term=term, notes=notes)


@app.route('/note', methods=['GET', 'POST'])
def note():
    if request.method == 'POST':
        notebook.add_comment(request.form['title'], request.form['content'])
        title = request.form['title']
    if request.method == 'GET':
        title = request.args.get('title')
    note = notebook[title]
    return render_template('note.html', note=note)


"""

curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/note?title=Animals

"""