print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choose = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
if choose == 'left'.capitalize():
    print("You Come to a lake. There is an island in the middle of the lake.")
    wait_path = input(
        "Type 'wait' to wait for a boot or 'swin' to swin across. ")
    if wait_path == 'wait'.capitalize():
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        color_path = input("Which colour do you choose? ")
        if color_path == "yellow".capitalize():
            print("You found a treasure, You Win!")
        elif color_path == "blue".capitalize():
            print("You enter a room of beasts. Game Over!")
        else:
            print("It's a room full of fire. Game Over!")
    else:
        print("You get attacked by an angly trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")

# Copy, I'll make another with my own history.
