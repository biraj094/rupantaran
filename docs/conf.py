# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# If your package (rupantaran) is one level up from docs/
sys.path.insert(0, os.path.abspath('..'))

project = 'rupantaran'
copyright = '2025, Biraj Koirala'
author = 'Biraj Koirala'
release = '0.2.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



html_theme = "sphinx_rtd_theme"
# html_theme = 'alabaster'

html_static_path = ['_static']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_copybutton',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'  # if you like Google/NumPy style docstrings
]






# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
