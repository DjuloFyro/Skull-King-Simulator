from src.game import Game
from src.player import Player

import pandas as pd

def play_multiple_game(players: Player, n_games: int=10, max_round: int=8, with_poisson: bool=True):
    """
    Play multiple games and return the stats of each game
    
    Args:
        - players (list[Player]): List of players
        - n_games (int): Number of games to play
    
    Returns:
        - list: List of the stats of each game
    """
    games_stats = []
    for _ in range(n_games):
        game = Game(players, max_round=max_round, with_poisson=with_poisson)
        game.play_game()

        games_stats.append(game.players_points)

    players_names = [player.name for player in players]
    stats_df = pd.DataFrame(games_stats, columns=players_names)

    return stats_df