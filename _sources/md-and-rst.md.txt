# Markdown and ReST

Sites can be written in Markdown on ReStructured Text.  Actually, in
theory any format that has a Sphinx parser could be used, however you
will be slightly limited without directive support.

The most important thing to note is that: To make a structured lesson,
one needs to write in something a bit more structured than HTML.

## Markdown

Markdown is the most common syntax for CodeRefinery lessons.  It's not
raw markdown but the MyST flavor, which has *much* more structured
directives than plain markdown.  These come straight from Sphinx and
what we use to

[MyST syntax reference](https://myst-parser.readthedocs.io/en/latest/using/syntax.html)


:::{note}
What is Markdown?  Markdown isn't a single language.  Its native form
is a simple syntax for HTML, and isn't very structured.  There are many different
flavors, some of which add extra syntax which gets it closer to
enough, but for our purposes these are different enough that they
should count as different languages (as similar as "markdown" and
ReST).  Since the Markdown creator says that [Markdown shouldn't
evolve or be strictly defined](https://en.wikipedia.org/wiki/Markdown#CommonMark), Markdown is
essentially a dead syntax: we should always specific which living
sub-syntax you are referring to.

sphinx-lesson uses the [MyST-parser] (MarkedlY Structured Text),
which is both completely compatible with CommonMark, and also supports
*all ReStructured Text directives*, unlike most other non-ReST Sphinx
parsers.  Thus, we finally have a way to write equivalent ReST and
Markdown without any compromises (though other CommonMark parsers
aren't expected to know Sphinx directives).
:::

## ReStructured Text

ReStructured Text has native support for roles and directives, which
makes it a more structured language such as LaTeX, rather than HTML.
It came before Sphinx, but Sphinx made it even more popular.

[ReST reference (from Sphinx)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

## MD and ReST syntax

This is a brief comparison of basic syntax:

ReST syntax (Sphinx has a good [restructured text primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html):

MyST markdown syntax:

````md
*italic*
**bold**
`literal`
# Heading

[inline link](https://example.com)
[link to page](relative-page-path)

structured links:
{doc}`link to page <page-filename>`
{ref}`page anchor link <ref-name>`
{py:mod}`intersphinx link <multiprocessing>`


```
code block
```
````

```rst
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
```

The most interesting difference is the use of single backquote for
literals in Markdown, and double in ReST.  This is because ReST uses
single quotes for *roles* - notice how there is a dedicated syntax for
inter-page links, references, and so on (it can be configured to
"figure it out" if you want).  This is very important for
things like verifying referential integrity of all of our pages.  But
this is configurable with [default_role](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-default_role):
set to `any` to automatically detect documents/references/anthing,
or `literal` to automatically be the same as literal text.

## Directives

A core part of any Sphinx site is the directives: this provides
structured parsing for blocks of text.  For example, we have an
`exercise` directive, which formats a text block into an exercise
callout.  This is not just a CSS class, it can do anything during the
build phase (but in practice we don't do such complex things).

### MyST directives

MyST-parser directives are done like this:

````md
:::{exercise}
:option: value

content
:::
````


### ReST directives

ReST directives are done like this:

```rst
.. exercise:: Optional title, some default otherwise
   :option: value

   This is the body

   You can put *arbitrary syntax* here.
```


## Roles

Roles are for inline text elements.  A lot like directives, they can
be as simple as styling or do arbitrary transformations in Python.

### ReST roles

Like this:

```rst
:rolename:`interpreted text`
```

### MyST roles

Like this:

```md
{rolename}`interpreted text`
```

[myst-parser]: https://github.com/executablebooks/myst-parser
