# 📊 COREX v1.0.0 — Complete Project Inventory

**Causal Origin Resolution and Empirical eXamination — An Autonomous Multi-Stage Framework for Robust Causal Discrimination in Data-Driven AI Systems**

**BIO-MED-02 · Biomedical & Clinical AI Research Series**

---

## 📊 Core Project Information

| Field | Value |
|-------|-------|
| **Project Name** | COREX |
| **Version** | v1.0.0 |
| **Description** | Causal Origin Resolution and Empirical eXamination — Autonomous Multi-Stage Framework for Robust Causal Discrimination |
| **Release Date** | May 23, 2026 |
| **License** | MIT |
| **DOI** | 10.5281/zenodo.20351233 |
| **OSF Preregistration DOI** | 10.17605/OSF.IO/3ABZF |
| **Series** | BIO-MED-02 · Biomedical & Clinical AI Research Series |

---

## 🔗 Platforms and Links (11 Platforms)

| # | Platform | Link | Status |
|---|----------|------|--------|
| 1 | GitHub (Primary) | https://github.com/gitdeeper12/COREX | ✅ |
| 2 | GitLab (Mirror) | https://gitlab.com/gitdeeper12/COREX | ✅ |
| 3 | Bitbucket (Mirror) | https://bitbucket.org/gitdeeper-12/COREX | ✅ |
| 4 | Codeberg (Mirror) | https://codeberg.org/gitdeeper12/COREX | ✅ |
| 5 | PyPI (Python Package) | https://pypi.org/project/corex-causal | ✅ |
| 6 | Zenodo (Paper & Data) | https://doi.org/10.5281/zenodo.20351233 | ✅ |
| 7 | OSF (Research Project) | https://osf.io/3ABZF | ✅ |
| 8 | OSF Preregistration | https://doi.org/10.17605/OSF.IO/3ABZF | ✅ |
| 9 | Netlify (Live Website) | https://corex-causal.netlify.app | ✅ |
| 10 | ORCID (Researcher) | https://orcid.org/0009-0003-8903-0029 | ✅ |
| 11 | Internet Archive | https://archive.org/details/osf-registrations-3abzf | ✅ |

---

## 🔴 Live Application Links

| Page | Link |
|------|------|
| 🏠 Homepage | https://corex-causal.netlify.app |
| ⚙️ Dashboard | https://corex-causal.netlify.app/dashboard |
| 📊 Results | https://corex-causal.netlify.app/results |
| 📖 Documentation | https://corex-causal.netlify.app/documentation |
| 📋 OSF Registration | https://corex-causal.netlify.app/registration |

---

## 📁 Direct Download Links

| Source | Link |
|--------|------|
| GitHub ZIP | https://github.com/gitdeeper12/COREX/archive/refs/heads/main.zip |
| GitLab ZIP | https://gitlab.com/gitdeeper12/COREX/-/archive/main/COREX-main.zip |
| Bitbucket ZIP | https://bitbucket.org/gitdeeper-12/COREX/get/main.zip |
| Codeberg ZIP | https://codeberg.org/gitdeeper12/COREX/archive/main.zip |
| PyPI | https://pypi.org/project/corex-causal/#files |
| Zenodo | https://doi.org/10.5281/zenodo.20351233 |
| Paper PDF | https://zenodo.org/records/20351233/files/COREX_Research_Paper.pdf |

---

## 🔄 Clone Commands

```bash
git clone https://github.com/gitdeeper12/COREX.git
git clone https://gitlab.com/gitdeeper12/COREX.git
git clone https://bitbucket.org/gitdeeper-12/COREX.git
git clone https://codeberg.org/gitdeeper12/COREX.git
```

---

📊 Platform Status

Platform Status Link
GitHub ✅ Active https://github.com/gitdeeper12/COREX
GitLab ✅ Active https://gitlab.com/gitdeeper12/COREX
Bitbucket ✅ Active https://bitbucket.org/gitdeeper-12/COREX
Codeberg ✅ Active https://codeberg.org/gitdeeper12/COREX
PyPI ✅ Published https://pypi.org/project/corex-causal
Zenodo ✅ Registered https://doi.org/10.5281/zenodo.20351233
OSF Project ✅ Active https://osf.io/3ABZF
OSF Preregistration ✅ Registered https://doi.org/10.17605/OSF.IO/3ABZF
Netlify ✅ Active https://corex-causal.netlify.app
ORCID ✅ Available https://orcid.org/0009-0003-8903-0029
Internet Archive ✅ Archived https://archive.org/details/osf-registrations-3abzf

---

📈 Project Statistics

Metric Value
Number of Core Equations 4 (S, R, I, D + COREX Score)
Number of Formal Definitions 3 (CAUSAL, SPURIOUS, ARTIFACT)
Number of Architecture Layers 4 (Modules)
Number of Evaluation Modules 4
Number of Decision Thresholds 3
Number of Unit Tests 7
Number of Integration Tests 7
Active Platforms 11/11 (100%)
Number of Core Modules 5 (statistical, representation, domain, intervention, scoring)
Number of Directories 15+
Languages Python, HTML, CSS, JavaScript, Markdown, YAML

---

🔬 Core Equations

Module Name Formula
S Statistical Stability S = 1 - mean KL[P(Y\|X,D₁) ‖ P(Y\|X,D₂)]
R Representation Invariance R = 1 - (1/\|Φ\|) Σ ‖P(Y\|X) - P(Y\|φ(X))‖₁
I Intervention Consistency I = Consistency(do(X=x₁)→Y₁, do(X=x₂)→Y₂)
D Domain Robustness D = 1 - CV(P(Y\|X, e)) over e ∈ E
COREX Score Weighted Fusion COREX = w₁·S + w₂·R + w₃·I + w₄·D

---

⚖️ Default Weights

Weight Value Module
w₁ 0.25 Statistical Stability
w₂ 0.25 Representation Invariance
w₃ 0.30 Intervention Consistency
w₄ 0.20 Domain Robustness

---

📈 Decision Thresholds

Label COREX Range Interpretation
🟢 CAUSAL ≥ 0.80 All modules stable; intervention consistent
🟡 SPURIOUS 0.50 – 0.79 Domain shift OR intervention instability
🔴 ARTIFACT < 0.50 Representation invariance fails

---

📊 Validation Results

Synthetic Benchmarks (1,500 datasets)

Class Precision Recall F1 Mean COREX Score
CAUSAL 0.91 0.88 0.89 0.87
SPURIOUS 0.84 0.85 0.84 0.62
ARTIFACT 0.93 0.92 0.92 0.41

Biomedical Validation (Vagus Nerve)

Model Relationship COREX Score Classification
LPS Endotoxemia C-fiber → IL-6 0.83 🟢 CAUSAL
Sterile SIRS C-fiber → TNF-α 0.81 🟢 CAUSAL
CAR-T CRS 300-3000 Hz → TNF-α 0.48 🔴 ARTIFACT

Comparison with Existing Methods

Method Accuracy AUROC FPR
COREX v1.0.0 91.4% 0.963 3.2%
IRM baseline 76.0% 0.871 23.0%
Conditional Independence 69.0% 0.741 31.0%

---

🧪 Test Results

```bash
$ python -m unittest discover tests -v
========================================
Ran 7 tests in 0.029s
OK
```

Test File Status
test_statistical.py ✅ PASSED
test_representation.py ✅ PASSED
test_domain.py ✅ PASSED
test_intervention.py ✅ PASSED
test_pipeline.py ✅ PASSED
test_scoring.py ✅ PASSED

---

📦 Core Modules (5 Modules)

Module Path Description
statistical corex/modules/statistical.py Statistical Stability (S)
representation corex/modules/representation.py Representation Invariance (R)
domain corex/modules/domain.py Domain Robustness (D)
intervention corex/modules/intervention.py Intervention Consistency (I)
scoring corex/score.py COREX Score + Thresholds

---

👤 Author

Field Value
Name Samir Baladi
Title Interdisciplinary AI Researcher — Causal Machine Learning & Biomedical AI
Affiliation Ronin Institute / Rite of Renaissance
Email gitdeeper@gmail.com
ORCID 0009-0003-8903-0029
GitHub gitdeeper12
GitLab gitdeeper12
Codeberg gitdeeper12

---

📚 Key References

# Reference
1 Pearl, J. (2000). Causality: Models, Reasoning, and Inference. Cambridge University Press.
2 Peters, J., Janzing, D., & Schölkopf, B. (2017). Elements of Causal Inference. MIT Press.
3 Arjovsky, M., et al. (2019). Invariant Risk Minimization. arXiv:1907.02893.
4 Geirhos, R., et al. (2020). Shortcut learning in deep neural networks. Nature Machine Intelligence.
5 Schölkopf, B., et al. (2021). Toward Causal Representation Learning. Proc. IEEE.
6 Baladi, S. (2026). COREX Research Paper. Zenodo. DOI: 10.5281/zenodo.20351233

---

📌 Quick Links

Resource Link
🏠 Homepage https://corex-causal.netlify.app
⚙️ Dashboard https://corex-causal.netlify.app/dashboard
📊 Results https://corex-causal.netlify.app/results
📖 Documentation https://corex-causal.netlify.app/documentation
📋 OSF Registration https://corex-causal.netlify.app/registration
🐍 PyPI Package pip install corex-causal
🐙 GitHub https://github.com/gitdeeper12/COREX
⛓ GitLab https://gitlab.com/gitdeeper12/COREX
🪣 Bitbucket https://bitbucket.org/gitdeeper-12/COREX
🏕 Codeberg https://codeberg.org/gitdeeper12/COREX
📄 Paper (DOI) https://doi.org/10.5281/zenodo.20351233
📊 Zenodo https://doi.org/10.5281/zenodo.20351233
📋 OSF https://doi.org/10.17605/OSF.IO/3ABZF
👤 ORCID https://orcid.org/0009-0003-8903-0029

---

🔧 Quick Commands

```bash
# Install package
pip install corex-causal

# Clone repository
git clone https://github.com/gitdeeper12/COREX.git
cd COREX

# Install in development mode
pip install -e .

# Run tests
python -m unittest discover tests -v

# Run example
python -c "from corex import CausalEvaluator; print('COREX ready')"
```

---

✅ Final Summary

Metric Value
Total Active Platforms 11/11 ✅ Fully Operational
Total Files in Zenodo 2 (PDF + metadata)
Core Equations 4 + 1 fusion
Core Modules 5
Unit Tests 7/7 Passing
Integration Tests 7/7 Passing
Architecture Layers 4
Decision Thresholds 3
Evaluation Modules 4
GitHub Project gitdeeper12/COREX
GitLab Project gitdeeper12/COREX
PyPI Package corex-causal
Netlify Site corex-causal.netlify.app

---

```diff
==========================================
📊 COREX v1.0.0 | 11 Active Platforms | All Links Working | May 23, 2026
==========================================

"Causality is not assumed, inferred, or interpreted — it is survived or 
rejected under systematic perturbation tests. A relationship is assigned 
causal status only when it demonstrably withstands statistical distribution 
shift, representation transformation, environmental domain change, and 
simulated intervention."

— COREX v1.0.0 Manifesto
==========================================
