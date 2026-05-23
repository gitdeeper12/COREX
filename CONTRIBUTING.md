# Contributing to COREX

Thank you for your interest in contributing to **COREX**!

## How to Contribute

### 1. Report Bugs
- Use GitHub/GitLab Issues
- Include: Python version, dataset characteristics, steps to reproduce
- Label: `bug`

### 2. Suggest Features
- Open an issue with label `enhancement`
- Describe the use case and expected behavior
- New evaluation modules or transformation families are welcome

### 3. Submit Code Changes

#### Prerequisites
```bash
pip install -e .[dev]
pre-commit install
```

Development Workflow

```bash
git clone https://github.com/gitdeeper12/COREX
cd COREX
git checkout -b feature/your-feature-name
pytest tests/ -v
git commit -m "feat: add new transformation"
git push origin feature/your-feature-name
```

1. Update Documentation

· Edit README.md, docs/, or docstrings
· Ensure decision thresholds are documented

Code Style

· Python: PEP 8 (use black)
· Type hints: Required for all public functions
· Docstrings: Google style

Testing Requirements

· All tests must pass: pytest tests/ -v
· Coverage should not decrease: pytest --cov=corex
· New features require tests
· All four modules must maintain accuracy

Commit Convention

Type Description
feat New feature
fix Bug fix
docs Documentation
test Testing
refactor Code refactor
perf Performance improvement

Questions?

Open an issue or email: gitdeeper@gmail.com

---

Thank you for contributing to causal discrimination in AI! 🧠
