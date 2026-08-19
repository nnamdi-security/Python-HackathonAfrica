#PAGE 108
# guest_list = ["Mr. Solomon", "Osita", "Favour", "Emmanuel", "Lilian", "Ekene"]
# for guest in guest_list:
#     print(f"Hello {guest}, you're invited to dinner in my place by 6PM tomorrow evening. Thank you")
#     print()


# print()
# print()
    

# for guest in guest_list:
#      print(f"{guest_list[1]} and {guest_list[2]} just informed me they won't be a ble to make it to the dinner")
#      print()


# guest_list.insert( 1, "Comfort")
# guest_list.insert(2, "David Ani")

# print()
# print()

# print(guest_list)

# for guest in guest_list:
#      print(f"{guest} is still interested in coming to the dinner")


# print()
# print()
# print("I have found a bigger table in this new nice rstaurant where we can go and have dinner")


# print()
# print()
# guest_list.insert(0, "Amaranchild")
# guest_list.insert(4, "Okechukwu")
# guest_list.append("Mathias")

# for guest in guest_list:
#      print(f"Hello {guest}, you're invited to dinner in my place by 6PM tomorrow evening. Thank you")
#      print()


# print("I'm sorry to inform you all that I can only invite two people to the dinner")
# print(guest_list)



# while len(guest_list) > 2:
#      removed_guest = guest_list.pop()
#      print(f"I am sorry to inform you {removed_guest} that we will not be able to accommodate you for the dinner. Thank you for your understanding")
    
# del guest_list[0:2]
# print(guest_list)













#PAGE 113
tourist_location = ["Ilujoka", "Iluboro", "Abuja", "Lagos", "Osun", "Russia"]

print(tourist_location)

sorted_list = sorted(tourist_location)
print(sorted_list)
print(tourist_location)

sorted_list.sort(reverse=True)
print(sorted_list)
print(tourist_location)

tourist_location.reverse()
print(tourist_location)

tourist_location.sort() #You cannot reassign .sort() to a variable
print(tourist_location)




#PAGE 134
#Counting to Twenty
for number in range(1, 21):
    print(number)


#One Million
for number in range(1, 1000001):
     print(number)


#Summing a Million
number = [i for i in range(1, 1000001)]
print(max(number))
print(min(number))
print(sum(number))


#Odd Numbers
for odd_number in range(1, 21, 2):
     print(odd_number)


#Multiples of 3
for number in range(1, 11):
     print(number * 3)


# Cubes
for cube_num in range(1, 11):
     print(cube_num ** 3)


#List Comprehensions
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)







#PAGE 141
#Slices
my_food = ["Yamarita", "Egusi", "Edikaikong", "Beans", "Rice", "Chicken pie"]

print(f"The first three items in the list are: {my_food[0:3]}")
print(f"Three items from the middle of the list are: {my_food[1:4]}")
print(f"The last three items in the list are: {my_food[3:6]}")


friend_food = my_food[:]

my_food.append("Garri")
friend_food.append("Akpu")

print("My favorite foods are: ")
for food in my_food:
     print(food)

print("My friend favorite foods are:")
for food in friend_food:
     print(food)



#PAGE 145
#Buffet
amala_joint = ("Ewedu", "Gbegiri", "Ata dindin", "Efo-riro", "Asun")
for food in amala_joint:
     print(food)

#print(amala_joint.append("amala felifeli"))

index = 1
new_food = ("Ewa gan", "Eba")
amala_joint_new_menu = amala_joint[:index] + new_food + amala_joint[index+1:]
for food in amala_joint_new_menu:
     print(food)






#PAGE 161
car = "subaru"
age = 25
country = "Nigeria"
score = 85
is_student = True

print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs country == 'Nigeria'? I predict True.")
print(country == "Nigeria")

print("\nIs score > 80? I predict True.")
print(score > 80)

print("\nIs is_student == True? I predict True.")
print(is_student == True)

print("\nIs car == 'Toyota'? I predict False.")
print(car == "Toyota")

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs country == 'Ghana'? I predict False.")
print(country == "Ghana")

print("\nIs score < 50? I predict False.")
print(score < 50)

print("\nIs is_student == False? I predict False.")
print(is_student == False)

#More Conditional Test
# 1. Tests for equality and inequality with strings

name = "Python"

print("Is name == 'Python'? I predict True.")
print(name == "Python")

print("\nIs name == 'Java'? I predict False.")
print(name == "Java")

print("\nIs name != 'Java'? I predict True.")
print(name != "Java")

print("\nIs name != 'Python'? I predict False.")
print(name != "Python")


# 2. Tests using the lower() method

language = "PYTHON"

print("\nIs language.lower() == 'python'? I predict True.")
print(language.lower() == "python")

print("\nIs language.lower() == 'java'? I predict False.")
print(language.lower() == "java")


# 3. Numerical tests

age = 25

print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age == 30? I predict False.")
print(age == 30)

print("\nIs age != 30? I predict True.")
print(age != 30)

print("\nIs age != 25? I predict False.")
print(age != 25)

print("\nIs age > 20? I predict True.")
print(age > 20)

print("\nIs age > 30? I predict False.")
print(age > 30)

print("\nIs age < 30? I predict True.")
print(age < 30)

print("\nIs age < 20? I predict False.")
print(age < 20)

print("\nIs age >= 25? I predict True.")
print(age >= 25)

print("\nIs age >= 30? I predict False.")
print(age >= 30)

print("\nIs age <= 25? I predict True.")
print(age <= 25)

print("\nIs age <= 20? I predict False.")
print(age <= 20)


# 4. Tests using the 'and' keyword

age = 25
country = "Nigeria"

print("\nIs age > 18 and country == 'Nigeria'? I predict True.")
print(age > 18 and country == "Nigeria")

print("\nIs age > 30 and country == 'Nigeria'? I predict False.")
print(age > 30 and country == "Nigeria")


# 5. Tests using the 'or' keyword

score = 85

print("\nIs score > 90 or score == 85? I predict True.")
print(score > 90 or score == 85)

print("\nIs score > 90 or score < 50? I predict False.")
print(score > 90 or score < 50)


# 6. Test whether an item is in a list

fruits = ["apple", "banana", "orange", "mango"]

print("\nIs 'banana' in the fruits list? I predict True.")
print("banana" in fruits)

print("\nIs 'grape' in the fruits list? I predict False.")
print("grape" in fruits)


# 7. Test whether an item is NOT in a list

print("\nIs 'grape' not in the fruits list? I predict True.")
print("grape" not in fruits)

print("\nIs 'apple' not in the fruits list? I predict False.")
print("apple" not in fruits)









#PAGE 171
alien_color = "green"

if alien_color == "green":
     print("You got earned 5 points")

alien_color = "red"
if alien_color == "orange":
     print()
alien_color = "green"
if alien_color == "green":
     print("You got earned 5 points")
else:
     print("You got earned 10 points")

alien_color = "yellow"
if alien_color == "green":
     print("You got earned 5 points")
else:
     print("You got earned 10 points")


alien_color = "green"
if alien_color == "green":
     print("You got earned 5 points")
elif alien_color == "yellow":
     print("You got earned 10 points")
elif alien_color == "red":
     print("You just earned 15 points")


alien_color = "yellow"
if alien_color == "green":
     print("You got earned 5 points")
elif alien_color == "yellow":
     print("You got earned 10 points")
elif alien_color == "red":
     print("You just earned 15 points")


alien_color = "red"
if alien_color == "green":
     print("You got earned 5 points")
elif alien_color == "yellow":
     print("You got earned 10 points")
elif alien_color == "red":
     print("You just earned 15 points")







#Stages of Life
age = 25

if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an egban.")



#Favorite Fruit
favorite_fruits = ["mango", "banana", "orange"]

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "apple" in favorite_fruits:
    print("You really like apples!")

if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "orange" in favorite_fruits:
    print("You really like oranges!")

if "grape" in favorite_fruits:
    print("You really like grapes!")




#PAGE 177
username = ["Admin", "Lilian", "Oke", "Okeke", "Shade", "Bunmi"]

for user in username:
     if user == "Admin":
          print("Hello admin, would you like to see a status report?")
     else:
        print(f"Welcome back {user}")


if len(username) == 0:
     print("We need to find some users!")




#Checking Usernames
current_users = ["Amara", "Lilian", "Ezeh", "Anthony", "Majesty", "James"]
new_users = ["Ijeoma", "James", "Peter", "Chizoba", "Lilian", "Ezeh", "Ogechi"]

for user in current_users:
     lowercase_current_user = user.lower
for user in new_users:
     if user in current_users or user == lowercase_current_user:
          print(f"Sorry {user}, this username has already been used.")
     else:
          print("Username is available")


#Ordinal Number
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in ordinal_numbers:
     if number == 1:
          print(f"{number}st")
     elif number == 2:
          print(f"{number}nd")
     elif number == 3:
          print(f"{number}rd")
     else:
          print(f"{number}th")







#PAGE 228
topping = input("Enter a pizza topping or 'quit' to finish\t:")

while topping != "quit":
    print(f"I'll add {topping} to your pizza.")
    topping = input("Enter another topping or 'quit' to finish:\t")

print("Your pizza is ready!")


#Movie Tickets
while True:
    age = int(input("Enter your age or enter 0 to quit: "))

    if age == 0:
        print("Thank you. Goodbye!")
        break
    elif age < 3:
        print("Your movie ticket is free.")
    elif age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")



age = int(input("Enter your age (-1 to quit): "))

while age != -1:
    if age < 3:
        print("Your movie ticket is free.")
    elif age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")

    age = int(input("Enter your age (-1 to quit): "))


active = True

while active:
    age = int(input("Enter your age or 0 to quit: "))

    if age == 0:
        active = False
    elif age < 3:
        print("Your movie ticket is free.")
    elif age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")

print("Thank you for using the movie ticket system.")


while True:
    age = input("Enter your age (or type 'quit' to stop): ")

    if age.lower() == "quit":
        break

    age = int(age)

    if age < 3:
        print("Your movie ticket is free.")
    elif age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")

print("Thank you for using the movie ticket system.")


#Infinite loop
count = 1
while True:
     print(count)
     count += 1



#PAGE 233
sandwich_orders = ["tuna", "chicken", "beef", "cheese"]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)



sandwich_orders = [
    "tuna",
    "pastrami",
    "chicken",
    "pastrami",
    "beef",
    "pastrami",
    "cheese"
]

finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)

    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)




responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("Would you like to let another person respond? (yes/no): ")

    if repeat.lower() == "no":
        polling_active = False

print("\n--- Dream Vacation Poll Results ---")

for name, place in responses.items():
    print(f"{name} would like to visit {place}.")