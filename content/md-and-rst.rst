Markdown and ReST
=================

Sites can be written in Markdown on ReStructured Text.  Actually, in
theory any format that has a Sphinx parser could be used, however you
will be slightly limited without directive support.



Markdown
--------

Let's start off with a basic fact: Markdown isn't a language.  It's
some html-like markup that is not structured enough for the purposes
of structured sites such as sphinx-lesson.  There are many different
flavors, some of which add extra syntax which gets it closer to
enough, but for our purposes these are different enough that they
should count as different languages (as similar as "markdown" and
ReST).  Since the Markdown creator says that `Markdown shouldn't
evolve or be strictly defined
<https://en.wikipedia.org/wiki/Markdown#CommonMark>`__, Markdown is
essentially a dead syntax: you should always specific which living
sub-syntax you are referring to.

sphinx-lesson uses the `MyST-parser`_ (markedly structured text),
which is both completely compatible with CommonMark, and also supports
*all ReStructured Text directives*, unlike most other non-ReST Sphinx
parsers.  Thus, we finally have a way to write equivalent ReST and
Markdown without any compromises (though other CommonMark parsers
aren't expected to know Sphinx directives).

.. _MyST-parser: https://github.com/executablebooks/myst-parser

`MyST syntax reference <https://myst-parser.readthedocs.io/en/latest/using/syntax.html>`__


ReStructured Text
-----------------

ReStructured Text has native support for roles and directives, which
makes it a more structured language such as LaTeX, rather than HTML.

`ReST reference (from Sphinx) <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__


MD and ReST syntax
------------------

This is a brief comparison of basic syntax:

ReST syntax (Sphinx has a good `restructured text primer
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__::

    *italic*
    **bold**
    ``literal``

    Heading
    -------

    `inline link <https://example.com>`__
    `out-of-line link <example_>`__

    .. _example: https://example.com

    :doc:`page-filename`
    :ref:`ref-name`
    :py:mod:`multiprocessing`

    :doc:`link to page <page-filename>`
    :ref:`page anchor link <ref-name>`
    :py:mod:`intersphinx link <multiprocessing>`


    ::

       code block that is standalone (two
       colons before it and indented)

    Code block after paragraph::

      The paragraph will end with
      a single colon.


MyST markdown syntax::

    *italic*
    **bold**
    `literal`
    # Heading

    [inline link](https://example.com)

    [link to page](relative-page-path)

    ```
    code block
    ```

The most interesting difference is the use of single backquote for
literals in Markdown, and double in ReST.  This is because ReST uses
single quotes for *roles* - notice how there is a dedicated syntax for
inter-page links, references, and so on.  This is very important for
things like verifying referential integrity of all of our pages.  But
this is configurable with `default_role
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-default_role>`__:
set to ``any`` to automatically detect documents/references/anthing,
or ``literal`` to automatically be the same as literal text.



Directives
----------

A core part of any Sphinx site is the directives: this provides
structured parsing for blocks of text.  For example, we have an
``exercise`` directive, which formats a text block into an exercise
callout.  This is not just a CSS class, it can do anything during the
build phase (but in practice we don't do such complex things).

ReST directives
~~~~~~~~~~~~~~~

ReST directives are done like this::

  .. challenge:: Optional title, some default otherwise
     :option: value

     This is the body

     You can put *arbitrary syntax* here.

MyST directives
~~~~~~~~~~~~~~~

MyST-parser directives are done like this::

  ```{exercise}
  :option: value

  content
  ```



Roles
-----

Roles are for inline text elements.  A lot like directives, they can
be as simple as styling or do arbitrary transformations in Python.

ReST roles
~~~~~~~~~~

Like this::

  :rolename:`interpreted text`

MyST roles
~~~~~~~~~~

Like this::

  {rolename}`interpreted text`

