Test sphinx lesson
==================

In this lesson, we learn how to make a CodeRefinery lesson using
sphinx.  It is designed to replace the Jekyll-based software carepntry
templates.  The source is on `github
<https://github.com/coderefinery/sphinx-test-lesson>`__.


.. prereq:: Required software

   * prereq1
   * prereq2

   This has the css class 'prereq', and like all blocks is implemented
   like::

     .. prereq::

	* prereq1
	* prereq2


The following directives are implemented:

* ``callout``
* ``challenge``
* ``checklist``
* ``discussion``
* ``keypoints``
* ``objectives``
* ``prereq``
* ``solution``
* ``testimonial``

All that remains is some proper CSS

.. toctree::
   :maxdepth: 2
   :caption: Episodes

   01_intro
   02_rst_tests
   03_md_tests
   04_executing
   05_jupyter
   06_convert-old-lesson

.. toctree::
   :caption: Other material

   cheatsheet
   guide

Installation and usage
----------------------

This is distributed as a normal Sphinx extension, so it is easy to
use.  To use it, install ``sphinx_lesson`` via PyPI (note: it is not
there yet, this may not be the name).

Then, enable the extension in your Sphinx ``conf.py``.  This will both
define our special directives, and load the other required extensions
(``myst_nb``).  The ``myst_nb`` extension can be configured normally::

  extensions = [
      'sphinx_lesson',
  ]

We are in theory compatible with any theme, but are most tested with
the sphinx_rtd_theme::

  html_theme = 'sphinx_rtd_theme'



* :ref:`genindex`
* :ref:`search`
