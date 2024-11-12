"""This module handles the movement functionality for the player and thief characters in the game,
providing directional movement, underground and boat travel validation, and random movement
for the thief. It also provides the `Command` Flag class to standardize movement directions
(NORTH, EAST, SOUTH, WEST, UP, and DOWN), as well as basic Item commands,
 ensuring consistent orientation throughout the game.

    Classes:
        Direction: Flag class defining the six primary directions: NORTH, EAST, SOUTH,
            WEST, UP, DOWN, Pick, Drop, Swap, Help, Quit. Provides a consistent set 
            of directions for charactermovement and world interaction,
            enhancing readability and usability within the module.
    
    Functions:
        move_player: Moves the player in the wished direction.
        move_thief: Moves the thief randomly one position.
        is_undergraund_possible: Checks if the player has the possibility to move by underground.
        is_boat_possible: Checks if the player has the possibility to move by boat.
"""

__all__ = ["move_player", "is_underground_possible", "is_boat_possible", "move_thief", "Command"]
__path__ = "movement.py"
__version__ = "1.2.0"

from enum import Flag, auto
from random import randint
from places import BOAT_DOCKS, UNDERGROUND_STATIONS, Location
from ticket import Ticket


class Command(Flag):
    """The `Direction` Flag class defines a set of constants representing the six main directions.
    These constants can be used to represent movement or orientation within
    a three-dimensional space, ensuring consistency and readability.

    Atributes:
        NORTH (str): Represents the northward direction.
        EAST (str): Represents the eastward direction.
        SOUTH (str): Represents the southward direction.
        WEST (str): Represents the westward direction.
        UP (str): Represents the upward direction.
        DOWN (str): Represents the downward direction.
        PICK (str): Represents the pickup command.
        DROP (str): Represents the drop command.
        SWAP (str): Represents the swap command.
        HELP (str): Represents the help command.
        QUIT (str): Represents the quit command.
    
    Example:
        >>> Command.NORTH
        <Direction.NORTH: 1>
        >>> Command.NORTH.value
        1
    """

    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()
    UP = auto()
    DOWN = auto()

    MOVEMENT = NORTH | EAST | SOUTH | WEST | UP | DOWN

    PICK = auto()
    DROP = auto()
    SWAP = auto()
    HELP = auto()
    QUIT = auto()


def move_player(player_position: Location, direction: Command, inhand: Ticket) -> int:
    """Moves the player in the specified direction if movement is possible.

    Based on the given direction, the function checks whether the player can
    move from the current location to the target location in that direction.
    It returns the new position if movement is successful, or retains the
    current position if movement is blocked by an obstacle or invalid ticket.

    Args:
        player_position (Location): The current position of the player as a grid index.
        direction (command): The direction to move in, one of 'NORTH', 'EAST', 'SOUTH',
            'WEST', 'UP', 'DOWN'.
        inhand (Ticket): The ticket currently held by the player.


    Raises:
        ValueError: If an unknown direction is passed as an argument.

    Returns:
        int: The coordinate of the new position if movement is allowed, or the 
        current position coordinate if movement is not possible.
    
    Example:
        >>> player_position = Location("Paddington Station", 1, west=1, up=2, down=3)
        >>> inhand = Ticket(0)
        >>> move_player(player_position, "NORTH", inhand)
        At Paddington Station you can not go north.
        New position: 1
    """
    match direction:
        case Command.NORTH:
            if not player_position.north:
                print(f"At {player_position} you can not go north.")
                return player_position.coordinate
            if not (is_underground_possible(player_position.coordinate, inhand) and
            is_boat_possible(direction, player_position.coordinate, inhand)):
                return player_position.coordinate
            return player_position.north

        case Command.EAST:
            if not player_position.east:
                print(f"At {player_position} you can not go east.")
                return player_position.coordinate
            if not is_underground_possible(player_position.coordinate, inhand):
                return player_position.coordinate
            return player_position.east

        case Command.SOUTH:
            if not player_position.south:
                print(f"At {player_position} you can not go south.")
                return player_position.coordinate
            if not (is_underground_possible(player_position.coordinate, inhand) and
            is_boat_possible(direction, player_position.coordinate, inhand)):
                return player_position.coordinate
            return player_position.south

        case Command.WEST:
            if not player_position.west:
                print(f"At {player_position} you can not go west.")
                return player_position.coordinate
            if not is_underground_possible(player_position.coordinate, inhand):
                return player_position.coordinate
            return player_position.west

        case Command.UP:
            if not player_position.up:
                print(f"At {player_position} you can not go up.")
                return player_position.coordinate
            return player_position.up

        case Command.DOWN:
            if not player_position.down:
                print(f"At {player_position} you can not go down.")
                return player_position.coordinate
            return player_position.down

        case _:
            raise ValueError("Input unknown movement direction. Please reoprt this to the author.")

def is_underground_possible(player_position: int, inhand: Ticket) -> bool:
    """Checks if underground travel is possible for the player based on their
    current position, chosen direction, and ticket status.

    This function determines whether the player can take the underground at their current location, 
    depending on the presence of a valid underground ticket and whether 
    they are at an underground station.If the player is attempting to travel 
    without a valid ticket, a message is displayed, and the function returns False.

    Args:
        player_position (int): The player's current position, which is checked
        against known underground station locations.
        inhand (Ticket): The ticket object representing the player's ticket,
        including type and remaining uses.

    Returns:
        bool: True if underground travel is possible, False otherwise
    
    Example:
        >>> inhand = Ticket(1)
        >>> is_undergraund_possible("NORTH", 71, inhand)
        True
    """
    if player_position not in UNDERGROUND_STATIONS:
        return True
    if inhand.vehicle == "UNDERGROUND":
        # This partis only executed if the player is traveling with the underground
        inhand.use_ticket()
        return True
    # This partis only executed if the player tyest to take the underground without a valid ticket
    print("You can not take the underground without a valid ticket.")
    return False

def is_boat_possible(direction:Command, player_position: int, inhand: Ticket) -> bool:
    """Checks if boat travel is possible for the player based on their
    current position, chosen direction, and ticket status.

    This function determines whether the player can take the boat at their current location, 
    depending on the presence of a valid boat ticket and whether 
    they are at an boat station.If the player is attempting to travel 
    without a valid ticket, a message is displayed, and the function returns False.

    Args:
        direction (command): The direction of travel.
        player_position (int): The player's current position, which is checked
        against known boat station locations.
        inhand (Ticket): The ticket object representing the player's ticket,
        including type and remaining uses.

    Returns:
        bool: True if boat travel is possible, False otherwise
    
    Example:
        >>> inhand = Ticket(1)
        >>> is_booat_possible("NORTH", 50, inhand)
        False
    """
    if player_position not in BOAT_DOCKS:
        return True
    if not ((player_position == 29 and direction == Command.SOUTH) or
            (player_position == 50 and direction == Command.NORTH)):
        return True
    if inhand.vehicle == "BOAT":
        # This partis only executed if the player is traveling with the boat
        inhand.use_ticket()
        return True
    # This partis only executed if the player tyest to take the boat without a valid ticket
    print("You can not take the boat without a valid ticket.")
    return False

def move_thief(thief_position: Location) -> int:
    """Moves the thief randomly in one of four directions if possible or let him use the boat.

    Args:
        thief_position (Location): The thief's current location.

    Returns:
        int: The coordinate of the new position of the thief.
    
    Example:
        >>> thief_position = Location(50)
        >>> thief_position.coordinate = move_thief(thief_position)
        >>> 29
    """

    match randint(1, 5):
        case 1:
            if thief_position.west:
                thief_position.coordinate = thief_position.west
        case 2:
            if thief_position.coordinate == 50:
                thief_position.coordinate = 29
            elif thief_position.north:
                thief_position.coordinate = thief_position.north
        case 3:
            if thief_position.coordinate == 29:
                thief_position.coordinate = 50
            elif thief_position.east:
                thief_position.coordinate = thief_position.east
        case 4:
            if thief_position.south:
                thief_position.coordinate = thief_position.south
        case _:
            pass

    return thief_position.coordinate
