class Restaurant:
    """Создает класс ресторан и его поведение"""

    def __init__(self, restaurant_name, cuisine_type: str):
        """Данные о ресторане и тип кухни"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Выводит информацию о ресторане"""
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}\n")

    def read_number_served(self):
        """Выводит информацию о количесвто гостей."""
        print(f"В этом ресторане обслужено {self.number_served} гостей!")

    def set_number_served(self,guests):
        """Меняет количество обслуженных гостей"""
        if guests < 0:
            print("Число гостей не может быть отрицательным")
        else:
            self.number_served = guests

    def increment_number_served(self, guest):
        """Увеличивает количество гостей"""
        if guest < 0:
            print("Число гостей не может быть отрицательным")
        else:
            self.number_served += guest

    def open_restaurant(self):
        """Открывает ресторан"""
        print(f"Ресторан  {self.restaurant_name} открыт")

restaurant = Restaurant('rit', "Итальянская")

print(f"{restaurant.restaurant_name} - {restaurant.cuisine_type}\n")

restaurant.set_number_served(1000)
restaurant.increment_number_served(100)

restaurant.read_number_served()