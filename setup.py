# setup.py at the same level as the 'rupantaran' folder
from setuptools import setup, find_packages

setup(
    name="rupantaran",
    version="0.2.1",
    packages=find_packages(),
    license="MIT",
    description="Rupantaran is a Python package that converts various Nepali-specific measurements into SI units or commonly used metric units.",
    author="BIRAJ KOIRALA",
    author_email="koiralabiraj@gmail.com",
    url="https://github.com/biraj094/rupantaran",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

)