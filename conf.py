# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Sphinx-lesson'
copyright = '2020, CodeRefinery'
author = 'CodeRefinery'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sys
sys.path.append('.')
extensions = [
    # githubpages just adds a .nojekyll file
    'sphinx.ext.githubpages',
    # myst_parser is not needed, because myst_nb replaces and conflicts with it
    # (provides all functionality and more).  But, myst_parser has fewer
    # dependencies so could be used instead.
    #'myst_parser',
    'sphinx_lesson',
    #'myst_nb',  # now done as part of sphinx_lesson
]

# Settings for myst_nb:
# https://myst-nb.readthedocs.io/en/latest/use/execute.html#triggering-notebook-execution
#jupyter_execute_notebooks = "off"
jupyter_execute_notebooks = "auto"
#jupyter_execute_notebooks = "force"

# Make myst-nb work with the dirhtml builder
# This can be removed once myst_parser>0.8.3 is released
# https://github.com/executablebooks/MyST-NB/pull/202
from myst_nb.transform import RENDER_PRIORITY
RENDER_PRIORITY['dirhtml'] = 'html'
del RENDER_PRIORITY

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['README*', '_build', 'Thumbs.db', '.DS_Store', '*venv*']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
