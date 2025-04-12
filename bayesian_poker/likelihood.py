import itertools
import random
from math import comb
from bayesian_poker.hand_types import classify_hand
from bayesian_poker.helper import get_deck

def compute_likelihood(partial_cards, hand_type, num_samples=10000):
    """
    Computes the likelihood of achieving a given hand_type given a list of partial_cards.

    If the number of unknown cards (5 - len(partial_cards)) is small enough,
    it enumerates all completions. Otherwise, it uses Monte Carlo sampling.

    Parameters:
      partial_cards: list of known card strings (e.g., ['AH', '10D'])
      hand_type: string representing the desired hand type (e.g., "Flush")
      num_samples: number of samples for Monte Carlo simulation (default 10,000)

    Returns:
      A float representing the probability (likelihood) of obtaining the hand_type.
    """
    deck = get_deck()
    # Remove known cards from deck
    remaining_deck = [card for card in deck if card not in partial_cards]
    num_missing = 5 - len(partial_cards)

    if num_missing < 0:
        raise ValueError("More than 5 cards provided.")

    total_possible = comb(len(remaining_deck), num_missing)

    # Use exact enumeration when possible
    if total_possible <= num_samples:
        total = 0
        favorable = 0
        for combo in itertools.combinations(remaining_deck, num_missing):
            hand = partial_cards + list(combo)
            total += 1
            if classify_hand(hand) == hand_type:
                favorable += 1
        return favorable / total if total > 0 else 0
    else:
        # Use Monte Carlo sampling
        favorable = 0
        for _ in range(num_samples):
            sample = random.sample(remaining_deck, num_missing)
            hand = partial_cards + sample
            if classify_hand(hand) == hand_type:
                favorable += 1
        return favorable / num_samples
