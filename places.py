"""This module defines locations in a game world, 
where each location has different attributes such as coordinates, 
connected locations, and potential objects (e.g., tickets). 
It provides a way to manage game locations and movement between them. 
The module also defines various lists of locations that are restricted 
for the player or thief to start from, and lists for underground stations and boat docks.

Classes:
    Location: Represents a location in the game world, with attributes for name, 
    coordinates, connected locations, and if a ticket is at this location.

Variables:
    locations (list[Location]): A list of all locations in the game world.
    forbidden_player_starts (list[int]): A list of location indices where 
    the player is not allowed to start.
    forbidden_thief_starts (list[int]): A list of location indices where 
    the thief is not allowed to start.
    underground_stations (list[int]): A list of location indices where
    underground stations are located.
    boat_docks (list[int]): A list of location indices where boat docks are located.
"""

__all__ = ["Location", "locations", "FORBIDDEN_PLAYER_STARTS", "FORBIDDEN_THIEF_STARTS",
           "UNDERGROUND_STATIONS", "BOAT_DOCKS"]
__path__ = "places.py"
__version__ = "1.0.0"

from random import randint
from typing import Final
from ticket import Ticket


class Location:
    """Represents a location in the game world with different attributes
    and some automated behavior.

    Arguments:
        name (str): The name of the location.
        coordinate (int): A unique identifier for the location.
        
    Keyword Arguments:
        object (bool): Indicates whether the location can contain a ticket. Defaults to True.
        north (int): The index of the location to the north of this one. Defaults to 0.
        south (int): The index of the location to the south of this one. Defaults to 0.
        east (int): The index of the location to the east of this one. Defaults to 0.
        west (int): The index of the location to the west of this one. Defaults to 0.
        up (int): The index of the location above this one. Defaults to 0.
        down (int): The index of the location below this one (undergroundstation). Defaults to 0.

    Attributes:
        ticket (Ticket): A ticket associated with this location. While innitializing a new location
        (at the beginning of the game), by chance, there will be either an underground ticket, a boat ticket
        or no ticket at all. Every case has a specific probability.
        - 83.3% chance to generate no ticket (ticket type 0).
        - 16.6% chance to generate an `Underground-ticket` (ticket type 1).
        - 4.16% chance to generate a `Boat-ticket` (ticket type 2).

    Methods:
        __repr__: Returns the location name as a string.

    Example:
        >>> loc = Location("Paddington Station", 1, west=1, up=2, down=3)
        >>> loc.north
        0
        >>> loc
        "Paddington Station"
        >>> loc.ticket
        <Ticket object>
    """

    def __init__(self, name: str, coordinate: int, objects: bool = True, north: int = 0,
                 south: int = 0, east: int = 0, west: int = 0, up: int = 0, down: int = 0) -> None:
        self.name: str = name
        self.coordinate: int = coordinate
        self.object: bool = objects
        self.north: int = north
        self.south: int = south
        self.east: int = east
        self.west: int = west
        self.up: int = up
        self.down: int = down
        self.ticket: Ticket

        self.ticket = self.__create_Ticket() if objects else Ticket(0)

    def __create_Ticket(self) -> Ticket:
        """Generates a random ticket with a certain probability.

        This method determines which type of ticket (underground or boat)
        is assigned to the location, based on random probabilities.

        - 83.3% chance to generate no ticket (ticket type 0).
        - 16.6% chance to generate an underground ticket (ticket type 1).
        - 4.16% chance to generate a boat ticket (ticket type 2).

        Returns:
            Ticket: A randomly generated ticket, either a ticket with type 0 (no ticket),
                    type 1 (underground ticket), or type 2 (boat ticket).
        """

        if randint(1, 6) != 5:      # The propability for any ticket is about 16,6%
            return Ticket(0)        # The propability for no ticket is about 83,3%
        if randint(1,4) != 1:       # The conditional propability for a boat ticket is 25%
            return Ticket(1)        # The Total probability for an undergraund-ticket is about 16,6%
        return Ticket(2)            # The total propability for a boat-ticket is about 4,16%s

    def __repr__(self) -> str:
        return self.name


# Creating all istances of the class. One for each place
locations: list[Location]

locations = [
    Location("", 0),  # This item only exists to start with index 0
    Location("Paddington Station", 1, down=71),
    Location("Regent's Park", 2, east=3),
    Location("Regent's Park", 3,  south=13, west=2),
    Location("Gower Street", 4, south=14, east=5),
    Location("Euston Road", 5, east=6, west=4),
    Location("King's Cross Station", 6, west=5, down=72),
    Location("Prime Meridian", 7, east=8),
    Location("Royal Observatorium", 8, east=9, west=7),
    Location("Greenwhich Park", 9, south=19, east=10, west=8),
    Location("Greenwhich Park", 10, west=9),
    Location("Hyde Park", 11, south=21, east=12),
    Location("Brook Street", 12, south=22, east=13, west=11),
    Location("Regent Street", 13, north=3, south=23, west=12),
    Location("British Museum", 14, north=4, south=24),
    Location("Queen Victoria Street", 15, south=25, east=16),
    Location("King William Street", 16, east=17, west=15),
    Location("Tower Hill Station", 17, south=27, west=16, down=73),
    Location( "National Maritim Museum", 18, east=19),
    Location("King William Walk", 19, north=9, south=29, east=20, west=18),
    Location("Greenwhich Market", 20, west=19),
    Location("Hyde Park Corner (Station)", 21, north=11, south=31, east=22, down=74),
    Location("Picadilly Street", 22, north=12, south=32, east=23, west=21),
    Location("Picadilly Circus Station", 23, north=13, east=24, west=22, down=75),
    Location("Shaftesbury Avenue", 24,  north=14, west=23),
    Location("White Lion Hill", 25, north=15, east=26),
    Location("Upper Thames Street", 26, east=27, west=25),
    Location("Lower Thames Street", 27, north=17, east=28, west=26),
    Location("Tower of London", 28, south=38, west=27),
    Location("Greenwhich Pier", 29, north=19, south=50, east=30),
    Location("Cutty Sark", 30, west=29),
    Location("Constitution Hill (Street)", 31, north=21, south=41),
    Location("St. James Park", 32, north=22, south=42),
    Location("White Hall (Street)", 33, south=43),
    Location("River", 34, False),
    Location("River", 35, False),
    Location("River", 36, False),
    Location("River", 37, False),
    Location("Tower Bridge", 38, north=28, south=48),
    Location("River", 39, False),
    Location("River", 40, False),
    Location("Buckingham Palace", 41, north=31, south=51, east=42),
    Location("Birdcage Walk", 42, north=32, south=52, east=43, west=41),
    Location("Palace of Westminister", 43, north=33, south=53, east=44, west=42),
    Location("Westminister Bridge", 44, east=45, west=43),
    Location("London Eye", 45, south=55, east=46, west=44),
    Location("Waterloo Road", 46, south=56, west=45),
    Location("Tooley Street", 47, south=57, east=48),
    Location("Tower Bridge Road", 48, north=38, south=58, east=49, west=47),
    Location("Tooley Street", 49, west=48),
    Location("City Cruises London Office", 50, north=29, south=60),
    Location("Buckingham Gate", 51, north=41, south=61, east=52),
    Location("St. James Park Station", 52, north=42, east=53, west=51, down=76),
    Location("Tothill Street", 53, north=43, west=52),
    Location("River", 54),
    Location("Westminister Bridge Road", 55, north=45, south=65),
    Location("London Road", 56, north=46, south=66),
    Location("Abbey Street", 57, north=47, east=58),
    Location("Tower Bridge Road", 58, north=48, south=68, east=59, west=57),
    Location("Abbey Street", 59, east=60, west=58),
    Location("Abbey Street", 60, north=50, west=59),
    Location("Victoria Street", 61, north=51, east=62),
    Location("Victoria Street", 62, east=63, west=61),
    Location("Victoria Street", 63, north=43, west=62),
    Location("River", 64, False),
    Location("Kennington Road", 65, north=55, east=66),
    Location("Kennington Station", 66, north=56, east=67, west=65, down=77),
    Location("New Kent Road", 67, east=68, west=66),
    Location("Tower Bridge Road", 68, north=58, east=69, west=67),
    Location("New Cross Road", 69, east=70, west=68),
    Location("New Cross Road", 70, south=80, west=69),
    Location("Paddington Station (underground)", 71, False, north=72, south=78, east=75, up=1),
    Location("King's Cross Station (underground)", 72, False, north=73, south=78, east=74,west=76, up=6),
    Location("Tower Hill Station (underground)", 73, False, north=72, west=71, up=17),
    Location("Hyde Park Corner Station (underground)", 74, False, north=72, east=75, up=21),
    Location("Picadilly Circus Station (underground)", 75, False, north=71, south=78, east=72, west=74, up=52),
    Location("St. James Park Station (underground)", 76, False, north=72, east=73, up=52),
    Location("Kennington Station (underground)", 77, False, north=72, east=78, up=66),
    Location("Elefant & Castle Station (underground)", 78, False, north=71, west=77, up=79),
    Location("Elefant & Castle Station", 79, east=80, down=78),
    Location("Old Kent Road", 80, north=70, west=79),
]

# Lists with special places to choose from in the later programm
FORBIDDEN_PLAYER_STARTS: Final[list[int]] = [0, 1, 7, 8, 9, 10, 18, 19, 20, 29, 30, 34, 35, 36, 37,
                                      38, 39, 49, 40, 54, 64, 71, 72, 73, 74, 75, 76, 77, 78]

FORBIDDEN_THIEF_STARTS: Final[list[int]] = [0, 34, 35, 36, 37, 38, 39, 40, 54,
                                            64, 71, 72, 73, 74, 75, 76, 77, 78]

UNDERGROUND_STATIONS: Final[list[int]] = [71, 72, 73, 74, 75, 76, 77, 78]

BOAT_DOCKS: Final[list[int]] = [29, 50]
