"""_summary_
"""

__all__ = ["move_player"]
__path__ = "movement.py"
__version__ = "1.0.0"

from places import BOAT_DOCKS, UNDERGROUND_STATIONS, Location
from ticket import Ticket
from icecream import ic


def move_player(player_position: Location, direction: str, inhand: Ticket) -> int:
    """Moves the player in the specified direction if movement is possible.

    Based on the given direction, the function checks whether the player can
    move from the current location to the target location in that direction.
    It returns the new position if movement is successful, or retains the
    current position if movement is blocked by an obstacle or invalid ticket.

    Args:
        player_position (Location): The current position of the player as a grid index.
        direction (str): The direction to move in, one of 'NORTH', 'EAST', 'SOUTH',
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
        case "NORTH":
            if not player_position.north:
                print(f"At {player_position} you can not go north.")
                ic(player_position.coordinate)
                return player_position.coordinate
            if not (is_undergraund_possible(player_position.coordinate, inhand) and
            is_booat_possible(direction, player_position.coordinate, inhand)):
                ic(player_position.coordinate)
                return player_position.coordinate
            ic(player_position.north)
            return player_position.north

        case "EAST":
            if not player_position.east:
                print(f"At {player_position} you can not go east.")
                ic(player_position.coordinate)
                return player_position.coordinate
            if not is_undergraund_possible(player_position.coordinate, inhand):
                ic(player_position.coordinate)
                return player_position.coordinate
            ic(player_position.east)
            return player_position.east

        case "SOUTH":
            if not player_position.south:
                print(f"At {player_position} you can not go south.")
                ic(player_position.coordinate)
                return player_position.coordinate
            if not (is_undergraund_possible(player_position.coordinate, inhand) and
            is_booat_possible(direction, player_position.coordinate, inhand)):
                ic(player_position.coordinate)
                return player_position.coordinate
            ic(player_position.south)
            return player_position.south

        case "WEST":
            if not player_position.west:
                print(f"At {player_position} you can not go west.")
                ic(player_position.coordinate)
                return player_position.coordinate
            if not is_undergraund_possible(player_position.coordinate, inhand):
                ic(player_position.coordinate)
                return player_position.coordinate
            ic(player_position.west)
            return player_position.west

        case "UP":
            if not player_position.up:
                print(f"At {player_position} you can not go up.")
                return player_position.coordinate
            return player_position.up

        case "DOWN":
            if not player_position.down:
                print(f"At {player_position} you can not go down.")
                return player_position.coordinate
            return player_position.down

        case _:
            raise ValueError("Input unknown movement direction. Please reoprt this to the author.")

def is_undergraund_possible(player_position: int, inhand: Ticket) -> bool:
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
    ic(inhand.vehicle)
    if inhand.vehicle == "UNDERGROUND":
        # This partis only executed if the player is traveling with the underground
        inhand.use_ticket()
        return True
    # This partis only executed if the player tyest to take the underground without a valid ticket
    print("You can not take the underground without a valid ticket.")
    return False

def is_booat_possible(direction:str, player_position: int, inhand: Ticket) -> bool:
    """Checks if boat travel is possible for the player based on their
    current position, chosen direction, and ticket status.

    This function determines whether the player can take the boat at their current location, 
    depending on the presence of a valid boat ticket and whether 
    they are at an boat station.If the player is attempting to travel 
    without a valid ticket, a message is displayed, and the function returns False.

    Args:
        direction (str): The direction of travel, with "UP" allowing exit from
        an boat station without a ticket.
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
    if not ((player_position == 29 and direction == "SOUTH") or
            (player_position == 50 and direction == "NORTH")):
        return True
    if inhand.vehicle == "BOAT":
        # This partis only executed if the player is traveling with the boat
        inhand.use_ticket()
        return True
    # This partis only executed if the player tyest to take the boat without a valid ticket
    print("You can not take the boat without a valid ticket.")
    return False
