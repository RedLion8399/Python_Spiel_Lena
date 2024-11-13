"""This module contains unit tests for the functions module."""

import unittest
from functions import process_input
from movement import Command
from places import Location
from ticket import Ticket


class TestProcessInput(unittest.TestCase):
    """Tests for the process_input function in the functions module."""
    def test_movement_possible(self):
        command: Command = Command.NORTH
        inhand: Ticket = Ticket(0)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        *_, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 3)
        self.assertEqual(inhand.ticket_type, 0)
        self.assertTrue(new_move)
    
    def test_movement_not_possible_direction(self):
        command: Command = Command.NORTH
        inhand: Ticket = Ticket(1)
        location: Location = Location("Hyde Park", 11, south=21, east=12)
        *_, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 11)
        self.assertEqual(inhand.ticket_type, 1)
        self.assertTrue(new_move)

    def test_pickup_possible(self):
        command: Command = Command.PICK
        inhand: Ticket = Ticket(0)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(1)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 1)
        self.assertEqual(location.ticket.ticket_type, 0)
        self.assertTrue(new_move)
    
    def test_pickup_not_possible_nothing_on_ground(self):
        command: Command = Command.PICK
        inhand: Ticket = Ticket(0)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(0)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 0)
        self.assertEqual(location.ticket.ticket_type, 0)
        self.assertFalse(new_move)
    
    def test_pickup_not_possible_already_ticket_inhand(self):
        command: Command = Command.PICK
        inhand: Ticket = Ticket(2)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(1)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 2)
        self.assertEqual(location.ticket.ticket_type, 1)
        self.assertFalse(new_move)

    def test_pickup_not_possible_already_ticket_inhand_and_nothing_on_ground(self):
        command: Command = Command.PICK
        inhand: Ticket = Ticket(2)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(0)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 2)
        self.assertEqual(location.ticket.ticket_type, 0)
        self.assertFalse(new_move)
    
    def test_drop_possible(self):
        command: Command = Command.DROP
        inhand: Ticket = Ticket(2)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(0)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 0)
        self.assertEqual(location.ticket.ticket_type, 2)
        self.assertTrue(new_move)
    
    def test_drop_not_possible_nothing_inhand(self):
        command: Command = Command.DROP
        inhand: Ticket = Ticket(0)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(0)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 0)
        self.assertEqual(location.ticket.ticket_type, 0)
        self.assertFalse(new_move)
    
    def test_drop_not_possible_already_ticket_on_ground(self):
        command: Command = Command.DROP
        inhand: Ticket = Ticket(2)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(3)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 2)
        self.assertEqual(location.ticket.ticket_type, 3)
        self.assertFalse(new_move)
    
    def test_drop_not_possible_nothing_inhand_and_already_ticket_on_ground(self):
        command: Command = Command.DROP
        inhand: Ticket = Ticket(0)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(2)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 0)
        self.assertEqual(location.ticket.ticket_type, 2)
        self.assertFalse(new_move)
    
    def test_swap_possible(self):
        command: Command = Command.SWAP
        inhand: Ticket = Ticket(2)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(1)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 1)
        self.assertEqual(location.ticket.ticket_type, 2)
        self.assertTrue(new_move)
    
    def test_swap_not_possible_nothing_inhand(self):
        command: Command = Command.SWAP
        inhand: Ticket = Ticket(0)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(1)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 0)
        self.assertEqual(location.ticket.ticket_type, 1)
        self.assertFalse(new_move)

    def test_swap_not_possible_nothing_on_ground(self):
        command: Command = Command.SWAP
        inhand: Ticket = Ticket(2)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(0)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 2)
        self.assertEqual(location.ticket.ticket_type, 0)
        self.assertFalse(new_move)

    def test_swap_not_possible_nothing_inhand_and_nothing_on_ground(self):
        command: Command = Command.SWAP
        inhand: Ticket = Ticket(0)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(0)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 0)
        self.assertEqual(location.ticket.ticket_type, 0)
        self.assertFalse(new_move)

    def test_unknown_command(self):
        command = "Unknown Command"
        inhand: Ticket = Ticket(0)
        location: Location = Location("Regent Street", 13, north=3, south=23, west=12)
        location.ticket = Ticket(0)
        location.coordinate, location.ticket, inhand, new_move = process_input(command, inhand, location)
        self.assertEqual(location.coordinate, 13)
        self.assertEqual(inhand.ticket_type, 0)
        self.assertEqual(location.ticket.ticket_type, 0)
        self.assertFalse(new_move)
