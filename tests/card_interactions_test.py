import pytest
from ..card_interactions import CardType, CardColor
from ..card import Card
from ..player import Player
from ..card_interactions import find_color, find_skullking_sirene_pirate, find_card_color, find_winner_card

# Helper function to create cards for testing
def create_cards(cards_info):
    return [Card(*info) for info in cards_info]

def test_find_color():
    cards_played = create_cards([(CardType.BASIC, CardColor.RED), (CardType.BASIC, CardColor.GREEN)])
    assert find_color(cards_played) == CardColor.RED

    cards_played = create_cards([(CardType.FUITE, CardColor.RED), (CardType.BASIC, CardColor.BLUE)])
    assert find_color(cards_played) == CardColor.BLUE

    assert find_color([]) is None

def test_find_skullking_sirene_pirate():
    cards_played = create_cards([(CardType.SKULLKING, CardColor.RED), (CardType.BASIC, CardColor.GREEN)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[0]

    cards_played = create_cards([(CardType.SIRENE, CardColor.RED), (CardType.BASIC, CardColor.GREEN)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[0]

    cards_played = create_cards([(CardType.PIRATE, CardColor.RED), (CardType.BASIC, CardColor.GREEN)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[0]

    cards_played = create_cards([(CardType.SKULLKING, CardColor.RED), (CardType.SIRENE, CardColor.GREEN), (CardType.PIRATE, CardColor.BLUE)])
    assert find_skullking_sirene_pirate(cards_played) == cards_played[1]

    assert find_skullking_sirene_pirate([]) is None

def test_find_card_color():
    cards_played = create_cards([(CardType.BASIC, CardColor.RED), (CardType.BASIC, CardColor.GREEN)])
    assert find_card_color(CardColor.RED, cards_played) is True
    assert find_card_color(CardColor.BLUE, cards_played) is False

def test_find_winner_card():
    cards_played = create_cards([(CardType.SKULLKING, CardColor.RED), (CardType.BASIC, CardColor.GREEN)])
    assert find_winner_card(cards_played) == cards_played[0]

    cards_played = create_cards([(CardType.BALEINE, CardColor.RED), (CardType.BASIC, CardColor.GREEN)])
    assert find_winner_card(cards_played) == cards_played[0]

    cards_played = create_cards([(CardType.POISSON, CardColor.RED), (CardType.BASIC, CardColor.GREEN)])
    assert find_winner_card(cards_played) == cards_played[1]

    cards_played = create_cards([(CardType.BASIC, CardColor.RED), (CardType.BASIC, CardColor.GREEN)])
    assert find_winner_card(cards_played) == cards_played[0]

    cards_played = create_cards([(CardType.SKULLKING, CardColor.RED), (CardType.SIRENE, CardColor.GREEN), (CardType.PIRATE, CardColor.BLUE)])
    assert find_winner_card(cards_played) == cards_played[1]

    cards_played = create_cards([(CardType.BASIC, CardColor.BLACK), (CardType.BASIC, CardColor.BLACK)])
    assert find_winner_card(cards_played) == cards_played[0]

    cards_played = create_cards([(CardType.BASIC, CardColor.RED), (CardType.BASIC, CardColor.GREEN)])
    assert find_winner_card(cards_played) == cards_played[0]

    assert find_winner_card([]) is None

