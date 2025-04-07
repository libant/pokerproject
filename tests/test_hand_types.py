from unittest import TestCase
from bayesian_poker.hand_types import get_rank, get_suit, is_flush, is_straight, classify_hand

class TestGetRank(TestCase):
    def test_get_rank(self):
        # Test Ace, face cards, and numeric cards
        self.assertEqual(get_rank('AH'), 14)
        self.assertEqual(get_rank('KH'), 13)
        self.assertEqual(get_rank('QH'), 12)
        self.assertEqual(get_rank('JH'), 11)
        self.assertEqual(get_rank('10S'), 10)
        self.assertEqual(get_rank('2D'), 2)

class TestGetSuit(TestCase):
    def test_get_suit(self):
        # Test suit extraction from different cards
        self.assertEqual(get_suit('AH'), 'H')
        self.assertEqual(get_suit('10S'), 'S')
        self.assertEqual(get_suit('2D'), 'D')
        self.assertEqual(get_suit('JH'), 'H')
        self.assertEqual(get_suit('QC'), 'C')
        self.assertEqual(get_suit('KD'), 'D')

class TestIsFlush(TestCase):
    def test_is_flush(self):
        # A flush: all cards have the same suit
        flush_hand = ['AH', 'KH', 'QH', 'JH', '10H']
        self.assertTrue(is_flush(flush_hand))

        # Not a flush: at least one card has a different suit
        non_flush = ['AH', 'KH', 'QH', 'JH', '10D']
        self.assertFalse(is_flush(non_flush))

class TestIsStraight(TestCase):
    def test_is_straight(self):
        # A standard straight
        straight_hand = ['2H', '3D', '4S', '5C', '6H']
        self.assertTrue(is_straight(straight_hand))

        # Not a straight
        not_straight = ['2H', '3D', '4S', '6C', '7H']
        self.assertFalse(is_straight(not_straight))

class TestClassifyHand(TestCase):
    def test_classify_hand(self):
        # Straight Flush
        sf = ['AH', 'KH', 'QH', 'JH', '10H']
        self.assertEqual(classify_hand(sf), "Straight Flush")

        # Four of a Kind: four 9s and a King
        four_kind = ['9H', '9D', '9C', '9S', 'KH']
        self.assertEqual(classify_hand(four_kind), "Four of a Kind")

        # Full House: three Aces and two Kings
        full_house = ['AH', 'AD', 'AC', 'KH', 'KD']
        self.assertEqual(classify_hand(full_house), "Full House")

        # Flush: all cards are hearts but not in sequence
        flush = ['2H', '5H', '7H', '9H', 'KH']
        self.assertEqual(classify_hand(flush), "Flush")

        # Straight: sequential cards, not all same suit
        straight = ['2H', '3D', '4S', '5C', '6H']
        self.assertEqual(classify_hand(straight), "Straight")

        # Three of a Kind: three Aces and two unrelated cards
        three_kind = ['AH', 'AD', 'AC', 'KH', 'QD']
        self.assertEqual(classify_hand(three_kind), "Three of a Kind")

        # Two Pair: two Aces, two Kings, and a Queen
        two_pair = ['AH', 'AD', 'KH', 'KD', 'QD']
        self.assertEqual(classify_hand(two_pair), "Two Pair")

        # One Pair: two Aces and three unrelated cards
        one_pair = ['AH', 'AD', 'KH', 'QD', 'JD']
        self.assertEqual(classify_hand(one_pair), "One Pair")

        # High Card: no combination, the highest card is the King
        high_card = ['2H', '5D', '7S', '9C', 'KD']
        self.assertEqual(classify_hand(high_card), "High Card")

if __name__ == '__main__':
    import unittest
    unittest.main()

