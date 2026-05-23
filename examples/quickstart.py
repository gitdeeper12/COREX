"""Quick start example for COREX"""

import numpy as np
from corex import CausalEvaluator

def main():
    # Generate synthetic data
    np.random.seed(42)
    X = np.random.randn(100, 10)
    y = X[:, 0] + 0.1 * np.random.randn(100)
    
    # Initialize evaluator
    evaluator = CausalEvaluator()
    
    # Evaluate
    result = evaluator.evaluate(X, y)
    
    print(f"COREX Score: {result.corex_score:.3f}")
    print(f"Classification: {result.label}")
    print(f"Module breakdown: {result.breakdown}")

if __name__ == "__main__":
    main()
