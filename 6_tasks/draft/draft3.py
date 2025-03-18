# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
#
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       "with the following toppings:")
#
# for topping in pizza['toppings']:
#     print(f"\t{topping}")
from PIL.ImageChops import offset

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c',],
    'edward': ['c++',],
    'phil': ['js', 'python'],
    'Aldo': '',
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language}")
    elif len(languages) == 1:
        print(f"{name.title()}'s favorite language are:")
        for language in languages:
            print(f"\t{language}")
    else:
        print(f"{name} ваш опрос пуст")