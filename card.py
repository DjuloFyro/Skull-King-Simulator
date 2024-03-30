"""
Card class
"""
from card_type import CardType, CardColor

class Card:
    def __init__(self, type: CardType, color: CardColor=None, rank=None) -> None:
        if type != CardType.BASIC and (color != None or rank != None):
            raise ValueError("Only basic card can have color and rank")
        self.type = type
        self.color = color
        self.rank = rank
    
    def __str__(self) -> str:
        return f"{self.type} {self.color} {self.rank}"
    
    