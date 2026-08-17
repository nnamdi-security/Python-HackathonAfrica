#Exercise 1 — Declare and Print Variables

instructor_name = "Dr. Seyi Makinde"
student_count = 20
course_name = "Python fundamental"

print(f"My name is Nnamdi and my instructor name is {instructor_name}")
print(f"I am currently learning {course_name}")
print(f"Number of student in class is {course_name}")


# Exercise 2 — Swap Two Variables Without a Third Variable
students_morning = 15
students_evening = 25

print("Before Swap")
print(f"Morning Batch = {students_morning}, Evening Batch = {students_evening}")

print("After Swap")
students_morning, students_evening = students_evening, students_morning
print(f"Morning Batch = {students_morning}, Evening Batch = {students_evening}")


#Exercise 3 — Assign Multiple Variables in One Line
Python = 25, Java = 18; AI = 12


#Exercise 4 — Check the Type of a Variable
age = 25
course_rating = 4.7
new_course_name = "Advanced Python"

print(type(age))
print(type(course_rating))
print(type(new_course_name))


#Exercise 5 — Concatenating Strings
instructor = "Dr. Seyi Makinde"
academy_name = "HackatonAfricademy"
slogan = "We will alright las las"

print("The instructor at" + academy_name + "says:" + " " + slogan)


#Exercise 6 — Convert String to Integer and Vice Versa
string_to_number = "100"
int_number = int(string_to_number)
print(type(int_number))

int_to_string = 42
string_num = str(int_to_string)
print(type(string_num))


#Exercise 7 — Convert Float to Integer and Vice Versa
float_num = 9.75
float_to_int = int(float_num)
int_num = 50
int_to_float = float(int_num)

print(float_to_int)
print(int_to_float)



# Exercise 8 — Convert a Boolean to an Integer
isRaining = True
bool_to_int = int(isRaining)

is_loggedin = False
bool2_to_int = int(is_loggedin)

print(bool_to_int)
print(bool2_to_int)




# Exercise 9 — Convert List to a String and Back
text = ["The", "Lord", "is", "good"]
text_string = " ".join(text)
print(text_string)

text_string.split()
print(text_string)




# Exercise 10 — Convert Dictionary Keys and Values to Lists
dict_example = {'a': 1, 'b': 2, 'c': 3}
keys = list(dict_example.keys())
values = list(dict_example.values())



# Exercise 11 — Perform Arithmetic Operations
a = 15
b = 4

print("Addition:", a + b)       
print("Subtraction:", a - b)     
print("Multiplication:", a * b)
print("Division:", a / b)        
print("Modulus:", a % b)        



# Exercise 12 — Use Comparison Operators
print("10 > 5:", 10 > 5)
print("10 < 5:", 10 < 5)
print("10 == 10:", 10 == 10)
print("10 != 5:", 10 != 5)
print("10 >= 5:", 10 >= 5)
print("10 <= 5:", 10 <= 5)



# Exercise 13 — Use Logical Operators
print("True and False:", True and False)
print("True or False:", True or False)
print("Not True:", not True)



# Exercise 14 — Use Assignment Operators
initial_number = 10
print("Initial Value:", initial_number)

initial_number += 5
print("After += :", initial_number)

initial_number -= 3
print("After -= :", initial_number)

initial_number *= 2
print("After *= :", initial_number)

initial_number /= 3
print("After /= :", initial_number)

initial_number %= 8
print("After %= :", initial_number)



#Exercise 15 — Use Bitwise Operators
print(f"5 & 3 = {5 & 3}")   #AND compares each bit. A bit is 1 only when both bits are 1.
print(f"5 | 3 = {5 | 3}")   #OR produces 1 if at least one of the bits is 1.
print(f"5 ^ 3 = {5 ^ 3}")   #XOR produces 1 when the two bits are different.
print(f"5 << 1 = {5 << 1}") #Shifting left by 1 position adds a 0 on the right:
print(f"5 >> 1 = {5 >> 1}") #For positive integers, shifting right by one position is essentially integer division by 2




# Exercise 16 — Check if a Number is Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is a odd number.")



# Exercise 17 — Find the Largest Number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")





#Exercise 18 — Check if a Year is a Leap Year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")




# Exercise 19 — Grade Classifier
score = float(input("Enter a score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} | Grade: {grade}")





# Exercise 20 — Extract the Domain from an Email
email = input("Enter an email address: ")

if "@" in email:
    domain = email.split("@")[1]
    print(f"Domain: {domain}")
else:
    print("Invalid email format.")