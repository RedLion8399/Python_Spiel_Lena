"""This module contains unit tests for the move_player function in the movement module."""

import unittest
from movement import move_player, Command, is_underground_possible, is_boat_possible, move_thief
from places import Location
from ticket import Ticket

class TestMovePlayer(unittest.TestCase):
    """Tests for the move_player function in the movement module."""
    def test_north_not_possible(self) -> None:
        player_position: Location = Location("Greenwhich Park", 9, south=19, east=10, west=8)
        inhand = Ticket(0)
        new_position: int = move_player(player_position, Command.NORTH, inhand)
        self.assertEqual(new_position, 9)

    def test_north_is_possible(self) -> None:
        player_position: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        inhand = Ticket(0)
        new_position: int = move_player(player_position, Command.NORTH, inhand)
        self.assertEqual(new_position, 3)

    def test_south_not_possible(self) -> None:
        player_position: Location = Location("Royal Observatorium", 8, east=9, west=7)
        inhand = Ticket(1)
        new_position: int = move_player(player_position, Command.SOUTH, inhand)
        self.assertEqual(new_position, 8)

    def test_south_is_possible(self) -> None:
        player_position: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        inhand = Ticket(1)
        new_position: int = move_player(player_position, Command.SOUTH, inhand)
        self.assertEqual(new_position, 23)

    def test_east_not_possible(self) -> None:
        player_position: Location = Location("Regent's Park", 3,  south=13, west=2)
        inhand = Ticket(2)
        new_position: int = move_player(player_position, Command.EAST, inhand)
        self.assertEqual(new_position, 3)

    def test_east_is_possible(self) -> None:
        player_position: Location = Location("Royal Observatorium", 8, east=9, west=7)
        inhand = Ticket(2)
        new_position: int = move_player(player_position, Command.EAST, inhand)
        self.assertEqual(new_position, 9)

    def test_west_not_possible(self) -> None:
        player_position: Location = Location("White Lion Hill", 25, north=15, east=26)
        inhand = Ticket(3)
        new_position: int = move_player(player_position, Command.WEST, inhand)
        self.assertEqual(new_position, 25)

    def test_west_is_possible(self) -> None:
        player_position: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        inhand = Ticket(3)
        new_position: int = move_player(player_position, Command.WEST, inhand)
        self.assertEqual(new_position, 12)

    def test_up_not_possible(self) -> None:
        player_position: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        inhand = Ticket(4)
        new_position: int = move_player(player_position, Command.UP, inhand)
        self.assertEqual(new_position, 13)

    def test_up_is_possible(self) -> None:
        player_position: Location = Location("Hyde Park Corner Station (underground)", 74, False, north=72, east=75, up=21)
        inhand = Ticket(4)
        new_position: int = move_player(player_position, Command.UP, inhand)
        self.assertEqual(new_position, 21)

    def test_down_not_possible(self) -> None:
        player_position: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        inhand = Ticket(0)
        new_position: int = move_player(player_position, Command.DOWN, inhand)
        self.assertEqual(new_position, 13)

    def test_down_is_possible(self) -> None:
        player_position: Location = Location("Hyde Park Corner Station (underground)", 74, False, north=72, east=75, down=21)
        inhand = Ticket(0)
        new_position: int = move_player(player_position, Command.DOWN, inhand)
        self.assertEqual(new_position, 21)

    def test_unknown_direction(self) -> None:
        player_position: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        inhand = Ticket(0)
        with self.assertRaises(ValueError):
            move_player(player_position, "UNKNOWN_DIRECTION", inhand)

class TestCommand(unittest.TestCase):
    """Tests for the Command enum in the movement module."""
    def test_invalid_command(self) -> None:
        with self.assertRaises(ValueError):
            Command("INVALID_COMMAND")

    def test_command_values(self) -> None:
        self.assertEqual(str(Command.NORTH), "Command.NORTH")
        self.assertEqual(str(Command.SOUTH), "Command.SOUTH")
        self.assertEqual(str(Command.EAST), "Command.EAST")
        self.assertEqual(str(Command.WEST), "Command.WEST")
        self.assertEqual(str(Command.UP), "Command.UP")
        self.assertEqual(str(Command.DOWN), "Command.DOWN")
        self.assertEqual(str(Command.SWAP), "Command.SWAP")
        self.assertEqual(str(Command.DROP), "Command.DROP")
        self.assertEqual(str(Command.PICK), "Command.PICK")
        self.assertEqual(str(Command.QUIT), "Command.QUIT")
        self.assertEqual(str(Command.HELP), "Command.HELP")

    def test_command_union(self) -> None:
        self.assertIn(Command.NORTH, Command.MOVEMENT)
        self.assertIn(Command.SOUTH, Command.MOVEMENT)
        self.assertIn(Command.EAST, Command.MOVEMENT)
        self.assertIn(Command.WEST, Command.MOVEMENT)
        self.assertIn(Command.UP, Command.MOVEMENT)
        self.assertIn(Command.DOWN, Command.MOVEMENT)
        self.assertNotIn(Command.SWAP, Command.MOVEMENT)

class TestIsUndergroundPossible(unittest.TestCase):
    """Tests for the is_underground_possible function in the movement module."""
    def test_player_not_in_underground_station(self) -> None:
        inhand: Ticket = Ticket(0)
        self.assertTrue(is_underground_possible(3, inhand))
        self.assertEqual(inhand.ticket_type, 0)

    def test_player_in_underground_station_unvalid_ticket(self) -> None:
        inhand: Ticket = Ticket(4)
        self.assertFalse(is_underground_possible(74, inhand))
        self.assertEqual(inhand.ticket_type, 4)
    
    def test_player_in_underground_station_no_ticket(self) -> None:
        inhand: Ticket = Ticket(0)
        self.assertFalse(is_underground_possible(74, inhand))
        self.assertEqual(inhand.ticket_type, 0)
    
    def test_player_in_underground_station_valid_ticket(self) -> None:
        inhand: Ticket = Ticket(1)
        self.assertTrue(is_underground_possible(74, inhand))
        self.assertEqual(inhand.ticket_type, 3)

class TestIsBoatPossible(unittest.TestCase):
    """Tests for the is_boat_possible function in the movement module."""
    def test_player_not_in_boat_dock(self) -> None:
        inhand: Ticket = Ticket(0)
        self.assertTrue(is_boat_possible(Command.NORTH, 3, inhand))
        self.assertEqual(inhand.ticket_type, 0)

    def test_player_in_boat_dock_unimportant_command(self) -> None:
        inhand: Ticket = Ticket(0)
        self.assertTrue(is_boat_possible(Command.NORTH, 29, inhand))
        self.assertEqual(inhand.ticket_type, 0)

    def test_player_in_boat_dock_valid_ticket(self) -> None:
        inhand: Ticket = Ticket(2)
        self.assertTrue(is_boat_possible(Command.NORTH, 50, inhand))
        self.assertEqual(inhand.ticket_type, 4)

        inhand: Ticket = Ticket(2)
        self.assertTrue(is_boat_possible(Command.SOUTH, 29, inhand))
        self.assertEqual(inhand.ticket_type, 4)

    def test_player_in_boat_dock_invalid_ticket(self) -> None:
        inhand: Ticket = Ticket(1)
        self.assertFalse(is_boat_possible(Command.NORTH, 50, inhand))
        self.assertEqual(inhand.ticket_type, 1)

        inhand: Ticket = Ticket(1)
        self.assertFalse(is_boat_possible(Command.SOUTH, 29, inhand))
        self.assertEqual(inhand.ticket_type, 1)

class TestMoeThief(unittest.TestCase):
    """Tests for the moe_thief function in the movement module."""
    def test_thief_moves_all_possible(self) -> None:
        for _ in range(1, 500):
            thief_position: Location = Location("Tower Bridge Road", 58, north=48, south=68, east=59, west=57)
            new_position: int = move_thief(thief_position)
            self.assertIn(new_position, [48, 58, 68, 59, 57])
    
    def test_thief_moves_north_west(self) -> None:
        for _ in range(1, 500):
            thief_position: Location = Location("Tothill Street", 53, north=43, west=52)
            new_position: int = move_thief(thief_position)
            self.assertIn(new_position, [43, 52, 53])
    
    def test_thief_boat(self) -> None:
        for _ in range(1, 500):
            thief_position: Location = Location("Greenwhich Pier", 29, north=19, south=50, east=30)
            new_position: int = move_thief(thief_position)
            self.assertIn(new_position, [19, 29, 30, 50])
