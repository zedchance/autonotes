# autonotes

A tool to automatically create LaTeX documents, intended for lecture notes.

## Use

Run `autonotes.py` with the directory name as the first argument:

```bash
python3 autonotes.py class_name
```

This creates a new directory called `class_name` (or whatever it was named) and makes a master file called `master.tex`.
When you want to create a new entry, run `new_note.py`.

```bash
python3 new_note.py
```

This creates a new .tex file (using the date as a filename) and adds it to the master.tex file automatically.
