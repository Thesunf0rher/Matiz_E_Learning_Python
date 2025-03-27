class Restaurant:
    """Создает функцию ресторанах и их поведение"""
    def __init__(self, restaurant_name, cuisine_type: str):
        """Данные о ресторана и тип кухни"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        """Выводит информацию о ресторане"""
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}\n")

    def open_restaurant(self):
        """Открывает ресторан"""
        print(f"Open {self.restaurant_name}")

restaurant1 = Restaurant('rit', "italian")
restaurant2 = Restaurant('bit','italian')
restaurant3 = Restaurant('kit', 'italian')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.open_restaurant()
