# print("Abiodun Oluwapelumi")
# print("0----")
# print(" ||||")
# print("*" * 10)

# Variable Data types
price = 20  # int
rating = 4.9  # float
name = 'Amos'  # str
is_published = False  # boolean

# simple application for a Hospital.
patientName = 'John Smith'
patientAge = 20
is_a_new_patient = True

# Using the input() function
name = input("What is your name? ")
print('Hi ' + name)
favColor = input("What is your Favorite Color? ")
print(name + ' likes ' + favColor)

# Asking for the birth year to calculate the year
date_of_birth = input("Birth year: ")
print(type(date_of_birth))  # checking the datatype of the birth_year variable using the type()
Age = 2021 - int(date_of_birth)   # here we convert the birth_year to an int()
print(type(Age))  # checking the datatype of the Age variable using the type()
print(name + ' is ' + str(Age) + ' years old.')


message = '''
Hi John,

Here is our first emnail to you.

Thank you,
The support teams.
'''
print(message)


course = "Python for Beginners"
courseCopy = course[:]
cour = course[1:-1]
print(courseCopy)
print(cour)

first = "John"
last = "Smith"
msg = f"{first} is also known as {last} in case you don't know"
print(msg)

course = "python for Beginners"
lent = len(course)
print(lent)
print(course.upper())
print(course.lower())
print(course)
print(course.find("n"))


