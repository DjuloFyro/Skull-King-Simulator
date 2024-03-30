from card_type import CardType, CardColor
from card import Card
from player import Player

def find_color(cards_played: list[Card]) -> CardColor:
    """
    Find the color of the round

    Args:
        - cards_played (list): List of cards played by players

    Returns:
        - CardColor: The color of the round
    """
    if len(cards_played) == 0:
        return None
    
    first_card = cards_played[0]
    if first_card.type == CardType.BASIC:
        return first_card.color
    elif first_card.type == CardType.FUITE:
        return find_color(cards_played[1:]) # If the first card is a Fuite, the color is the color of the next card
    else:
        return None
    
def find_skullking_sirene_pirate(cards_played: list) -> Card:
    """
    Check if the round is won by a Skullking, Sirene or Pirate

    Args:
        - cards_played (list[Card]): List of cards played by players

    Returns:
        - Card: The card that won the round
    """
    if Card(CardType.SKULLKING) in cards_played and Card(CardType.SIRENE) not in cards_played: # if Skullking is played but not Sirene
        return [card for card in cards_played if card == Card(CardType.SKULLKING)][0] # the skullking wins
    if Card(CardType.SIRENE) in cards_played and Card(CardType.PIRATE) not in cards_played: # if Sirene is played but not Pirate
        return [card for card in cards_played if card == Card(CardType.SIRENE)][0] # the sirene wins
    if Card(CardType.PIRATE) in cards_played and Card(CardType.SKULLKING) not in cards_played: # if Pirate is played but not Skullking
        return [card for card in cards_played if card == Card(CardType.PIRATE)][0] # the pirate wins
    
     # if Skullking and Sirene and Pirate are played, the winner is the player who played Sirene
    if Card(CardType.SKULLKING) in cards_played and Card(CardType.SIRENE) in cards_played and Card(CardType.PIRATE) in cards_played:
        return [card for card in cards_played if card == Card(CardType.SIRENE)][0]
    
    return None # No Skullking, Sirene or Pirate played

def find_card_color(color: CardColor, cards_played: list[Card]) -> bool:
    """
    Check if a card of a specific color is played

    Args:
        - color (CardColor): The color to check
        - cards_played (list[Card]): List of cards played by players

    Returns:
        - bool: True if a card of the color is played, False otherwise
    """
    return any([card.color == color for card in cards_played])

def find_winner_card(cards_played: list[Card]) -> Card:
    """
    Find the winner of the round

    Args:
        - cards_played (list): List of cards played by players

    Returns:
        - Card: The card that won the round
    """
    color_asked = find_color(cards_played)

    if Card(CardType.KRAKEN) in cards_played:
        return None # No winner
    if Card(CardType.BALEINE) in cards_played:
        return max(cards_played, key=lambda card: card.rank) # The winner is the player who played the highest card
    if Card(CardType.POISSON) in cards_played:
        return min(cards_played, key=lambda card: card.rank) # The winner is the player who played the lowest card

    # check for sirene/skullking/pirate
    if find_skullking_sirene_pirate(cards_played):
        return find_skullking_sirene_pirate(cards_played)
    
    if find_card_color(CardColor.BLACK, cards_played):
        return max([card for card in cards_played if card.color == CardColor.BLACK], key=lambda card: card.rank) # The winner is the player who played the highest black card
    
    if color_asked:
        return max([card for card in cards_played if card.color == color_asked], key=lambda card: card.rank) # The winner is the player who played the highest card of the color asked

    return None # No winner, should not happen
