favorite_languages = {
    'jen': 'python',
    'sarah': '',
    'edward': '',
    'phil': '',
    'zhalgas': 'c#',
    'alimkhan': 'python',
}

for name, language in favorite_languages.items():
    if language == '':
        print(f"{name.title()} напишите пожалуйста любой язык программирование.")
    else:
        print(f"{name.title()} спасибо что прошли опрос. Ваш любимый язык {language.title()}.")