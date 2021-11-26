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
birth_year = input("Birth year: ")
print(type(birth_year))  # checking the datatype of the birth_year variable
Age = 2021 - int(birth_year)   # here we convert the birth_year to an int()
print(type(Age))  # checking the datatype of the Age variable
print(name + ' is ' + str(Age) + ' years old.')