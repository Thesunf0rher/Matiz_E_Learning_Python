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

show_messages(short_texts)
send_messages(short_texts[:], sent_messages)


print(short_texts)
print(sent_messages)