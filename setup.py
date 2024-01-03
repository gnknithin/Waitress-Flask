from setuptools import find_packages, setup

setup(
    name="Waitress-Flask",
    version="0.1.0",
    description="A simple flask app using Waitress",
    url="https://github.com/gnknithin/Waitress-Flask",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    test_suit="tests"
)
