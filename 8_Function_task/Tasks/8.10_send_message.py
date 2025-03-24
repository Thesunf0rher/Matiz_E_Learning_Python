def show_message(short_texts):
    """Выводит список сообщение"""
    print(f"\nИсходное сообщение:")
    for short_text in short_texts:
        print(f"\t{short_text}")

def send_messages(short_texts, send_messages):
    """Перемешает сообщение в новый список и выводит их"""
    print("\nОтправленные сообщение:")
    while short_texts:
        short_text = short_texts.pop(0)
        print(f"\t{short_text}")
        send_messages.append(short_text)

short_texts = ['Hello', 'How are you?', "I'm fine"]
send_messages = []

show_message(short_texts)
send_message(short_texts[:], send_messages)

print()
print(short_texts)
print(send_messages)