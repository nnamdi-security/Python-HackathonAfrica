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




