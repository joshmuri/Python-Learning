#Python Lists
# Lists are used to store multiple items in a single variable
# Lists are created using square brackets

thislist = ["apple", "banana", "cherry"]
print(thislist)

# lists items are ordered, changeable and allow duplicate values.
# Lists items are indexed, the first item has index [0], the second item has index[1]
# Ordered - it means items have a defined order, new items will be place at the end of the list.
# Changeable - change, add and remove items in a list
# Allow duplicates - lists can have items with the same value

thislist2 = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
print(thislist2)

# List length
# To determine how many items a list has, use the len() function

#print the number of items in the list
thislist2 = ["apple", "banana", "cherry"]
print(len(thislist2))

# Lists Items can be of any data type
# string, int and boolean

list = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# list can contain different data types
list4 =  ["abc", 34, True, 40, "Male"]

# Data type of a list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
# Using the list() constructor to make a list

thislistconstructor = list(("apple", "banana", "cherry"))
print(thislistconstructor)

# Python Collections (Arrays)
# List is a collection which is ordered and changeable. Allows duplicate members
# Tuple is a collection of which is ordered and unchangeable. Allows duplicate members.
# set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered and changeable. No duplicate members.

# Python - Access List Items
# Access items
# Lists items are indexed and you can access them by referring to the index number.

thislist3 = ["apple", "banana", "cherry"]
print(thislist3[1])

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item

thislist3 = ["apple", "banana", "cherry"]
print(thislist3[-1])

# Range of Indexes
# Specify a range of indexes by specifying where to start and where to end the range
# Return the third, fourth and fifth item

# The search will start at index 2 (included) and end at index 5 (not included)
thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4)

# Leaving our start value
# This one returns the items from the beginning to, but NOT including, "Kiwi"

thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[:4])

# Leaving out the end value.
# This returns the items from "cherry to the end"

thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[2:])

# range of Negative indexes
# specify negative indexes if you want to start the search from the end of the list
# This below returns the items from "orance" (-4) to, but NOT including "mango" (-1)

thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[-4:-1])

# Check if item Exists
# To determine if a specified item is present in a list use the in keyword.

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")