import unittest
from corex.score import compute_corex_score, classify_causal

class TestScoring(unittest.TestCase):
    def test_compute_score(self):
        score = compute_corex_score(0.9, 0.9, 0.9, 0.9)
        self.assertEqual(score, 0.9)
    
    def test_classify_causal(self):
        label, _ = classify_causal(0.85)
        self.assertEqual(label, "CAUSAL")
        
        label, _ = classify_causal(0.65)
        self.assertEqual(label, "SPURIOUS")
        
        label, _ = classify_causal(0.35)
        self.assertEqual(label, "REPRESENTATION_ARTIFACT")

if __name__ == '__main__':
    unittest.main()
