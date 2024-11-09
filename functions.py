"""The Module holds function definitions they are used in the game.

By separating the functions into this module, the main game file remains cleaner 
and easier to read. The functions provide essential gameplay features such as 
welcoming the player or displaying instructions.

Functions:
    greeting: Prints a welcome message and gives a brief game description.
    command_help: Lists all available commands for the player to navigate through the game.
"""
__all__ = ["greeting", "command_help", "print_moving_opportunitys", "print_relative_positions",
           "check_winning"]
__path__ = "functions.py"
__version__ = "1.0.0"

from color import Color
from places import Location

def greeting() -> None:
    """Prints a welcome message to the player and provides a brief 
    description of how to play the game.

    This function introduces the player to the game world, outlining the role of the detective and 
    the objective of finding the criminal.

    Example:
        >>> greeting()
        Prints a welcome message and a game description.
    """
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

def command_help() -> None:
    """Prints a list of all available commands that the player can use to navigate through the game.

    This function helps the player understand the controls and how to interact with the game world. 
    It outlines the possible directions, actions with items, and other gameplay functionalities.

    Example:
        >>> command_help()
        Prints a list of commands such as movement and interaction options.
    """
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
    print("[H] to show this help again")
    print(" ")

def print_moving_opportunitys(location : Location) -> None:
    """Displays the available movement options from the current location.

    This function prints the available directions the player can move from the given 
    location. For each possible direction (north, south, east, west, up, and down), 
    it checks if there is an accessible location in that direction. If movement is possible, 
    it prints the direction and the target location; otherwise, it notifies the player that 
    movement in that direction is not possible.

    Args:
        location (Location): The object of the current location of the player, containing references 
        to adjacent locations in each direction.
    """
    if location.north:
        print(f"You can go North to {location.north}.")
    else:
        print("You cannot go North.")
    print()

    if location.south:
        print(f"You can go South to {location.south}.")
    else:
        print("You cannot go South.")
    print()

    if location.east:
        print(f"You can go East to {location.east}.")
    else:
        print("You cannot go East.")
    print()

    if location.west:
        print(f"You can go West to {location.west}.")
    else:
        print("You cannot go West.")
    print(Color.PURPLE)

    if location.down:
        print(f"You can go down to {location.down}.")
    else:
        print("There is no (other) underground station here.")
    print()

    if location.up:
        print(f"You can go up to {location.up}.")
    else:
        print("You are currently not in an underground station.")
    print(Color.YELLOW)

def print_relative_positions(player_position: int, thief_position: int) -> None:
    """Displays the relative position of the thief in relation to the player's current position.

    This function calculates and prints the directional relationship between the player's 
    and the thief's positions on a grid. By comparing the coordinates (row and column) of 
    the two positions, it determines whether the thief is more north, south, east, or west 
    of the player. If the thief is aligned with the player on either axis, the function 
    notifies the player that they are close to the target and suggests the next move.

    Args:
        player_position (int): The current position of the player as a grid index.
        thief_position (int): The current position of the thief as a grid index.
    """

    def coordinate_unpacking(place_value:int) -> tuple[int, int]:
        # Converting the Value of that place in a tuple with two items
        first_digit: int
        second_digit: int
        # A Value < 10 only has one item.
        # So it can not be converted because a n integer has no unessesery zerros
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

def check_winning(player_position: int, thief_position: int) -> None:
    """Checks if the player has won the game by catching the thief.

    This function compares the player's and the thief's positions. If they match, it 
    prints a congratulatory message in red to indicate the player's success in catching 
    the thief and then exits the program. Otherwise, the game continues.

    Args:
        player_position (int): The current position of the player as a grid index.
        thief_position (int): The current position of the thief as a grid index.
    """
    if player_position == thief_position:
        print(Color.RED)
        print()
        print("Congratulations! You have successfully caught the thief!")
        print("Good job!")
        print(Color.RESET)
        exit()
