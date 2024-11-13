"""This module contains unit tests for the color module."""

import unittest
from places import Location

class TestLocation(unittest.TestCase):
    """Test the location module."""
    def test_initialisation(self):
        for _ in range(100):
            location: Location = Location("Greenwhich Park", 9, south=19, east=10, west=8)
            self.assertEqual(location.name, "Greenwhich Park")
            self.assertEqual(location.north, 0)
            self.assertEqual(location.south, 19)
            self.assertEqual(location.east, 10)
            self.assertEqual(location.west, 8)
            self.assertTrue(location.ticket)
            self.assertTrue(location.object)

    def test_initialisation_without_ticket(self):
        for _ in range(100):
            location: Location = Location("Greenwhich Park", 9, objects=False, south=19, east=10, west=8)
            self.assertFalse(location.ticket.ticket_type)
            self.assertFalse(location.object)
    
    def test_create_ticket(self):
        ticket_types_list: list[int] = []
        for _ in range(100):
            location: Location = Location("Greenwhich Park", 9, south=19, east=10, west=8)
            ticket_types_list.append(location.ticket.ticket_type)
        self.assertIn(0, ticket_types_list)
        self.assertIn(1, ticket_types_list)
        self.assertIn(2, ticket_types_list)

    def test_repr(self):
        location: Location = Location("Greenwhich Park", 9, south=19, east=10, west=8)
        self.assertEqual(str(location), "Greenwhich Park")
