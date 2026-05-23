"""Class C: True causal chains X → Y → Z"""

import numpy as np
from typing import Tuple

def generate_causal_chain(
    n_samples: int = 1000,
    n_features: int = 10,
    noise: float = 0.1,
    seed: int = None
) -> Tuple[np.ndarray, np.ndarray]:
    """Generate causal dataset where X causes Y"""
    if seed:
        np.random.seed(seed)
    
    # Causal relationship: Y = X[:, 0] + noise
    X = np.random.randn(n_samples, n_features)
    y = X[:, 0] + noise * np.random.randn(n_samples)
    
    return X, y
