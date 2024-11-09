"""Module for console text coloring.

This module provides a set of pre-formatted ANSI color codes that can be used 
to modify the color and style of text output in the console. The `Color` class 
contains static attributes representing different color codes, as well as formatting 
styles like bold and underline. These codes can be concatenated with text to 
produce colored or styled output in terminal environments that support ANSI escape sequences.

Classes:
    Color: A class containing pre-formatted color codes and styles for console output.
        Each attribute represents an ANSI escape sequence for a specific color or text style.
"""

__all__ = ["Color"]
__path__ = "color.py"
__version__ = "1.0.0"

from dataclasses import dataclass


@dataclass
class Color:
    """A class to provide pre-formatted ANSI color codes and text styles for console output.

    This class contains class-level attributes that represent ANSI escape sequences for various 
    colors and text styles, which can be used to modify the appearance of text in a terminal. 
    The codes are meant to be concatenated with text strings to change the color and style 
    of the output in terminals that support ANSI escape sequences.

    Example:
    >>> print(f"{Color.RED}This text is red{Color.RESET}")
        This text is red
    The text will appear red in a supported terminal.

    Notes:
    - The color codes are only effective in terminals that support ANSI escape sequences.
    - To reset any style applied, append `Color.RESET` to the text.
    - To apply multiple styles, concatenate them as needed.
    """

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\033[30m'
    RESET = '\033[0m'
