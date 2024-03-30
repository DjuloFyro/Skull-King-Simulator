
from card import Card

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []

    def add_card(self, card: Card):
        self.hand.append(card)

    def play_card(self):
        if len(self.hand) > 0:
            return self.hand.pop()
        else:
            return None