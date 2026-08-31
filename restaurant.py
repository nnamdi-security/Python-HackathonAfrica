class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_types = cuisine_type
        self.number_served = 0


    def set_number_served(self, number_served):
        return number_served
    

    def increment_number_served(self, number_served):
        self.number_served += number_served
        return self.number_served