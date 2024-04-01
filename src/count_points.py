from src.card import Card, CardType, CardColor
from src.card_interactions import find_winner_card


def occurence_of_card_type(cards_played: list[Card], card_type: CardType):
    """
    Count the number of occurence of a card type in the list of cards played
    
    Args:
        - cards_played (list[Card]): List of cards played by players
        - card_type (CardType): The card type to count
    
    Returns:
        - int: The number of occurence of the card type
    """
    return len([card for card in cards_played if card.type == card_type])

def count_points_of_trick(cards_played: list[Card]):
    """
    Count the points of the trick
    
    Args:
        - cards_played (list[Card]): List of cards played by players
    
    Returns:
    
    """
    winner_card = find_winner_card(cards_played)

    if not winner_card:
        return 0
    
    points = 0
    if winner_card.type == CardType.SKULLKING:
        points = 30 * occurence_of_card_type(cards_played, CardType.PIRATE)
    elif winner_card.type == CardType.PIRATE:
        points = 20 * occurence_of_card_type(cards_played, CardType.SIRENE)
    elif winner_card.type == CardType.SIRENE:
        points = 40 * occurence_of_card_type(cards_played, CardType.SKULLKING)

    for card in cards_played:
        points += card.points
    
    return  20 + points # Add 20 points per trick

def count_player_points_of_round(predicted_tricks: int, cards_played: list[list], current_round: int):
    """
    Count the points of the round
    
    Args:
        - players_current_tricks (dict): The number of tricks won by each player
        - current_round (int): The current round
    
    Returns:
        - dict: The points of each player for the round
    """
    current_tricks = len(cards_played) # The number of tricks won by the player
    if predicted_tricks != current_tricks:
        if predicted_tricks == 0: # If the player predicted 0 tricks, he loses 10 points per card
            return -10 * current_round 
        else: # If the player predicted a number of tricks, he loses 10 points per difference between the predicted and the actual number of tricks
            return -10 * abs(predicted_tricks - current_tricks)
    else:
        if current_tricks == 0:
            if cards_played != []:
                raise ValueError("If the player current 0 tricks, he should not have any card won")
            return 10 * current_round
        else:
            points = 0
            for card_played in cards_played:
                points += count_points_of_trick(card_played)
            return points




