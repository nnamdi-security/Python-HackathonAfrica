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