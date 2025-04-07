from unittest import TestCase
import random
from bayesian_poker.likelihood import compute_likelihood

class TestComputeLikelihood(TestCase):
    def test_full_hand_exact(self):
        # When partial_cards is a full hand (5 cards), the likelihood should be 1.0 if the hand type matches,
        # and 0.0 if it does not.
        straight_flush_hand = ['AH', 'KH', 'QH', 'JH', '10H']
        self.assertEqual(compute_likelihood(straight_flush_hand, "Straight Flush"), 1.0)
        self.assertEqual(compute_likelihood(straight_flush_hand, "Flush"), 0.0)

    def test_partial_hand_enumeration(self):
        # With 4 cards provided, exact enumeration is used
        # For a flush: if partial hand has 4 hearts, the probability is the fraction of hearts left.
        partial_hand = ['2H', '5H', '7H', '9H']  # 4 hearts

        expected_prob = 9 / 48
        result = compute_likelihood(partial_hand, "Flush")
        self.assertAlmostEqual(result, expected_prob, places=4)

    def test_invalid_partial_cards(self):
        # More than 5 cards should raise a ValueError.
        with self.assertRaises(ValueError):
            compute_likelihood(['AH', 'KH', 'QH', 'JH', '10H', '9H'], "Straight Flush")

    def test_partial_hand_monte_carlo(self):
        # Using a 1-card partial hand forces the Monte Carlo sampling branch.
        partial_hand = ['AH']  # Only one card given.
        # Fixing the random seed to ensure reproducible results.
        random.seed(42)
        result = compute_likelihood(partial_hand, "High Card", num_samples=1000)
        # The result should be a float between 0 and 1.
        self.assertTrue(0.0 <= result <= 1.0)

if __name__ == '__main__':
    import unittest
    unittest.main()
