"""The Module holds function definitions they are used in the game.

By separating the functions into this module, the main game file remains cleaner 
and easier to read. The functions provide essential gameplay features such as 
welcoming the player or displaying instructions.

Functions:
    greeting: Prints a welcome message and gives a brief game description.
    command_help: Lists all available commands for the player to navigate through the game.
    print_positions: Prints the current position of the player and the thief.
    print_hand_status: Prints the current ticket the player is holding.
    check_winning: Checks if the player has won the game.
    print_moving_opportunity: Prints if the player has the possibility to move.
    process_input: Processes the input of the player.
    print_relative_positions: Prints the relative positions of the player and the thief.
    print_object_status: Prints the status of the ticket.
    get_command: Asking the player for input and returning the command type.
"""
__all__ = ["greeting", "command_help", "print_moving_opportunitys", "print_relative_positions",
           "check_winning", "print_hand_status", "print_positions", "print_object_status",
           "process_input", "get_command"]
__path__ = "functions.py"
__version__ = "1.2.0"

from color import Color
from movement import Command, move_player
from places import Location, locations
from ticket import Ticket

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

def print_moving_opportunitys(location: Location) -> None:
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
        print(f"You can go North to {locations[location.north]}.")
    else:
        print("You cannot go North.")
    print()

    if location.south:
        print(f"You can go South to {locations[location.south]}.")
    else:
        print("You cannot go South.")
    print()

    if location.east:
        print(f"You can go East to {locations[location.east]}.")
    else:
        print("You cannot go East.")
    print()

    if location.west:
        print(f"You can go West to {locations[location.west]}.")
    else:
        print("You cannot go West.")
    print(Color.PURPLE)

    if location.down:
        print(f"You can go down to {locations[location.down]}.")
    else:
        print("There is no (other) underground station here.")
    print()

    if location.up:
        print(f"You can go up to {locations[location.up]}.")
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

def print_hand_status(inhand: Ticket) -> None:
    """Displays if the player is holding a valid tickit.

    This function checks if the player is holding a ticket. If the player has 
    no ticket in hand, it prints a message indicating an empty hand. Otherwise, 
    it displays the type of ticket the player is currently holding.

    (The player always has one ticket in hand but if the `ticket_type = 0`,
    its equel to the empty hand.)

    Args:
        inhand (Ticket): The ticket object representing the item currently held 
        by the player.
    """
    if not inhand.ticket_type:
        print("You have currently nothing in your hand.")
    else:
        print(f"You are currently in possession of a/an {inhand}.")
    print()
    print()

def print_positions(player_position: int, thief_position: int) -> None:
    """Displays the current locations of the player and the thief.

    This function outputs the player's current position and the thief's position
    in the game environment. It uses color formatting to differentiate the output.

    Args:
        player_position (int): The current position of the player as a grid index.
        thief_position (int): The current position of the thief as a grid index.
    """
    print(Color.GREEN)
    print(f"You are in/on/at {locations[player_position]}.")
    print()
    print(f"The thief is in/on/at {locations[thief_position]}.")
    print(Color.CYAN)

def print_object_status(player_position: Location, inhand: Ticket) -> None:
    """Displays if the player is possible to pick up a tickit
    or switch it if he's currently holding one.

    Based on the player's current location and whether they are holding a ticket, this 
    function informs the player if they can pick up a new ticket or switch their 
    current ticket with one available at the location.

    Args:
        player_position (Location): The current position of the player.
        inhand (Ticket): The ticket currently held by the player, he's always holding 
        a tickit but if the `ticket_type = 0`, its equel to the empty hand.
    """
    if (player_position.ticket.ticket_type and not inhand.ticket_type):
        print(f"You can pick-up the: {player_position.ticket}.")
    elif (player_position.ticket.ticket_type and inhand.ticket_type):
        print(f"You can switch the: {inhand} with a/an {player_position.ticket}.")
    print(Color.RESET)

def process_input(command: Command, inhand: Ticket,
                  player_position: Location) -> tuple[int, Ticket, Ticket, bool]:
    """Processes the player's command and updates the game state, including the player's 
    position and ticket status.

    Args:
        command (Command): The input command from the player, specifying a movement or interaction.
        inhand (Ticket): The ticket currently held by the player.
        player_position (Location): The player's current location.
    
    Returns:
        tuple[int, Ticket, Ticket, bool]: A tuple consisting of: \n
            - int: The player's updated coordinate. \n
            - Ticket: The ticket placed at the player's location. \n
            - Ticket: The ticket held by the player after the command is processed. \n
            - bool: A flag indicating whether a valid move or action occurred (`True`),
              or if no change took place (`False`).
    
    Example:
        >>> inhand = Ticket(1)
        >>> player_position = Location("Paddington Station", 1, west=1, up=2, down=3)
        >>> command = Command.PICK
        >>> process_input(command, inhand, player_position)
        (1, Ticket(0), Ticket(1), True)
    """
    match command:
        case Command.NORTH | Command.SOUTH | Command.EAST | Command.WEST | Command.UP | Command.DOWN:
            player_position.coordinate = move_player(player_position, command, inhand)

        case Command.DROP:
            if not inhand.ticket_type:
                print("Yo have no item in your hand.")
                return (player_position.coordinate, player_position.ticket, inhand, False)
            if player_position.ticket.ticket_type:
                print("There is already a ticket on the ground.")
                return (player_position.coordinate, player_position.ticket, inhand, False)
            player_position.ticket, inhand = inhand, player_position.ticket
            inhand.ticket_type = 0

        case Command.PICK:
            if inhand.ticket_type:
                print("Yo have already an item in your hand.")
                return (player_position.coordinate, player_position.ticket, inhand, False)
            if not player_position.ticket.ticket_type:
                print("There is no ticket on the ground.")
                return (player_position.coordinate, player_position.ticket, inhand, False)
            player_position.ticket, inhand = inhand, player_position.ticket

        case Command.SWAP:
            if not player_position.ticket.ticket_type:
                print("There is no ticket on the ground.")
                return (player_position.coordinate, player_position.ticket, inhand, False)
            if not inhand.ticket_type:
                print("Yo have no item in your hand.")
                return (player_position.coordinate, player_position.ticket, inhand, False)
            player_position.ticket, inhand = inhand, player_position.ticket

        case Command.QUIT:
            print()
            print("Good bye! I hope you had fun playing this game!")
            print()
            exit()

        case Command.HELP:
            command_help()
            return (player_position.coordinate, player_position.ticket, inhand, False)

        case _:
            print(f"This command is not available at {player_position}. Please try again.")
            return (player_position.coordinate, player_position.ticket, inhand, False)

    return (player_position.coordinate, player_position.ticket, inhand, True)

def get_command() -> Command:
    """Prompts the player to select a command and returns the corresponding `Command` enum value.

    This function continuously prompts the user to input a command until a valid command is entered.
    Based on the user's input, it returns a specific `Command` enum value representing
    a direction (e.g., NORTH, EAST), an action (e.g., PICK, DROP), or a control command 
    (e.g., HELP, QUIT). If an invalid command is entered, a message indicating that the 
    command is unavailable is displayed, and the prompt restarts.

    Returns:
        Command: The enum value corresponding to the entered command.

    Raises:
        ValueError: If an unknown command value is somehow assigned. This case should not occur
            under normal use, as only valid commands are accepted.

    Commands:
        - Movement: "N" (NORTH), "E" (EAST), "S" (SOUTH), "W" (WEST), "U" (UP), "D" (DOWN)
        - Actions: "X" (DROP), "P" (PICK), "K" (SWAP)
        - Controls: "Q" (QUIT), "H" (HELP)

    Example:
        >>> get_command()  # User inputs "N" for NORTH
        <Command.NORTH: 'N'>
    """

    while True:
        input_command = input("Select a command out of the list above: ").upper()
        if input_command not in ["N", "E", "S", "W", "U", "D", "X", "P", "K", "Q", "H"]:
            print()
            print()
            print()
            print()
            print("This is not a valid command. Please try again")
            continue

        match input_command:
            case "N":
                return Command.NORTH
            case "E":
                return Command.EAST
            case "S":
                return Command.SOUTH
            case "W":
                return Command.WEST
            case "U":
                return Command.UP
            case "D":
                return Command.DOWN
            case "X":
                return Command.DROP
            case "P":
                return Command.PICK
            case "K":
                return Command.SWAP
            case "Q":
                return Command.QUIT
            case "H":
                return Command.HELP
            case _:
                raise ValueError("""A wrong command value was assigned.
                                 Please report this to the author.""")
