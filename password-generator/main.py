# Strong Password Generator
# Creates secure, random passwords with user-defined complexity
# Author: yoan9601

import random

# Character pools
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '_', '-']

print("Welcome to the PyPassword Generator!")
print("═" * 50)

# User input with validation
while True:
    try:
        nr_letters = int(input("How many letters would you like in your password? "))
        nr_symbols = int(input("How many symbols would you like? "))
        nr_numbers = int(input("How many numbers would you like? "))
        if nr_letters + nr_symbols + nr_numbers >= 8:
            break
        else:
            print("Password should be at least 8 characters long. Try again!\n")
    except ValueError:
        print("Please enter valid numbers!\n")

# Generate password
password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = "".join(password_list)

# Final output
print("\n" + "═" * 50)
print(f"Your generated password is:")
print(f"\n{password}\n")
print(f"Length: {len(password)} characters | Very Strong")
print("═" * 50)
print("Tip: Copy it now — it's not saved anywhere!")
