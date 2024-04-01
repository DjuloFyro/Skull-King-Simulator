import pytest
from src.card_interactions import CardType, CardColor
from src.card import Card
from src.player import Player
from src.card_interactions import find_color, find_skullking_sirene_pirate, find_card_color, find_winner_card

# Helper function to create cards for testing
def create_cards(cards_info):
    return [Card(*info) for info in cards_info]

def test_find_color():

    # Test with a basic card
    cards_played = create_cards([(CardType.BASIC, CardColor.BLUE, 3), (CardType.BASIC, CardColor.GREEN, 3)])
    assert find_color(cards_played) == CardColor.BLUE

    # Test with a fuite card
    cards_played = create_cards([(CardType.FUITE, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.BLUE, 3)])
    assert find_color(cards_played) == CardColor.BLUE

    # Test 3 fuite cards
    cards_played = create_cards([(CardType.FUITE, CardColor.NOCOLOR, 0), (CardType.FUITE, CardColor.NOCOLOR, 0), (CardType.FUITE, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.BLUE, 3)])
    assert find_color(cards_played) == CardColor.BLUE

    # Test with a skullking card
    cards_played = create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.BLUE, 3)])
    assert find_color(cards_played) is CardColor.NOCOLOR

    # Piece played first
    cards_played = create_cards([(CardType.PIECE, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.GREEN, 14), (CardType.BASIC, CardColor.YELLOW, 5)])
    assert find_color(cards_played) == CardColor.GREEN

    assert find_color([]) is None

def test_find_skullking_sirene_pirate():

    # Test with a skullking card
    cards_played = create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.GREEN, 4)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[0]

    # Test with a sirene card
    cards_played = create_cards([(CardType.SIRENE, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.GREEN, 4)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[0]

    # Test with a pirate card
    cards_played = create_cards([(CardType.PIRATE, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.GREEN, 5)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[0]

    # Test with a skullking, sirene and pirate card
    cards_played = create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.SIRENE, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[1]

    # Test with a skullking and sirene card
    cards_played = create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.SIRENE, CardColor.NOCOLOR, 0)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[1]

    # Test with a skullking and pirate card
    cards_played = create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[0]

    # Test with a sirene and pirate card
    cards_played = create_cards([(CardType.SIRENE, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[1]

    # Test with a skullking, sirene and pirate card BUT the sirene is played first
    cards_played = create_cards([(CardType.SIRENE, CardColor.NOCOLOR, 0), (CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[0]

    # Test with 3 pirates
    cards_played = create_cards([(CardType.PIRATE, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[0]

    assert find_skullking_sirene_pirate([]) is None

def test_find_card_color():
    cards_played = create_cards([(CardType.BASIC, CardColor.BLACK, 3), (CardType.BASIC, CardColor.GREEN, 5)])
    assert find_card_color(CardColor.BLACK, cards_played) is True
    assert find_card_color(CardColor.BLUE, cards_played) is False

def test_find_winner_card():
    cards_played = create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.GREEN, 5)])
    assert find_winner_card(cards_played) == cards_played[0]

    # Test with baleine
    cards_played = create_cards([(CardType.BALEINE, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.GREEN, 5), (CardType.BASIC, CardColor.BLACK, 2)])
    assert find_winner_card(cards_played) == cards_played[1]

    # Test with poisson
    cards_played = create_cards([(CardType.POISSON, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.GREEN, 5), (CardType.BASIC, CardColor.GREEN,13)])
    assert find_winner_card(cards_played) == cards_played[1]

    cards_played = create_cards([(CardType.BASIC, CardColor.BLACK, 5), (CardType.BASIC, CardColor.GREEN, 13)])
    assert find_winner_card(cards_played) == cards_played[0]

    cards_played = create_cards([(CardType.SKULLKING, CardColor.NOCOLOR, 0), (CardType.SIRENE, CardColor.NOCOLOR, 0), (CardType.PIRATE, CardColor.NOCOLOR, 0)])
    assert find_winner_card(cards_played) == cards_played[1]

    cards_played = create_cards([(CardType.BASIC, CardColor.BLACK, 2), (CardType.BASIC, CardColor.BLACK, 14)])
    assert find_winner_card(cards_played) == cards_played[1]

    # Piece played first
    cards_played = create_cards([(CardType.PIECE, CardColor.NOCOLOR, 0), (CardType.BASIC, CardColor.GREEN, 14), (CardType.BASIC, CardColor.YELLOW, 5)])
    print(find_winner_card(cards_played))
    assert find_winner_card(cards_played) == cards_played[1]

    assert find_winner_card([]) is None

