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
    command (Command): The player's input command.
    moves (int): Counts the number of moves until the thief moves.

Functions:
    main: The main function that initializes and runs the game loop.
"""

__version__ = "2.0.1"
__all__ = ["main"]
__path__ = "main.py"


from random import randint
from movement import Command, move_thief
from places import locations, FORBIDDEN_PLAYER_STARTS, FORBIDDEN_THIEF_STARTS
from functions import greeting, command_help, print_moving_opportunitys, print_relative_positions
from functions import check_winning, print_hand_status, print_positions, print_object_status
from functions import process_input, get_command
from ticket import Ticket


def main() -> None:
    """Contains the adventure game and controls the main game loop.
    This function is the entry point of the game. After greeting the player and explaning the basics
    the programm continues with the main game loop.

    1. Sets the initial positions of the player and the thief and declares the game variables.
    2. Displays the player's current position, available movement options, and ticket status.
    3. Prompts the player for input and processes the command via `process_input()`.
    4. Checks if the player has won by catching the thief using `check_winning()`.
    5. Tracks the thief's movement every three player turns.
    
    The loop continues until the player either catches the thief or quits the game.

    Example:
    >>> main()
    """

    command: Command
    inhand: Ticket = Ticket(0)
    moves: int = 0
    new_move: bool = True  # Decides if stats are shown
    thief_position: int = 0
    player_position: int = 0

    # setting beginning variables of player and computer
    # Selecting a random point to start with excluding those, who can only reached by underground
    while player_position in FORBIDDEN_PLAYER_STARTS:
        player_position = randint(1, 80)

    FORBIDDEN_THIEF_STARTS.append(player_position)

    while thief_position in FORBIDDEN_THIEF_STARTS:
        thief_position = randint(1, 80)
        while (thief_position + 2 == player_position or thief_position - 2 == player_position):
            thief_position = randint(1, 80)
        while (thief_position + 20 == player_position or thief_position - 20 == player_position):
            thief_position = randint(1, 80)


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
        command = get_command()
        print()

        player_position, locations[player_position].ticket, inhand, new_move = process_input(
            command, inhand, locations[player_position])
        check_winning(player_position, thief_position)

        # Every three player_moves the thief moves one location
        if new_move:
            moves += 1
        if moves == 3:
            thief_position = move_thief(locations[thief_position])
            moves = 0


if __name__ == "__main__":
    main()
