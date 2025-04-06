from collections import Counter

def get_rank(card):
    """
    Extracts and returns the numeric rank from a card string.
    Assumes cards are strings like 'AH', '10S', '3D', etc.
    """
    rank = card[:-1]
    if rank == 'A':
        return 14
    elif rank == 'K':
        return 13
    elif rank == 'Q':
        return 12
    elif rank == 'J':
        return 11
    else:
        return int(rank)

def get_suit(card):
    """
    Returns the suit character from a card string.
    """
    return card[-1]

def is_flush(cards):
    """
    Checks if all cards have the same suit.
    """
    suits = [get_suit(card) for card in cards]
    return len(set(suits)) == 1

def is_straight(cards):
    """
    Checks if the hand is a straight.
    Accounts for Ace-low straights (A,2,3,4,5).
    """
    ranks = sorted(get_rank(card) for card in cards)
    # Check for Ace-low straight
    if ranks == [2, 3, 4, 5, 14]:
        return True
    for i in range(len(ranks) - 1):
        if ranks[i + 1] - ranks[i] != 1:
            return False
    return True

def classify_hand(cards):
    """
    Given a list of 5 cards, classify the poker hand type.
    Returns a string representing the hand type.
    """
    ranks = [get_rank(card) for card in cards]
    rank_counts = Counter(ranks)
    counts = sorted(rank_counts.values(), reverse=True)

    if is_straight(cards) and is_flush(cards):
        return "Straight Flush"
    if counts[0] == 4:
        return "Four of a Kind"
    if counts[0] == 3 and counts[1] == 2:
        return "Full House"
    if is_flush(cards):
        return "Flush"
    if is_straight(cards):
        return "Straight"
    if counts[0] == 3:
        return "Three of a Kind"
    if counts[0] == 2 and counts[1] == 2:
        return "Two Pair"
    if counts[0] == 2:
        return "One Pair"
    return "High Card"

