# autonotes

A tool to automatically create LaTeX documents, intended for lecture notes.

## Use

These commands assume that `autonotes` is added to your `PATH` variable.

### `init`

To initialize a new note directory named `myNotes` run:

```bash
autonotes init -n myNotes
```

This creates a new directory, and creates 2 files: `preamble.tex`, and `master.tex`.

```
myNotes
├── master.tex
└── preamble.tex
```

You can optionally specify a path to an existing preamble file using `-p`:

```bash
autonotes init -n name -p preamble.tex
```

This will copy the specified preamble file into the created directory.

### `new`

When you want to create a new entry, run:

```bash
autonotes new
```

inside a directory created by `init`.
This creates a new .tex file, and adds that file to the `master.tex` file using `\input{}`.
For example, your directory may look like this now:

```
myNotes
├── entry-20201231.tex
├── master.tex
└── preamble.tex
```

By default, the file will be named `entry-{date}.tex` where date is the current date.
You can change the name by using the `-n` option, for example:

```bash
autonotes new -n lecture
```

will result in

```
myNotes
├── entry-20201231.tex
├── lecture-20201231.tex
├── master.tex
└── preamble.tex
```

### Help

To see usage about a command, use `--help`, for example:

```bash
autonotes --help
autonotes init --help
autonotes new --help
```
