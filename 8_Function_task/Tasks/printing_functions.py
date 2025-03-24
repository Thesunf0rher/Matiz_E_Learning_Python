def make_car(manufacturer, model_name, **car_info):
    """Создает словарь с информацией об автомобиле"""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info
