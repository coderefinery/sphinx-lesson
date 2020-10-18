sphinx-lesson: structured lessons with Sphinx
=============================================

.. seealso::

   See a real demo lesson at
   https://coderefinery.github.io/github-without-command-line/.

sphinx-lesson is a set of Sphinx extensions and themes for creating
interactive, hands-on lessons.  It was originally made to replace the
CodeRefinery jekyll themes, but is designed to be used by others.

As the name says, it is based on the `Sphinx documentation generator
<https://www.sphinx-doc.org/>`__.  It is also inspired by and based on
`jupyter-book <https://jupyterbook.org/>`__, but both is jupyter-book
and isn't.  It *is* because jupyter-book is based on Sphinx and
modular, we reuse all of those same Sphinx extensions which
jupyter-book has made.  It *isn't* jupyter-book because we configure
Sphinx directly, instead of wrapping it through jupyter-book
configuration and building.  Thus, we get full control and high
compatibility.

Features:

* Separate content and presentation: easy to adjust theme or control
  the parts independently.
* Based on jupyter-book, cross-compatible.
* Built with Sphinx, providing a structured, controlled output.
* Distributed as Python pip packages
* Markdown and ReStructured equally supported (yes, including all
  directives), though ReStructured Text is still a bit nicer
* Jupyter notebooks as an input format.  Can execute code (in jupyter
  and other formats, too)
* Transparent transformation of jekyll-style markdown styles into
  CommonMark with directives
* Also renders with sphinx-book-theme (theme of jupyterbook) (`preview
  <https://coderefinery.github.io/sphinx-lesson/branch/sphinx-book-theme/>`__)

This is in an alpha state: we use it for lessons, but there is still
refinement work to go.


.. prereq::

   * If you know Sphinx, it helps some.  If not, it's easy to copy
   * Markdown or ReStructured text
   * Hosting is usually by github-pages


.. toctree::
   :maxdepth: 1
   :caption: Getting started

   getting-started
   installation
   building
   changelog

.. toctree::
   :maxdepth: 1
   :caption: Basic syntax

   md-and-rst
   toctree
   directives
   figures

.. toctree::
   :maxdepth: 1
   :caption: Examples

   sample-episode-rst

.. toctree::
   :maxdepth: 1
   :caption: Advanced features

   md-transforms
   jupyter
   executing-code
   substitutions-replacements
   gh-action
   convert-old-lessons

.. toctree::
   :maxdepth: 1
   :caption: Extras

   cheatsheet



* :ref:`genindex`
* :ref:`search`
