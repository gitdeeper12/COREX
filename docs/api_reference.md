# COREX API Reference

## CausalEvaluator

```python
class CausalEvaluator:
    def evaluate(self, X, y, environments=None) -> EvaluationResult
```

compute_corex_score

```python
def compute_corex_score(S, R, I, D, weights=None) -> float
```

classify_causal

```python
def classify_causal(score) -> Tuple[str, float]
```

