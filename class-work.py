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
# tourist_location = ["Ilujoka", "Iluboro", "Abuja", "Lagos", "Osun", "Russia"]

# print(tourist_location)

# sorted_list = sorted(tourist_location)
# print(sorted_list)
# print(tourist_location)

# sorted_list.sort(reverse=True)
# print(sorted_list)
# print(tourist_location)

# tourist_location.reverse()
# print(tourist_location)

# tourist_location.sort() #You cannot reassign .sort() to a variable
# print(tourist_location)




#PAGE 134
# Counting to Twenty
# for number in range(1, 21):
#     print(number)


#One Million
# for number in range(1, 1000001):
#      print(number)


# Summing a Million
# number = [i for i in range(1, 1000001)]
# print(max(number))
# print(min(number))
# print(sum(number))


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
