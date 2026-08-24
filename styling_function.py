def user_profile(first, last, **user_info):
    """
    This is function that takes first and last name as postional arguments and user info as keyword arguments. It then print all
    """
   
    print(f"first name: {first:<12}\nLast name: {last}")
    for key, value in user_info.items():
        print(f"{key:<12}: {value}")


def print_models(unprinted_designs, completed_models): 
    """ 
    Simulate printing each design, until none are left. 
    Move each design to completed_models after printing. 
    """ 
    while unprinted_designs: 
        current_design = unprinted_designs.pop() 
        print(f"Printing model: {current_design}") 
        completed_models.append(current_design) 



def show_completed_models(completed_models): 
    """Show all the models that were printed.""" 
    print("\nThe following models have been printed:") 
    for completed_model in completed_models: 
        print(completed_model) 
