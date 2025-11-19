# Rock Paper Scissors Game
# Classic game with ASCII art and score tracking
# Author: yoan9601

import random

# ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock Paper Scissors!")
print("Type 0 for Rock, 1 for Paper, 2 for Scissors\n")

# User input with validation
while True:
    try:
        user_choice = int(input("Your choice: "))
        if user_choice in [0, 1, 2]:
            break
        else:
            print("Invalid number! Please type 0, 1 or 2.\n")
    except ValueError:
        print("Please type a number (0, 1 or 2)!\n")

print("\nYou chose:")
print(game_images[user_choice])

# Computer choice
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Result logic
print("\n" + "═" * 40)
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
print("═" * 40)

print(f"\nYou: {choices[user_choice]}  |  Computer: {choices[computer_choice]}")
print("Thanks for playing!")
