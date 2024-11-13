"""This module contains unit tests for the color module."""

import unittest
from color import Color

class TestColor(unittest.TestCase):
    """Tests for the Color class."""
    def test_color_code(self) -> None:
        self.assertEqual(Color.RED, "\033[91m")
        self.assertEqual(Color.GREEN, "\033[92m")
        self.assertEqual(Color.YELLOW, "\033[93m")
        self.assertEqual(Color.BLUE, "\033[94m")
        self.assertEqual(Color.PURPLE, "\033[95m")
        self.assertEqual(Color.CYAN, "\033[96m")
        self.assertEqual(Color.WHITE, "\033[97m")
        self.assertEqual(Color.BOLD, "\033[1m")
        self.assertEqual(Color.UNDERLINE, "\033[4m")
        self.assertEqual(Color.BLACK, "\033[30m")
        self.assertEqual(Color.RESET, "\033[0m")
    
    def test_color_name(self) -> None:
        self.assertEqual(Color.RED, Color.RED)
        self.assertEqual(Color.GREEN, Color.GREEN)
        self.assertEqual(Color.YELLOW, Color.YELLOW)
        self.assertEqual(Color.BLUE, Color.BLUE)
        self.assertEqual(Color.PURPLE, Color.PURPLE)
        self.assertEqual(Color.CYAN, Color.CYAN)
        self.assertEqual(Color.WHITE, Color.WHITE)
        self.assertEqual(Color.BOLD, Color.BOLD)
        self.assertEqual(Color.UNDERLINE, Color.UNDERLINE)
        self.assertEqual(Color.BLACK, Color.BLACK)
        self.assertEqual(Color.RESET, Color.RESET)
