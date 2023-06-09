"""
Python conditions and if statements
Python supports the usual logical conditions from maths:
equals: a == b
Not equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

# if statement

a = 40
b = 300
if b > a:
    print("b has more value than a")

# Indentation 
"""
Python relies on indentation to define scope in the code.
"""

# Elif
# used where there are more conditions to be met

a = 40
b = 300
if b > a:
    print("b has more value than a")
elif a == b:
    print("a and b are equal")

# else
# The else keyword catches anything which isn't caught by the preceding conditions

a = 4768
b = 300
if b > a:
    print("b has more value than a")
elif a == b:
    print("a and b are equal")
else:
    print("a has value that b")

# Short Hand If ... Else
"""
If you have only one statement to execute, one for if, and one for else,
you can put it all on the same line"""

a = 10
b = 145
print("Yes") if a > b else print("No")

# And
# The and keyword is a logical operator, and is used to combine conditional statements

a = 100
b = 56
c = 1000
if a > b and c > a:
    print("Both conditions are True")

# Or - The or keyword is a logical operator and is used to combine conditional statements

a = 100
b = 56
c = 1000
if a > b or a > c:
    print("At least one of the conditions is True")

"""
Not - The not keyword is a logical operator, and is used to reverse the result of the conditional statement
"""

a = 100
b = 56
if  not a > b:
    print(" a is NOT greater than b")

"""
Nested If - You can have if statements inside if statements,
this is called nested if statements"""

x = 67

if x > 30:
    print("Above Fifty")
    if x > 50:
        print("and also above 50")
    else:
        print("but not above 50.")

"""
The Pass Statement
if statements cannot be empty, but if you for some reason have an if
statement with no content, put in the pass statement to avoid getting an error"""

a = 21
b = 300

if b > a:
    pass

# ------------------------------------------

# Python While Loops
# With while loops we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
    print(i)
    i += 1 # remember to increment i, or else the loop will continue forever.

# The break statement
# With break statement we can stop the loop even if the while condition is true.

# Exit the loop when i is 3:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue statement
# With the continue statement we can stop the current iteration, and 
# continue with the next

# continue with the next iteration if i is 3

i = 0
while i < 6:
    print(i)
    if i == 3:
        continue
    print(i)

""" The else Statement
With the else statement we can run a block of code once when the 
condition no longer is true"""

# Print a message once the condition is false
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


#--------------------------------------------------------------------------------

# Python For Loops
""" A for loop is used for iterating over a sequence (list, dict etc).
With the for loop we can execute a set of statements, once for each item 
in a list, tuple, set etc. """

# Print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# The for loop does not require an indexing variable to set beforehand.

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters
# loop through the letters in the word "banana"

for x in "banana":
    print(x)

# The break statement
""" With the break statement we can stop the loop before it has looped
through all the items"""
# Exit the loop when x is banana

fruits = ["apple", "banana", "Melon"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# The continue statement
""" With the continue statement we can stop the current iteration of the loop, 
and continue with the next"""

# Do not print banana
fruits = ["apple", "banana", "Melon"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
""" To loop through a set of code a specified number of times, we can use
the range() function,
The range() function returns a sequence of numbers, starting from 0 by default 
and increments by 1 (by default), and ends at a specified number"""

for x in range(8):
    print(x)

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
""" The range() function defaults to 0 as a starting value, however it is possible
to speecify the starting value by adding a parameter: range(2, 6), which means values
from 2 to 6 (but not inclunding 6)"""

for x in range(2, 6):
    print(x)

""" The range() function defaults to increment the sequence by 1, however it is possible to 
specify the increment value by adding a third parameter
range(2, 30, 3)"""

for x in range(2, 30, 3):
    print(x)

# Else in For Loop
""" The else keyword in a for loop specifies a block of code to be executed when the loop
is finished"""

# Print all numbers from 0 to 5 and print a message when the loop has ended

for x in range(6):
    print(x)
else:
    print("Finally ended")

# Note: The else block will NOT be executed is the loop is stopped by a break statement

# Break the loop when x is 3

for x in range(8):
    if x ==3: break
    print(x)
else:
    print("Finally ended")

# Nested Loops
""" A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop" """

# Print each adjective for every fruit

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# The pass statement
""" for loops cannot be empty, but if you for some reason have a for loop with no content,
put in the pass statement to avoid getting an error."""

for x in [0, 1, 2]:
    pass