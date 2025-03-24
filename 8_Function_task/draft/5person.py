def build_person(first_name, last_name, age=''):
    """"Возвращает словарь с информацией о человеке."""
    person = {'first': first_name, 'last': last_name, 'age': age}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)