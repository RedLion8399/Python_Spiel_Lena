class Ticket:
    def __init__(self, ticket_type:int) -> None:
        self.ticket_type: int = ticket_type
        self.left_uses: int = 2
        self.vehicle: str

        self.vehicle = "UNDERGROUND" if self.ticket_type == 1 else "BOAT"

    
    def use_ticket(self) -> None:
        self.left_uses -= 1
        if self.left_uses == 1:
            self.ticket_type = 3 if self.vehicle == "UNDERGROUND" else 4
        else:
            self.ticket_type = 1 if self.vehicle == "UNDERGROUND" else 2


    def __repr__(self) -> str:
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
                raise ValueError("Unknown ticket type assigned. Please reoprt this to the author.")