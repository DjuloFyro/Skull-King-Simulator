from src.card import Card, CardColor, CardType

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
    elif first_card.type == CardType.PIECE: # If the first card is a Piece, the color is the color of the next card
        return find_color(cards_played[1:])
    else:
        return CardColor.NOCOLOR
    
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

def find_kraken_baleine_poisson(cards_played: list) -> Card:
    """
    Check if the round is won by a Kraken, Baleine or Poisson

    Args:
        - cards_played (list[Card]): List of cards played by players

    Returns:
        - Card: The card that won the round
    """
    # if kraken, baleine and poisson are played, th effect is the last card played
    for card in reversed(cards_played):
        if card in [Card(CardType.KRAKEN), Card(CardType.BALEINE), Card(CardType.POISSON)]:
            return card
    return None


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

    # check for kraken/baleine/poisson
    special_card = find_kraken_baleine_poisson(cards_played)
    if special_card:
        if special_card == Card(CardType.KRAKEN):
            return None
        if special_card == Card(CardType.BALEINE):
            return max(cards_played, key=lambda card: card.rank)
        if special_card == Card(CardType.POISSON):
            return min(cards_played, key=lambda card: card.rank if card.rank != 0 else float('inf')) # The winner is the player who played the lowest card

    # check for sirene/skullking/pirate
    if find_skullking_sirene_pirate(cards_played):
        return find_skullking_sirene_pirate(cards_played)
    
    if find_card_color(CardColor.BLACK, cards_played):
        return max([card for card in cards_played if card.color == CardColor.BLACK], key=lambda card: card.rank) # The winner is the player who played the highest black card
    
    if color_asked:
        return max([card for card in cards_played if card.color == color_asked], key=lambda card: card.rank) # The winner is the player who played the highest card of the color asked

    return None # No winner, should not happen

def play_next_card(cards_played: list[Card], player_hand: list[Card]) -> Card:
    """
    Choose the next card to play to try to win the trick

    Args:
        - cards_played (list[Card]): List of cards played by players in the trick
        - player_hand (list[Card]): List of cards in the player's hand

    Returns:
        - Card: The card to play next
    """
    # If it's the first turn, play the highest card in hand
    if len(cards_played) == 0:
        # if there is a pirate, play it
        pirate_card = [card for card in player_hand if card.type == CardType.PIRATE]
        if pirate_card:
            return pirate_card[0]
        else:
            return max(player_hand, key=lambda card: card.rank) # The player plays the highest card in hand

    # Determine the color asked in this trick
    color_asked = find_color(cards_played)

    # Check if the player has cards of the color asked
    if color_asked:
        playable_cards = [card for card in player_hand if card.color == color_asked]
        if playable_cards:
            return max(playable_cards, key=lambda card: card.rank)
        
    # if there is a balene played, play the highest card
    if Card(CardType.BALEINE) in cards_played:
        return max(player_hand, key=lambda card: card.rank)
    
    # if there is a kraken played, play the lowest card
    if Card(CardType.KRAKEN) in cards_played:
        return min(player_hand, key=lambda card: card.rank)
    
    # if there is a poisson played, play the lowest card
    if Card(CardType.POISSON) in cards_played:
        return min(player_hand, key=lambda card: card.rank)

    # if there is a pirate played and no siren, play skullking
    if Card(CardType.PIRATE) in cards_played and Card(CardType.SIRENE) not in cards_played:
        skullking_card = [card for card in player_hand if card.type == CardType.SKULLKING]
        if skullking_card:
            return skullking_card[0]
    
    # if there is a siren played and no skullking, play pirate
    if Card(CardType.SIRENE) in cards_played and Card(CardType.SKULLKING) not in cards_played:
        pirate_card = [card for card in player_hand if card.type == CardType.PIRATE]
        if pirate_card:
            return pirate_card[0]
        
    # if there is a skullking played, play sirene
    if Card(CardType.SKULLKING) in cards_played:
        sirene_card = [card for card in player_hand if card.type == CardType.SIRENE]
        if sirene_card:
            return sirene_card[0]
    
    # If the player has a black card, play the highest black card
    black_card = [card for card in player_hand if card.color == CardColor.BLACK]
    if black_card:
        return max(black_card, key=lambda card: card.rank)
    
    # Otherwise, play the highest card of another color pour se defausser de la plus petite carte
    return min(player_hand, key=lambda card: card.rank)

def play_next_card_to_loose(cards_played: list[Card], player_hand: list[Card]) -> Card:
    """
    Choose the next card to play to try to win the trick

    Args:
        - cards_played (list[Card]): List of cards played by players in the trick
        - player_hand (list[Card]): List of cards in the player's hand

    Returns:
        - Card: The card to play next
    """
    # If it's the first turn, play the highest card in hand
    if len(cards_played) == 0:
        # if there is a pirate, play it
        fuite_card = [card for card in player_hand if card.type == CardType.FUITE]
        if fuite_card:
            return fuite_card[0]
        piece_card = [card for card in player_hand if card.type == CardType.PIECE]
        if piece_card:
            return piece_card[0]
        return min(player_hand, key=lambda card: card.rank) # The player plays the highest card in hand

    # Determine the color asked in this trick
    color_asked = find_color(cards_played)

    # Check if the player has cards of the color asked
    if color_asked:
        playable_cards = [card for card in player_hand if card.color == color_asked]
        if playable_cards:
            return min(playable_cards, key=lambda card: card.rank)
        
    # if there is a balene played, play the highest card
    if Card(CardType.BALEINE) in cards_played:
        return min(player_hand, key=lambda card: card.rank)
    
    # if there is a kraken played, play the lowest card
    if Card(CardType.KRAKEN) in cards_played:
        return max(player_hand, key=lambda card: card.rank)
    
    # if there is a poisson played, play the lowest card
    if Card(CardType.POISSON) in cards_played:
        return max(player_hand, key=lambda card: card.rank)

    # if there is a pirate played, defaut pirates or sirene
    if Card(CardType.PIRATE) in cards_played:
        pirate_card = [card for card in player_hand if card.type == CardType.PIRATE]
        if pirate_card:
            return pirate_card[0]
        sirene_card = [card for card in player_hand if card.type == CardType.SIRENE]
        if sirene_card:
            return sirene_card[0]
    
    if Card(CardType.SIRENE) in cards_played:
        skullking_card = [card for card in player_hand if card.type == CardType.SKULLKING]
        if skullking_card:
            return skullking_card[0]
        sirene_card = [card for card in player_hand if card.type == CardType.SIRENE]
        if sirene_card:
            return sirene_card[0]
        
    # if there is a skullking played, play pirate
    if Card(CardType.SKULLKING) in cards_played:
        pirate_card = [card for card in player_hand if card.type == CardType.PIRATE]
        if pirate_card:
            return pirate_card[0]
    
    # if there is a siren or pirate or skullking played, play black
    if Card(CardType.SKULLKING) in cards_played or Card(CardType.PIRATE) in cards_played or Card(CardType.SIRENE) in cards_played:
        black_card = [card for card in player_hand if card.color == CardColor.BLACK]
        if black_card: # return max black card
            return max(black_card, key=lambda card: card.rank)
    
    # Otherwise, play the max card of another color pour se defausser de la plus haute carte
    return max(player_hand, key=lambda card: card.rank)