"""Custom weight configuration example for COREX"""

from corex import CausalEvaluator

# Custom weights prioritizing intervention consistency
evaluator = CausalEvaluator(
    weights={
        "statistical": 0.20,
        "representation": 0.20,
        "intervention": 0.40,
        "domain": 0.20
    }
)

print("Custom weights configured successfully")
print(f"Weights: {evaluator.weights}")
