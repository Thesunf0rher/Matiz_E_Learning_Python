from pathlib import Path

list_path = ['alice.txt','little_women.txt','moby_dick.txt','siddhartha.txt']
word_user = input('Enter a word: ').lower()
total_count = 0

for path in list_path:
    try:
        contents = Path(path).read_text(encoding='utf-8').lower()
        word_count = contents.count(word_user)
        print(f"В файле '{path}' найден {word_count} вхождений слова '{word_user}'.")
        total_count +=word_count
    except FileNotFoundError:
        print(f"Файл '{path}' не найден.")

print(total_count)