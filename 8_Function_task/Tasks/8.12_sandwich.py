def sandwich_info (*components):
    """Выводит компонент буте"""
    print("Sandwich components:")
    for component in components:
        print(f"- {component}")
    print("\n")

sandwich_info('meat','salad','sauce',)
sandwich_info('salad','chicken','tomato',)
sandwich_info('avocado','salad','tomato',)