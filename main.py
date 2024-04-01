from src.card_type import CardType, CardColor
from src.card  import Card
from src.player import Player, SmartPlayer
from src.game import Game
from src.stats_on_game import play_multiple_game

import pandas as pd

def main():
    # Create players
    players = [Player("Alice"), Player("Bob"), SmartPlayer("Charlie"), Player("David"), SmartPlayer("Eve"), Player("Frank")]
    
    # Initialize game
    game = Game(players)
    game.play_game(verbose=True)

    # Get the names of the players
    print(game.players_points)

if __name__ == "__main__":
    main()