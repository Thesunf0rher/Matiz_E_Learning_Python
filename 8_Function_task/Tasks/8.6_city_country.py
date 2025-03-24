def city_country(city, country):
    """Возвращает информацию о городе и стране"""
    city_c = f"{city}, {country}"
    return city_c.title()

print(city_country('santiago', 'chile'))
print(city_country('astana', 'kazakhstan'))
print(city_country('moscow', 'russia'))
