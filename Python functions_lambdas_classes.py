# Python Functions
""" A function is a block of code which only runs when it is called.
You can pass data, k    nown as parameters, into a function. 
A function can return data as a result."""

# Creating a function

def my_function():
    print("Hello, DevOps Engineer")

# Calling a function

def my_function():
    print("Hello, DevOps Engineer")

my_function()

#Arguments
""" Info can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses.
You can add as many arguments as you want, just separate them with a comma."""

def my_function(fname):
    print(fname + " Murikis")

my_function("Joshua")
my_function("Mwendas")
my_function("Linus")

# Number of Arguments
""" By default, a function must be called with the correct number of 
arguments. Meaning that if your function expects 2 arguments, you have 
to call the function with 2 arguments, not more and not less."""

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Joshua", "Muriki") # if you try to call the function with 1 or 3 arguments,
# you will get an error

# Arbitrary Arguments, *args
""" If you don't know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments and can access
the items accordingly"""

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("John", "Brian", "Tobias")

# Keyword Arguments
""" You can also send arguments with the key = value syntax
This way the order of the argument does not matter"""

def my_function(child3, child2, child1):
    print("The oldest child is " + child3)

my_function(child1 = "Emilio", child2 = "Tobias", child3 = "Linus")

# Arbitrary keyword Arguments, ** kwargs
""" Two asterisk are added before the parameter name in the function, when unknown 
number of keyword arguments will be passed.

This way the function will receive a dictionary of arguments and can 
access the items accordingly"""

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Johnson")

# Default parameter value
# The following example shows how to use a default parameter value
# If we call the function without argumentm it uses the default value

def my_function(country = "Kenya"):
    print(f"I am from + {country}")

my_function("Sweden")
my_function("China")
my_function("India")
my_function()
my_function("Brazil")

# Passing a list as an Argument
""" You can send any data types of argument to a function (string, number,
list, dict etc) and it will be treated as the same data type inside the function
If you send a List as an argument, it will still be a list when it reaches the function"""

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cheery"]

my_function(fruits)

# Return Values
# To let a function return a value, use the return statement

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(8))

# The pass statement
""" function definitions cannot be empty, but in case there is
put in the pass statement to avoid geetting an error"""

def myfunction():
    pass

# Recursion 
""" Python also accepts function recursion, which means a defined function 
can call itself.

Recursion is a common mathematical and programming concept. It means that a 
function calls itself. This has the benefit of meaning that you can loop through
data to reach a result. 

E.g. tri_recursion() is a function that we have defined to call itself ("recurse).
We use the k variable as the data, which decrements (-1) every time we recurse. The 
recursion ends when the condition is not greater that 0 (i.e. when it is 0)."""

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else: 
        result = 0
    return result

print ("\n\nRecursion Example Results")
tri_recursion(6)

#---------------------------------------------------------------------------------------------

# Python Lambda
""" A lambda function is a small anonymous function, it can take any number of arguments, 
but can only have one expression"""

# Syntax
# lambda arguments : expression
# e.g. add 8 to argument a, and return the result

x = lambda a : a + 8
print(x(5))

# Lambda functions can take any number of arguments
# Multiply argument a with argument b and return the result

x = lambda a, b :a * b
print(x(5, 6))

# Why use Lambda Functions?
"""The power of lambda is better shown when you use them as an anonymous 
function inside another function."""

def myfunc(n):
    return lambda a : a * n

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Use lambda functions when an anonymous function is required for a 
# short period of time.

# -----------------------------------------------------------------------------

# Python classes and Objects
""" Since Python is an object oriented programming language, 
A class is like an object constructor, or a "blueprint" for creating objects"""

# To create a class, use the keyword class:

class MyClass:
    x = 2

print(MyClass)

# We can create object in classes

class MyClass:
    x = 2

p1 = MyClass()
print(p1.x)

# The_init_() Function

""" To understand the meaning of classes we have to understand the built-in
_init_() function.

All classes have a function called _init_(), which is always executed when
the class is being initiated.

Use the _init_() function to assign values to object properties, or other operations
that are necessary to do when the object is being created"""

# Create a class named person, use the _init_() function to assign values for 
# name and age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Joshua", 27)

print(p1.name)
print(p1.age)

# The _init_() function is called automatically every time the class is being used 
# to create a new object

# The _str_() Function

""" The _str_() function controls what should be returned when the class object is represented as a string.

If the _str_() function is not set, the string representation of the object is returned."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Joshua", 27)

print(p1)

# Object Methods

""" Objects can also contain methods. Methods in objects are functions
that belong to the object."""

# Insert a function that prints a greeting, and execute it on the p1 object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Joshua", 27)
p1.myfunc()

# The self Parameter

"""The self parameter is a reference to the current instance of the class,
and is used to access variables that belong to the class

It does not have to be named self"""

class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def myfunc(abc):
        print(f"my name is {abc.name} and am a DevOps Engineer")

p1 = Person("Joshua", 27)
print(myfunc)

# The pass Statement
""" Class definitions cannot be empty, bit if you for some reason have a 
class definition with no content, put in the pass statement to avoid
getting an error."""

class Person:
    pass

#-----------------------------------------------------------------------------