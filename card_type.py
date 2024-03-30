"""
Description: This file contains the enum type for the card type
"""

from enum import Enum

class CardType(Enum):
    """
    Description: This class is an enum type for the card type
    """
    # Enum values
    BASIC = 1
    PIRATE = 2
    SIRENE = 3
    SKULL = 4
    FUITE = 5
    PIECE = 6
    KRAKEN = 7
    BALEINE = 8
    POISSON = 9

    def __str__(self):
        return self.name
    

class CardColor(Enum):
    """
    Description: This class is an enum type for the card color
    """
    # Enum values
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    BLACK = 4

    def __str__(self):
        return self.name
 