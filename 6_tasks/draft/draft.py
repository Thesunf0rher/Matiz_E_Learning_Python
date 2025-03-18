# alien_0 = {
#     'color': 'green',
#     'points': 5,
# }
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# alien_0['speed'] = 'medium'
# alien_0['color'] = 'red'
#
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# del alien_0['color']
# alien_0['color'] = 'blue'
#
# alien_color = alien_0['color'].title()
#
# del alien_0 ['color']
#
# a_color = alien_0.get('color', 'Такого ключа нету')
#
# print(a_color)
# print(alien_color)
# print(alien_0)

# user_0 ={
#     'username': 'efermi',
#     'first': 'enroico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print(f"Key:{key}\nValue:{value.title()}")

# for name in user_0.keys():
#     print(name)

# for name in user_0.keys():
#     print(name)

# for key in sorted(user_0.keys()):
#     print(key)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())