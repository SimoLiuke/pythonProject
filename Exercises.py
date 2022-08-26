import math
import sys

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

sys(exit(1))

# 2.5 (non functional)

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