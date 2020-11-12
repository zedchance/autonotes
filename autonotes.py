import os
import sys
from shutil import copyfile

# Check to see if directory name was supplied
if len(sys.argv) < 2:
    print("Please enter a name for the directory.")
    exit(1)

# Make dir
dir_name = sys.argv[1]
if os.path.isdir(dir_name):
    print(f'Directory "{dir_name}" already exists.')
    exit(2)
print(f'Creating "{dir_name}" directory.')
os.mkdir(dir_name)

# Create master.tex file
print('Creating master.tex file.')
master = open(f'{dir_name}/master.tex', 'w')
master_str = f'% {dir_name} master file\n' \
             '\n' \
             '\\documentclass{article}\n' \
             '\\input{../preamble.tex}\n' \
             '\n' \
             '\\title{' \
             f'{dir_name}' \
             '}\n' \
             '\\date{}\n' \
             '\n' \
             '\\begin{document}\n' \
             '\\maketitle\n' \
             '\\tableofcontents\n' \
             '\\newpage\n' \
             '%BEGIN NOTES\n\n%END NOTES\n' \
             '\\end{document}'
master.write(master_str)
master.close()

# Copy new_note.py into new dir
print(f'Copying new_note.py into {dir_name}')
new_note_script = open('new_note.py', 'r')
note_script = new_note_script.readlines()
new_note_script.close()
copied_new_note_script = open(f'{dir_name}/new_note.py', 'w')
copied_new_note_script.writelines(note_script)
copied_new_note_script.close()
