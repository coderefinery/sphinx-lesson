Sphinx test lesson
==================

This is a Sphinx extension for software-carpentry style
lessons.  It is designed as a replacement for the Jekyll-based software
templates.

`View it on github pages
<https://coderefinery.github.io/sphinx-lesson/>`__.



Features
--------

- Sphinx, including power from all of its extensions.
- ReST
- Markdown via the `myst_parser` parser, so has access to all Sphinx
  directives natively
- Jupyter as a source format, including executing the notebook (via
  ``myst_nb``).
- Automatically building via Github Actions and automatic deployment
  to Github Pages.  Included workflow file builds all branches, so you
  can also preview pull requests.
- Directives for exercises/prereq/etc, works in both ReST and md.
- The Sphinx part can be separated into a separately installable
  and versionable Python package, so we don't need git sub-modules.
- Execute code cells in markdown (via ``myst_nb``).
- Consists of sub-extensions for substitutions.  Adding
  ``sphinx_lesson`` as an extension will bring in these:

  - ``sphinx_lesson.directives`` (the core directives)
  - ``sphinx_lesson.md_transforms`` (reprocess some other markdown
    format into myst_nb format)
  - ``myst_nb`` (not developed by us)



Status
------

In beta use by CodeRefinery and active development.  External users
would be fine (but let us know so we know to keep things stable).
