Sphinx test lesson
==================

This is a Sphinx lesson template for a software-carpentry style
lesson.  It is designed as a replacement for the Jekyll-based software
templates (but we don't know if it will be used yet).

`View it on github pages
<https://coderefinery.github.io/sphinx-test-lesson/>`__.

Features
--------

- Sphinx
- ReST
- Markdown via the `myst_parser` parser, so has access to all Sphinx
  directives natively
- Automatically building via Github Actions and automatic deployment
  to Github Pages.
- Directives for exercises/prereq/etc, works in both ReST and md.
- The Sphinx part can be separated into a separately installable
  and versionable Python package, so we don't need sub-modules.
- Jupyter includes, including executing the notebook (via
  ``myst_nb``).
- Execute code cells in markdown (via ``myst_nb``).


To activate the github pages branch
-----------------------------------

... it may be necessary to flip the github pages config setting to
master and back, and then re-push.

