import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password_list = []
# the password has to be a list in order for the shuffle() function to work. hence we are creating an empty list to
# contain the not generated password characters

for letter in range(0, nr_letters):
    password_list += random.choice(letters)

for symbol in range(0, nr_symbols):
    psymbol = random.choice(symbols)
    password_list += psymbol
for number in range(0, nr_numbers):
    pnumbers = random.choice(numbers)
    password_list += pnumbers

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
# Now we have to create an empty password string to capture the password characters, for we to be able to turn the
# earlier created password_list to a string. And by doing this we need a for loop to loop through the password_list
# list to add each character to the empty password string now created
for lett in password_list:
    password += lett
print(f" Your password is: {password}")

# An example to show me how to use the range function on a list
# lst = [10, 50, 75, 83, 98, 84, 32]
# for x in range(len(lst)):
#     print(lst[x])
