from src.deck import Deck
from src.card_interactions import find_winner_card
from src.count_points import count_player_points_of_round

class Game:
    def __init__(self, players, max_round: int = 8, with_poisson: bool = True):
        self.deck = Deck(with_poisson=with_poisson)
        self.players = players

        self.players_predicted_tricks = {}
        self.round_history_winner = {current_round: {player.name: [] for player in players} for current_round in range(1, max_round + 1)}
        self.players_points = {player.name: 0 for player in players}
        self.current_round = 1
        self.max_round = max_round

    def deal_cards(self):
        """
        Shuffle card and deal cards to players

        Args:
            - verbose (bool): Print the cards in the deck

        Returns:
            - None
        """
        # We update the starting player index at each round
        starting_player_index = (self.current_round - 1) % len(self.players)

        self.deck.shuffle()
        for _ in range(self.current_round):
            for i, player in enumerate(self.players):
                player_index = (starting_player_index + i) % len(self.players)
                self.players[player_index].add_card(self.deck.deal())

    def player_guess_tricks(self):
        self.players_predicted_tricks[self.current_round] = {}
        for player in self.players:
            self.players_predicted_tricks[self.current_round][player.name] = player.guess_tricks()
     
    def play_round(self, verbose: bool = False):
        # We update the starting player index at each round
        starting_player_index = (self.current_round - 1) % len(self.players)

        for _ in range(self.current_round): # Play the number of cards corresponding to the round
            cards_played = []
            for i, player in enumerate(self.players):
                player_index = (starting_player_index + i) % len(self.players)
                
                is_want_to_win_trick = self.players_predicted_tricks[self.current_round][self.players[player_index].name] != len(self.round_history_winner[self.current_round][self.players[player_index].name])
                card = self.players[player_index].play_card(cards_played, is_want_to_win=is_want_to_win_trick)
                if card:
                    cards_played.append(card)
                if verbose:
                    print(f"{self.players[player_index].name} plays for round {self.current_round} with {card}")
            # Find the winner of the round
            winner_card = find_winner_card(cards_played)
            if winner_card:
                winner_idx = cards_played.index(winner_card)
                winner = self.players[(starting_player_index + winner_idx) % len(self.players)]
                self.round_history_winner[self.current_round][winner.name] += [cards_played]
                starting_player_index = (starting_player_index + winner_idx) % len(self.players) # the winner starts the next round
                if verbose:
                    print(f"{winner.name} won the round with {winner_card}")

        if verbose:
            print(f"End of round {self.current_round}\n")
        self.deck = Deck() # Reset the deck
        self.current_round += 1 # Increment the round
    
    def count_points(self):
        """
        Count the points of the players

        Args:
            - None

        Returns:
            - dict: A dictionary with the points of each player
        """
        for round_nb, (predicted_tricks, cards_from_trick_won) in enumerate(zip(self.players_predicted_tricks.values(), self.round_history_winner.values())):
            for player in self.players:
                # cards_from_trick_won[player.name] is a list of list representing the tricks won by the player
                player_point = count_player_points_of_round(predicted_tricks[player.name], cards_from_trick_won[player.name], round_nb + 1)
                self.players_points[player.name] += player_point
    
    def play_game(self, verbose: bool = False):
        """
        Play the game

        Args:
            - None

        Returns:
            - None
        """
        for current_round in range(self.max_round):
            self.deal_cards()
            self.player_guess_tricks()
            self.play_round(verbose=verbose)
        self.count_points()

