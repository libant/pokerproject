# Bayesian Poker Inference

## Overview
This project develops a Bayesian inference module to estimate the likelihood of various poker hand types from partial 
information of a player’s 5‑card draw. The goal is to predict which type of hand a player might hold by applying 
combinatorial techniques and Bayesian updating.


## File Structure

The repo is structured as:

-   `bayesian_poker/hand_types.py` contains functions to compute and classify poker hand types.
-   `bayesian_poker/likelihood.py` contains methods to calculate the likelihood of a hand type given partial observations.
-   `bayesian_poker/bayesian_update.py` contains functions to perform Bayesian updating and compute posterior probabilities.
-   `bayesian_poker/visualization.py` contains tools to visualize posterior distributions.
-   `bayesian_poker/helper.py` contains helper functions.
-   `docs` contain documentation.
-   `tests` contain tests.

## Statement on LLM usage

Some aspects of the code were written with the help of ChatGPT.