people = {
    'tima': {
        'firstname': 'Tima',
        'lastname': 'Kad',
        'location': 'kz',
    },
    'aldik': {
        'firstname': 'aldik',
        'lastname': 'kad',
        'location': 'kz'
    },
    'raim': {
        'firstname': 'raim',
        'lastname': 'kad',
        'location': 'kz',
    },
}

for person, person_info in people.items():
    print(f"{person.title()}:")
    for tamplate, info in person_info.items():
        print(f"\t{tamplate.title()}: {info.title()}")

