
from . import model

class NoteBook:

    def __init__(self):
        self.notes = model.Note.get_all()

    def __str__(self):
        return f'<NoteBook with {len(self)} notes>'

    def __len__(self):
        return len(self.notes)

    def __getitem__(self, title: str):
        return model.Note.get(title)

    def note_names(self):
        return sorted([note.title for note in self.notes])

    def add(self, note_title: str, note_content: str):
        note = model.Note.add(note_title, note_content)
        if note is not None:
            self.notes.append(note)

    def add_comment(self, note_title: str, comment:str):
        # As a side effect this makes the comment available on the note
        comment = model.Comment.add(note_title, comment)

    def delete(self, note_title: str):
        model.Note.delete(note_title)
        self.notes = [n for n in self.notes if n.title != note_title]

    def find(self, term: str):
        term = term.lower()
        notes = []
        for note in self.notes:
            if term in note.title.lower() or term in note.content.lower():
                notes.append(note.title)
            for comment in note.comments:
                if term in comment.content.lower():
                    notes.append(note.title)
        return sorted(set(notes))
