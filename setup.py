from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
long_description = (HERE / "README.md").read_text()

setup(
    name="rupantaran",
    version="0.2.5",
    packages=find_packages(),
    license="MIT",
    description="Rupantaran converts Nepali-specific measurements into SI or metric units.",
    long_description=long_description,  # Adds README content
    long_description_content_type="text/markdown",  # Specifies format
    author="BIRAJ KOIRALA",
    author_email="koiralabiraj@gmail.com",
    url="https://github.com/biraj094/rupantaran",
    project_urls={  # Additional links
        "Documentation": "https://rupantaran.github.io/",
        "Source Code": "https://github.com/biraj094/rupantaran",
        "Bug Tracker": "https://github.com/biraj094/rupantaran/issues",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)