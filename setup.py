from setuptools import setup, find_packages

setup(
    name="corex",
    version="1.0.0",
    description="COREX: Causal Origin Resolution and Empirical eXamination",
    author="Samir Baladi",
    author_email="gitdeeper@gmail.com",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "numpy>=2.0.0",
        "scipy>=1.14.0",
    ],
)
