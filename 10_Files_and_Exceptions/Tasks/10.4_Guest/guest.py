from pathlib import Path

path = Path("guest.txt")

guest = input("Enter a name: ").strip()

if guest:
    path.write_text(guest)
    print(f"Name '{guest}' saved in guest.txt!")
else:
    print("Name cannot be empty.")