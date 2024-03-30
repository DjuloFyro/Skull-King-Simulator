from card_type import CardType, CardColor
from card  import Card
from player import Player
from game import Game


def main():
    # Create players
    players = [Player("Player 1"), Player("Player 2")]
    
    # Initialize game
    game = Game(players)

    
    game.play_game()
    

if __name__ == "__main__":
    main()
    #l = [Card(CardType.BASIC, CardColor.BLUE, 1), Card(CardType.BASIC, CardColor.BLACK, 2), Card(CardType.KRAKEN)]
    #print(Card(CardType.Black) in l)