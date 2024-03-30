from card_type import CardType, CardColor
from card  import Card
from player import Player
from game import Game


def main():
    # Create players
    players = [Player("Player 1"), Player("Player 2")]
    
    # Initialize game
    game = Game(players)
    
    # Deal cards
    game.deal_cards(1, verbose=True)
    
    # Play rounds (example: 5 rounds)
    for _ in range(1):
        game.play_turn()

if __name__ == "__main__":
    main()
