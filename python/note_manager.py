class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)

    def get_notes(self):
        return self.notes

    def remove_note(self, title):
        self.notes = [note for note in self.notes if note.get_title() != title]

    def display_notes(self):
        return "\n".join([f"{note.get_title()}: {note.get_content()}" for note in self.notes])
