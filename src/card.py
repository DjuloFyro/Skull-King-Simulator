"""
Card class
"""
from src.card_type import CardType, CardColor

class Card:
    def __init__(self, type: CardType, color:CardColor=CardColor.NOCOLOR, rank=0) -> None:
        if type != CardType.BASIC and (color != CardColor.NOCOLOR or rank != 0):
            raise ValueError("Only basic card can have color and rank")
        if type == CardType.BASIC and (color == CardColor.NOCOLOR or (rank < 1 or rank > 14)):
            raise ValueError("Basic card must have color and rank between 1 and 14")
        self.type = type
        self.color = color
        self.rank = rank
        self.points = 0
        if self.type == CardType.PIECE:
            self.points = 20
        elif self.type == CardType.BASIC and self.rank == 14:
            if self.color == CardColor.BLACK:
                self.points = 20
            else:
                self.points = 10

    def same_color(self, __value: object) -> bool:
        return self.color == __value.color
    
    def __str__(self) -> str:
        return f"{self.type} {self.color} {self.rank} {self.points}"
    
    def __eq__(self, __value: object) -> bool:
        return self.type == __value.type and self.color == __value.color and self.rank == __value.rank
    
    