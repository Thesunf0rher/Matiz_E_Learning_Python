from pathlib import Path
import json

path = Path('text_json/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)