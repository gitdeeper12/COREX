import unittest
import numpy as np
from corex import CausalEvaluator

class TestPipeline(unittest.TestCase):
    def test_evaluate(self):
        evaluator = CausalEvaluator()
        X = np.random.randn(100, 10)
        y = np.random.randn(100)
        result = evaluator.evaluate(X, y)
        self.assertIn(result.label, ["CAUSAL", "SPURIOUS", "REPRESENTATION_ARTIFACT"])
        self.assertGreaterEqual(result.corex_score, 0)
        self.assertLessEqual(result.corex_score, 1)

if __name__ == '__main__':
    unittest.main()
