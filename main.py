"""This Python Program creates an immercive adventure 
located in London. The players goal is to find a fugitive
criminal while having the possibility to take the underground
and the boat to catch the criminal with the help of so called
"passes" the player needs to find. After two travels, the pass
is not valid anymore and the player needs to switch it with a new one.

Variables:
    player_position (int): The current position of the player.
    thief_position (int): The current position of the thief.
    inhand (Ticket): The ticket the player is holding.
    command (str): The input of the player.
    moves (int): Counts the number of moves until the thief moves.

Functions:
    print_positions: Prints the current position of the player and the thief.
    print_hand_status: Prints the current ticket the player is holding.
    check_winning: Checks if the player has won the game.
    print_moving_opportunity: Prints if the player has the possibility to move.
    process_input: Processes the input of the player.
    print_relative_positions: Prints the relative positions of the player and the thief.
    print_object_status: Prints the status of the ticket.
    move_player: Moves the player in the wished direction.
    move_thief: Moves the thief randomly one position.
    is_undergraund_possible: Checks if the player has the possibility to move by underground.
    is_boat_possible: Checks if the player has the possibility to move by boat.
    main: The main function of the program.
"""

__title__ = "Adventure Game"
__author__ = "Lena Weinstock, Paul Jonas Dohle"
__version__ = "1.8.1"
__status__ = "Production"
__date__ = "9.11.2024"
__all__ = ["main"]
__path__ = "main.py"
__coure__ = "Computer Science ICS 3u"
__school__ = "Glebe Collegiate Institute, Ottawa; Europagymnaium Warstein"
__teacher__ = "Mr Giassante"


from random import randint
from places import locations, FORBIDDEN_PLAYER_STARTS, FORBIDDEN_THIEF_STARTS
from places import BOAT_DOCKS, UNDERGROUND_STATIONS
from functions import greeting, command_help, print_moving_opportunitys
from ticket import Ticket
from color import Color


# setting beginning variables of player and computer

# Selecting a random point to start with excluding those, who can only reached by underground
player_position: int = 0  # position at beginning
while player_position in FORBIDDEN_PLAYER_STARTS:
    player_position = randint(1, 80)

FORBIDDEN_THIEF_STARTS.append(player_position)
thief_position: int = 0

while thief_position in FORBIDDEN_THIEF_STARTS:
    thief_position = randint(1, 80)
    while (thief_position + 2 == player_position or thief_position - 2 == player_position):
        thief_position = randint(1, 80)
    while (thief_position + 20 == player_position or thief_position - 20 == player_position):
        thief_position = randint(1, 80)

# defining some variables for later
command: str = " "
inhand: Ticket = Ticket(0)
transition: int  # Only used once TODO maybe there's an alternative
moves: int = 0
new_move: bool = True  # Decides if stats are shown

def check_winning() -> None:
    if thief_position == player_position:
        print(Color.RED)
        print()
        print("Congratulations! You have successfully caught the thief!")
        print("Good job!")
        print(Color.RESET)
        exit()

def print_positions() -> None:
    print(Color.GREEN)
    print(f"You are in/on/at {locations[player_position]}.")
    print()
    print(f"The thief is in/on/at {locations[thief_position]}.")
    print(Color.CYAN)

def print_hand_status() -> None:
    if not inhand.ticket_type:
        print("You have currently nothing in your hand.")
    else:
        print(f"You are currently in possession of a/an {inhand}.")
    print()
    print()

def print_object_status() -> None:
    if (locations[player_position].ticket.ticket_type and not inhand.ticket_type):
        print(f"You can pick-up the: {locations[player_position].ticket}.")
    elif (locations[player_position].ticket.ticket_type and inhand.ticket_type):
        print(f"You can switch the: {inhand} with a/an {locations[player_position].ticket}.")
    print(Color.RESET)

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
    print(Color.BLUE)

def move_player(direction: str) -> None:
    global locations, player_position

    match direction:
        case "NORTH":
            if not locations[player_position].north:
                print(f"At {locations[player_position]} you can not go north.")
                return
            if not is_undergraund_possible(direction):
                return
            if not is_booat_possible(direction):
                return
            player_position = locations[player_position].north

        case "EAST":
            if not locations[player_position].east:
                print(f"At {locations[player_position]} you can not go east.")
                return
            if not is_undergraund_possible(direction):
                return
            player_position = locations[player_position].east

        case "SOUTH":
            if not locations[player_position].south:
                print(f"At {locations[player_position]} you can not go south.")
                return
            if not is_undergraund_possible(direction):
                return
            if not is_booat_possible(direction):
                return
            player_position = locations[player_position].south

        case "WEST":
            if not locations[player_position].west:
                print(f"At {locations[player_position]} you can not go west.")
                return
            if not is_undergraund_possible(direction):
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

def is_undergraund_possible(direction:str) -> bool:
    if player_position not in UNDERGROUND_STATIONS:
        return True
    if direction == "UP":
        return True
    if inhand.vehicle == "UNDERGROUND":
        # This partis only executed if the player is traveling with the underground
        inhand.use_ticket()
        return True
    # This partis only executed if the player tyest to take the underground without a valid ticket
    print("You can not take the underground without a valid ticket.")
    return False

def is_booat_possible(direction:str) -> bool:
    if player_position not in BOAT_DOCKS:
        return True
    if not (player_position == 29 and direction == "SOUTH" or player_position == 50 and direction == "NORTH"):
        return True
    if inhand.vehicle == "BOAT":
        # This partis only executed if the player is traveling with the boat
        inhand.use_ticket()
        return True
    # This partis only executed if the player tyest to take the boat without a valid ticket
    print("You can not take the boat without a valid ticket.")
    return False

def move_thief() -> None:
    global thief_position
    match randint(1, 5):
        case 1:
            if locations[thief_position].west:
                thief_position -= 1
        case 2:
            if thief_position == 50:
                thief_position = 29
            elif locations[thief_position].north:
                thief_position -= 10
        case 3:
            if thief_position == 29:
                thief_position = 50
            elif locations[thief_position].east:
                thief_position += 1
        case 4:
            if locations[thief_position].south:
                thief_position += 10
        case _:
            pass


def main() -> None:
    """Contains the adventure game and controls the main game loop.
    This function is the entry point of the game. After greeting the player and explaning the basics
    the programm continues with the main game loop.
    1. Displays the player's current position, available movement options, and ticket status.
    2. Prompts the player for input and processes the command via `process_input()`.
    3. Checks if the player has won by catching the thief using `check_winning()`.
    4. Tracks the thief's movement every three player turns.
    
    The loop continues until the player either catches the thief or quits the game.

    Example:
    >>> main()
    """
    global new_move, command, moves
    greeting()
    command_help()

    while True:
        # Show status
        if new_move:
            print_positions()
            print_moving_opportunitys(locations[player_position])
            print_relative_positions()
            print_hand_status()
            new_move = False
        print_object_status()

        # Asking user to input a command
        command = input("select a command out of the list above: ").upper()
        print()

        process_input()
        check_winning()

        # Every three player_moves the thief moves one location
        if new_move:
            moves += 1
        if moves == 3:
            move_thief()
            moves = 0


if __name__ == "__main__":
    main()
