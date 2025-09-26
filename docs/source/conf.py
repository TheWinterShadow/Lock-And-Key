"""Configuration file for the Sphinx documentation builder."""

# -- Project information -----------------------------------------------------

project = "Lock & Key"
copyright = "2025, WinterShadow"
author = "WinterShadow"
version = "1.0.1"
release = "1.0.1"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output ------------------------------------------------

html_theme = "furo"
html_static_path = ["_static"]
html_title = f"{project} {version}"

# -- Options for autodoc ----------------------------------------------------

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

# -- Options for intersphinx ------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "boto3": ("https://boto3.amazonaws.com/v1/documentation/api/latest/", None),
    "click": ("https://click.palletsprojects.com/en/8.1.x/", None),
}

# -- Options for MyST parser ------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# Add the project root to the Python path
import os
import sys
sys.path.insert(0, os.path.abspath("../.."))
