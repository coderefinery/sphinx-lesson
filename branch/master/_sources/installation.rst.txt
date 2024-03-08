Installation
============

Sphinx Python package
---------------------

This is distributed as a normal Sphinx extension, so it is easy to
use.  To use it, install ``sphinx_lesson`` via PyPI.

Then, enable the extension in your Sphinx ``conf.py``.  This will both
define our special directives, and load the other required extensions
(``myst_nb``).  The ``myst_nb`` extension can be configured normally::

  extensions = [
      'sphinx_lesson',
  ]

HTML theme
----------

We are in theory compatible with any theme, but are most tested with
the sphinx_rtd_theme (which you need to set yourself)::

  html_theme = 'sphinx_rtd_theme'

The Jupyter Book (Executable Books Project) Sphinx theme
(`sphinx-book-theme
<https://sphinx-book-theme.readthedocs.io/en/latest/>`__) has some
very nice features and also deserves some consideration.  Using it
should be clear: ``html_theme = "sphinx_book_theme"``.  You can see a
preview of it `as a branch on github-pages
<https://coderefinery.github.io/sphinx-lesson/branch/sphinx-book-theme/>`__.



Under the hood
--------------

Adding ``sphinx_lesson`` as an extension adds these sub-extensions:

  * ``sphinx_lesson.directives`` - see :doc:`directives`.
  * ``sphinx_lesson.md_transforms`` - see :doc:`md-transforms`.
  * ``sphinx_lesson.exerciselist`` - see :doc:`exercise-list`.
  * ``sphinx_lesson.term_role_formatting`` - makes glossary term
    references bold
  * Enables the `myst_notebook extension
    <https://myst-nb.readthedocs.io/en/latest/>`__, which also enables
    `myst_parser
    <https://myst-parser.readthedocs.io/en/latest/index.html>`__
    (included as a dependencies)
  * Enables the `sphinx-copybutton extension
    <https://github.com/executablebooks/sphinx-copybutton>`__
    (included as a dependency)
  * Same for `sphinx-tabs <https://sphinx-tabs.readthedocs.io/>`__
  * Same for `sphinx-togglebutton <https://pypi.org/project/sphinx-togglebutton/>`__

Any of these can be used independently to get the same effect.
