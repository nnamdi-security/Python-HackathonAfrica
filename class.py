def divider(heading):
    print()
    print("=" * 23)
    print(heading)
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