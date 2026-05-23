# COREX Scoring Function

## Formula

COREX = w₁·S + w₂·R + w₃·I + w₄·D

## Default Weights

- Statistical: 0.25
- Representation: 0.25
- Intervention: 0.30
- Domain: 0.20

## Decision Thresholds

- CAUSAL: ≥ 0.80
- SPURIOUS: 0.50 – 0.79
- ARTIFACT: < 0.50
