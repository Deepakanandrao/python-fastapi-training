# Python Basics - Quick Brush Up

A quick reference for Python 3.14+ syntax and common constructs.

---

## 1. Variables and Data Types

```python
# Variables (no declaration needed)
name = "Alice"          # String
age = 25                # Integer
height = 5.8            # Float
is_student = True       # Boolean
nothing = None          # None type

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0

# Type checking
print(type(name))       # <class 'str'>
```

### Basic Data Types

| Type    | Example              | Description             |
| ------- | -------------------- | ----------------------- |
| `int`   | `42`, `-10`          | Whole numbers           |
| `float` | `3.14`, `-0.5`       | Decimal numbers         |
| `str`   | `"hello"`, `'world'` | Text                    |
| `bool`  | `True`, `False`      | Boolean values          |
| `None`  | `None`               | Represents nothing/null |

---

## 2. Strings

```python
# String creation
single = 'Hello'
double = "World"
multi = """Multiple
lines"""

# String formatting (modern way - f-strings)
# How to display variable values in strings
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")
print(f"Next year I'll be {age + 1}")

# String methods
text = "  Hello World  "
print(text.lower())         # "  hello world  "
print(text.upper())         # "  HELLO WORLD  "
print(text.strip())         # "Hello World"
print(text.replace("World", "Python"))  # "  Hello Python  "
print(text.split())         # ["Hello", "World"]

# String slicing
word = "Python"
print(word[0])              # "P" (first character)
print(word[-1])             # "n" (last character)
print(word[0:3])            # "Pyt" (slice)
print(word[:3])             # "Pyt" (from start)
print(word[3:])             # "hon" (to end)
```

---

## 3. Lists (Arrays)

```python
# List creation
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# List operations
numbers.append(6)           # Add to end: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)        # Insert at index: [0, 1, 2, 3, 4, 5, 6]
numbers.remove(3)           # Remove value: [0, 1, 2, 4, 5, 6]
numbers.pop()               # Remove last: [0, 1, 2, 4, 5]
numbers.pop(0)              # Remove at index: [1, 2, 4, 5]

# List access
first = numbers[0]          # First element
last = numbers[-1]          # Last element
length = len(numbers)       # List length

# List slicing
subset = numbers[1:3]       # Elements 1 to 2
reversed_list = numbers[::-1]  # Reverse list

# List comprehension (create lists quickly)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

---

## 4. Dictionaries (Key-Value Pairs)

```python
# Dictionary creation
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Dictionary access
print(person["name"])       # "Alice"
print(person.get("age"))    # 25
print(person.get("country", "USA"))  # "USA" (default if not found)

# Dictionary operations
person["email"] = "alice@example.com"  # Add/update
del person["city"]          # Delete key
keys = person.keys()        # Get all keys
values = person.values()    # Get all values
items = person.items()      # Get key-value pairs

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 5. Tuples (Immutable Lists)

```python
# Tuple creation
coordinates = (10, 20)
single = (1,)               # Single element tuple needs comma
empty = ()

# Tuple unpacking
x, y = coordinates          # x=10, y=20

# Tuples are immutable (cannot change)
# coordinates[0] = 5        # ERROR!
```

---

## 6. Sets (Unique Values)

```python
# Set creation
numbers = {1, 2, 3, 4, 5}
unique = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Set operations
numbers.add(6)              # Add element
numbers.remove(3)           # Remove element
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)                # Union: {1, 2, 3, 4, 5}
print(a & b)                # Intersection: {3}
print(a - b)                # Difference: {1, 2}
```

---

## 7. If Statements

```python
# Basic if
age = 18
if age >= 18:
    print("Adult")

# If-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# If-elif-else
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# Ternary operator (one-liner)
status = "Adult" if age >= 18 else "Minor"

# Multiple conditions
if age >= 18 and score >= 80:
    print("Eligible")

if age < 18 or score < 50:
    print("Not eligible")
```

---

## 8. For Loops

```python
# Loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8 (start, stop, step)
    print(i)

# Loop with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Loop through dictionary
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")

# List comprehension (alternative to loops)
squares = [x**2 for x in range(5)]
```

---

## 9. While Loops

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

# While with continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue        # Skip even numbers
    print(count)        # Only prints odd numbers
```

---

## 10. Functions

Functions are defined using the `def` keyword.

```python
# Basic function
def greet():
    print("Hello!")

greet()                     # Call function

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)          # result = 8

# Function with default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}"

print(greet_with_title("Smith"))           # "Hello, Mr. Smith"
print(greet_with_title("Smith", "Dr."))    # "Hello, Dr. Smith"

# Function with multiple return values
def get_user():
    return "Alice", 25, "NYC"

name, age, city = get_user()

# Lambda functions (one-liners)
square = lambda x: x**2
print(square(5))            # 25

# Type hints (Python 3.14+)
def add_numbers(a: int, b: int) -> int:
    return a + b
```

---

## 11. Special Functions and Built-ins

```python
# Common built-in functions
print(len([1, 2, 3]))       # 3 (length)
print(max([1, 5, 3]))       # 5 (maximum)
print(min([1, 5, 3]))       # 1 (minimum)
print(sum([1, 2, 3]))       # 6 (sum)
print(abs(-5))              # 5 (absolute value)
print(round(3.7))           # 4 (round)
print(sorted([3, 1, 2]))    # [1, 2, 3] (sorted list)

# Type conversion
int("42")                   # String to int
float("3.14")               # String to float
str(42)                     # Int to string
list("hello")               # String to list: ['h', 'e', 'l', 'l', 'o']

# Input/Output
name = input("Enter name: ")    # Get user input
print("Hello", name)            # Print output

# Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, numbers))     # [2, 4, 6, 8, 10]
evens = list(filter(lambda x: x%2==0, numbers)) # [2, 4]

# Zip (combine lists)
names = ["Alice", "Bob"]
ages = [25, 30]
combined = list(zip(names, ages))  # [('Alice', 25), ('Bob', 30)]

# Any and All
print(any([False, True, False]))   # True (at least one True)
print(all([True, True, False]))    # False (not all True)
```

---

## 12. Classes and Objects

```python
# Basic class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# Create object
person = Person("Alice", 25)
print(person.greet())

# Class with properties
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area)          # 78.5

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying"

student = Student("Bob", 20, "S123")
print(student.greet())
print(student.study())
```

---

## 13. Exception Handling

```python
# Try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    number = int("abc")
except ValueError:
    print("Invalid number")
except Exception as e:
    print(f"Error: {e}")

# Try-except-else-finally
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
else:
    print("File opened successfully")
    file.close()
finally:
    print("This always runs")

# Raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

---

## 14. Modules and Packages

A **module** is simply any Python file (`.py`). You use `import` to use code from one file in another. A **package** is a folder containing multiple modules.

```python
import my_module            # Import entire module
from my_module import func  # Import specific part
import my_module as mm      # Import with alias
```

---

## 15. File Operations

```python
# Read file
with open("file.txt", "r") as file:
    content = file.read()       # Read entire file
    # lines = file.readlines()  # Read as list of lines

# Write file
with open("file.txt", "w") as file:
    file.write("Hello World\n")

# Append to file
with open("file.txt", "a") as file:
    file.write("New line\n")

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

## 16. Most Important Packages

### requests - HTTP requests

```python
import requests

response = requests.get("https://api.example.com/data")
print(response.status_code)     # 200
print(response.json())          # Parse JSON response

# POST request
data = {"name": "Alice", "age": 25}
response = requests.post("https://api.example.com/users", json=data)
```

### datetime - Date and time

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)                      # Current date/time
print(now.strftime("%Y-%m-%d")) # Format: "2026-01-08"

tomorrow = now + timedelta(days=1)
week_ago = now - timedelta(weeks=1)
```

### json - JSON handling

```python
import json

# Python to JSON
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)

# JSON to Python
parsed = json.loads(json_string)

# Read JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Write JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)
```

### os - Operating system

```python
import os

print(os.getcwd())              # Current directory
os.mkdir("new_folder")          # Create directory
os.listdir(".")                 # List files
os.path.exists("file.txt")      # Check if exists
os.path.join("folder", "file")  # Join paths
```

### pathlib - Modern path handling

```python
from pathlib import Path

path = Path("folder/file.txt")
print(path.exists())            # Check if exists
print(path.name)                # "file.txt"
print(path.parent)              # "folder"
print(path.suffix)              # ".txt"

# Create directory
Path("new_folder").mkdir(exist_ok=True)

# Read/write files
path.write_text("Hello")
content = path.read_text()
```

---

## 17. Pandas - Data Analysis

```python
import pandas as pd

# Create DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["NYC", "LA", "Chicago"]
}
df = pd.DataFrame(data)

# Display data
print(df)
print(df.head())                # First 5 rows
print(df.info())                # DataFrame info
print(df.describe())            # Statistics

# Access columns
print(df["name"])               # Single column
print(df[["name", "age"]])      # Multiple columns

# Filter rows
adults = df[df["age"] >= 30]
nyc_people = df[df["city"] == "NYC"]

# Add column
df["country"] = "USA"
df["age_next_year"] = df["age"] + 1

# Read/write CSV
df.to_csv("data.csv", index=False)
df = pd.read_csv("data.csv")

# Read/write Excel
df.to_excel("data.xlsx", index=False)
df = pd.read_excel("data.xlsx")

# Grouping and aggregation
grouped = df.groupby("city")["age"].mean()

# Sorting
sorted_df = df.sort_values("age", ascending=False)

# Handle missing data
df.dropna()                     # Remove rows with NaN
df.fillna(0)                    # Fill NaN with 0
```

---

## 18. Modern & Intermediate Concepts

### Async/Await (`async def`)

Crucial for modern web frameworks like FastAPI. Allows code to run non-blocking.

```python
import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(1)  # Simulate I/O work
    print("Done fetching")
    return {"data": 123}

# To run it:
# asyncio.run(fetch_data())
```

### Decorators (`@wrapper`)

Functions that wrap other functions to add behavior (used in routes, logging, auth).

```python
def log_execution(func):
    def wrapper():
        print("Running...")
        func()
        print("Done!")
    return wrapper

@log_execution
def say_hello():
    print("Hello!")

# say_hello() output:
# Running...
# Hello!
# Done!
```

### Dataclasses (`@dataclass`)

Modern, cleaner way to define classes that primarily hold data.

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    active: bool = True

user = User("Alice", 25)
print(user)  # User(name='Alice', age=25, active=True)
```

### Context Managers (`with`)

Ensures resources (files, connections) are closed properly, even if errors occur.

```python
# 'with' handles opening and closing automatically
with open("file.txt", "w") as f:
    f.write("Safe writing")
# File is automatically closed here
```

### Variable Arguments (`*args`, `**kwargs`)

Allow functions to accept any number of positional or keyword arguments.

```python
def flexible_func(*args, **kwargs):
    print(args)    # Tuple of positional arguments
    print(kwargs)  # Dictionary of keyword arguments

flexible_func(1, 2, name="Alice", active=True)
# Output:
# (1, 2)
# {'name': 'Alice', 'active': True}
```

### Script Entry Point

Standard boilerplate to ensure code only runs when executed as a script, not when imported.

```python
def main():
    print("Main program running")

if __name__ == "__main__":
    main()
```

### Generators (`yield`)

Functions that return values one at a time (lazy evaluation), saving memory.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Usage
for number in count_up_to(5):
    print(number)
```

---

## 19. Common Patterns

### List operations

```python
# Remove duplicates
unique_list = list(set([1, 2, 2, 3, 3]))

# Flatten nested list
nested = [[1, 2], [3, 4], [5]]
flat = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4, 5]

# Count occurrences
from collections import Counter
counts = Counter([1, 2, 2, 3, 3, 3])  # {3: 3, 2: 2, 1: 1}
```

### String operations

```python
# Join list to string
words = ["Hello", "World"]
sentence = " ".join(words)      # "Hello World"

# Check if string contains
if "hello" in "hello world":
    print("Found")

# Remove whitespace
text = "  hello  ".strip()      # "hello"
```

### Dictionary operations

```python
# Merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}     # {"a": 1, "b": 2, "c": 3, "d": 4}

# Get value with default
value = my_dict.get("key", "default")
```

---

## Quick Reference Card

```python
# Variables
x = 10

# Strings
f"Hello {name}"

# Lists
[1, 2, 3]
list.append(x)

# Dictionaries
{"key": "value"}
dict["key"]

# If
if condition:
    pass

# For
for item in items:
    pass

# While
while condition:
    pass

# Function
def func(param):
    return value

# Class
class MyClass:
    def __init__(self):
        pass

# Async
async def func():
    await other()

# Try-except
try:
    pass
except Exception:
    pass

# Import
import module
from module import function
```

---

## Practice Exercise

Try creating a simple program that:

1. Takes user input
2. Stores data in a list/dictionary
3. Processes the data with loops
4. Uses functions to organize code
5. Handles errors with try-except

```python
# Example: Simple contact manager
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added {name}")

def show_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

while True:
    action = input("Add (a) or Show (s) or Quit (q): ")
    if action == "q":
        break
    elif action == "a":
        name = input("Name: ")
        phone = input("Phone: ")
        add_contact(name, phone)
    elif action == "s":
        show_contacts()
```
