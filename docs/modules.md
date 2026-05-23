# COREX Modules Documentation

## Statistical Stability Module

Formula: S = 1 - mean_{i≠j} KL[P(Y|X, D_i) || P(Y|X, D_j)]

## Representation Invariance Module

Formula: R = 1 - (1/|Φ|) Σ_φ ||P(Y|X) - P(Y|φ(X))||₁
