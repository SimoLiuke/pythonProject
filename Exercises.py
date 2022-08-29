import math
import sys

# 3.3

gender = input("Please enter your biological gender (male/female)\n")
hglobin = float(input("Please enter hemoglobin value in g/L \n"))

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
else:
    print("invalid input")

sys(exit(1))

# 3.2
cabin = str(input("Enter cabin class: \n"))

if cabin == str("LUX"):
    print("LUX: Upper-deck cabin with a balcony")
elif cabin == str("A"):
    print("A: Above the car deck, equipped with a window")
elif cabin == str("LUX"):
    print("B: Windowless cabin above the car deck")
elif cabin == str("LUX"):
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