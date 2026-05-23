#!/usr/bin/env python3

"""COREX-Causal Upload v1.0.0 - PyPI"""

import requests
import hashlib
import os
import glob

TOKEN = ""

print("="*60)
print("🔬 COREX-Causal v1.0.0 Upload - PyPI")
print("="*60)
print("Causal Origin Resolution and Empirical eXamination")
print("="*60)

# قراءة README.md
try:
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    print(f"\n📄 README.md: {len(readme)} characters")
except:
    readme = "COREX-Causal: Causal Origin Resolution and Empirical eXamination"

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

for filepath in wheel_files + tar_files:
    filename = os.path.basename(filepath)
    print(f"\n📤 Uploading: {filename}")

    if filename.endswith('.tar.gz'):
        filetype = 'sdist'
        pyversion = 'source'
    else:
        filetype = 'bdist_wheel'
        pyversion = 'py3'

    with open(filepath, 'rb') as f:
        content = f.read()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()

    data = {
        ':action': 'file_upload',
        'metadata_version': '2.1',
        'name': 'corex-causal',
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
        'summary': 'COREX-Causal: Causal Origin Resolution and Empirical eXamination — Framework for Robust Causal Discrimination',
        'home_page': 'https://corex.netlify.app',
        'requires_python': '>=3.11',
        'keywords': 'causal-inference, machine-learning, causal-discrimination, spurious-correlations, representation-artifacts'
    }

    try:
        with open(filepath, 'rb') as f:
            response = requests.post(
                'https://upload.pypi.org/legacy/',
                files={'content': (filename, f, 'application/octet-stream')},
                data=data,
                auth=('__token__', TOKEN),
                timeout=90,
                headers={'User-Agent': 'COREX-Causal-Uploader/1.0'}
            )

        print(f"   Status: {response.status_code}")

        if response.status_code == 200:
            print("   ✅✅✅ SUCCESS!")
        else:
            print(f"   ❌ Error: {response.text[:300]}")
    except Exception as e:
        print(f"   ❌ Exception: {str(e)}")

print("\n" + "="*60)
print("🔗 https://pypi.org/project/corex-causal/1.0.0/")
print("="*60)
print("\n📦 Install:")
print("   pip install corex-causal")
