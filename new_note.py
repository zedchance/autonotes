import os
from datetime import date

# Make new note
today = date.today().strftime("%Y%m%d")
filename = f'entry-{today}.tex'
if os.path.exists(filename):
    print("File already exists.")
    exit(1)
file = open(filename, 'w')
print(f'Created {filename}')
new_note_str = f'\\section{today}\n\n'
file.close()

# Open master file
print("Inserting entry into master.tex")
master = open('master.tex', 'r')
lines = master.readlines()
master.close()
end = lines.index("%END NOTES\n")
lines.insert(end, '\\input{'
                  f'{filename}'
                  '}\n')
master = open('master.tex', 'w')
master.writelines(lines)
master.close()
