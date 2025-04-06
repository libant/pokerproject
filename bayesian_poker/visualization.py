import matplotlib.pyplot as plt

def plot_posteriors(posteriors):
    """
    Plots a bar chart of posterior probabilities for each poker hand type.

    Parameters:
      posteriors: dict mapping hand type to posterior probability.

    Example:
      posteriors = {"Flush": 0.3, "Straight": 0.1, ...}
    """
    hand_types = list(posteriors.keys())
    probabilities = list(posteriors.values())

    plt.figure(figsize=(10, 6))
    plt.bar(hand_types, probabilities, alpha=0.7)
    plt.xlabel("Poker Hand Type")
    plt.ylabel("Posterior Probability")
    plt.title("Posterior Probabilities of Poker Hand Types")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
