import tkinter as tk
from note import Note
from password_manager import PasswordManager

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes and Passwords Manager")

        self.add_note_button = tk.Button(root, text="Add Note", command=self.add_note_window)
        self.view_notes_button = tk.Button(root, text="View Notes", command=self.view_notes)
        self.view_notes_button.pack()


        self.add_note_button.pack()

    def add_note_window(self):
        # Create a new window for adding a note
        note_window = tk.Toplevel(self.root)
        note_window.title("Add Note")

        title_label = tk.Label(note_window, text="Title:")
        title_label.pack()
        title_entry = tk.Entry(note_window)
        title_entry.pack()

        content_label = tk.Label(note_window, text="Content:")
        content_label.pack()
        content_entry = tk.Text(note_window, height=10, width=30)
        content_entry.pack()

        add_button = tk.Button(note_window, text="Add", command=lambda: self.add_note(title_entry.get(), content_entry.get("1.0", tk.END).strip()))
        add_button.pack()

    def add_note(self, title, content):
        # Add the note using NoteManager
        note_manager.add_note(title, content)


    def view_notes(self):
        notes_display = tk.Toplevel(self.root)
        notes_display.title("Notes")

        notes_text = tk.Text(notes_display, height=15, width=50)
        notes_text.pack()

        notes = note_manager.display_notes()
        notes_text.insert(tk.END, notes)

        close_button = tk.Button(notes_display, text="Close", command=notes_display.destroy)
        close_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
