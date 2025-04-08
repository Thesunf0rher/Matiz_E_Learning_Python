from pathlib import Path
import json

path = Path('text_json/username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}")