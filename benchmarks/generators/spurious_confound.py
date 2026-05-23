"""Class S: Spurious correlation with latent confounder H → X, H → Y"""

import numpy as np
from typing import Tuple

def generate_spurious_confound(
    n_samples: int = 1000,
    n_features: int = 10,
    confounder_strength: float = 0.8,
    seed: int = None
) -> Tuple[np.ndarray, np.ndarray]:
    """Generate spurious dataset with latent confounder"""
    if seed:
        np.random.seed(seed)
    
    # Latent confounder H
    H = np.random.randn(n_samples)
    
    # X and Y both depend on H
    X = np.random.randn(n_samples, n_features) + confounder_strength * H[:, np.newaxis]
    y = H + 0.1 * np.random.randn(n_samples)
    
    return X, y
