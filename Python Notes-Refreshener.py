# OOP Object Oriented Programming *SOS*
class Person:
    #constructor
    def __init__(self, name, age):

        self.name = name
        self.age = age

    #Magic Method
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

    #a simple method inside the Student object
    def average(self):
        return sum(self.grades) / len(self.grades)

# Magic methods
Bob = Person("Bob", 35)

print(Bob.name)
print(Bob)


# Static and Class Methods!
class ClassTest:

    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod # A decorator that creates a class method
    def class_method(cls):
        # Used as a factory
        print(f"Called class_method of {cls}")


    @staticmethod # A decorator that creates a static method
    def static_method():
        # just a function to do something
        print("Called static_method.")


class Book:

    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, book_weight: int):

        self.name = name
        self.book_type = book_type
        self.weight = book_weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, Book.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)

        
print(Book.TYPES)
book = Book("Harry Potter", "hardcover", 1500)
print(book)

book1 = Book.hardcover("Harry Potter", 1500)
print(book1)

# Class Inheritance
class Device:

    def __init__(self, name, connected_by):

        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")

printer = Device("Printer", "USB")
print(printer)
printer.disconnect()

class Printer(Device):

    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):

        if not self.connected:
            print("Your printer is not connected")
            return 
        print("Printing {pages} pages")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
printer.print(30)
print(printer)s
        
printer.disconnect() 

# Class Composition --> Classes that have other classes 
# Inheritance will not be used that much, composition will be used more

class BookShelf:

    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookself with {len(self.books)} books."

shelf = BookShelf(300)

print(shelf)

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"
    
book1 = Book("Harry Potter")
book2 = Book("The Hobbit")

shelf = BookShelf(book1, book2)
print(shelf)

# Type Hinting in python > 3.5
# It is important cause you 're get told what to pass

from typing import List

def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books"

# Errors/Exceptions and How to catch 'em
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

grades = []

print("Welcome to the AVG grade program.")

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")
except ValueError as v:
    pass
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you!")

# Custom Error Classes | Inherit from built-in Python Error Classess
class TooManyPagesReadError(ValueError):
    pass    

class Book:
    
    def __init__(self, name: str, page_count: int):
        self.name = name 
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
            )

        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")

python101 = Book("Python 101", 50)

# First Class Functions
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values) # *values means that a number of values is imported

# We pass as an argument a function
result = calculate(20, 4, operator = divide)
print(result)

def search(sequence, expected, finder_function):
    for elem in sequence:
        if finder_function(elem) == expected:
            return elem
    
    raise RuntimeError(f"")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Rolf Smith", lambda friend: friend["name"]))

# Simple Decorators in Python
# Decorators allow us to modify functions
user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return 1234

def make_secure(func):
    def secure_function(): # this function replaces the get_admin_password
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user["username"]}."
        
    return secure_function

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())

# The at syntax for Decorators
import functools

user = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func) # add this line to keep the function's name
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."
        
    return secure_function

@make_secure
def get_admin_password():
    return 1234

print(get_admin_password())
print(get_admin_password.__name__)

# Decorating with parameters
import functools

user = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func) 
    def secure_function(*args, **kwargs): # use *args or **kwargs to be able to use this decorator with every argument
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."
        
    return secure_function

@make_secure
def get_admin_password():
    return 1234

print(get_admin_password())
print(get_admin_password.__name__)

# Decorators with parameters 
import functools

user = {"username": "jose", "access_level": "admin"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func) 
        def secure_function(*args, **kwargs): # use *args or **kwargs to be able to use this decorator with every argument
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No admin permissions for {user['username']}."
            
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())

# Mutability in Python
a = 8597
b = 8597

c = "hello"
d = c

print(id(c))
print(id(d))

# Mutable Default parameters
from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: List[int] = []): #This is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)

# Better approach
class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None): #This is bad!
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
