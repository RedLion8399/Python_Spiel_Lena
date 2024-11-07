# Title: Adventure Game
# Version: 1.6
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
from places import locations, forbidden_player_starts, forbidden_thief_starts, boat_docks
from functions import greeting, command_help
from ticket import Ticket


# setting beginning variables of player and computer

# Selecting a random point to start with excluding those, who can only reached by underground
player_position: int = 0  # position at beginning
while player_position in forbidden_player_starts:
    player_position = randint(1, 80)

forbidden_thief_starts.append(player_position)
thief_position: int = 0

while thief_position in forbidden_thief_starts:
    thief_position = randint(1, 80)
    while (thief_position + 2 == player_position or thief_position - 2 == player_position):
        thief_position = randint(1, 80)
    while (thief_position + 20 == player_position or thief_position - 20 == player_position):
        thief_position = randint(1, 80)

# defining some variables for later
running: bool = True  # Variable is never changed TODO deleting the variable or giving a sence to it
command: str = " "
inhand: Ticket = Ticket(0)
transition: int  # Only used once TODO maybe there's an alternative
moves: int = 0
new_move: bool = True  # Decides if stats are shown

# Shows where the player can go from his current location
def print_moving_opportunitys() -> None:
    if locations[player_position].north:
        print(f"You can go North to {locations[locations[player_position].north]}.")
    else:
        print("You cannot go North.")
    print()

    if locations[player_position].south:
        print(f"You can go South to {locations[locations[player_position].south]}.")
    else:
        print("You cannot go South.")
    print()

    if locations[player_position].east:
        print(f"You can go East to {locations[locations[player_position].east]}.")
    else:
        print("You cannot go East.")
    print()

    if locations[player_position].west:
        print(f"You can go West to {locations[locations[player_position].west]}.")
    else:
        print("You cannot go West.")
    print()

    if locations[player_position].down:
        print(f"You can go down to {locations[locations[player_position].down]}.")
    else:
        print("There is no (other) underground station here.")
    print()

    if locations[player_position].up:
        print(f"You can go up to {locations[locations[player_position].up]}.")
    else:
        print("You are currently not in an underground station.")
    print()

def free_ticket_use_fix() -> None:
    global player_position, inhand
    print()
    if (player_position == 71 and inhand.ticket_type not in [1, 3]):
        print("You cannot take the underground without a valid ticket.")
        print("Please try again.")
        player_position = 1
    elif (player_position == 72 and inhand.ticket_type not in [1, 3]):
        print("You cannot take the underground without a valid ticket.")
        print("Please try again.")
        player_position = 6
    elif (player_position == 73 and inhand.ticket_type not in [1, 3]):
        print("You cannot take the underground without a valid ticket.")
        print("Please try again.")
        player_position = 17
    elif (player_position == 74 and inhand.ticket_type not in [1, 3]):
        print("You cannot take the underground without a valid ticket.")
        print("Please try again.")
        player_position = 21
    elif (player_position == 75 and inhand.ticket_type not in [1, 3]):
        print("You cannot take the underground without a valid ticket.")
        print("Please try again.")
        player_position = 23
    elif (player_position == 76 and inhand.ticket_type not in [1, 3]):
        print("You cannot take the underground without a valid ticket.")
        print("Please try again.")
        player_position = 52
    elif (player_position == 77 and inhand.ticket_type not in [1, 3]):
        print("You cannot take the underground without a valid ticket.")
        print("Please try again.")
        player_position = 66
    elif (player_position == 78 and inhand.ticket_type not in [1, 3]):
        print("You cannot take the underground without a valid ticket.")
        print("Please try again.")
        player_position = 79
    elif (player_position in boat_docks and inhand.ticket_type not in [2, 4]):
        print("You cannot take the boat without a valid ticket.")
        print("Please try again.")
    print()

def check_winning() -> None:
    if thief_position == player_position:
        print()
        print()
        print("Congratulations! You have successfully caught the thief!")
        print("Good job!")
        print()
        exit()

def print_positions() -> None:
    print()
    print(f"You are in/on/at {locations[player_position]}.")
    print()
    print(f"The thief is in/on/at {locations[thief_position]}.")
    print()

def print_relative_positions() -> None:
    def coordinate_unpacking(place_value:int) -> tuple[int, int]:
        # Converting the Value of that place in a tuple with two items
        first_digit: int
        second_digit: int
        # A Value < 10 only has one item. So it can not be converted because a n integer has no unessesery zerros
        if place_value > 10:
            place_string: str = str(place_value)
            first_digit = int(place_string[0])
            second_digit = int(place_string[1])
        else:
            first_digit = 0
            second_digit = place_value
        return (first_digit, second_digit)
    
    player_coordinate: tuple[int, int] = coordinate_unpacking(player_position)
    thief_coordinate: tuple[int, int] = coordinate_unpacking(thief_position)

    # Comparing the singular coordinates to calucalte the relative direction
    if player_coordinate[0] < thief_coordinate[0]:
        print("The thief is more in the South.")
    elif player_coordinate[0] > thief_coordinate[0]:
        print("The thief is more in the North.")
    elif player_coordinate[0] == thief_coordinate[0]:
        print("The thief is on the same height as you. You are close, try to go West or East.")
    print()

    if player_coordinate[1] > thief_coordinate[1]:
        print("The thief is more in the West.")
    elif player_coordinate[1] < thief_coordinate[1]:
        print("The thief is more in the East.")
    elif player_coordinate[1] == thief_coordinate[1]:
        print("The thief is on the same height as you. You are close, try to go North or South.")
    print()
    print()

def move_player(direction: str) -> None:
    global locations, player_position

    match direction:
        case "NORTH":
            if not locations[player_position].north:
                print(f"At {locations[player_position]} you can not go north.")
                return
            player_position = locations[player_position].north

        case "EAST":
            if not locations[player_position].east:
                print(f"At {locations[player_position]} you can not go east.")
                return
            player_position = locations[player_position].east

        case "SOUTH":
            if not locations[player_position].south:
                print(f"At {locations[player_position]} you can not go south.")
                return
            player_position = locations[player_position].south

        case "WEST":
            if not locations[player_position].west:
                print(f"At {locations[player_position]} you can not go west.")
                return
            player_position = locations[player_position].west

        case "UP":
            if not locations[player_position].up:
                print(f"At {locations[player_position]} you can not go up.")
                return
            player_position = locations[player_position].up

        case "DOWN":
            if not locations[player_position].down:
                print(f"At {locations[player_position]} you can not go down.")
                return
            player_position = locations[player_position].down

        case _:
            raise ValueError("Input unknown movement direction. Please reoprt this to the author.")

def process_input() -> None:
    global command, inhand, transition, new_move

    match command:
        case "N":
            move_player("NORTH")

        case "E":
            move_player("EAST")

        case "S":
            move_player("SOUTH")

        case "W":
            move_player("WEST")

        case "U":
            move_player("UP")

        case "D":
            move_player("DOWN")

        case "X":
            if not inhand.ticket_type:
                print("Yo have no item in your hand.")
                return
            if locations[player_position].ticket.ticket_type:
                print("There is already a ticket on the ground.")
                return
            locations[player_position].ticket.ticket_type = inhand.ticket_type
            inhand.ticket_type = 0
        
        case "P":
            if inhand.ticket_type:
                print("Yo have already an item in your hand.")
                return
            if not locations[player_position].ticket.ticket_type:
                print("There is no ticket on the ground.")
                return
            inhand.ticket_type = locations[player_position].ticket.ticket_type
            locations[player_position].ticket.ticket_type = 0

        case "K":
            if not locations[player_position].ticket.ticket_type:
                print("There is no ticket on the ground.")
                return
            if not inhand.ticket_type:
                print("Yo have no item in your hand.")
                return
            transition = inhand.ticket_type
            inhand.ticket_type = locations[player_position].ticket.ticket_type
            locations[player_position].ticket.ticket_type = transition

        case "Q":
            print()
            print("Good bye! I hope you had fun playing this game!")
            print()
            exit()
        
        case "H":
            command_help()
            return

        case _:
            print()
            print()
            print()
            print()
            print(f"This command is not possible in/on/at {locations[player_position]}. Please try again")
            return
        
    new_move = True

def drive() -> None:
    pass

# The main programm starts here.
# TODO Wrap this programm into a main function to set a main entrence point.
greeting()
command_help()

while running:
    # Show status
    if new_move:
        print_positions()
        print_moving_opportunitys()
        print_relative_positions()

        # inventary
        if not inhand.ticket_type:
            print("You have currently nothing in your hand.")
        else:
            print(f"You are currently in possession of a/an {inhand}.")
        print()
        print()
        new_move = False

    # Objects
    if (locations[player_position].ticket.ticket_type and not inhand.ticket_type):
        print(f"You can pick-up the: {locations[player_position].ticket.ticket_type}.")
    elif (locations[player_position].ticket.ticket_type and inhand.ticket_type):
        print(f"You can switch the: {inhand} with a/an {locations[player_position].ticket.ticket_type}.")
    print()


    # Asking user to input a command
    command = input("select a command out of the list above: ").upper()
    print()

    # Validity boat tickets

    if inhand.vehicle == "BOAT":
        if player_position == 50 and command == "N":
            inhand.use_ticket()
        elif player_position == 29 and command == "S":
            inhand.use_ticket()


    # Validity underground tickets

    if inhand.vehicle == "UNDERGROUND":
        if player_position == 71 and (command == "N" or command == "S" or command == "E"):
            inhand.use_ticket()
        if player_position == 72 and (command == "N" or command == "S" or command == "E" or command == "W"):
            inhand.use_ticket()
        if player_position == 73 and (command == "N" or command == "W"):
            inhand.use_ticket()
        if player_position == 74 and (command == "N" or command == "E"):
            inhand.use_ticket()
        if player_position == 75 and (command == "N" or command == "S" or command == "E" or command == "W"):
            inhand.use_ticket()
        if player_position == 76 and (command == "N" or command == "E"):
            inhand.use_ticket()
        if player_position == 77 and (command == "N" or command == "E"):
            inhand.use_ticket()
        if player_position == 78 and (command == "N" or command == "W"):
            inhand.use_ticket()


    process_input()
    free_ticket_use_fix()
    check_winning()

    # thief position(pos_com)
    moves += 1

    if moves == 3:
        pos_com_random = randint(1, 5)
        if pos_com_random == 1 and locations[thief_position].west != 0:
            thief_position -= 1
            moves = 0
        elif pos_com_random == 2 and thief_position == 50:
            thief_position = 29
            moves = 0
        elif pos_com_random == 2 and locations[thief_position].north != 0:
            thief_position -= 10
            moves = 0
        elif pos_com_random == 3 and locations[thief_position].east != 0:
            thief_position += 1
            moves = 0
        elif pos_com_random == 3 and thief_position == 29:
            thief_position = 50
            moves = 0
        elif pos_com_random == 4 and locations[thief_position].south != 0:
            thief_position += 10
            moves = 0

        elif pos_com_random == 1 and locations[thief_position].west == 0:
            break
        elif pos_com_random == 2 and locations[thief_position].north == 0:
            break
        elif pos_com_random == 3 and locations[thief_position].east == 0:
            break
        elif pos_com_random == 4 and locations[thief_position].south == 0:
            break
