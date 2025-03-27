class Car:
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Иницализирует атрибуты описание автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возврашает отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит данные о пробеге машины в милях"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """Устанавливает заданное значение на одометре."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can`t roll back an odometer!")

    def increment_odometer(self, miles):
        """Уведичивает показатели однометра с заданным приращением"""
        self.odometer_reading += miles

class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=40):
        """Инициализирует атрибуты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит данные о приблизительном запасе хода для аккумулятора"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This is car can go about {range} miles on a full charge")


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("This car doesn't have a gas tank!")

