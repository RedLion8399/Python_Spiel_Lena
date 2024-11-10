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
__version__ = "1.8.3"
__status__ = "Production"
__date__ = "9.11.2024"
__all__ = ["main"]
__path__ = "main.py"
__coure__ = "Computer Science ICS 3u"
__school__ = "Glebe Collegiate Institute, Ottawa; Europagymnaium Warstein"
__teacher__ = "Mr Giassante"


from random import randint
from places import locations, FORBIDDEN_PLAYER_STARTS, FORBIDDEN_THIEF_STARTS
from functions import greeting, command_help, print_moving_opportunitys, print_relative_positions
from functions import check_winning, print_hand_status, print_positions, print_object_status
from movement import move_player
from ticket import Ticket


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
command: str = " " # TODO Design an own dada Type
inhand: Ticket = Ticket(0)
transition: int  # Only used once # TODO maybe there's an alternative
moves: int = 0
new_move: bool = True  # Decides if stats are shown

def process_input() -> None:
    global command, inhand, transition, new_move, player_position

    match command:
        case "N":
            player_position = move_player(locations[player_position], "NORTH", inhand)

        case "E":
            player_position = move_player(locations[player_position],"EAST", inhand)

        case "S":
            player_position = move_player(locations[player_position],"SOUTH", inhand)

        case "W":
            player_position = move_player(locations[player_position],"WEST", inhand)

        case "U":
            player_position = move_player(locations[player_position],"UP", inhand)

        case "D":
            player_position = move_player(locations[player_position],"DOWN", inhand)

        case "X":
            if not inhand.ticket_type:
                print("Yo have no item in your hand.")
                return
            if locations[player_position].ticket.ticket_type:
                print("There is already a ticket on the ground.")
                return
            locations[player_position].ticket, inhand = inhand, locations[player_position].ticket
            inhand.ticket_type = 0

        case "P":
            if inhand.ticket_type:
                print("Yo have already an item in your hand.")
                return
            if not locations[player_position].ticket.ticket_type:
                print("There is no ticket on the ground.")
                return
            locations[player_position].ticket, inhand = inhand, locations[player_position].ticket

        case "K":
            if not locations[player_position].ticket.ticket_type:
                print("There is no ticket on the ground.")
                return
            if not inhand.ticket_type:
                print("Yo have no item in your hand.")
                return
            locations[player_position].ticket, inhand = inhand, locations[player_position].ticket

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
            print(f"""This command is not possible in/on/at {locations[player_position]}.
                  Please try again""")
            return

    new_move = True

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
            print_positions(player_position, thief_position)
            print_moving_opportunitys(locations[player_position])
            print_relative_positions(player_position, thief_position)
            print_hand_status(inhand)
            new_move = False
        print_object_status(locations[player_position], inhand)

        # Asking user to input a command
        command = input("select a command out of the list above: ").upper()
        print()

        process_input()
        check_winning(player_position, thief_position)

        # Every three player_moves the thief moves one location
        if new_move:
            moves += 1
        if moves == 3:
            move_thief()
            moves = 0


if __name__ == "__main__":
    main()
