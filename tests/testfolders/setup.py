import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mammath",
    version="0.1.2",
    author="Vihaan Mathur & Harihar Rengan",
    author_email="vihaan.harihar341@gmail.com",
    description="A package that contains all you will need when you need to do complicated maths in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages = ["mammath"],
    python_requires=">=3.6",
    install_requires=["sympy", "tabulate", "numpy", "matplotlib", "keyboard"],
)