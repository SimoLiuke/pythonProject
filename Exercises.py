import math
import sys



sys.exit(0)

# 4.5

Username = "simo"
Password = "1234"

tries = 0

while tries < 5:
    name = str(input("Enter Username: \n"))
    pw = input("Enter Password: \n")
    if name == str(Username) and pw == str(Password):
        print("Welcome")
        tries = 5
    else:
        tries = tries + 1
        print("Access denied")
        print(5-tries, "trie(s) remaining")


# 4.4

from random import randint
n = randint(1, 10)
guess = 0

while n != guess:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < n != guess:
        print("Too low")
    elif guess > n != guess:
        print("Too High")
    elif n == guess:
        print("Correct")


# 4.3

my_list = []

while True:
    user_input = input("Enter numbers, when done input an empty field: ")

    if user_input == "":
        break
    my_list.append(user_input)

print("Maximum element in the list is: ", max(my_list), "\n Minimum element in the list is: ", min(my_list))
print(my_list)

# 4.2

inches = 1

while float(inches > 0):
    inches = float(input("Give length in inches: \n"))
    if inches > 0:
        cm = inches * 2.54
        print("Length is equal to: " + str(cm) + " cm")
else:
    print("Input was negative")

# 4.1

for value in range(1, 1000):
    if value % 3 == 0:
        print(value)

# 3.4 (unfinished)
# input year from user
year = float(input("Input a year: "))

# test if year is leap year, by testing divisibility
if year % 4 == 0:
    print("year is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("Year is a leap year")
else:
    print("Year isn't a leap year")

# 3.3
# input from user
gender = input("Please enter your biological gender (male/female)\n")
hglobin = float(input("Please enter hemoglobin value in g/L \n"))
# Check input against predetermined values
if gender == str("male") and hglobin in range(134, 167):
    print("Your hemoglobin value is normal")
elif gender == str("female") and hglobin in range(117, 155):
    print("Your hemoglobin value is normal")
elif gender == str("male") and hglobin < 134:
    print("Your hemoglobin value is low")
elif gender == str("male") and hglobin > 167:
    print("Your hemoglobin value is high")
elif gender == str("female") and hglobin < 117:
    print("Your hemoglobin value is low")
elif gender == str("female") and hglobin < 155:
    print("Your hemoglobin value is high")
# if input is not valid
else:
    print("invalid input")

# 3.2
cabin = str(input("Enter cabin class: \n"))

if cabin == str("LUX"):
    print("LUX: Upper-deck cabin with a balcony")
elif cabin == str("A"):
    print("A: Above the car deck, equipped with a window")
elif cabin == str("B"):
    print("B: Windowless cabin above the car deck")
elif cabin == str("C"):
    print("C: Windowless cabin below the car deck")
else:
    print("Invalid cabin class")

# 3.1

fish_length = float(input("Give Zander length: \n"))

if fish_length >= float(42):
    print("The Zander is long enough")
else:
    print("The Zander is "+str(42-fish_length)+" cm too short, Release it to the lake.")

# 2.6

from random import randint
# 3 numbers
tdc = ""    # Three-digit code
for x in range(3):
    tdc = tdc + str(randint(0, 9))

print(tdc)

# 4 numbers
fdc = ""    # Four-digit code
for y in range(4):
    fdc = fdc + str(randint(1, 6))

print(fdc)

# 2.5

tal = float(input("Enter Talents: \n"))
pou = float(input("Enter Pounds: \n"))
lot = float(input("Enter Lots: \n"))

kilo = float((8.512*tal)+(0.4256*pou)+(0.0133*lot))
kilo2 = int(kilo)
gram = float((kilo-kilo2)*1000)

print("Weight in modern units:")
print(str(kilo2)+" kilograms & "+str(gram)+" grams.")

# 2.4

num1 = (int(input("Give any number between 0 - 9:\n")))
num2 = (int(input("Give any number between 0 - 9:\n")))
num3 = (int(input("Give any number between 0 - 9:\n")))

sum_1 = num1 + num2 + num3
prod_1 = num1*num2*num3
avg_1 = (num1+num2+num3)/3
print("The sum of the numbers is: ")
print(sum_1)
print("The product of the numbers is: ")
print(prod_1)
print("The average of the numbers is: ")
print(avg_1)

# 2.3

length = float(input('Please Enter the Length of a Rectangle: '))
width = float(input('Please Enter the Width of a Rectangle: '))

perimeter = 2 * (length + width)
area = length * width

print("Perimeter of a Rectangle using", length, "and", width, " = ", perimeter)
print("Area of rectangle using", length, "and", width, "=", area)

# 2.2

r = float(input("Give a radius of a circle: "))
area = math.pi * r * r
print("The are of a circle with that radius is = %.2f" %area)

# 2.1
user = input("Enter your name:\n ")

print("Hello, " + user + "!")

# 1.1
print("Hello, Simo!")
