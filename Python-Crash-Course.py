import math
import random

print("Hello")
# Accurate to 5 digits
f1 = 1.111111
f2 = 1.111111
print(f1 + f2)
# Cast with int, float, str
print("Cast ", int(f1))
# Math Operators
print("5 + 2 =", 5 + 2)
# Formatted print with 2 decimals or less
print("5 - 2 = {:.2f}".format(5 - 2))
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

# ----- Math Functions -----
print("abs(-1) ", abs(-1))
print("max(5, 4) ", max(5, 4))
print("min(5, 4) ", min(5, 4))
print("pow(2, 2) ", pow(2, 2))
print("ceil(4.5) ", math.ceil(4.5))
print("floor(4.5) ", math.floor(4.5))
print("round(4.5) ", round(4.5))
print("exp(1) ", math.exp(1))  # e**x
print("log(e) ", math.log(math.exp(1)))
print("log(100) ", math.log(100, 10))  # Base 10 Log
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("radians(0) ", math.radians(0))
print("degrees(pi) ", math.degrees(math.pi))

# Random number between 1 and 100
print("Random", random.randint(1, 101))

# ----- Conditionals -----
# Comparison Operators : < > <= >= == !=
# Logical Operators : and or not
age = 6
if age < 5:
    print("Stay Home")
elif (age >= 5) and (age < 6):
    print("Kindergarten")
elif (age >= 6) and (age <= 17):
    print("Grade {:d}".format(age - 5))
else:
    print("College")

# Ternary operator and another formatting option
print("Can Vote : %s" % (True if age >= 18 else False))

# ----- Strings -----
str1 = "Hello You"
print("Length :", len(str1))
print("1st : ", str1[0])
print("1st 3 ", str1[0:3])
print(str1.replace("Hello", "Goodbye"))
print("You" in str1)
print("you" not in str1)
# Find first index for match or -1
print("You Index :", str1.find("you"))
print("    Hello    ".strip())
# Convert a list into a string and separate with
# spaces
print(" ".join(["Some", "Words"]))
int1 = int2 = 5
print(f"{int1} + {int2} = {int1 + int2}")
# Is characters
print("abc".isalpha())
# Is numbers
print("abc".isdigit())

# ----- Lists -----
# Lists can contain mutable pieces of data of
# varying data types or even functions
l1 = [1, 3.14, "Derek", True]
# Get length
print("Length ", len(l1))
print("1st", l1[0])
# Change values
l1[0] = 2
# Change multiple values
l1[2:4] = ["Bob", False]
# Insert at index without deleting
# Also l1.insert(2, "Paul")
l1[2:2] = ["Paul", 9]
# Add to the end
l2 = l1 + ["Egg", 4]
# Remove a value
l2.remove("Paul")
# Remove at index
l2.pop(0)
print("l2", l2)
# Add to the beginning
l2 = ["Egg", 4] + l1
# Slice out parts
print("1st 2", l2[0:2])
# Multidimensional list
l3 = [[1, 2], [3, 4]]
print("[1, 1]", l3[1][1])

# ----- LOOPS -----
# While : Execute while condition is True
w1 = 0
while w1 <= 20:
    if w1 % 2 == 0:
        print(w1)
    elif w1 == 9:
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        w1 += 1
        # Skips to the next iteration of the loop
        continue
    w1 += 1

# Cycle through list
while len(l1):
    print(l1.pop(0))

# For Loop
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
# end="" eliminates newline
for x in range(0, 10):
    print(x, ' ', end="")
print('\n')

# Cycle through list
l4 = [1, 3.14, "Derek", True]
for x in l4:
    print(x)

# You can also define a list of numbers to
# cycle through
for x in [2, 4, 6]:
    print(x)

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# ----- TUPLES -----
# Tuples are just like lists except they are
# immutable
t1 = (1, 3.14, "Derek", False)

# Get length
print("Length ", len(t1))

# Get value / values
print("1st", t1[0])
print("Last", t1[-1])
print("1st 2", t1[0:2])

# ----- DICTIONARIES -----
# Dictionaries are lists of key / value pairs
# Keys and values can use any data type
# Duplicate keys aren't allowed

d1 = {"name": "Bread", "price": .88}
print("Length", len(d1))
# Add more
d1["slices"] = 16

# Change a value
d1["slices"] = 18

# Get value with key
print(d1["slices"])

# Formatted print with dictionary mapping
print("%(name)s costs $%(price).2f" % d1)

# Get list of keys and values
print(list(d1.keys()))
print(list(d1.values()))

# Delete
del d1["slices"]

# Search for key
print("price" in d1)

# Cycle through a dictionary
for k in d1:
    print(k)

for v in d1.values():
    print(v)


# ----- FUNCTIONS -----
# Functions provide code reuse, organization
# and much more
# Add 2 values using 1 as default
# You can define the data type using function
# annotations
def get_sum(num1: int = 1, num2: int = 1):
    return num1 + num2


print(get_sum(5, 4))


# Accept multiple values
def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(get_sum2(1, 2, 3, 4))


# Return multiple values
def next_2(num):
    return num + 1, num + 2


i1, i2 = next_2(5)
print(i1, i2)


# A function that makes a function that
# multiplies by the given value
def mult_by(num):
    # You can create anonymous (unnamed functions)
    # with lambda
    return lambda x: x * num


print("3 * 5 =", (mult_by(3)(5)))


# Pass a function to a function
def mult_list(list, func):
    for x in list:
        print(func(x))


mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)

# ----- MAP -----
# Map is used to execute a function on a list
one_to_4 = range(1, 5)
times2 = lambda x: x * 2
print(list(map(times2, one_to_4)))

# ----- FILTER -----
# Filter selects items based on a function
# Print out the even values from a list
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))


# ----- CLASSES OBJECTS -----
# Real world objects have
# attributes : height, weight
# capabilities : run, eat

# Classes are blueprints for creating objects
class Square:
    # init is used to set values for each Square
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # This is the getter
    # self is used to refer to an object that
    # we don't possess a name for
    @property
    def height(self):
        print("Retrieving height")

        # Put a __ before this private field
        return self.__height

    # This is the setter
    @height.setter
    def height(self, value):

        # We protect the height from receiving
        # a bad value
        if value.isdigit():

            # Put a __ before this private field
            self.__height = value
        else:
            print("Only enter numbers for height")

    # This is the getter
    @property
    def width(self):
        print("Retrieving width")
        return self.__width

    # This is the setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Only enter numbers for width")

    def get_area(self):
        return int(self.__width) * int(self.__height)


# Create a Square object
square = Square()
square.height = "10"
square.width = "10"
print("Area", square.get_area())


# ----- INHERITANCE & POLYMORPHISM-----
# When a class inherits from another it gets all
# its fields and methods and can change as needed
class Animal:
    def __init__(self, name="unknown", weight=0):
        self.__name = name
        self.__weight = weight

    @property
    def name(self, name):
        self.__name = name

    def make_noise(self):
        return "Grrrrr"

    # Used to cast to a string type
    def __str__(self):
        return "{} is a {} and says {}".format(self.__name,
                                               type(self).__name__, self.make_noise())


# Dog inherits everything from Animal
class Dog(Animal):
    def __init__(self, name="unknown", owner="unknown", weight=0):
        # Have the super class handle initializing
        Animal.__init__(self, name, weight)
        self.__owner = owner

    # Overwrite str
    def __str__(self):
        # How to call super class methods
        return super().__str__() + " and is owned by " + \
               self.__owner


animal = Animal("Spot", 100)
print(animal)

dog = Dog("Bowser", "Bob", 150)
print(dog)


# ---------- RECURSIVE FUNCTIONS ----------
# A function that refers to itself is a recursive function
# Calculating factorials is commonly done with a recursive
# function 3! = 3 * 2 * 1
def factorial(num):
    # Every recursive function must contain a condition
    # when it ceases to call itself
    if num <= 1:
        return 1
    else:

        result = num * factorial(num - 1)
        return result


print(factorial(4))
# 1st : result = 4 * factorial(3) = 4 * 6 = 24
# 2nd : result = 3 * factorial(2) = 3 * 2 = 6
# 3rd : result = 2 * factorial(1) = 2 * 1 = 2
