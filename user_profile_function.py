#PAGE 273
#8-16. Imports:
#This is a program I wrote that has one function in it

# def user_profile(first, last, **user_info):
#     user_info["fist name"] = first
#     user_info["last name"] = last

#     return user_info

# my_profile = user_profile("Nnamdi", "Ileh", location="Enugu", Language=["Igbo", "Yoruba", "English"])

# print(my_profile)




def user_profile(first, last, **user_info):
   
    print(f"first name: {first:<12}\nLast name: {last}")
    for key, value in user_info.items():
        print(f"{key:<12}: {value}")
    


