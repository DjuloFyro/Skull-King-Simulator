from card import Card, CardType, CardColor

import random

class Deck:
    def __init__(self):
        self.cards = []
        # add 5 pirates, 2 sirenes, 1 skulls, 5 fuites, 2 pieces, 1 kraken, 1 baleine, 1 poisson
        for _ in range(5):
            self.cards.append(Card(CardType.PIRATE)) # Add 5 pirates
        for _ in range(2):
            self.cards.append(Card(CardType.SIRENE)) # Add 2 sirenes
        for _ in range(5):
            self.cards.append(Card(CardType.FUITE)) # Add 5 fuites
        for _ in range(2):
            self.cards.append(Card(CardType.PIECE)) # Add 2 pieces
        self.cards.append(Card(CardType.SKULLKING)) # Add 1 skull
        self.cards.append(Card(CardType.KRAKEN)) # Add 1 kraken
        self.cards.append(Card(CardType.BALEINE)) # Add 1 baleine
        self.cards.append(Card(CardType.POISSON)) # Add 1 poisson

        # add 14 basic cards for each color
        for color in [CardColor.BLUE, CardColor.GREEN, CardColor.YELLOW, CardColor.BLACK]:
            for rank in range(1, 15):
                self.cards.append(Card(CardType.BASIC, color=color, rank=rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    
    def __str__(self) -> str:
        return ''.join([str(card) + ", " for card in self.cards])