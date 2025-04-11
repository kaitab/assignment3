"""

At first I had lazy=True but then ran into a weird error:

sqlalchemy.orm.exc.DetachedInstanceError: Parent instance <Note at 0x10dab1c90> is
not bound to a Session; lazy load operation of attribute 'comments' cannot proceed
(Background on this error at: https://sqlalche.me/e/20/bhk3)

This happend on the very first note in the list. And it happend while running the 
find() method on the NoteBook, which uses note.comments. Which is also used here in
the delete() clas method, maybe should push the find functionality down from the
NoteBook to the model. For now, not doing lazy loading.

"""

from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func

from . import app, db


class Note(db.Model):

    identifier = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(), unique=False, nullable=False)
    #comments = db.relationship('Comment', backref='note', lazy=False)
    comments = db.relationship('Comment', backref='note', cascade='all, delete', lazy=False)

    def __repr__(self):
        return f"Note({self.identifier}, '{self.title}')"

    @classmethod
    def get(cls, title: str):
        return Note.query.filter_by(title=title).first()

    @classmethod
    def get_all(cls):
        with app.app_context():
            notes = Note.query.all()
            return notes

    @classmethod
    def add(cls, title: str, content: str):
        try:
            note = Note(title=title, content=content)
            db.session.add(note)
            db.session.commit()
            return note
        except IntegrityError as e:
            db.session.rollback()
            return None

    @classmethod
    def delete(cls, title: str):
        note = Note.get(title)
        #for comment in note.comments:
        #    db.session.delete(comment)
        db.session.delete(note)
        db.session.commit()


class Comment(db.Model):

    identifier = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    content = db.Column(db.String(), unique=False, nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.identifier'), nullable=False)

    def __repr__(self):
        content = self.content[:50]
        return f"Comment({self.identifier}, {self.timestamp} {self.note_id} '{content}')"
 
    @classmethod
    def add(cls, note_title: str, content: str):
        try:
            note = Note.query.filter_by(title=note_title).first()
            comment = Comment(content=content, note_id=note.identifier)
            db.session.add(comment)
            db.session.commit()
            return comment
        except IntegrityError as e:
            db.session.rollback()
            return None
