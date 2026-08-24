#PAGE 192
#6-1. Person
person = {"first name": "Erastus", "last name": "Michael", "age": 28, "city": "Enugu"}

def person_info(dict):
    for key, value in dict.items():
        print(f"{key:<12} -> {value}")

person_info(person)       
   


#6-3. Glossary:
glossary = {"f-sting": "This is the equivalent of template literal in JS which is used to combine string and variable in one line", "set": "an unordered list of data types that is mutable", "List": "A list of ordered items that is mutable", "Dictionary": "A list of key value pairs", "Function": "A piece of reusable code that does a particular task"}
    
def display_dict(dict):
    for key, value in dict.items():
        print(f"{key:<12}{value}\n")

display_dict(glossary)




#PAGE 201
#6-4. Glossary 2:
glossary_2 = {
                "f-sting": "This is the equivalent of template literal in JS which is used to combine string and variable in one line",
                "set": "an unordered list of data types that is mutable",
                "List": "A list of ordered items that is mutable", "Dictionary": "A list of key value pairs",
                "Function": "A piece of reusable code that does a particular task",
                "identation": "refers to the spaces at the beginning of a code line",
                "Global variable": "Variable that belongs to the global scope",
                "Attribute": "A variable or method that belongs to an object or class. Accessed using dot notation",
                "Break": "A statement that exits a loop immediately, skipping any remaining iterations",
                "Built-in Function": "A function provided by Python itself that is always available without importing anything. E.g print(), len(), type()",

             }
    
def display_dict(dict):
    for key, value in dict.items():
        print(f"{key:<12}{value}\n")

display_dict(glossary_2)




#6-5. Rivers:
rivers = {
          "Nile": "Egypt", 
          "Congo": "Central Africa", 
          "Mississippi-Missouri": "North America", 
          "Niger": "West Africa-Biafra"
          }

def describe_river():
    for key, value in rivers.items():
        print(f"{key} run through {value}.")

describe_river()







#6-2. Favorite Numbers:
favorite_number_of_friends = {"Peter": 21, "Onuchukwu": 30, "Emmanuel": 69, "Erastus": 47}

def favorite_number(favorite_num):
    for key, value in favorite_num.items():
        print(f"{key}:\t{value}")

favorite_number(favorite_number_of_friends)



#PAGE 261
#8-1. Message:
def display_message():
    print("I am learning how to define a function")
display_message()


#8-2. Favorite Book:
def favorite_book(title):
    print(f"One of my favorite book is {title}")
favorite_book("7 Habits of Highly Effective People")





#8-3. T-Shirt
def make_shirt(size, msg):
    print(f"The size of the shirt you have chosen is {size} and you want '{msg}' to be printed on it")

make_shirt("XL","This is Nnamdi learning Python")

make_shirt(size="XL", msg="Backend Developer")

print()
print("Excersie 8-4")
#8.4. Large Shirts:
def make_shirt(size = "large", msg = "I love Python"):
    print(f"The size of the shirt you have chosen is {size} and you want '{msg}' to be printed on it")

make_shirt("large")
make_shirt("medium")
make_shirt("XXL", "I'm a good backend programmer")

print()
print("Excersie 8-5")
#8-5. Cities:
def describe_city(city, country = "Biafraland"):
    print(f"{city} is in {country}")


describe_city("Enugu")
describe_city("Abuja")
describe_city("Lagos")


#PAGE 255

#8-6. City Names:
def city_country(city, country):
    print(f"{city}, {country}")

print(city_country("Enugu", "Nigeria"))
print(city_country("Nairobi", "Kenya"))
print(city_country("Accra", "Ghana"))


#8-7. Album:
def make_album(artist, album, songs=None):
    record = {"artist": artist, "Album title": album, "Number of songs": songs}
    return record

first_album = make_album("Flavour", "Nabania")
second_album = make_album("Inspirational singers", "Helleluyah")
third_album = make_album("Harmony singers", "Fortress God")
fourth_album = make_album("Heavenly Echoes", "If God be for Us", 20)

print(first_album)
print(second_album)
print(third_album)
print(fourth_album)



#8-8. User Albums:
def make_album(artist, album, songs=None):
    while True:
        print("Please enter your favorite artist name and album or type 'quit' to stop")
        artist_name = input("Artist name\t")
        if artist_name == "quit":
            break
        album_title = input("Album title\t")
       
        print({"Artist": artist_name, "Album": album_title}) 
  
make_album("artist_name", "album_title")


#PAGE 261
#8-9. Messages:
messages = ["morning time", "midday time", "noon time", "evening time", "twilight time", "night time", "midnight time"]
def show_messages(msg):
    print(msg)

show_messages(messages)



#8-10. Sending Messages:
def send_messages(messages, sent_messages):
    while len(messages) > 0:
        popped_msg = messages.pop()
        print(f"Adding {popped_msg} to the new list")
        sent_messages.append(popped_msg)
        

sent_messages = []
print(send_messages(messages, sent_messages))
print(messages)
print(sent_messages)



#8-11. Archived Messages:
print(send_messages(messages[:], sent_messages))
print(f"Old messages list: {messages}")
print(f"New message list: {sent_messages}")




#PAGE 266
#8-12. Sandwiches:
def sandwiche_order(*sandwich_addendum):
    print(f"Adding {sandwich_addendum} to your sandwich")

print(sandwiche_order("pepperoni", "shrimp", "beef","doritos"))
print(sandwiche_order("pepperoni", "shrimp", "beef","doritos", "seafood"))
print(sandwiche_order("pepperoni", "shrimp", "beef","doritos", "seafood", "landfood"))



#8-13. User Profile:
def build_profile(first, last, **user_info): 
    """
    Build a dictionary containing everything we know about a user.
    """ 
    user_info['first_name'] = first 
    user_info['last_name'] = last 
    return user_info 


user_profile = build_profile('Peter', 'Ileh', 
                             location='Enugu',
                             skill='Python developer', 
                             field='IT') 
print(user_profile)



#8-14. Cars:
def car_make(manufacturer, model, **other_car_features):
    other_car_features["car manufacturer"] = manufacturer
    other_car_features["Car model"] = model
    return other_car_features

car1 = car_make("Toyota", "camry", color="white", shift_stick=True, all_wheel_drive=False)
print(car1)




#PAGE 342
#10-6. Addition

def addition():
    try:
        number_1 = int(input("Enter the first number\t"))
        number_2 = int(input("Enter the second number\t"))

    except ValueError:
        print("Sorry, the value you enter is not a number. Try again")

    else:
        return number_1 + number_2

result = addition()
print(result)




#10-5. Guest Book:
from pathlib import Path

path = Path("guest_book.txt")

def guest():
    
    while True:
        name = str(input("Enter your name\t"))
        print(name)
        path.write_text(name)

        if name == "quit":
            break
guest() 





#10-8. Cats and Dogs
with open("cat.txt" "w") as file:
    file.write("mongo", "debe", "meaw", "busu")

with open("dog.txt" "w") as file:
    file.write("Bingo", "ekuke", "")

