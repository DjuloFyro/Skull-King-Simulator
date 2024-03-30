from deck import Deck

class Game:
    def __init__(self, players):
        self.deck = Deck()
        self.players = players

    def deal_cards(self, turn: int = 1, verbose : bool = False):
        """
        Shuffle card and deal cards to players

        Args:
            - turn (int): Number of turn to deal cards
            - verbose (bool): Print the cards in the deck

        Returns:
            - None
        """
        self.deck.shuffle()
        if verbose:
            print("Cards in deck: ", self.deck)
        for _ in range(turn):
            for player in self.players:
                player.add_card(self.deck.deal())
    
    def play_turn(self):
        for player in self.players:
            print(f"{player.name} played {player.play_card()}")
