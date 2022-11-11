import math
import _mysql_connector
import random
import sys
import json
import requests

# 12.2

# municipality = input("Enter a municipality: \n")

request = "https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={afab5d7b968764f2a0308f0607c28fa9}&units=metric"
response = requests.get(request).json()

print(json.dumps(response, indent=2))

sys.exit(0)

# 12.1

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()


print("\n", response["value"])

sys.exit(0)

# 11.2


class Car:

    def __init__(self, registration, max_speed, speed=0, travelled_distance=0):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = speed
        self.travelled_distance = travelled_distance

    def drive(self, hours):
        if hours > 0:
            self.travelled_distance = self.travelled_distance + self.speed * hours

    def accelerate(self, speed_change):
        if self.speed + speed_change >= 0:
            self.speed = self.speed + speed_change
        else:
            self.speed = 0

        if self.speed + speed_change <= self.max_speed:
            self.speed = self.speed + speed_change
        else:
            self.speed = self.max_speed


class ElectricCar(Car):

    def __init__(self,  battery_cap, registration, max_speed, speed=0, travelled_distance=0):
        super().__init__(registration, max_speed, speed, travelled_distance)
        self.battery_cap = battery_cap


class GasolineCar(Car):

    def __init__(self,  tank_vol, registration, max_speed, speed=0, travelled_distance=0):
        super().__init__(registration, max_speed, speed, travelled_distance)
        self.tank_vol = tank_vol


# main

cars = []

cars.append(ElectricCar("52.5 kWh", "ABC-15", 180, random.randrange(50, 100), 0))
cars.append(GasolineCar("32.3 l", "ACD-123", 165, random.randrange(50, 100), 0))


for car in cars:
    car.drive(3)

for car in cars:        # as I randomized speed value distance values vary between executions
    print(car.registration, ":", car.travelled_distance, "Km")

sys.exit(0)

# 11.1

class Publication:

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"{self.name}")


class Book(Publication):

    def __init__(self, name, author, p_count):
        super().__init__(name)
        self.author = author
        self.p_count = p_count

    def print_info(self):
        super().print_info()
        print(f"{self.author}, {self.p_count} pages")


class Magazine(Publication):

    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_info(self):
        super().print_info()
        print(f"{self.chief_editor}")


# main

publications = []

publications.append(Magazine("Donald Duck", "Aki Hyyppä"))
publications.append(Book("Compartment No. 6", "Rosa Liksom", 192))

for i in publications:
    i.print_info()
    print("")


sys.exit(0)

# 10.4


class Car:

    def __init__(self, registration, max_speed, speed, travelled_distance):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        if self.speed == 0 and speed_change < 0:
            self.speed = self.speed
        elif speed_change > 0 and speed_change + self.speed <= self.max_speed:
            self.speed = self.speed + speed_change
        elif speed_change < 0 and self.speed + speed_change > 0:
            self.speed = self.speed - speed_change
        elif speed_change < 0 and self.speed + speed_change < 0:
            self.speed = 0
        else:
            self.speed = self.max_speed

    def drive(self, hours):
        if hours < 0:
            self.travelled_distance = self.travelled_distance + self.speed / hours
        else:
            self.travelled_distance = self.travelled_distance + self.speed * hours


class Race:

    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.distance = kilometers
        self.car_list = car_list

    def hour_passes(self):
        for car in cars:
            car_accelerate = randint(-10, 15)

            if 0 < car.speed + car_accelerate < car.max_speed:
                car.speed += car_accelerate
                car.drive(1)

            elif car.speed + car_accelerate > car.max_speed:
                car.speed = car.max_speed
                car.drive(1)
        return

    def print_values(self):
        for car in self.car_list:
            print(f"Name: {car.registration}, Max Speed: {car.max_speed}, Current Speed: {car.speed}, Travelled Distance: {car.travelled_distance}")
        return

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.distance:
                return True
        return

# Main

car_list=[]

BMW = Car("BMW", 200, 0, 0)
Ferrari = Car("Ferrari", 200, 0, 0)
car_list.append(BMW), car_list.append(Ferrari)

race = Race("Grand Demolition Derby", 8000, car_list)

while True:
    race.hour_passes()
    race.print_values()
    if race.race_finished():
        break


# 10.2 + 10.3

class Elevator:

    def __init__(self, bottom_floor, top_floor, current_floor=0):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor

    def floor_up(self):
        if self.current_floor != self.top_floor:
            self.current_floor = self.current_floor + 1

    def floor_down(self):
        if self.current_floor != self.bottom_floor:
            self.current_floor = self.current_floor - 1

    def go_to_floor(self, floor_change):
        if self.current_floor < floor_change:
            while self.current_floor != floor_change:
                self.floor_up()
                print("You are at floor", self.current_floor)
        elif self.current_floor > floor_change:
            while self.current_floor != floor_change:
                self.floor_down()
                print("You are at floor", self.current_floor)


class Building:

    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_count = elevator_count
        self.elevators = []

        for i in range(elevator_count):
            self.elevators.append(Elevator(bottom_floor, top_floor))
            print(self.elevators[i])

    def run_elevator(self, elevator_number, floor_change):
        elevator_index = elevator_number - 1
        self.elevators[elevator_index].go_to_floor(floor_change)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(0)


h = Elevator(0, 10)
h.go_to_floor(3)
building = Building(0, 8, 3)
building.run_elevator(1, 6)
building.fire_alarm()

sys.exit(0)

# 10.1


class Elevator:

    def __init__(self, bottom_floor, top_floor, current_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor

    def floor_up(self):
        if self.current_floor != self.top_floor:
            self.current_floor = self.current_floor + 1

    def floor_down(self):
        if self.current_floor != self.bottom_floor:
            self.current_floor = self.current_floor - 1

    def go_to_floor(self, floor_change):
        if self.current_floor < floor_change:
            while self.current_floor != floor_change:
                self.floor_up()
                print("You are at floor", self.current_floor)
        elif self.current_floor > floor_change:
            while self.current_floor != floor_change:
                self.floor_down()
                print("You are at floor", self.current_floor)


h = Elevator(0, 10, 0)
print(vars(h))
h.go_to_floor(10)
print(vars(h))
h.go_to_floor(0)
print(vars(h))

sys.exit(1)

# 9.4


class Car:

    def __init__(self, registration, max_speed, speed=0, travelled_distance=0):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        if self.speed + speed_change >= 0:
            self.speed = self.speed + speed_change
        else:
            self.speed = 0

        if self.speed + speed_change <= self.max_speed:
            self.speed = self.speed + speed_change
        else:
            self.speed = self.max_speed

    def drive(self, hours):
        if hours > 0:
            self.travelled_distance = self.travelled_distance + self.speed * hours


max_distance = 10000
finished = False

cars = []
register = 1

for i in range(10):
    car = Car("ABC-" + str(i), random.randrange(100, 200), 0, 0)
    cars.append(car)

distance = []
loops = 0       # for testing

while not finished:
    for car in cars:
        car.accelerate(random.randrange(-10, 15))
        car.drive(1)
        print("Hours Driven", loops)    # for testing

        if car.travelled_distance >= max_distance:
            finished = True
            print("")
        else:
            loops = loops + 1   # for testing

for car in cars:
    print(vars(car))

sys.exit(0)

# 9.3


class Car:

    def __init__(self, registration, max_speed, speed, travelled_distance):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        if self.speed == 0 and speed_change < 0:
            self.speed = self.speed
        elif speed_change > 0 and speed_change + self.speed <= self.max_speed:
            self.speed = self.speed + speed_change
        elif speed_change < 0 and self.speed + speed_change > 0:
            self.speed = self.speed - speed_change
        elif speed_change < 0 and self.speed + speed_change < 0:
            self.speed = 0
        else:
            self.speed = self.max_speed

    def drive(self, hours):
        if hours < 0:
            self.travelled_distance = self.travelled_distance + self.speed / hours
        else:
            self.travelled_distance = self.travelled_distance + self.speed * hours


BMW = Car("ABC-123", 142, 0, 0)
BMW.accelerate(30)
BMW.drive(1.5)
print(BMW.speed, BMW.travelled_distance)
BMW.accelerate(70)
BMW.drive(0.1)
print(BMW.speed, BMW.travelled_distance)
BMW.accelerate(50)
BMW.drive(2.5)
print(BMW.speed, BMW.travelled_distance)
BMW.accelerate(-200)
print(BMW.speed, BMW.travelled_distance)
print(f"The BMW's registration is {BMW.registration}, it's max speed is {BMW.max_speed} km/h, it's currently travelling at {BMW.speed} km/h, and it has travelled {BMW.travelled_distance} km.")


# 9.2


class Car:

    def __init__(self, registration, max_speed, speed):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = speed

    def accelerate(self, speed_change):
        if self.speed == 0 and speed_change < 0:
            self.speed = self.speed
        elif speed_change > 0 and speed_change + self.speed <= self.max_speed:
            self.speed = self.speed + speed_change
        elif speed_change < 0 and self.speed + speed_change > 0:
            self.speed = self.speed - speed_change
        elif speed_change < 0 and self.speed + speed_change < 0:
            self.speed = 0
        else:
            self.speed = self.max_speed


car = Car("ABC-123", 142, 0)
car.travelled_distance = "0 km"
car.accelerate(30)
print(car.speed)
car.accelerate(70)
print(car.speed)
car.accelerate(50)
print(car.speed)
car.accelerate(-200)
print(car.speed)
print(f"The car's registration is {car.registration}, it's max speed is {car.max_speed} km/h, it's currently travelling at {car.speed} km/h, and it has travelled {car.travelled_distance}.")


# 9.1


class Car:

    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed


car = Car(registration="ABC-123", max_speed="142 km/h")
car.current_speed = "80 km/h"
car.travelled_distance = "0 km"

print(f"The car's registration is {car.registration}, it's max speed is {car.max_speed} km/h, it's currently travelling at {car.current_speed}, and it has travelled {car.travelled_distance}.")

# 7.2

names = set()
name = 0
while name != "":
    name = input("Enter a Name: \n")

    if name == "":
        break
    if name in names:
        print("Existing Name"), print("")
    else:
        print("New Name"), print("")
        names.add(str(name))

for name in names:
    print(name)


# 8.1
def fetch(name, location):
    1


code = input("Enter IACO code:")
print(name, location)

# 7.1, not exactly what was instructed, but this is the solution I could make work
month = input("Input the number of the month: \n")

if month in ('12', '1', '2'):
    season = 'winter'
elif month in ('3', '4', '5'):
    season = 'spring'
elif month in ('6', '7', '8'):
    season = 'summer'
elif month in ('9', '10', '11'):
    season = 'autumn'
else:
    print("Invalid input")
    sys.exit(1)

print("Season is", season)

# 6.6


def calculate(diameter, price):
    r = diameter / 2
    area = math.pi * (r * r)
    value = area / price
    return value


# User Input
diameter = float(input("Give Diameter of the first pizza: \n"))
price = float(input("Give the price of the first  pizza: \n"))
diameter2 = float(input("Give Diameter of the second pizza: \n"))
price2 = float(input("Give the price of the second pizza: \n"))


# Calculating values
value1 = calculate(diameter, price)
value2 = calculate(diameter2, price2)

# Sorting value, larger value is better, as it's area given per €
pizzas = [value1, value2]
pizzas.sort()

# Formatting results
if value1 > value2:
    pizza = "first"
else:
    pizza = "second"

print("The", pizza, "pizza is better value for money, giving %.2f" % pizzas[1], "cm^2 per €")

# 6.5

# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def remove_even(numbers):
    new_list = []
    for i in numbers:
        if i % 2 != 0:
            new_list.append(i)
    return new_list


remove_even(numbers)
new_list = remove_even(numbers)

# Printing results
print(numbers)
print(new_list)

# 6.4

# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def remove_even(numbers):
    new_list = []
    for i in numbers:
        if i % 2 != 0:
            new_list.append(i)
    return new_list


remove_even(numbers)
new_list = remove_even(numbers)

# Print results
print(new_list)

# 6.3

# User input
gallon = float(input("Enter amount of gasoline in Gallons: \n"))


def convert():
    liter = gallon * 3.785411784
    print("The amount of gasoline in Liters is ", liter, " L")
    return gallon


liter = convert()

# Loop with results and checking for non 0 input
while gallon > 0:
    convert()
    print("")
    gallon = float(input("Enter amount of gasoline in Gallons: \n"))

# 6.2
import random
from random import randint


def roll2(sides):   # Strange bug, won't give max value for range without +1, works fine with it
    dice = random.randrange(1, sides + 1)
    print(dice)
    return dice


sides = float(input("How many sided Die to roll?: \n"))
print("")
dice = roll2(sides)

while dice != sides:
    dice = roll2(sides)

# 6.1


def roll():
    dice = randint(1, 6)
    print(dice)
    return dice


dice = roll()

while dice != 6:
    dice = roll()

# 5.4, easy solution, but not with the structures that the exersice asked for, I was unable to make them work

cities = []
while len(cities) != 5:
    city = input("Enter a name of a city: \n")
    cities.append(city)

print(""), print(cities[0]), print(cities[1]), print(cities[2]), print(cities[3]), print(cities[4]),

# 5.3

num = int(input("Give a number between 0 and 9: \n"))

if num > 1:

    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# 5.2

num = []

while True:
    user_input = input("Enter numbers, when done input an empty field: ")

    if user_input == "":
        break
    num.append(user_input)

num.sort(reverse=True)

print(""), print(num[0]), print(num[1]), print(num[2]), print(num[3]), print(num[4])

# 5.1

from random import randint

dice = []
rolls = int(input("How many dice do you want to roll: \n"))

while rolls == rolls and rolls != 0:
    rnum = randint(1, 6)
    dice.append(rnum)
    rolls = rolls - 1
    rnum = 0

print("The rolled values are: ")

for n in dice:
    print(n)

print("")
print("The sum of the rolls is: ", sum(dice))

# 4.6

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
        print(5 - tries, "trie(s) remaining")

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

# 3.4
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
    print("The Zander is " + str(42 - fish_length) + " cm too short, Release it to the lake.")

# 2.6

from random import randint

# 3 numbers
tdc = ""  # Three-digit code
for x in range(3):
    tdc = tdc + str(randint(0, 9))

print(tdc)

# 4 numbers
fdc = ""  # Four-digit code
for y in range(4):
    fdc = fdc + str(randint(1, 6))

print(fdc)

# 2.5

tal = float(input("Enter Talents: \n"))
pou = float(input("Enter Pounds: \n"))
lot = float(input("Enter Lots: \n"))

kilo = float((8.512 * tal) + (0.4256 * pou) + (0.0133 * lot))
kilo2 = int(kilo)
gram = float((kilo - kilo2) * 1000)

print("Weight in modern units:")
print(str(kilo2) + " kilograms & " + str(gram) + " grams.")

# 2.4

num1 = (int(input("Give any number between 0 - 9:\n")))
num2 = (int(input("Give any number between 0 - 9:\n")))
num3 = (int(input("Give any number between 0 - 9:\n")))

sum_1 = num1 + num2 + num3
prod_1 = num1 * num2 * num3
avg_1 = (num1 + num2 + num3) / 3

print("The sum of the numbers is: ", sum_1)
print("The product of the numbers is: ", prod_1)
print("The average of the numbers is: ", avg_1)


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
print("The are of a circle with that radius is = %.2f" % area)

# 2.1
user = input("Enter your name:\n ")

print("Hello, " + user + "!")

# 1.1
print("Hello, Simo!")