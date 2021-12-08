print("Abiodun Oluwapelumi")
print("0----")
print(" ||||")
print("*" * 10)

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


# Using some python methods to format strings
course = "python for Beginners"
lent = len(course)
cupper = course.upper()
clower = course.lower()
crep = course.replace("python", "Javascript & PHP")
print(lent)
print(cupper)
print(clower)
print(crep)
print("Javascript" in crep)
print(course.title())


# Using Math module
import math

print(math.ceil(2.9))

#If statement
house_price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = (house_price * 10) / 100
    print(f"Down Payment = ${down_payment}")
else:
    down_payment = (house_price * 20) / 100
    print(f"Down Payment = ${down_payment}")

high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible for loan.")
else:
    print("Oh!, You are not eligible for the loan.")

name = input("What is your name? ")
if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good.")


i = 1

while i <= 5:
    print(i)
    i += 1

i = 0
while i <= 5:
    print(i * '*')
    i += 1
print('done')

# Guessing game
secret_number = 2
guess_limit = 3
count = 0

while count < guess_limit:
    guess = int(input("Guess: "))
    count += 1

    if guess == secret_number:
        print("Congratulations! you won.")
        break
else:
    print("Sorry!, you ran out of luck.")

# car engine game
guide = '''
    Start: This start the car engine.
    Stop: This stop the car engine.
    Quit: This stop the car engine.
'''
name = input("Hello what is your name? ")
intro = f"Welcome, {name} kindly type 'GUIDE' to show guide on how to use the system"
print(intro)
i = 0
has_started = False

while i < 5:
    req = input("Input a request: ")
    req = req.upper()
    if req == 'GUIDE':
        print(guide)
    elif req == 'START':
        if has_started:
            print("Car already started!")
        else:
            has_started = True
            print("Car started.. ready to go.")

    elif req == 'STOP':
        if not has_started:
            print("Car stopped already")
        else:
            has_started = False
            print("Car stopped.")

    elif req == 'QUIT':
        print("Application Terminated.")
        break
    else:
        print("Sorry i don't understand you")

else:
    print("Hello you have put too much of invalid request, App terminated.")

# using the for loop
for one in [1, 2, 3, 4, 5]:
    print(one)

for one in range(2, 10, 2):
    print(one)

names = ['shola', 'subomi', 'gideon']
for name in names:
    print(f'Happy Birthday {name}')

prices = [10, 20, 30]
total = 0
for price in prices:
    price += price
print(f"Total Price = {price}")

# nested loop
for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")


numbers = [5,2,5,2,2]

for number in numbers:
    print("x" * number)

numbers = [2, 4, 5, 8, 10, 15, 22]
max = numbers[3]

for number in numbers:
    if number > max:
        max = number
print(max)

 # List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix.reverse()
print(matrix)
matrix.sort()
print(matrix)
print(matrix[1])
print(matrix.index([4, 5, 6]))
print([4, 5, 6] in matrix)

numbers = [1, 2, 2, 3, 3, 4, 5, 6]
uniq = []

for number in numbers:
    if number not in uniq:
        uniq.append(number)
print(uniq)


nu = (1, 2, 3, 4)
numm = list(nu)
numm.insert(0, 10)
print(numm)

messages = input("How are you feeling today? ")
words = messages.split(' ')
Emojis = {
    ":)": "😀",
    ":(": "😔"
}

output = " "

for message in words:
    output += Emojis.get(message, message) + " "
print(output)

function
def greet_user(name):
    print(f'Hi, {name}')
    print('Welcome on board')


print('start')
greet_user('Joshua')
print('Finish')

# making use of try and except to handle error messages.
try:
    message = int(input("> "))
    print(message)
except ValueError:
    print("Heyo! we expected an integer not a string")



def emoji_converter(messages):
    words = messages.split(' ')
    emoji = {
        "sad": "😭",
        "happy": "🤣"
    }
    output = " "
    for message in words:
        output += emoji.get(message, message) + " "
    return output


messages = input("How do you feel today? ")
result = emoji_converter(messages)
print(result)

class Point:
    message = input("What is your name? ")


    def greetings(self):
        message = input("What is your name? ")
        words = message.split(' ')
        print(words)

Myclass = Point()
print(Myclass.message)
print(Myclass.greetings())

# Class and inheritance
class HumanBeing:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, my name is {self.name}')


class Person(HumanBeing):
    pass


person = Person("John")
person.talk()







