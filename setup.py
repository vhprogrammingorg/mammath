from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mammath",
    version="0.3.0",
    author="Vihaan Mathur & Harihar Rengan",
    author_email="vihaan.harihar314@gmail.com",
    description="A comprehensive package for advanced mathematics and science in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages = find_packages(),
    python_requires=">=3.6",
    install_requires=["tabulate", "numpy", "matplotlib", "keyboard"],
)
