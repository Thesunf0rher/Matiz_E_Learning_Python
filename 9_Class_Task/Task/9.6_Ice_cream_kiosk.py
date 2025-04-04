class Restaurant:
    """Создает функцию ресторанах и их поведение"""
    def __init__(self, restaurant_name, cuisine_type: str):
        """Данные о ресторана и тип кухни"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Выводит информацию о ресторане"""
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}\n")

    def open_restaurant(self):
        """Открывает ресторан"""
        print(f"Open {self.restaurant_name}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Выводит список доступных сортов мороженного"""
        print(f"В киоске {self.restaurant_name} есть следующие сорта мороженного")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


ice_cram_stand = IceCreamStand('Морожко','Мороженное', ['шоколадное','ванильное',])

ice_cram_stand.display_flavors()