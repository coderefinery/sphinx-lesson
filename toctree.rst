Table of Contents tree
======================

Pages are not found by globbing a pattern: you can explicitly define a
table of contents list.  There must be one master toctree in the index
document, but then they can be nested down.  For the purposes of
sphinx-lesson, we probably don't need such features

ReST::

  .. toctree::
  caption: Episodes
  maxdepth: 1

  basics
  creating-using-web
  creating-using-desktop
  contributing
  doi
  websites


MyST::

  ```{toctree}
  ---
  caption: Episodes
  maxdepth: 1
  ---

  basics
  creating-using-web
  creating-using-desktop
  contributing
  doi
  websites
  ```

The pages are added by filename (no extension needed).  The name by
default comes from the document title, but you can override it if you
want.

You can have multiple toctrees: check sphinx-test-lesson, we have one
for the episodes, and one for extra material (like quick ref and
instructor guide).
