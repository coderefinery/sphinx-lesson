Installation
============

This is distributed as a normal Sphinx extension, so it is easy to
use.  To use it, install ``sphinx_lesson`` via PyPI (note: it is not
there yet, so use this in ``requirements.txt`` and with ``pip
install``:
``https://github.com/coderefinery/sphinx-lesson/archive/master.zip``).

Then, enable the extension in your Sphinx ``conf.py``.  This will both
define our special directives, and load the other required extensions
(``myst_nb``).  The ``myst_nb`` extension can be configured normally::

  extensions = [
      'sphinx_lesson',
  ]

We are in theory compatible with any theme, but are most tested with
the sphinx_rtd_theme (which you need to set yourself)::

  html_theme = 'sphinx_rtd_theme'

The Jupyter Book (Executable Books Project) Sphinx theme
(`sphinx-book-theme
<https://sphinx-book-theme.readthedocs.io/en/latest/>`__) has some
very nice features and also deserves some consideration.  Using it
should be clear: ``html_theme = "sphinx_book_theme"``.
