Installation
============

Sphinx Python package
---------------------

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



Github Pages initial commit
---------------------------

The included Github Actions file will automatically push to Github
Pages, but due to some quirk/bugs in gh-pages *the very first
non-human gh-pages push won't enable Github Pages*.  So, you have to
do one push yourself (or go to settings and disable-enable gh-pages
the first time).

You can make an empty commit to gh-pages this way, which will trigger
the gh-pages deployment (and everything will be automatic after that)::

  git checkout -b gh-pages origin/gh-pages
  git commit -m 'empty commit to trigger gh-pages' --allow-empty
  git push




Under the hood
--------------

Adding ``sphinx_lesson`` as an extension adds these sub-extensions:

  * ``sphinx_lesson.directives`` - see :doc:`directives`.
  * ``sphinx_lesson.md_transforms`` - see :doc:`md-transforms`.
  * Enables the `myst_notebook extension
    <https://myst-nb.readthedocs.io/en/latest/>`__, which also enables
    `myst_parser
    <https://myst-parser.readthedocs.io/en/latest/index.html>`__
    (included as a dependencies)
  * Enables the `sphinx-copybutton extension
    <https://github.com/executablebooks/sphinx-copybutton>`__
    (included as a dependency)
  * Same for `sphinx-togglebutton <https://pypi.org/project/sphinx-togglebutton/>`__

Any of these can be used independently to get the same effect.
