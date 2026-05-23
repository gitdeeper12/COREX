"""Causal scoring function and decision logic"""

import numpy as np
from typing import Tuple

def compute_corex_score(
    S: float,
    R: float,
    I: float,
    D: float,
    weights: Tuple[float, float, float, float] = (0.25, 0.25, 0.30, 0.20)
) -> float:
    """
    Compute COREX score from four module scores
    
    COREX = w₁·S + w₂·R + w₃·I + w₄·D
    """
    return weights[0] * S + weights[1] * R + weights[2] * I + weights[3] * D


def classify_causal(score: float) -> Tuple[str, float]:
    """
    Classify relationship based on COREX score
    
    Args:
        score: COREX score in [0, 1]
    
    Returns:
        (label, threshold_lower_bound)
    """
    if score >= 0.80:
        return "CAUSAL", 0.80
    elif score >= 0.50:
        return "SPURIOUS", 0.50
    else:
        return "REPRESENTATION_ARTIFACT", 0.00
