
#8-1. MEssage:
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


#PAGE 25

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

