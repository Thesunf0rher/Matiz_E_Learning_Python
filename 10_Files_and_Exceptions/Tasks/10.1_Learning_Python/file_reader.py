from pathlib import Path

path = Path('learning_python')
contents = path.read_text(encoding='utf-8')

lines = contents.splitlines()
py_string = ''

for line in lines:
    py_string += line.strip()

print(contents)


