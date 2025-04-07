from unittest import TestCase
import matplotlib.pyplot as plt
from bayesian_poker.visualization import plot_posteriors

class TestPlotPosteriors(TestCase):
    def test_plot_posteriors(self):
        # Sample posterior probabilities dictionary.
        posteriors = {"Flush": 0.3, "Straight": 0.2, "High Card": 0.5}

        # Override plt.show() to prevent displaying the plot during tests.
        original_show = plt.show
        plt.show = lambda: None

        try:
            # Call the function to generate the plot.
            plot_posteriors(posteriors)

            # Get the current figure and axis.
            fig = plt.gcf()
            ax = plt.gca()

            # Ensure a figure is created.
            self.assertIsNotNone(fig, "A figure should be created by plot_posteriors.")

            # Check that the plot title is as expected.
            self.assertEqual(ax.get_title(), "Posterior Probabilities of Poker Hand Types",
                             "The plot title should be 'Posterior Probabilities of Poker Hand Types'.")

            # Verify the axis labels.
            self.assertEqual(ax.get_xlabel(), "Poker Hand Type", "The x-label should be 'Poker Hand Type'.")
            self.assertEqual(ax.get_ylabel(), "Posterior Probability", "The y-label should be 'Posterior Probability'.")

            # Verify that the number of bars matches the number of entries in the posteriors dict.
            bars = ax.patches  # Each bar is a Rectangle instance.
            self.assertEqual(len(bars), len(posteriors), "The number of bars should match the number of posterior entries.")

        finally:
            # Restore plt.show to its original function and close all figures.
            plt.show = original_show
            plt.close('all')

if __name__ == '__main__':
    import unittest
    unittest.main()
