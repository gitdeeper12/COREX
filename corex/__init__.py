"""COREX: Causal Origin Resolution and Empirical eXamination

An Autonomous Multi-Stage Framework for Robust Causal Discrimination
in Data-Driven AI Systems

BIO-MED-02 · Biomedical & Clinical AI Research Series
"""

__version__ = "1.0.0"
__author__ = "Samir Baladi"
__license__ = "MIT"
__doi__ = "10.5281/zenodo.20351233"
__series__ = "BIO-MED-02"

from corex.pipeline import CausalEvaluator
from corex.score import compute_corex_score, classify_causal

__all__ = [
    "CausalEvaluator",
    "compute_corex_score",
    "classify_causal",
    "__version__",
    "__doi__"
]
