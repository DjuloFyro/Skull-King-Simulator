import pytest
from src.card_interactions import CardType, CardColor
from src.card import Card
from src.count_points import occurence_of_card_type, count_points_of_trick, count_player_points_of_round

# Helper function to create cards for testing
def create_cards(cards_info):
    return [Card(*info) for info in cards_info]

def test_occurence_of_card():

    # Test with 2 pirates
    cards_played = create_cards([(CardType.PIRATE, CardColor.NOCOLOR, 0), (CardType.SIRENE, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])
    assert occurence_of_card_type(cards_played, CardType.PIRATE) == 2

    # Test with SKUllKING
    cards_played = create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.BLUE, 3)])
    assert occurence_of_card_type(cards_played, CardType.SKULLKING) == 1

    # Test with 3 sirenes
    cards_played = create_cards([(CardType.SIRENE, CardColor.NOCOLOR, 0), (CardType.SIRENE, CardColor.NOCOLOR, 0), (CardType.SIRENE, CardColor.NOCOLOR, 0)])
    assert occurence_of_card_type(cards_played, CardType.SIRENE) == 3


def test_count_points_of_trick():

    # Test with a skullking card
    cards_played = create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.GREEN, 4)])
    assert count_points_of_trick(cards_played) == 20

    # Test with a 2 sirene card
    cards_played = create_cards([(CardType.SIRENE, CardColor.NOCOLOR, 0), (CardType.SIRENE, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])
    assert count_points_of_trick(cards_played) == 60

    # Test with a basic black card
    cards_played = create_cards([(CardType.BASIC, CardColor.BLUE, 14), (CardType.BASIC, CardColor.BLACK, 14)])
    assert count_points_of_trick(cards_played) == 50

    # Test with a basic card
    cards_played = create_cards([(CardType.BASIC, CardColor.BLUE, 14), (CardType.BASIC, CardColor.GREEN, 14), (CardType.BASIC, CardColor.YELLOW, 14)])
    assert count_points_of_trick(cards_played) == 50

    # Test with piece
    cards_played = create_cards([(CardType.PIECE, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.GREEN, 14), (CardType.BASIC, CardColor.YELLOW, 5)])
    assert count_points_of_trick(cards_played) == 50

    # big trick
    cards_played = create_cards([(CardType.BASIC, CardColor.BLUE, 14), (CardType.BASIC, CardColor.GREEN, 14),
                                 (CardType.BASIC, CardColor.BLACK, 14), (CardType.SIRENE, CardColor.NOCOLOR, 0),
                                 (CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])
    assert count_points_of_trick(cards_played) == 100


def test_count_player_points_of_round():

    # Case won one trick
    cards_played = [create_cards([(CardType.BASIC, CardColor.BLUE, 3), (CardType.BASIC, CardColor.GREEN, 2)])]
    assert count_player_points_of_round(1, cards_played, 1) == 20

    # Case won multiple tricks
    cards_played =([create_cards([(CardType.BASIC, CardColor.BLUE, 14), (CardType.BASIC, CardColor.GREEN, 14)])]
                    + [create_cards([(CardType.BASIC, CardColor.BLACK, 14), (CardType.SIRENE, CardColor.NOCOLOR, 0)])]
                    + [create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])]
    )
    assert count_player_points_of_round(3, cards_played, 3) == 60 + 20 + 20 + 30

    # Case won by saying 0 tricks
    assert count_player_points_of_round(0, [], 3) == 30

    # Case lost by saying 0 tricks and win 3 tricks
    cards_played = ([create_cards([(CardType.BASIC, CardColor.BLUE, 14), (CardType.BASIC, CardColor.GREEN, 14)])]
                    + [create_cards([(CardType.BASIC, CardColor.BLACK, 14), (CardType.SIRENE, CardColor.NOCOLOR, 0)])]
                    + [create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])]
    )
    assert count_player_points_of_round(0, cards_played, 3) == -30

    # Case lost by saying 0 tricks and win 1 tricks
    cards_played = [create_cards([(CardType.BASIC, CardColor.BLUE, 14), (CardType.BASIC, CardColor.GREEN, 14)])]
    assert count_player_points_of_round(0, cards_played, 3) == -30

    # Case lost by saying 2 trick and win 1 trick
    cards_played = [create_cards([(CardType.BASIC, CardColor.BLUE, 14), (CardType.BASIC, CardColor.GREEN, 14)])]
    assert count_player_points_of_round(2, cards_played, 3) == -10

    # Case lost by saying 4 trick and win 2 trick
    cards_played = ([create_cards([(CardType.BASIC, CardColor.BLUE, 14), (CardType.BASIC, CardColor.GREEN, 14)])]
                    + [create_cards([(CardType.BASIC, CardColor.BLACK, 14), (CardType.SIRENE, CardColor.NOCOLOR, 0)])]
    )
    
    assert count_player_points_of_round(4, cards_played, 4) == -20



    
