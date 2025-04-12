"""
Bayesian Poker Inference – Project Documentation
==================================================

How to Use the Project
----------------------

### Demonstration Notebook

Open the notebook `Bayesian_Poker_Inference.ipynb` in the `notebooks/` folder to see a step-by-step
demonstration of the package functionality, including:
  - Hand classification,
  - Likelihood computation,
  - Bayesian updating, and
  - Visualization of posterior probabilities.

### Running Tests

To verify that the project is working as expected, run the tests from the root of the repository:

       python -m unittest discover

How It Works
------------
1. **Hand Type Computation:**
   The module `hand_types.py` analyzes a 5‑card hand and classifies it (for example, as a Straight Flush, Four of a Kind, etc.) by examining the card ranks and suits.

2. **Partial Observation Likelihood:**
   In `likelihood.py`, functions calculate the probability of forming a specific poker hand type from a
   partial hand. Depending on the number of unknown cards, the code uses exact enumeration or Monte Carlo sampling.

3. **Bayesian Updating:**
   The module `bayesian_update.py` combines prior probabilities and computed likelihoods (using Bayes’ theorem) to produce the posterior probabilities.

4. **Visualization:**
   `visualization.py` provides functions to create bar charts that display the updated probability for each hand type.

5. **Utility Functions:**
   The module `utils.py` includes useful helper functions, such as generating the standard 52‑card deck and
   computing combinatorial values.

Additional Information
----------------------
- **Contributing:** Contributions, suggestions, and bug reports are welcome. Please feel free to submit pull requests
   or open issues.
- **Acknowledgments:** Some portions of the code and this documentation were developed with the assistance of ChatGPT.

Happy Inference!
"""


def main():
    """
    Prints the project documentation when the script is executed.
    """
    # Printing the module docstring
    print(__doc__)


if __name__ == "__main__":
    main()
