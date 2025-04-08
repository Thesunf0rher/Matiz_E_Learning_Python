from pathlib import Path

path = Path("guest.txt")

print("Enter a 'q' to log out")

while True:
    guest = input("Enter a name: ").strip()
    if guest.lower() == 'q':
        break

    print(f"Hello, {guest}!")

    with path.open("a", encoding="utf-8") as file:
        file.write(f"{guest}\n")