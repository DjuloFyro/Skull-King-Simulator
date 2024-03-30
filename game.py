from deck import Deck
from card_interactions import find_winner_card

class Game:
    def __init__(self, players, max_round: int = 8):
        self.deck = Deck()
        self.players = players
        self.current_round = 1
        self.max_round = 8

    def deal_cards(self):
        """
        Shuffle card and deal cards to players

        Args:
            - verbose (bool): Print the cards in the deck

        Returns:
            - None
        """
        self.deck.shuffle()
        for _ in range(self.current_round):
            for player in self.players:
                player.add_card(self.deck.deal())
    
    def play_round(self):
        print(f"\nRound {self.current_round}:")
        cards_played = []

        for player in self.players:
            card = player.play_card()
            if card:
                cards_played.append(card)
                print(f"{player.name} played {card}")
            else:
                print(f"{player.name} has no card left")

        # Find the winner of the round
        winner_card = find_winner_card(cards_played)
        winner = self.players[cards_played.index(winner_card)]

        print(f"{winner.name} won the round with {winner_card}")
        self.current_round += 1

    
    def play_game(self):
        """
        Play the game

        Args:
            - None

        Returns:
            - None
        """
        for _ in range(self.max_round):
            self.deal_cards()
            self.play_round()
