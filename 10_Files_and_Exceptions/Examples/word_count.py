from pathlib import Path

def count_words(path):
    """Подсчитывает приблизительное количество строк в файле."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

file_names = ['alice.txt', 'text_files/siddhartha.txt', 'text_files/moby_dick.txt', 'text_files/little_women.txt']
for filename in file_names:
    path = Path(filename)
    count_words(path)