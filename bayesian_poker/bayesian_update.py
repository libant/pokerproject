def bayesian_update(priors, likelihoods):
    """
    Performs Bayesian updating.

    Parameters:
      priors: dict mapping each hand type to its prior probability.
      likelihoods: dict mapping each hand type to the likelihood of the observed data given that hand.

    Returns:
      A dictionary mapping each hand type to its posterior probability.

    Example:
      priors = {"Flush": 0.2, "Straight": 0.1, ...}
      likelihoods = {"Flush": 0.05, "Straight": 0.02, ...}
    """
    posterior = {}
    evidence = sum(priors[h] * likelihoods[h] for h in priors)
    if evidence == 0:
        raise ValueError("Total evidence is zero; check your priors and likelihoods.")

    for h in priors:
        posterior[h] = (priors[h] * likelihoods[h]) / evidence
    return posterior
