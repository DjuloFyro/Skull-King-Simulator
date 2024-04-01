from src.card import Card, CardColor, CardType
from src.count_points import occurence_of_card_type
from src.card_interactions import play_next_card, play_next_card_to_loose

import random

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []

    def add_card(self, card: Card):
        self.hand.append(card)

    def play_card(self, cards_played: list[Card], is_want_to_win: bool = False):
        if len(self.hand) > 0:
            return self.hand.pop()
        else:
            return None
        
    def guess_tricks(self):
        # random between 0 and number of cards in hand
        return random.randint(0, len(self.hand) + 1)
    
class SmartPlayer(Player):
    """
    A smart player that will try to win the trick and will choose the number of tricks to win based on the number of strong cards in hand
    """

    def play_card(self, cards_played: list[Card], is_want_to_win: bool = False):
        if len(self.hand) > 0:
            if is_want_to_win:
                card_to_play = play_next_card(cards_played, self.hand)
                self.hand.remove(card_to_play)
            else:
                # TODO: Want to loose 
                #card_to_play = self.hand.pop()
                card_to_play = play_next_card_to_loose(cards_played, self.hand)
        else:
            card_to_play = None
        return card_to_play
    
    def guess_tricks(self):
        nb_pirates = occurence_of_card_type(self.hand, CardType.PIRATE)
        nb_sirene = occurence_of_card_type(self.hand, CardType.SIRENE)
        nb_skullking = occurence_of_card_type(self.hand, CardType.SKULLKING)

        # COUNT NUMBER OF CARTE >= 12 OF RANK
        nb_strong_card = 0
        for card in self.hand:
            if card.rank >= 11:
                nb_strong_card += 1

        return nb_pirates + nb_sirene + nb_skullking + nb_strong_card
    
class RandomTrickPlayer(Player):
    """
    A smart player that will try to win the trick.
    But will choose a random number of tricks
    """
    def play_card(self, cards_played: list[Card], is_want_to_win: bool = False):
        if len(self.hand) > 0:
            if is_want_to_win:
                card_to_play = play_next_card(cards_played, self.hand)
                self.hand.remove(card_to_play)
            else:
                # TODO: Want to loose 
                #card_to_play = self.hand.pop()
                card_to_play = play_next_card_to_loose(cards_played, self.hand)
        else:
            card_to_play = None
        return card_to_play
    
    def guess_tricks(self):
        return random.randint(0, len(self.hand) + 1)


