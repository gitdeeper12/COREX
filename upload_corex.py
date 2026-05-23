#!/usr/bin/env python3

"""COREX Upload v1.0.0 - PyPI"""

import requests
import hashlib
import os
import glob

TOKEN = "pypi-AgEIcHlwaS5vcmcCJDdiNjk3MjgyLTBkYzYtNGM2MS05YTFjLTBlZGE3YzhhZDE1MAACKlszLCJlZjQ3ZDllOS04YmU5LTQ2OWMtYWQ0OC0wODRhZTg4YzZjMTUiXQAABiDOK65Z6I5JsEaTXzLUJplolFdaeFLdfi-JIskqo_qIWQ"

print("="*60)
print("🔬 COREX v1.0.0 Upload - PyPI")
print("="*60)
print("Causal Origin Resolution and Empirical eXamination")
print("An Autonomous Multi-Stage Framework for Robust Causal Discrimination")
print("="*60)

# قراءة README.md
try:
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    print(f"\n📄 README.md: {len(readme)} characters")
except FileNotFoundError:
    print("\n⚠️ README.md not found, using fallback description")
    readme = "COREX: Causal Origin Resolution and Empirical eXamination — An Autonomous Multi-Stage Framework for Robust Causal Discrimination in Data-Driven AI Systems"

# البحث عن ملفات التوزيع
wheel_files = glob.glob("dist/*.whl")
tar_files = glob.glob("dist/*.tar.gz")

if not wheel_files and not tar_files:
    print("\n❌ No distribution files found. Building package...")
    os.system("python -m build")
    
    wheel_files = glob.glob("dist/*.whl")
    tar_files = glob.glob("dist/*.tar.gz")

print(f"\n📦 Distribution files:")
for f in wheel_files + tar_files:
    print(f"   • {os.path.basename(f)}")

upload_success = False

for filepath in wheel_files + tar_files:
    filename = os.path.basename(filepath)
    print(f"\n📤 Uploading: {filename}")

    # تحديد نوع الملف
    if filename.endswith('.tar.gz'):
        filetype = 'sdist'
        pyversion = 'source'
    else:
        filetype = 'bdist_wheel'
        pyversion = 'py3'

    # حساب الهاشات
    with open(filepath, 'rb') as f:
        content = f.read()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()

    # بيانات الرفع لـ COREX
    data = {
        ':action': 'file_upload',
        'metadata_version': '2.1',
        'name': 'corex',
        'version': '1.0.0',
        'filetype': filetype,
        'pyversion': pyversion,
        'md5_digest': md5_hash,
        'sha256_digest': sha256_hash,
        'description': readme,
        'description_content_type': 'text/markdown',
        'author': 'Samir Baladi',
        'author_email': 'gitdeeper@gmail.com',
        'license': 'MIT',
        'summary': 'COREX: Causal Origin Resolution and Empirical eXamination — An Autonomous Multi-Stage Framework for Robust Causal Discrimination in Data-Driven AI Systems',
        'home_page': 'https://corex.netlify.app',
        'requires_python': '>=3.11',
        'keywords': 'causal-inference, machine-learning, shortcut-learning, representation-invariance, domain-robustness, intervention-consistency, causal-discrimination, spurious-correlations, representation-artifacts, empirical-causality, biomedical-ai'
    }

    # رفع الملف
    try:
        with open(filepath, 'rb') as f:
            response = requests.post(
                'https://upload.pypi.org/legacy/',
                files={'content': (filename, f, 'application/octet-stream')},
                data=data,
                auth=('__token__', TOKEN),
                timeout=90,
                headers={'User-Agent': 'COREX-Uploader/1.0'}
            )

        print(f"   Status: {response.status_code}")

        if response.status_code == 200:
            print("   ✅✅✅ SUCCESS!")
            upload_success = True
        else:
            print(f"   ❌ Error: {response.text[:300]}")
    except Exception as e:
        print(f"   ❌ Exception: {str(e)}")

print("\n" + "="*60)
if upload_success:
    print("✅ COREX v1.0.0 uploaded successfully!")
    print("🔗 https://pypi.org/project/corex/1.0.0/")
else:
    print("⚠️ Upload completed with some issues.")
    print("🔗 https://pypi.org/project/corex/")
print("="*60)

print("\n📦 Install COREX:")
print("   pip install corex")
print("")
print("📖 Documentation:")
print("   https://corex.netlify.app")
