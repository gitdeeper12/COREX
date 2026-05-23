
🚀 Deployment Guide for COREX

Package Deployment (PyPI)

Prerequisites

```bash
pip install build twine
```

Build Package

```bash
python -m build
```

Upload to PyPI (Production)

```bash
twine upload dist/*
```

---

Docker Deployment

Build Image

```bash
docker build -t corex:latest .
```

Run Container

```bash
docker run -it --rm corex:latest --evaluate --dataset synthetic
```

---

CI/CD Pipeline (GitLab CI)

The .gitlab-ci.yml includes:

1. Test - Run unit tests on Python 3.11-3.12
2. Build - Create PyPI package
3. Deploy - Auto-deploy to PyPI on tags
4. Mirror - Push to GitHub, Bitbucket, Codeberg

Trigger Deployment

```bash
git tag v1.0.0
git push origin v1.0.0
```

---

Netlify Deployment (Documentation)

```bash
cd Netlify/
netlify deploy --prod
```

Configuration

· Site name: corex.netlify.app
· Publish directory: Netlify/

---

Repository Mirrors

```bash
git push github main
git push gitlab main
git push bitbucket main
git push codeberg main
```

---

Verification

```bash
pip install corex
curl https://doi.org/10.5281/zenodo.20351233
curl https://corex.netlify.app
```

---

Learnable Layer Training

```bash
# Train meta-learner on synthetic benchmarks
python -m corex.train --benchmark-dir ./benchmarks --epochs 1000

# Export trained weights
python -m corex.export_weights --output corex_meta_weights.pt
```

---

For production deployments, ensure all tests pass and documentation is up to date.
