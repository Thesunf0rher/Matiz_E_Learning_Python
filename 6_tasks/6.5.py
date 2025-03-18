rivers = {
    'nile': 'egypt',
    'amazon': 'peru',
    'mississippi': 'usa',
}

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}\n")

for river in sorted(rivers.keys()):
    print(f"River: {river.title()}\n")

for country in sorted(rivers.values()):
    print(f"Country: {country.title()}\n")