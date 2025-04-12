from unittest import TestCase
from bayesian_poker.helper import get_deck, comb
import math

class TestGetDeck(TestCase):
    def test_get_deck(self):
        deck = get_deck()
        # Ensure the deck has 52 cards
        self.assertEqual(len(deck), 52, "Deck should have 52 cards")
        # Check that all cards are unique
        self.assertEqual(len(set(deck)), 52, "All cards in the deck should be unique")

        # Verify that all four suits are present
        suits = {card[-1] for card in deck}
        self.assertEqual(suits, {"H", "D", "C", "S"}, "Deck must contain all four suits")

        # Check that each rank appears exactly 4 times (one per suit)
        ranks = [card[:-1] for card in deck]
        for rank in set(ranks):
            self.assertEqual(ranks.count(rank), 4, f"Rank {rank} should appear 4 times in the deck")

class TestComb(TestCase):
    def test_comb(self):
        # Test some known combinations
        self.assertEqual(comb(4, 2), math.comb(4, 2), "comb(4, 2) should equal math.comb(4, 2)")
        self.assertEqual(comb(10, 5), math.comb(10, 5), "comb(10, 5) should equal math.comb(10, 5)")
        self.assertEqual(comb(5, 0), math.comb(5, 0), "comb(5, 0) should equal math.comb(5, 0)")
        self.assertEqual(comb(5, 5), math.comb(5, 5), "comb(5, 5) should equal math.comb(5, 5)")
        # Test a bigger example
        self.assertEqual(comb(52, 5), math.comb(52, 5), "comb(52, 5) should equal math.comb(52, 5)")

if __name__ == '__main__':
    import unittest
    unittest.main()
