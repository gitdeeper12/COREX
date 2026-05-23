
📦 Installation Guide for COREX

Quick Install (PyPI)

```bash
pip install corex
```

Install from Source

```bash
git clone https://github.com/gitdeeper12/COREX.git
cd COREX
pip install -e .
```

Verify Installation

```python
import corex
print(corex.__version__)  # 1.0.0
print(corex.__doi__)      # 10.5281/zenodo.20351233
```

```bash
python -c "from corex import COREX; print('COREX ready')"
```

---

Requirements

Package Version Required
Python ≥ 3.11
numpy ≥ 2.0.0
scipy ≥ 1.14.0
scikit-learn ≥ 1.5.0
torch (optional) ≥ 2.4.0

---

Platform Support

Platform Support
Linux ✅ Fully tested
macOS ✅ Compatible
Windows ✅ Compatible
Termux (Android) ✅ Compatible

---

Docker Installation

```bash
docker pull gitdeeper12/corex:latest
docker run --rm corex --evaluate --dataset synthetic
```

---

Uninstall

```bash
pip uninstall corex
rm -rf COREX
```

---

For issues, open a ticket on GitHub/GitLab.
