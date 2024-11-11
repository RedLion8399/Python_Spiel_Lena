"""This is a module to handle the creation and usage of tickets 
for traveling with boats and underground.

This module defines the Ticket class which is used to handle the creation and usage of 
tickets for traveling on either the underground or the boat. Each ticket has a limited 
number of uses and tracks the vehicle associated with it.

Classes:
    Ticket: A class that manages ticket types and tracks the usage of tickets for
            underground and boat travel.
"""
__all__ = ["Ticket"]
__path__ = "ticket.py"
__version__ = "1.0.0"


class Ticket:
    """A class representing a ticket for the underground or boat.

    Attributes:
        ticket_type (int): The type of ticket (1 for underground, 2 for boat).
        left_uses (int): The remaining uses for the ticket (starts at 2).
        vehicle (str): The type of vehicle associated with the ticket 
        (either 'UNDERGROUND' or 'BOAT').

    Arguments:
        ticket_type (int): The type of ticket (1 for underground, 2 for boat).

    Methods:
        use_ticket(self) -> None: Decreases the remaining uses and updates the ticket status.
    
    Example:
        >>> ticket = Ticket(1)
        Creates an underground ticket
        >>> ticket.use_ticket()
        Uses one of the ticket's two available uses
        >>> print(ticket)
        Prints "Used_once_underground-ticket"
    """

    def __init__(self, ticket_type:int) -> None:
        self.ticket_type: int = ticket_type
        self.left_uses: int = 2
        self.vehicle: str

        if self.ticket_type in [1, 3]:
            self.vehicle = "UNDERGROUND"
        elif self.ticket_type in [2, 4]:
            self.vehicle = "BOAT"
        else:
            self.vehicle = ""


    def use_ticket(self) -> None:
        """Decreases the remaining uses and updates the ticket status."""
        self.left_uses -= 1
        if self.left_uses == 1:
            self.ticket_type = 3 if self.vehicle == "UNDERGROUND" else 4
        else:
            self.ticket_type = 0
            self.vehicle = ""


    def __repr__(self) -> str:
        """Returns a string representation of the current ticket status.

        Raises:
            ValueError: Error appears if the assigned ticket_type doesn't 
                match to the existing types. In this case a wrong value was assigned.

        Returns:
            str: The status of the ticket (e.g., 'underground-ticket', 
                 'Used_once_underground-ticket', etc.).
        """
        match self.ticket_type:
            case 0:
                return ""
            case 1:
                return "underground-ticket"
            case 2:
                return "boat-ticket"
            case 3:
                return "Used_once_underground-ticket"
            case 4:
                return "Used_once_boat-ticket"
            case _:
                # TODO raise a better error here
                raise ValueError("Unknown ticket type assigned. Please reoprt this to the author.")
