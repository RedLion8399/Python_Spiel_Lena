"""This project is a text-based adventure game set in London, where the main objective
is to pursue and capture a fugitive criminal. The player navigates the city, uses tickets
to access special transportation options, and gaining information about criminals position
to travial toward him and catch him.

Main Modules:
- movement: Provides movement logic for both the player and the criminal character,
  including support for special transportation options like the underground and boat.
- places: Defines city locations and special stations,
  including the positions of underground stations and boat docks.
- ticket: Defines the ticket system, enabling the player to use
  specific trave options and managing ticket usage and durability.
- colors: Contains color codes used to enhance the console output and improve readability. 
  This module centralizes color settings, allowing consistent styling and easy adjustments
  if the visual style of the game needs updating.
- main: Contains the main game loop and logic for gameplay
- functions: Contains various helper functions for gameplay and visual output.

Usage:
Once started, the player can control the game through console commands to navigate the city.
This project uses a modular structure to separate game functionalities,
ensuring clear organization and ease of expansion.
"""
__title__ = "Adventure Game"
__author__ = "Lena Weinstock, Paul Jonas Dohle"
__status__ = "Production"
__date__ = "11.11.2024"
__coure__ = "Computer Science ICS 3u"
__school__ = "Glebe Collegiate Institute, Ottawa; Europagymnaium Warstein"
__teacher__ = "Mr Giassante"
