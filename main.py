# Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters = []
for letter in range(1, nr_letters + 1):
    random_letters.append(letters[random.randint(0,len(letters) - 1)])

random_symbols = []
for symbol in range(1, nr_symbols + 1):
    random_symbols.append(symbols[random.randint(0,len(symbols) - 1)])

random_number = []
for num in range(1,nr_numbers + 1):
    random_number.append(numbers[random.randint(0,len(numbers) - 1)])

concatenate_lists = random_letters + random_symbols + random_number

shuffle_list = random.sample(concatenate_lists,k=len(concatenate_lists))
password = ''.join(shuffle_list)
print(f'Your password is: {password}')
print('Password lenght is:', len(password))