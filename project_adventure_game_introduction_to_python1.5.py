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

# setting beginning variables of payer and computer

# Selecting a random point to start with excluding those, 
position = 0  # position at beginning
while position == 0 or position == 1 or position == 7 or position == 8 or position == 9 or position == 10 or position == 18 or position == 19 or position == 20 or position == 29 or position == 30 or position == 34 or position == 35 or position == 36 or position == 37 or position == 38 or position == 39 or position == 40 or position == 54 or position == 64 or position == 71 or position == 72 or position == 73 or position == 74 or position == 75 or position == 76 or position == 77 or position == 78:
    position = randint(1,81)


pos_com = 0 # position of computer

while pos_com == 0 or pos_com == position or pos_com == 34 or pos_com == 35 or pos_com == 36 or pos_com == 37 or pos_com == 38 or pos_com == 39 or pos_com == 40 or pos_com == 54 or pos_com == 64 or pos_com == 71 or pos_com == 72 or pos_com == 73 or pos_com == 74 or pos_com == 75 or pos_com == 76 or pos_com == 77 or pos_com == 78:
    pos_com = randint(1,81)
    while pos_com + 2 == position or pos_com - 2 == position:
        pos_com = randint(1,81)
    while pos_com + 20 == position or pos_com - 20 == position:
        pos_com = randint(1,81)

# defining some variables for later
quitting = False
command = " "
boat_or_train = 0
inhand = " "
transition = " "
moves = 0



print("""
   ____         __  __             __  __  __            __
  / __/______  / /_/ /__ ____  ___/ /  \ \/ /__ ________/ /
 _\ \/ __/ _ \/ __/ / _ `/ _ \/ _  /    \  / _ `/ __/ _  / 
/___/\__/\___/\__/_/\_,_/_//_/\_,_/     /_/\_,_/_/  \_,_/  
                                                           
""")
   
print("Let's play a game!")
print("You are a detective in London.")
print("The goal is to find the criminal.")
print("You will be able to find tickets to use the underground and even the boat,")
print("but be careful! The tickets are only valid two times.")
print("Have fun!")


while not quitting:
    while command != "N" and command != "S" and command != "W" and command != "E" and command != "U" and command != "D" and command != "X" and command != "P" and command != "K" and command != "Q" :     
        print(" ")
        print(" ")
        print("[N] to go north")
        print("[S] to go south")
        print("[W] to go west")
        print("[E] to go est")
        print("[U] to go up(underground)")
        print("[D] to go down(underground)")
        print("[X] to drop the item in that place (You will not find it there again)")
        print("[P] to pick up the item in that place")
        print("[K] to switch the item you have with the item in that place")
        print("[Q] to quit the game")
        print(" ")

        # where am I + thief
        print(" ")
        print(f"You are in/on/at {Desc[position]}.")
        print(" ")
        print(f"The thief is in/on/at {Desc[pos_com]}.")
        print(" ")

        # position directions and options

        if North[position] != 0:
            print(f"You can go North to {Desc[North[position]]}.")
            print(" ")
        else:
            print("You cannot go North.")
            print(" ")
        if South[position] != 0:
            print(f"You can go South to {Desc[South[position]]}.")
            print(" ")
        else:
            print("You cannot go South.")
            print(" ")
        if East[position] != 0:
            print(f"You can go East to {Desc[East[position]]}.")
            print(" ")
        else:
            print("You cannot go East.")
            print(" ")
        if West[position] != 0:
            print(f"You can go West to {Desc[West[position]]}.")
            print(" ")
            print(" ")
        else:
            print("You cannot go West.")
            print(" ")
            print(" ")
        if Down[position] != 0:
            print(f"You can go down to {Desc[Down[position]]}.")
            print(" ")
            print(" ")
        else:
            print("There is no (other) underground station here.")
            print(" ")
            
        if Up[position] != 0:
            print(f"You can go up to {Desc[Up[position]]}.")
            print(" ")
            print(" ")
        else:
            print("You are currently not in an underground station.")
            print(" ")
            print(" ")

        second_digit_com = 0

        # Explain where the thief is: 
        pos_com_str = str(pos_com)
        pos_com_list = list(pos_com_str)

        position_str = str(position)
        position_list = list(position_str)

        if pos_com < 10:
            pos_com_list = [0] + pos_com_list
        if position < 10:
            position_list = [0] + position_list


        first_digit_com = int(pos_com_list[0])
        second_digit_com = int(pos_com_list[1])

        first_digit_player = int(position_list[0])
        second_digit_player = int(position_list[1])

        if pos_com == position:
            print(" ")
            print(" ")
            print("Congratulations! You have successfully caught the thief!")
            print("Good job!")
            print(" ")
            exit()

        if first_digit_player < first_digit_com:
            print("The thief is more in the South.")
            print(" ")
        elif first_digit_player > first_digit_com:
            print("The thief is more in the North.")
            print(" ")        
        elif first_digit_player == first_digit_com:
            print("The thief is on the same height as you. You are close, try to go West or East.")
            print(" ")


        if second_digit_player > second_digit_com:
            print("The thief is more in the West.")
            print(" ")
            print(" ")
        elif second_digit_player < second_digit_com:
            print("The thief is more in the East.")
            print(" ")
            print(" ")
        elif second_digit_player == second_digit_com:
            print("The thief is on the same height as you. You are close, try to go North or South.")
            print(" ")
            print(" ")

        # random object

        if Objects[position] == 5:
            str(Objects[position])
            boat_or_train = randint(1,4)
            if boat_or_train == 1:
                Objects[position] = "boat-ticket"
            else:
                Objects[position] = "underground-ticket"
        elif Objects[position] != 5:
            str(Objects[position])
            Objects[position] = " "

       
        # inventary
        if inhand == " ":
            print("You have currently nothing in your hand.")
            print(" ")
            print(" ")
        else:
            print(f"You are currently in possession of a/an {inhand}.")
            print(" ")
            print(" ")

        # Objects

        if Objects[position] == ("underground-ticket" or Objects[position] == "boat-ticket") and inhand == " ":
            print(f"You can pick-up the: {Objects[position]}.")
            print(" ")
        elif Objects[position] == ("underground-ticket" or Objects[position] == "boat-ticket") and inhand != " ":
            print(f"You can switch the: {inhand} with a/an {Objects[position]}.")
            print(" ")


        # Choice after information
        command = input("select a command out of the list above: ")
        print(" ")

        ### Validity boat tickets


        if inhand == "Used_once_boat-ticket":
            if position == 29 and command != "S":
                inhand = inhand
            if position == 50 and command != "N":
                inhand = inhand
            if position == 50 and command == "N":
                inhand = " "
            elif position == 29 and command == "S":
                inhand = " "
        

        if inhand == "boat-ticket":
            if position == 29 and command != "S":
                inhand = inhand
            if position == 50 and command != "N":
                inhand = inhand        
            elif position == 29 and command == "S":
                inhand = "Used_once_boat-ticket"
            elif position == 50 and command == "N":
                inhand = "Used_once_boat-ticket"
        

        # atempt nr. 3 validity of tickets
            
        if inhand == "Used_once_underground-ticket":
            if position == 71 and (command == "N" or command == "S" or command == "E"):
                inhand = " "
            if position == 72 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = " "
            if position == 73 and (command == "N" or command == "W"):
                inhand = " "
            if position == 74 and (command == "N" or command == "E"):
                inhand = " "
            if position == 75 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = " "
            if position == 76 and (command == "N" or command == "E"):
                inhand = " "
            if position == 77 and (command == "N" or command == "E"):
                inhand = " "
            if position == 78 and (command == "N" or command == "W"):
                inhand = " "
            
        if inhand == "underground-ticket":
            if position == 71 and (command == "N" or command == "S" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif position == 72 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = "Used_once_underground-ticket" 
            elif position == 73 and (command == "N" or command == "W"):
                inhand = "Used_once_underground-ticket"
            elif position == 74 and (command == "N" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif position == 75 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = "Used_once_underground-ticket"
            elif position == 76 and (command == "N" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif position == 77 and (command == "N" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif position == 78 and (command == "N" or command == "W"):
                inhand = "Used_once_underground-ticket"
            
            

        # What happens with selected command:

        if command == "N" and North[position] != 0:
            position = North[position]

        elif command == "S" and South[position] != 0:
            position = South[position]

        elif command == "W" and West[position] != 0:
            position = West[position]

        elif command == "E" and East[position] != 0:
            position = East[position]

        elif command == "U" and Up[position] != 0:
            position = Up[position]

        elif command == "D" and Down[position] != 0:
            position = Down[position]

        elif command == "X" and inhand != " " and Objects[position] == " ":
            Objects[position] = inhand
            inhand = " "

        elif command == "P" and inhand == " " and Objects[position] != " ":
            inhand = Objects[position]
            Objects[position] = " "

        elif command == "K" and inhand != " " and Objects[position] != " ":
            transition = inhand
            inhand = Objects[position]
            Objects[position] = transition

        elif command == "Q":
            print(" ")
            print("Good bye! I hope you had fun playing this game!")
            print(" ")
            exit()
        
        else:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(f"This command is not possible in/on/at {Desc[position]}. Please try again")



        

        # fix problem with free rides underground and boat

        if position == 71 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 1
        elif position == 72 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 6
        elif position == 73 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 17
        elif position == 74 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 21
        elif position == 75 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 23
        elif position == 76 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 52
        elif position == 77 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 66
        elif position == 78 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 79
        elif position == 50 and inhand != "boat-ticket" and inhand != "Used_once_boat-ticket":
            print(" ")
            print("You cannot take the boat without a valid ticket.")
            print("Please try again.")
            print(" ")
        elif position == 29 and inhand != "boat-ticket" and inhand != "Used_once_boat-ticket":
            print(" ")
            print("You cannot take the boat without a valid ticket.")
            print("Please try again.")
            print(" ")
            
        
        # thief position(pos_com)
        moves += 1
        
        # emptying command for while loop
        command = " "


        if moves == 3:
            pos_com_random = randint(1,5)
            if pos_com_random == 1 and West[pos_com] != 0:
                pos_com -= 1
                moves = 0
            elif pos_com_random == 2 and pos_com == 50:
                pos_com = 29
                moves = 0
            elif pos_com_random == 2 and North[pos_com] != 0:
                pos_com -= 10
                moves = 0
            elif pos_com_random == 3 and East[pos_com] != 0:
                pos_com += 1
                moves = 0
            elif pos_com_random == 3 and pos_com == 29:
                pos_com = 50
                moves = 0
            elif pos_com_random == 4 and South[pos_com] != 0:
                pos_com += 10
                moves = 0

            elif pos_com_random == 1 and West[pos_com] == 0:
                break
            elif pos_com_random == 2 and North[pos_com] == 0:
                break
            elif pos_com_random == 3 and East[pos_com] == 0:
                break
            elif pos_com_random == 4 and South[pos_com] == 0:
                break
