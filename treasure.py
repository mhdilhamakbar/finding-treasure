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


print("Welcome to treasure land")
print("Your Mission is to find the treasure")
game_1 = input("Where do you want to go? Type 'left' or 'right' \n").lower()

if game_1 == "left":
   game_2 = input('You\'ve come to a lake,type "wait" to wait or "swim" to swim \n').lower()
   if game_2 == "wait":
        game_3 = input('A boat pick you up, you\'ve arrive the destination, there are 3 doors, choose one you want "blue","yellow" or "red"\n').lower()
        if game_3 == "yellow":
            print("It's a room full of fire. Game Over")
        elif game_3 == "blue":
            print("You found the treasure. You win!")
        elif game_3 == "red":
            print("You enter a wrong room. Game Over")
        else:
            print("You choose the door doesn't exist.Game Over")
   else :
       print("you got attacked by shark. Game Over")

else :
    print("You fell into hole.Game Over")
  
               