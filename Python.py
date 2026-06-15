# ==================================================
# Chapter 1: Python Basics
# ==================================================

# --------------------------
# String Operations
# --------------------------

# Create a string variable
name = "aryan"

# Print the complete string
print("Original String:", name)

# Print the string from index 0 to the end
print("String from index 0:", name[0:])

# Print the length of the string
print("Length of string:", len(name))

# Check whether the string ends with 'n'
print("Ends with 'n':", name.endswith("n"))

# Find the index of the first occurrence of 'n'
print("Index of 'n':", name.find("n"))

# Capitalize the first letter of the string
print("Capitalized string:", name.capitalize())

# Replace 'aryan' with 'arman'
print("After replacement:", name.replace("aryan", "arman"))

# Strings are immutable, so the original string remains unchanged
print("Original string after replacement:", name)

# --------------------------
# Variables and Data Types
# --------------------------

# Integer variables
a = 5
b = 5

# Get the data type of variable 'a'
data_type = type(a)

# Print the data type
print("Data type of a:", data_type)

# --------------------------
# User Input
# --------------------------

# Take input from the user
user_name = input("Enter your name: ")

# Display a greeting message
print("Hello,", user_name)

# ==================================================
# End of Program
# ==================================================
# ==================================================
# Chapter 02: Operators, Type Casting & User Input
# ==================================================

# --------------------------
# Arithmetic Operators
# --------------------------

# a = 15
# b = 15
# print(a + b)

# sub = 15 - 5
# print(sub)

# --------------------------
# Assignment Operators
# --------------------------

# b += 5
# print(b)

# a -= 10
# print(a)

# --------------------------
# Comparison Operators
# --------------------------

a = 1 > 2
print("Is 1 > 2?", a)

# true_value = 1 < 3
# print(true_value)

# false_value = 1 > 3
# print(false_value)

# --------------------------
# Logical Operators
# --------------------------

logic = 1 < 2 or 2 < 1
print("OR Result:", logic)

# logic1 = 1 < 2 and 2 < 1
# print(logic1)

print("NOT Result:", not logic)

# --------------------------
# Type Casting
# --------------------------

string = "1.5"

# Convert string to float
t = float(string)

print("Converted Type:", type(t))
print("Original Type:", type(string))

# --------------------------
# User Input
# --------------------------

# ip1 = int(input("Enter first number: "))
# ip2 = int(input("Enter second number: "))
# print("Sum =", ip1 + ip2)

# --------------------------
# Square of a Number
# --------------------------

# sq1 = int(input("Enter a number: "))
# sq2 = sq1 * sq1
# print("Square =", sq2)

# --------------------------
# Celsius to Fahrenheit Converter
# --------------------------

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

# ==================================================
# End of Chapter 02
# ==================================================

# ==================================================
# Chapter 03: Strings
# ==================================================

# Create a string
name = "aryan"

# --------------------------
# String Slicing
# --------------------------

# Extract characters from index 0 to 2
name_short = name[0:3]

# Access a single character
character_1 = name[1]

# Negative indexing
print(name[-4:-2])

print(character_1)
print(name_short)

# --------------------------
# String Slicing with Skip
# --------------------------

num = "0123456789"

# Print every 2nd character
print(num[0:9:2])

# Start from index 1 and print every 2nd character
print(num[1:9:2])

# --------------------------
# String Length
# --------------------------

give_length = "aryan"
print(len(give_length))

# --------------------------
# String Methods
# --------------------------

# Check ending
print(give_length.endswith("n"))

# Check beginning
print(give_length.startswith("a"))

# Capitalize first letter
print(give_length.capitalize())

# Convert to uppercase
print(give_length.upper())

# Replace text
print(give_length.replace("aryan", "aryan mahakur"))

# --------------------------
# Escape Characters
# --------------------------

ex = "My name is \n \"aryan\""
print(ex)

# --------------------------
# User Input
# --------------------------

input_name = input("Enter your name: ")
input_date = input("Enter the date: ")

print("Good Morning,", input_name)

# --------------------------
# Letter Template Program
# --------------------------

letter = '''
Dear <|name|>,

Greetings from ABC Coding House.
I am happy to tell you about your selection.

Date: <|date|>
'''

# Replace placeholders
letter = letter.replace("<|name|>", input_name)
letter = letter.replace("<|date|>", input_date)

print(letter)

# --------------------------
# Find Double Spaces
# --------------------------

print("Index of double spaces:", input_name.find("  "))

# --------------------------
# Practice: String Slicing
# --------------------------

name = "aryan"

name2 = name[0:3]

print(name2)

# ==================================================
# End of Chapter 03
# ==================================================
# ==================================================
# Chapter 04: Lists & Tuples
# ==================================================

# --------------------------
# Lists
# --------------------------

# Create a list
lists = [1, 2, 3, 4, 5]

print("Original List:", lists)

# Access elements
print("First Element:", lists[0])

# Lists are mutable (can be modified)
lists[0] = 6

print("After Modification:", lists)

# --------------------------
# List Methods
# --------------------------

# Add an element at the end
lists.append(6)

print("After Append:", lists)

# Create another list
sorting = [11, 44, 22, 33]

print("Original Sorting List:", sorting)

# Sort the list
# sorting.sort()

# Reverse the list
# sorting.reverse()

print("Current List:", sorting)

# Insert element at index 2
# sorting.insert(2, 55)

print("After Insert:", sorting)

# Remove a specific value
# sorting.remove(44)

print("After Remove:", sorting)

# Remove element using index
sorting.pop(3)

print("After Pop:", sorting)

# Remove specific value
sorting.remove(11)

print("After Removing 11:", sorting)

# --------------------------
# Tuples
# --------------------------

# Create a tuple
tuples = (1, 2, 3, 4, 5)

# Count occurrences of a value
count = tuples.count(4)

print("Count of 4:", count)

# Check data type
print("Type:", type(tuples))

# ==================================================
# End of Chapter 04
# ==================================================
# ==================================================
# Chapter 05: Dictionaries & Sets
# ==================================================

# --------------------------
# Dictionaries
# --------------------------

# Create a dictionary
marks = {
    "Andy": 88,
    "Amy": 66,
    "lists": [1, 2, 3, 4, 5],
    0: "ANDY"
}

# Print complete dictionary
print(marks)

# Access values using keys
print(marks["Andy"])
print(marks["lists"])
print(marks[0])

# Dictionary methods
print(marks.items())    # Returns key-value pairs
print(marks.keys())     # Returns all keys
print(marks.values())   # Returns all values

# Get value safely
print(marks.get("Andy"))

# Access value directly
print(marks["Amy"])

# Update dictionary
marks.update({"Amy": 99})

print("After Update:")
print(marks)

# Remove a key-value pair
marks.pop("Andy")

print("After Removing Andy:")
print(marks)

# Difference between [] and get()
# print(marks["aryan"])   # KeyError
# print(marks.get("aryan"))  # None

# --------------------------
# Sets
# --------------------------

# Duplicate values are automatically removed
s = {1, 2, 3, 4, 5, 5, "andy"}

print(s)

# Check type
print(type(s))

# Add an element
s.add(6)

print("After Adding 6:")
print(s)

# Create an empty set
e = set()

print(type(e))

# Another set
s1 = {1, 2, 3, 4, 5, 6, 7, 8}

# Union
print("Union:", s.union(s1))

# Difference
print("Difference:", s1.difference(s))

# Intersection
print("Intersection:", s.intersection(s1))

# Length of set
print("Length:", len(s))

# Remove element
s.remove(5)

print("After Removing 5:")
print(s)

# ==================================================
# End of Chapter 05
# ==================================================
# ==================================================
# Chapter 06: Conditional Statements
# ==================================================

# --------------------------
# Check Positive, Negative, or Zero
# --------------------------

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# --------------------------
# Find the Largest of Three Numbers
# --------------------------

a = 1
b = 2
c = 3

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")

# --------------------------
# Simple if-else Example
# --------------------------

if 1 < 2:
    print("Positive number")
else:
    print("Negative number")

# --------------------------
# Compare Two Numbers
# --------------------------

a = 5
b = 6

if a > b:
    print(f"a ({a}) is bigger than b ({b})")
else:
    print(f"b ({b}) is bigger than a ({a})")

# ==================================================
# End of Chapter 06
# ==================================================
# ==================================================
# Chapter 07: Loops
# ==================================================

# --------------------------
# 1. FOR LOOP
# --------------------------

for i in range(1, 6):
    print(i)

# --------------------------
# 2. WHILE LOOP
# --------------------------

i = 1

while i <= 5:
    print(i)
    i += 1

# --------------------------
# 3. NESTED FOR LOOP
# --------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# --------------------------
# 4. NESTED WHILE LOOP
# --------------------------

i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1

# --------------------------
# 5. BREAK
# --------------------------

for i in range(1, 6):
    if i == 3:
        break

    print(i)

# --------------------------
# 6. CONTINUE
# --------------------------

for i in range(1, 6):
    if i == 3:
        continue

    print(i)

# --------------------------
# 7. PASS
# --------------------------

for i in range(5):
    pass

# --------------------------
# 8. FOR-ELSE
# --------------------------

for i in range(1, 6):
    print(i)
else:
    print("Loop completed")

# --------------------------
# 9. WHILE-ELSE
# --------------------------

i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed")

# --------------------------
# 10. LIST COMPREHENSION
# --------------------------

squares = [x * x for x in range(1, 6)]

print(squares)

# ==================================================
# End of Chapter 07
# ==================================================

# ==================================================
# Chapter 08: Functions & Recursion
# ==================================================

# --------------------------
# Simple Function
# --------------------------

def sum_numbers():
    a = 5
    b = 6
    c = a + b

    print("The sum of", a, "and", b, "is", c)

sum_numbers()

# --------------------------
# Square of a Number
# --------------------------

def square():
    num = 5
    sq = num * num

    print("The square of", num, "is", sq)

square()

# --------------------------
# Check Even or Odd
# --------------------------

def even():
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")

even()

# --------------------------
# Recursion Example
# Factorial of a Number
# --------------------------

def factorial(n):
    if n == 1 or n < 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# --------------------------
# Function with User Input
# --------------------------

def hello():
    name = input("Enter your name: ")

    print("Hello", name)

hello()

# ==================================================
# Additional Examples (Practice)
# ==================================================

# Function without arguments
#
# def greet():
#     name = input("Enter your name: ")
#     print("Hello", name)
#
# greet()

# Function with arguments
#
# def greet(name, ending):
#     print("Hello", name)
#     print(ending)
#     return "ok"
#
# result = greet("Aryan", "Thanks")
# print(result)

# Default arguments
#
# def good_day(name, ending="Good Morning"):
#     print(f"{ending} {name}")
#
# good_day("Aryan", "Good Night")
# good_day("Arman")

# Average of two numbers
#
# def avg():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#
#     average = (a + b) / 2
#
#     print("Average =", average)
#
# avg()

# ==================================================
# End of Chapter 08
# ==================================================


# ==================================================
# Chapter 09: OOP - Classes & Objects
# ==================================================

# --------------------------
# Creating a Class
# --------------------------

class Employees:

    # Constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


# --------------------------
# Creating Objects
# --------------------------

aryan = Employees("Aryan", 23, 10000)

# Accessing Object Attributes
print(aryan.name)
print(aryan.age)
print(aryan.salary)

# --------------------------
# Another Class Example
# --------------------------

class City:

    # Class Attributes
    nameofcity = "Delhi"
    population = "1.5 M"

    # Instance Method
    def getinfo(self):
        print(
            "The city of",
            self.nameofcity,
            "has a population of",
            self.population
        )

    # Static Method
    @staticmethod
    def greet():
        print("Hello Mumbai")


# --------------------------
# Creating Objects
# --------------------------

delhi = City()
delhi.nameofcity = "Delhi"
delhi.population = 11

mumbai = City()
mumbai.nameofcity = "Mumbai"
mumbai.population = 12

bengaluru = City()

# --------------------------
# Calling Static Method
# --------------------------

mumbai.greet()

# --------------------------
# Accessing Attributes
# --------------------------

print(delhi.nameofcity, delhi.population)

print(mumbai.nameofcity, mumbai.population)

# --------------------------
# Calling Instance Method
# --------------------------

delhi.getinfo()

# Equivalent:
# City.getinfo(delhi)

# ==================================================
# OOP Concepts Learned
# ==================================================

# 1. Class
# 2. Object
# 3. Constructor (__init__)
# 4. Instance Attributes
# 5. Class Attributes
# 6. Instance Methods
# 7. Static Methods

# ==================================================
# End of Chapter 09
# ==================================================
# ==================================================
# Chapter 10: Advanced OOP in Python
# ==================================================

# Topics Covered:
# 1. Inheritance
# 2. Method Overriding
# 3. super()
# 4. Class Methods
# 5. Properties & Setters
# 6. Operator Overloading

# --------------------------
# Example 1: Inheritance
# --------------------------

class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.type = animal_type

    def speak(self):
        return "Some Sound"


class Dog(Animal):
    def speak(self):
        return "Bark"


class Cat(Animal):
    def speak(self):
        return "Meow"


dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

print(f"{dog.name} ({dog.type}) says {dog.speak()}")
print(f"{cat.name} ({cat.type}) says {cat.speak()}")

# --------------------------
# Example 2: super()
# --------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee1(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)

        self.job_title = job_title
        self.salary = salary

    def details(self):
        super().details()

        print(f"Job Title: {self.job_title}")
        print(f"Salary: {self.salary}")


person1 = Person("Alice", 23)
employee1 = Employee1("Bob", 30, "Software Engineer", 70000)

person1.details()
print()

employee1.details()

# --------------------------
# Example 3: Method Overriding
# --------------------------

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee2(Person2):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)

        self.job_title = job_title
        self.salary = salary

    def details(self):
        super().details()

        print(f"Job Title: {self.job_title}")
        print(f"Salary: {self.salary}")


employee = Employee2(
    "Alice",
    28,
    "Software Developer",
    80000
)

employee.details()

# --------------------------
# Example 4: Class Method
# --------------------------

class Employee5:

    a = 10

    @classmethod
    def show(cls):
        print(cls.a)


p = Employee5()

p.a = 20

p.show()

# --------------------------
# Example 5: Properties
# --------------------------

class Employee3:

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):

        if new_salary < 0:
            print("Salary cannot be negative!")

        else:
            self._salary = new_salary


emp = Employee3("Alice", 50000)

print(emp.salary)

emp.salary = 60000

print(emp.salary)

emp.salary = -5000

# --------------------------
# Example 6: Operator Overloading
# --------------------------

class Number:

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


a = Number(5)
b = Number(6)

print(a + b)

# ==================================================
# End of Chapter 10
# ==================================================
# ==================================================
# Chapter 10: Advanced OOP & Practice Projects
# ==================================================

# Topics Covered:
# 1. Classes & Objects
# 2. Constructors
# 3. Inheritance
# 4. Method Overriding
# 5. super()
# 6. Class Methods
# 7. Properties
# 8. Getters & Setters
# 9. Static Methods

# ==================================================
# Example 1: Bank Account System
# ==================================================

class BankAccount:

    def __init__(self, accountholder="Blank", balance=0.0):
        self.accountholder = accountholder
        self.balance = balance

    def addmoney(self, money):
        self.balance += money
        print(f"Deposited: {money}")
        print(f"New Balance: {self.balance}")

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            print(f"Withdrawn: {money}")
            print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def display(self):
        print(f"Account Holder: {self.accountholder}")
        print(f"Balance: {self.balance}")

    @staticmethod
    def greet():
        print("Hello, welcome to our bank!")


john = BankAccount("John", 500)

john.addmoney(1000)
john.withdraw(500)
john.display()

BankAccount.greet()

# ==================================================
# Example 2: Inheritance
# ==================================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(
            f"Name: {self.name} "
            f"is a good person and is "
            f"{self.age} years old."
        )


class Employee(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)

        self.salary = salary

    def details(self):
        print(
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Salary: {self.salary}"
        )


employee1 = Employee("Bob", 30, 70000)

employee1.details()

# ==================================================
# Example 3: Student & College
# ==================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class College(Student):

    def __init__(self, name, age, course):
        super().__init__(name, age)

        self.course = course

    def details(self):
        super().details()

        print(f"Course: {self.course}")


student2 = College(
    "John",
    20,
    "Computer Science"
)

student2.details()

# ==================================================
# Example 4: Class Method
# ==================================================

class StudentSchool:

    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

    def details(self):
        print(
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"School: {self.school_name}"
        )


student1 = StudentSchool("John", 20)

student1.details()

StudentSchool.change_school("XYZ School")

student1.details()

# ==================================================
# Example 5: Property, Getter & Setter
# ==================================================

class StudentProperty:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            print("Age can't be negative!")

        else:
            self._age = value


student = StudentProperty("John", 20)

print(student.name)
print(student.age)

student.name = "Jane"
student.age = 25

print(student.name)
print(student.age)

student.age = -5

# ==================================================
# End of Chapter 10
# ==================================================