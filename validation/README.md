# COREX Validation Results

This directory contains validation results for COREX v1.0.0.

## Files

| File | Description |
|------|-------------|
| `biomedical_validation.json` | Validation on vagus nerve electrophysiology data |
| `synthetic_validation.json` | Validation on synthetic benchmarks (1,500 datasets) |

## Summary

### Biomedical Validation

| Model | Relationship | COREX Score | Classification |
|-------|-------------|-------------|----------------|
| LPS Endotoxemia | C-fiber → IL-6 | 0.83 | CAUSAL |
| Sterile SIRS | C-fiber → TNF-α | 0.81 | CAUSAL |
| CAR-T CRS | 300-3000 Hz → TNF-α | 0.48 | ARTIFACT |

### Synthetic Validation

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| CAUSAL | 0.91 | 0.88 | 0.89 |
| SPURIOUS | 0.84 | 0.85 | 0.84 |
| ARTIFACT | 0.93 | 0.92 | 0.92 |

### Ablation Study

| Configuration | Accuracy | AUROC | FPR |
|---------------|----------|-------|-----|
| Full COREX | 91.4% | 0.963 | 3.2% |
| No Intervention | 84.4% | 0.931 | 5.8% |
| No Representation | 81.2% | 0.901 | 6.9% |

## Usage

```python
import json

with open('validation/results/biomedical_validation.json', 'r') as f:
    results = json.load(f)
    print(results['summary'])
```

