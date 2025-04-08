from pathlib import Path
import json

def creating_favorite_number ():
    favorite_number = input("Введите любимое число: ").strip()
    path = Path('favorite_num.json')
    contents = json.dumps(favorite_number)
    path.write_text(contents, encoding='utf-8')

def tell_favorite_number():
    path = Path('favorite_num.json')
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        favorite_number = json.loads(contents)
        print(f"Я знаю ваше любимое число! Это {favorite_number}")
    else:
        print("Любимое число пока не сохранено")
        creating_favorite_number()

tell_favorite_number()
