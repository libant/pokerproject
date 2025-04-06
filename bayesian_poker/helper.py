from math import comb as math_comb

def get_deck():
    """
    Generates and returns a standard 52-card deck.
    Cards are represented as strings, e.g., 'AH', '10S', '3D'.
    Ranks: 2-10, J, Q, K, A
    Suits: Hearts (H), Diamonds (D), Clubs (C), Spades (S)
    """
    suits = ['H', 'D', 'C', 'S']
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    deck = [rank + suit for suit in suits for rank in ranks]
    return deck

def comb(n, k):
    """
    A helper wrapper around math.comb for clarity.
    """
    return math_comb(n, k)
