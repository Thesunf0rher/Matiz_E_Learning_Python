#1
def make_shirt(size, text):
    """"Выводит информацию о футболке"""
    print(f"Size '{size}' shirt")
    print(f"{text} on the shirt")

make_shirt('S', 'Python')
print()
make_shirt(text='RICH', size='M')

#2
def build_profile(first, last, **user_info):
    """Создает словарь с информацией о пользователе"""
    user_info['first_name'] =  first
    user_info['last_name'] =  last
    return user_info

user_1 = build_profile(
                    'Raim','kad',
                          age=19,
                          location='KZ'
                          )

print(user_1)

#3
def show_message(short_texts):
    """Выводит список сообщений"""
    print("\nИсходные сообщения:")
    for short_text in short_texts:
        print(f"\t{short_text}")

def send_messages(short_texts, sent_messages):
    """Перемещает сообщения в новый список и выводит их"""
    print("\nОтправленные сообщения:")
    while short_texts:
        short_text = short_texts.pop(0)
        print(f"\t{short_text}")
        sent_messages.append(short_text)

short_texts = ['Hello', 'How are you?', "I'm fine"]
sent_messages = []

show_message(short_texts)
send_messages(short_texts[:], sent_messages)

print()
print(short_texts)
print()
print(sent_messages)