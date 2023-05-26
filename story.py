# #welcome message for Azubi Africa
# print("Welcome to Azubi Africa!")

# # Prompt the user to enter personal details
# print("Kindly enter your name, country and favourite drinks, tea/coffee/water")
# name = input("Enter your name ")
# country = input("Enter your country ")
# drink = input("Enter drink ")

# # Print the final word
# print (f'Hello,  {name} . Your country is  {country}  and favourite drink is  {drink}')


# Calculator
# x =5
# y = 9

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error: division by zero"
#     else:
#         return x / y

# print(add(x,y))
# print(subtract(x,y))
# print(multiply(x,y))
# print(divide(x,y))

## Sample function example
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     return sum

# result = add_numbers(5, 4)
# result_2 = add_numbers(7, 9)

# print('Sum: ', result)
# print('Sum: ', result_2)

eng_ger_colors = {"red" : "rot", "green" : "grun", "blue" : "blau", "yellow" : "gelb"}
print(eng_ger_colors)

eng_color = input("Please enter an English color: ")
ger_color = input("Please enter the German translation: ")

eng_ger_colors[eng_color] = ger_color

color = input("Which color should be translated? ")
print("The German word for", color, "is", eng_ger_colors[color])

# Bank account
name = "Joshua"
country = "Kenya"
Account_no = 33044567
contact = "0799085432"
next_of_kin = "James"
balance = 100

# Working with Dictionaries
person_1_dict = {name : "Joshua", country : "Kenya", Account_no : 33044567,
                contact : "0799085432", next_of_kin : "James", balance : 100}

# print("Account Holder: " + person_1_dict[name])
# print("Account Country: " + person_1_dict[country])
# print(f"Account number: {person_1_dict[Account_no]}")
# print(f"Account balance: {person_1_dict[balance]}")


# store bank accounts
list_of_accounts = [
    {name : "Joshua", country : "Kenya",Account_no : 33044567,
    contact : "0799085432", next_of_kin : "James", balance : 100},
    {name : "Ruth", country : "Malawi",Account_no : 34568473,
    contact : "0756789565", next_of_kin : "Shane", balance : 50},]

# Print name, account number and balance
for account in list_of_accounts:
    name = account[name]
    Account_no = account[Account_no]
    balance = account[balance]
    print("Name: ", name)
    print("Account Number: ", Account_no)
    print("Balance: ", balance)
    print("---------------------")

# print(f"Account 1: {list_of_accounts[0][balance]}")
# print(f"Account 2: {list_of_accounts[1][balance]}")
# print(f"Account 3: {list_of_accounts[2][balance]}")
# print(f"Account 4: {list_of_accounts[3][balance]}")


