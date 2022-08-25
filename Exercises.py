import math
import sys

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

sys(exit(1))

# 2.3
length = float(input('Please Enter the Length of a Rectangle: '))
width = float(input('Please Enter the Width of a Rectangle: '))

perimeter = 2 * (length + width)

print("Perimeter of a Rectangle using", length, "and", width, " = ", perimeter)

# 2.2

r = float(input("Give a radius of a circle: "))
area = math.pi *r*r
print("The are of a circle with that radius is = %.2f" %area)

# 2.1
user = input("Enter your name:\n ")

print("Hello, " + user + "!")

# 1.1
print("Hello, Simo!")