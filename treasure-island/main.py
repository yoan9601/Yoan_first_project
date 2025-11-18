# Treasure Island – Text Adventure Game
# Classic "choose your own adventure" game
# Author: yoan9601

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|         |  ,-.    |    |  |   |  |    |   |  |    |   |
|_________|__""|____|____|__|___|__|____|___|__|____|___|
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")

# First choice
choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right": ').strip().lower()

if choice1 == "left":
    # Second choice
    choice2 = input("\nYou\'ve come to a lake. There is an island in the middle of the lake.\n"
                    "Type 'wait' to wait for a boat. Type 'swim' to swim across: ").strip().lower()

    if choice2 == "wait":
        # Third choice
        choice3 = input("\nYou arrive at the island unharmed.\n"
                        "There is a house with 3 doors: one red, one yellow, and one blue.\n"
                        "Which door do you choose? ").strip().lower()

        print("\n" + "═" * 50)
        if choice3 == "yellow":
            print("You open the yellow door...")
            print("CONGRATULATIONS! You found the treasure! YOU WIN!")
            print('''
    ████████╗██████╗ ███████╗ █████╗ ███████╗██╗   ██╗██████╗ ███████╗
    ╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝
       ██║   ██████╔╝█████╗  ███████║███████╗██║   ██║██████╔╝█████╗
       ██║   ██╔══██╗██╔══╝  ██╔══██║╚════██║██║   ██║██╔══██╗██╔══╝
       ██║   ██║  ██║███████╗██║  ██║███████║╚██████╔╝██║  ██║███████╗
       ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
            ''')
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You entered a room full of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
        print("═" * 50)

    else:
        print("You tried to swim... An angry trout attacks you. Game Over.")

else:
    print("You fell into a deep hole. Game Over.")

print("\nThanks for playing Treasure Island!")
