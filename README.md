# autonotes

A tool to automatically create LaTeX documents, intended for lecture notes.

## Use

These commands assume that `autonotes` is added to your `PATH` variable.

### `init`

To initialize a new note directory run:

```bash
autonotes init -n name
```

where `name` is the directory name.

This creates a new directory, and creates 2 files: `preamble.tex`, and `master.tex`.
You can optionally specify a path to an existing preamble file using `-p`:

```bash
autonotes init -n name -p preamble.tex
```

### `new`

When you want to create a new entry, run:

```bash
autonotes new
```

inside a directory created by `init`.
This creates a new .tex file, and adds that file to the `master.tex` file using `\input{}`.

### Help

To see usage about a command, use `--help`, for example:

```bash
autonotes --help
autonotes init --help
autonotes new --help
```
