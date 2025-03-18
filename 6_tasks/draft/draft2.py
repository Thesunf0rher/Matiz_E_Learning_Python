# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

aliens = []
#Создал 30 зеленых пришельцев.
for alien_number in range(30):
    new_alien = {
        'id': alien_number,
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }
    aliens.append(new_alien)

#Поменял первые три зеленых пришельца на желтый.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Вывод о данных о первых пяти пришельцах.
for alien in aliens[:5]:
    print(alien)
print("...")

#Вывод количество созданных пришельцев.
print(f"Total number of aliens: {len(aliens)}")

### Остановился на  144стр. Тема "Список в словаре".