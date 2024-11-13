"""This module contains unit tests for the color module."""

import unittest
from ticket import Ticket

class TestTicket(unittest.TestCase):
    """Tests for the Ticket class in the ticket module."""
    def test_create_ticket(self):
        test_ticket: Ticket = Ticket(1)
        self.assertEqual(test_ticket.ticket_type, 1)
        self.assertEqual(test_ticket.left_uses, 2)
        self.assertEqual(test_ticket.vehicle, 'UNDERGROUND')

        test_ticket: Ticket = Ticket(2)
        self.assertEqual(test_ticket.ticket_type, 2)
        self.assertEqual(test_ticket.left_uses, 2)
        self.assertEqual(test_ticket.vehicle, 'BOAT')

        test_ticket: Ticket = Ticket(3)
        self.assertEqual(test_ticket.ticket_type, 3)
        self.assertEqual(test_ticket.left_uses, 1)
        self.assertEqual(test_ticket.vehicle, 'UNDERGROUND')

        test_ticket: Ticket = Ticket(4)
        self.assertEqual(test_ticket.ticket_type, 4)
        self.assertEqual(test_ticket.left_uses, 1)
        self.assertEqual(test_ticket.vehicle, 'BOAT')

        test_ticket: Ticket = Ticket(0)
        self.assertEqual(test_ticket.ticket_type, 0)
        self.assertEqual(test_ticket.left_uses, 0)
        self.assertEqual(test_ticket.vehicle, "")

    def test_use_ticket_new_underground(self):
        test_ticket: Ticket = Ticket(1)
        self.assertEqual(test_ticket.ticket_type, 1)
        self.assertEqual(test_ticket.left_uses, 2)
        self.assertEqual(test_ticket.vehicle, 'UNDERGROUND')

        test_ticket.use_ticket()
        self.assertEqual(test_ticket.ticket_type, 3)
        self.assertEqual(test_ticket.left_uses, 1)
        self.assertEqual(test_ticket.vehicle, 'UNDERGROUND')

        test_ticket.use_ticket()
        self.assertEqual(test_ticket.ticket_type, 0)
        self.assertEqual(test_ticket.left_uses, 0)
        self.assertEqual(test_ticket.vehicle, "")

    def test_use_ticket_new_boat(self):
        test_ticket: Ticket = Ticket(2)
        self.assertEqual(test_ticket.ticket_type, 2)
        self.assertEqual(test_ticket.left_uses, 2)
        self.assertEqual(test_ticket.vehicle, 'BOAT')

        test_ticket.use_ticket()
        self.assertEqual(test_ticket.ticket_type, 4)
        self.assertEqual(test_ticket.left_uses, 1)
        self.assertEqual(test_ticket.vehicle, 'BOAT')

        test_ticket.use_ticket()
        self.assertEqual(test_ticket.ticket_type, 0)
        self.assertEqual(test_ticket.left_uses, 0)
        self.assertEqual(test_ticket.vehicle, "")
    
    def test_use_ticket_underground_used(self):
        test_ticket: Ticket = Ticket(3)
        self.assertEqual(test_ticket.ticket_type, 3)
        self.assertEqual(test_ticket.left_uses, 1)
        self.assertEqual(test_ticket.vehicle, 'UNDERGROUND')
        
        test_ticket.use_ticket()
        self.assertEqual(test_ticket.ticket_type, 0)
        self.assertEqual(test_ticket.left_uses, 0)
        self.assertEqual(test_ticket.vehicle, "")
    
    def test_use_ticket_boat_used(self):
        test_ticket: Ticket = Ticket(4)
        self.assertEqual(test_ticket.ticket_type, 4)
        self.assertEqual(test_ticket.left_uses, 1)
        self.assertEqual(test_ticket.vehicle, 'BOAT')
        
        test_ticket.use_ticket()
        self.assertEqual(test_ticket.ticket_type, 0)
        self.assertEqual(test_ticket.left_uses, 0)
        self.assertEqual(test_ticket.vehicle, "")
    
    def test_ticket_type_representation(self):
        test_ticket: Ticket = Ticket(1)
        self.assertEqual(str(test_ticket), "underground-ticket")

        test_ticket: Ticket = Ticket(2)
        self.assertEqual(str(test_ticket), "boat-ticket")

        test_ticket: Ticket = Ticket(3)
        self.assertEqual(str(test_ticket), "Used_once_underground-ticket")

        test_ticket: Ticket = Ticket(4)
        self.assertEqual(str(test_ticket), "Used_once_boat-ticket")
