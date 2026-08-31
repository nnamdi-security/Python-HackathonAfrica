def divider(heading):
    print()
    print("=" * 23)
    x = heading.upper()
    print(x)
    print("=" * 23)
    

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_types = cuisine_type

    def describe_restaurant(self):
        print(f"My restaurant name is {self.restaurant_name} and the cuisine type is {self.cuisine_types}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business")

divider("9-1. Restaurant:")
restaurant = Restaurant("La-Veranda", "italian cuisine")

print(f"My restaurant name is {restaurant.restaurant_name}")
print(f"My cuisine type is {restaurant.cuisine_types}")


divider("9-2. Three Restaurants:")
restaurant_1 = Restaurant("La-Veda-Loca", "vatican city cuisine")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("MamaPutOnline", "Mama-Africa cuisine")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("Iya Meta", "ofe nmanu cuisine")
restaurant_3.describe_restaurant()


divider("9-3. Users:")
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 28
        self.username = first_name.upper()
        self.email = first_name + "@gmail.com"
        self.country = "Ghana"

    def describe_user(self):
        print(f"First name: {self.first_name} | Last name: {self.last_name} | Age: {self.age} | Username: {self.username} | Country: {self.country}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}. Happy to have you in our class")


user_1 = User("Amara", "Ekwebelem")
print(user_1.first_name)
print(user_1.last_name)
print(user_1.age)
print(user_1.username)
print(user_1.country)
print(user_1.email)
user_1.greet_user()

user_2 = User("Peter", "Onwuegbulam")
user_2.describe_user()

user_2.greet_user()

user_3 = User("Big-Steph", "Ayanfunogu")
user_3.greet_user()





#PAGE 291
divider("9-4. Number Served:")

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


restaurant_4 = Restaurant("Amala Joint", "African cuisine")
print(restaurant_4.number_served)

restaurant_4.number_served = 67
print(restaurant_4.number_served)


print(restaurant_4.set_number_served(126))

print(restaurant_4.increment_number_served(13))



divider("9-5. Login Attempts")

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


user_4 = User("Nnamdi", "Ileh")
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
print(user_4.login_attempts)

user_4.reset_login_attempts()
print(user_4.login_attempts)




divider("9-6. Ice Cream Stand")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = ["Vanilla", "chocolate", "strawberry"]

    def ice_cream_flavors(self):
        print(f"Here are the available flavors: ")
        for flavor in self.flavors:
            print(f"\n{flavor}")
                


ice_cream = IceCreamStand("Iya Basira", "Ogbomoso cuisine")
ice_cream.ice_cream_flavors()


divider("9-7. Admin")
# class Admin(User):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)

#         self.privileges = ["can add post", "can delete post", "can ban user"]

#     def show_privileges(self):
#         print("The Administrator can do the following:")
#         for privilege in self.privileges:
#             print(privilege)

# admin = Admin("Amara", "Ekwebelem")
# admin.show_privileges()



divider("9-8. Privileges")
class privileges:
    def __init__(self):
        self.privileges = ["add post", "delete post", "ban user"]

    def show_privileges(self):
            print("The Administrator can do the following:")
            for privilege in self.privileges:
                print(f"-> {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.privileges = privileges()



admin = Admin("Amara", "Ekwebelem")
admin.privileges.show_privileges()



divider("9-9. Battery Upgrade")
class Car: 
    """A simple attempt to represent a car.""" 
    def __init__(self, make, model, year): 
        """Initialize attributes to describe a car.""" 
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 
    def get_descriptive_name(self): 
        """Return a neatly formatted descriptive name.""" 
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title() 
    def read_odometer(self): 
        """Print a statement showing the car's mileage.""" 
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): 
        """Set the odometer reading to the given value.""" 
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles): 
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading += miles

class Battery: 
    """A simple attempt to model a battery for an electric car.""" 
    def __init__(self, battery_size=40): 
        """Initialize the battery's attributes.""" 
        self.battery_size = battery_size 

    def describe_battery(self): 
        """Print a statement describing the battery size.""" 
        print(f"This car has a {self.battery_size}-kWh battery.") 

    def get_range(self): 
        """Print a statement about the range this battery provides.""" 
        if self.battery_size == 40: 
            range = 150 
        elif self.battery_size == 65: 
            range = 225 
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self, battery_size):
        if battery_size != 65:
            battery_size = 65


class ElectricCar(Car): 
    """Represent aspects of a car, specific to electric vehicles.""" 
    def __init__(self, make, model, year, battery_size=40): 
        """
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an electric car. 
        """
        super().__init__(make, model, year)

        self.battery = Battery() 
        self.battery_size = battery_size



my_leaf = ElectricCar('nissan', 'leaf', 2024) 

my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery(40)



#PAGE 312
divider("9-10. Imported Restaurant")

