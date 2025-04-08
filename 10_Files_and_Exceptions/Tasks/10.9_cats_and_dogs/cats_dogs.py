from pathlib import Path

list_path = ['cats.txt','dogs.txt']

for path in  list_path:
    try:
        contents = Path(path).read_text(encoding='utf-8')
        print(f"{path}:\n{contents}\n")
    except FileNotFoundError:
        pass