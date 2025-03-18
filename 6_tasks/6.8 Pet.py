pets = {
    'ponchik': {
        'pet': 'dog',
        'master': 'raim',
    },
    'barsik': {
        'pet': 'cat',
        'master': 'Al',
    },
    'leo': {
        'pet': 'cat',
        'master': 'Rak',
    },
}

for nickname, pet_info in pets.items():
    print(f"{nickname.title()}:")
    for tamplate, info  in pet_info.items():
        print(f"\t{tamplate.title()}: {info.title()}")