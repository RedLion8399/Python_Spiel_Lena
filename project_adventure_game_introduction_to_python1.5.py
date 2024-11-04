# Title: Adventure Game
# Version: 1.5.1
# Date: October 15, 2024 - November xx, 2024
# 
# Author: Lena Weinstock
# Linter: Paul Jonas Dohle
# Course: Computer Science ICS 3u
# School: Glebe Collegiate Institute, Ottawa
# Teacher: Mr Giassante
# 
# Description: This Python Program creates an immercive adventure
#               located in London. The players goal is to find a fugitive
#               criminal while having the possibility to take the underground
#               and the boat to catch the criminal with the help of so called
#               "passes" the player needs to find. After two travels, the pass
#               is not valid anymore and the player needs to switch it with a
#               new one.


from random import randint
from places import Desc, Objects, North, South, East, West, Up, Down
from functions import greeting, command_help


# setting beginning variables of player and computer

# Selecting a random point to start with excluding those, who can only reached by underground
player_position = 0  # position at beginning
while player_position == 0 or player_position == 1 or player_position == 7 or player_position == 8 or player_position == 9 or player_position == 10 or player_position == 18 or player_position == 19 or player_position == 20 or player_position == 29 or player_position == 30 or player_position == 34 or player_position == 35 or player_position == 36 or player_position == 37 or player_position == 38 or player_position == 39 or player_position == 40 or player_position == 54 or player_position == 64 or player_position == 71 or player_position == 72 or player_position == 73 or player_position == 74 or player_position == 75 or player_position == 76 or player_position == 77 or player_position == 78:
    player_position = randint(1,81)


thief_position = 0

while thief_position == 0 or thief_position == player_position or thief_position == 34 or thief_position == 35 or thief_position == 36 or thief_position == 37 or thief_position == 38 or thief_position == 39 or thief_position == 40 or thief_position == 54 or thief_position == 64 or thief_position == 71 or thief_position == 72 or thief_position == 73 or thief_position == 74 or thief_position == 75 or thief_position == 76 or thief_position == 77 or thief_position == 78:
    thief_position = randint(1,81)
    while thief_position + 2 == player_position or thief_position - 2 == player_position:
        thief_position = randint(1,81)
    while thief_position + 20 == player_position or thief_position - 20 == player_position:
        thief_position = randint(1,81)

# defining some variables for later
quitting = False
command = " "
boat_or_train = 0
inhand = " "
transition = " "
moves = 0

greeting()

while not quitting:
    while command != "N" and command != "S" and command != "W" and command != "E" and command != "U" and command != "D" and command != "X" and command != "P" and command != "K" and command != "Q" :     
        command_help()

        # Printing the position of the thief an the player
        print()
        print(f"You are in/on/at {Desc[player_position]}.")
        print()
        print(f"The thief is in/on/at {Desc[thief_position]}.")
        print()

        # position directions and options
        if North[player_position]:
            print(f"You can go North to {Desc[North[player_position]]}.")
        else:
            print("You cannot go North.")
        print()

        if South[player_position]:
            print(f"You can go South to {Desc[South[player_position]]}.")
        else:
            print("You cannot go South.")
        print()

        if East[player_position]:
            print(f"You can go East to {Desc[East[player_position]]}.")
        else:
            print("You cannot go East.")
        print()
        
        if West[player_position]:
            print(f"You can go West to {Desc[West[player_position]]}.")
        else:
            print("You cannot go West.")
        print()

        if Down[player_position]:
            print(f"You can go down to {Desc[Down[player_position]]}.")
        else:
            print("There is no (other) underground station here.")
        print()
            
        if Up[player_position]:
            print(f"You can go up to {Desc[Up[player_position]]}.")
        else:
            print("You are currently not in an underground station.")
        print()

        second_digit_com = 0

        # Explain where the thief is: 
        pos_com_str = str(thief_position)
        pos_com_list = list(pos_com_str)

        position_str = str(player_position)
        position_list = list(position_str)

        if thief_position < 10:
            pos_com_list = [0] + pos_com_list
        if player_position < 10:
            position_list = [0] + position_list


        first_digit_com = int(pos_com_list[0])
        second_digit_com = int(pos_com_list[1])

        first_digit_player = int(position_list[0])
        second_digit_player = int(position_list[1])

        if thief_position == player_position:
            print()
            print()
            print("Congratulations! You have successfully caught the thief!")
            print("Good job!")
            print()
            exit()

        if first_digit_player < first_digit_com:
            print("The thief is more in the South.")
            print()
        elif first_digit_player > first_digit_com:
            print("The thief is more in the North.")
            print()        
        elif first_digit_player == first_digit_com:
            print("The thief is on the same height as you. You are close, try to go West or East.")
            print()


        if second_digit_player > second_digit_com:
            print("The thief is more in the West.")
            print()
            print()
        elif second_digit_player < second_digit_com:
            print("The thief is more in the East.")
            print()
            print()
        elif second_digit_player == second_digit_com:
            print("The thief is on the same height as you. You are close, try to go North or South.")
            print()
            print()

        # random object

        if Objects[player_position] == 5:
            str(Objects[player_position])
            boat_or_train = randint(1,4)
            if boat_or_train == 1:
                Objects[player_position] = "boat-ticket"
            else:
                Objects[player_position] = "underground-ticket"
        elif Objects[player_position] != 5:
            str(Objects[player_position])
            Objects[player_position] = " "

       
        # inventary
        if inhand == " ":
            print("You have currently nothing in your hand.")
            print()
            print()
        else:
            print(f"You are currently in possession of a/an {inhand}.")
            print()
            print()

        # Objects

        if Objects[player_position] == ("underground-ticket" or Objects[player_position] == "boat-ticket") and inhand == " ":
            print(f"You can pick-up the: {Objects[player_position]}.")
            print()
        elif Objects[player_position] == ("underground-ticket" or Objects[player_position] == "boat-ticket") and inhand != " ":
            print(f"You can switch the: {inhand} with a/an {Objects[player_position]}.")
            print()


        # Choice after information
        command = input("select a command out of the list above: ")
        print()

        ### Validity boat tickets


        if inhand == "Used_once_boat-ticket":
            if player_position == 29 and command != "S":
                inhand = inhand
            if player_position == 50 and command != "N":
                inhand = inhand
            if player_position == 50 and command == "N":
                inhand = " "
            elif player_position == 29 and command == "S":
                inhand = " "
        

        if inhand == "boat-ticket":
            if player_position == 29 and command != "S":
                inhand = inhand
            if player_position == 50 and command != "N":
                inhand = inhand        
            elif player_position == 29 and command == "S":
                inhand = "Used_once_boat-ticket"
            elif player_position == 50 and command == "N":
                inhand = "Used_once_boat-ticket"
        

        # atempt nr. 3 validity of tickets
            
        if inhand == "Used_once_underground-ticket":
            if player_position == 71 and (command == "N" or command == "S" or command == "E"):
                inhand = " "
            if player_position == 72 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = " "
            if player_position == 73 and (command == "N" or command == "W"):
                inhand = " "
            if player_position == 74 and (command == "N" or command == "E"):
                inhand = " "
            if player_position == 75 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = " "
            if player_position == 76 and (command == "N" or command == "E"):
                inhand = " "
            if player_position == 77 and (command == "N" or command == "E"):
                inhand = " "
            if player_position == 78 and (command == "N" or command == "W"):
                inhand = " "
            
        if inhand == "underground-ticket":
            if player_position == 71 and (command == "N" or command == "S" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif player_position == 72 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = "Used_once_underground-ticket" 
            elif player_position == 73 and (command == "N" or command == "W"):
                inhand = "Used_once_underground-ticket"
            elif player_position == 74 and (command == "N" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif player_position == 75 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = "Used_once_underground-ticket"
            elif player_position == 76 and (command == "N" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif player_position == 77 and (command == "N" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif player_position == 78 and (command == "N" or command == "W"):
                inhand = "Used_once_underground-ticket"
            
            

        # What happens with selected command:

        if command == "N" and North[player_position]:
            player_position = North[player_position]

        elif command == "S" and South[player_position]:
            player_position = South[player_position]

        elif command == "W" and West[player_position]:
            player_position = West[player_position]

        elif command == "E" and East[player_position]:
            player_position = East[player_position]

        elif command == "U" and Up[player_position]:
            player_position = Up[player_position]

        elif command == "D" and Down[player_position]:
            player_position = Down[player_position]

        elif command == "X" and inhand != " " and Objects[player_position] == " ":
            Objects[player_position] = inhand
            inhand = " "

        elif command == "P" and inhand == " " and Objects[player_position] != " ":
            inhand = Objects[player_position]
            Objects[player_position] = " "

        elif command == "K" and inhand != " " and Objects[player_position] != " ":
            transition = inhand
            inhand = Objects[player_position]
            Objects[player_position] = transition

        elif command == "Q":
            print()
            print("Good bye! I hope you had fun playing this game!")
            print()
            exit()
        
        else:
            print()
            print()
            print()
            print()
            print(f"This command is not possible in/on/at {Desc[player_position]}. Please try again")



        

        # fix problem with free rides underground and boat

        if player_position == 71 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print()
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print()
            player_position = 1
        elif player_position == 72 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print()
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print()
            player_position = 6
        elif player_position == 73 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print()
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print()
            player_position = 17
        elif player_position == 74 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print()
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print()
            player_position = 21
        elif player_position == 75 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print()
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print()
            player_position = 23
        elif player_position == 76 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print()
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print()
            player_position = 52
        elif player_position == 77 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print()
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print()
            player_position = 66
        elif player_position == 78 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print()
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print()
            player_position = 79
        elif player_position == 50 and inhand != "boat-ticket" and inhand != "Used_once_boat-ticket":
            print()
            print("You cannot take the boat without a valid ticket.")
            print("Please try again.")
            print()
        elif player_position == 29 and inhand != "boat-ticket" and inhand != "Used_once_boat-ticket":
            print()
            print("You cannot take the boat without a valid ticket.")
            print("Please try again.")
            print()
            
        
        # thief position(pos_com)
        moves += 1
        
        # emptying command for while loop
        command = " "


        if moves == 3:
            pos_com_random = randint(1,5)
            if pos_com_random == 1 and West[thief_position] != 0:
                thief_position -= 1
                moves = 0
            elif pos_com_random == 2 and thief_position == 50:
                thief_position = 29
                moves = 0
            elif pos_com_random == 2 and North[thief_position] != 0:
                thief_position -= 10
                moves = 0
            elif pos_com_random == 3 and East[thief_position] != 0:
                thief_position += 1
                moves = 0
            elif pos_com_random == 3 and thief_position == 29:
                thief_position = 50
                moves = 0
            elif pos_com_random == 4 and South[thief_position] != 0:
                thief_position += 10
                moves = 0

            elif pos_com_random == 1 and West[thief_position] == 0:
                break
            elif pos_com_random == 2 and North[thief_position] == 0:
                break
            elif pos_com_random == 3 and East[thief_position] == 0:
                break
            elif pos_com_random == 4 and South[thief_position] == 0:
                break
