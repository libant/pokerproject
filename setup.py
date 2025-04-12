from setuptools import setup, find_packages

setup(
    name="bayesian-poker-inference",
    version="0.1.0",
    description="A Bayesian inference module for estimating poker hand types from partial information.",
    author="Liban Timir",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
    ],
)

