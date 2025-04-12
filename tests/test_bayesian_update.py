from unittest import TestCase
from bayesian_poker.bayesian_update import bayesian_update


class TestBayesianUpdate(TestCase):
    def test_bayesian_update_normal(self):
        # Test with a simple two-hypothesis scenario.
        # Priors for two hypothetical hand types "A" and "B"
        priors = {"A": 0.5, "B": 0.5}
        # Likelihoods: Suppose evidence favors "B" more than "A"
        likelihoods = {"A": 0.2, "B": 0.8}

        expected = {"A": 0.2, "B": 0.8}

        result = bayesian_update(priors, likelihoods)
        self.assertAlmostEqual(result["A"], expected["A"])
        self.assertAlmostEqual(result["B"], expected["B"])

    def test_bayesian_update_zero_evidence(self):
        # Test that a ValueError is raised when total evidence is zero.
        priors = {"A": 0.5, "B": 0.5}
        likelihoods = {"A": 0, "B": 0}

        with self.assertRaises(ValueError):
            bayesian_update(priors, likelihoods)

if __name__ == "__main__":
    import unittest
    unittest.main()
