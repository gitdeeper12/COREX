"""Class A: Encoding-dependent associations (artifacts)"""

import numpy as np
from typing import Tuple

def generate_artifact_encoding(
    n_samples: int = 1000,
    n_features: int = 10,
    artifact_dim: int = 5,
    seed: int = None
) -> Tuple[np.ndarray, np.ndarray]:
    """Generate artifact dataset where relationship exists only in specific encoding"""
    if seed:
        np.random.seed(seed)
    
    # Relationship exists only in first artifact_dim dimensions
    X = np.random.randn(n_samples, n_features)
    y = np.sum(X[:, :artifact_dim], axis=1) + 0.1 * np.random.randn(n_samples)
    
    return X, y
