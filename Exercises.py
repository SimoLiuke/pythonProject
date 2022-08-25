import math
import sys

length = float(input('Please Enter the Length of a Rectangle: '))
width = float(input('Please Enter the Width of a Rectangle: '))

perimeter = 2 * (length + width)

print("Perimeter of a Rectangle using", length, "and", width, " = ", perimeter)

sys(exit(1))

# 2.2

r = float(input("Give a radius of a circle: "))
area = math.pi *r*r
print("The are of a circle with that radius is = %.2f" %area)

# 2.1
user = input("Enter your name:\n ")

print("Hello, " + user + "!")

# 1.1
print("Hello, Simo!")