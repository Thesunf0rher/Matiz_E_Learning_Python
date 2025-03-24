def print_models(unprinted_designs, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым
    Каждая модель после печати перемещается в complated_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design.title()}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Выводит инфоормацию обо всех напечатнных моделях."""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(f"\t{completed_model.title()}")


unprinted_designs = ['phone case', 'robot pedant', 'dodecahedron']
completed_models = []


print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)