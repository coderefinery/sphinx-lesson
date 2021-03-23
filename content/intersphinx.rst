Intersphinx: easy linking
=========================

There is a common problem: you want to link to documentation in other
sites, for example the documentation of ``list.sort``.  Isn't it nice
to have a structured way to do this so you don't have to a) look up a
URL yourself b) risk having links break?  Well, what do you know,
Sphinx has a native solution for this: :std:doc:`Intersphinx
<usage/extensions/intersphinx>`.



Enable the extension
--------------------
It's built into Sphinx, and in the sphinx-lesson-template ``conf.py`` but
commented out.  Enable it:

.. code-block:: python

  extensions.append('sphinx.ext.intersphinx')
  intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    }



Usage
-----

Just like ``:doc:`` is a structured way to link to other documents,
there are other **domains** of links, such as ``:py:class:``,
``:py:meth:``, and so on.  So we can link to documentation of a class
or method like this:

.. admonition:: Rendered (note the links)

   The :py:class:`list` class :py:meth:`sort <list.sort>` method.

.. code-block:: rst

   # Restructured Text
   The :py:class:`list` class :py:meth:`sort <list.sort>` method.

.. code-block:: md

   # MyST markdown
   The {py:class}`list` class {py:meth}`sort <list.sort>` method.

Note that this is structured information, and thus has no concept in
Markdown, only MyST "markdown".  This is, in fact, a major reason why
plan markdown is hardly suitable for complex docs.



See also
--------

* :std:doc:`Sphinx: domains <usage/restructuredtext/domains>` - how to
  document classes/functions to be referrable this way, and link to them.
* :std:doc:`Intersphinx <usage/extensions/intersphinx>`.
