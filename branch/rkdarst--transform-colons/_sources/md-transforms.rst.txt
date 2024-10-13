Markdown transforms
===================

To ease the transition from other Markdown dialects(like the one used
in software-carpentry), we implement some transformations in sphinx.
These are implemented in the ``sphinx_lessons.md_transforms`` Python
package and are implemented using regular expressions, so they are a
bit fragile.

Code fences
-----------

Code fence syntax is translated to CommonMark.  Input::

        ```
        blah
        ```
        {: output}

Output::

        ```{output}
        blah
        ```

Block quotes
------------

Transform CSS styles into MyST directives (implemented as code
fences.  Input::

        > ## some-heading
        > text
        > text
        {: .block-class}

Output::

        ```{block-class} some-heading
        text
        text
        ```

The ``block-class`` is the directive name (we maintain compatibility
with old jekyll-common)

Raw HTML images
---------------

Raw HTML isn't a good idea in portable formats.  Plus, in the old
jekyll formats, bad relative path handling caused absolute paths to be
embedded a lot.Transform this::

        <img src="/path/to/img.png">

into this::

        ```{figure} /path/to/img.png
        ```

Exclude any possible ``{{ ... }}`` template variables used to
semi-hard code absolute paths.

Triple colons
-------------

Since MyST directive blocks are actually literal code blocks, other
markdown parsers will show the text inside as literal text, not
interpreted markdown.  This may be inconvenient.  This is why there is
a "colon" syntax for directives, so that any other markdown parser
(for example, Github preview) *will* process the embedded text as
markdown.

For example, this text will *not* have the link work on GitHub
preview, and the text won't wrap well::

  ```{seealso}

  See the [sphinx-lesson](https://github.com/coderefinery/sphinx-lesson/) documentation for more information.
  ```

While this will have a good preview::

  :::{seealso}

  See the [sphinx-lesson](https://github.com/coderefinery/sphinx-lesson/) documentation for more information.
  :::

MyST parser [can do this
mapping](https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html#admonition-directives),
but it *only* does it for certain directives, which doesn't include
sphinx-lesson directives.

The version included in ``sphinx_lesson.md_transforms`` also handles
embedded directives.

If you set the ``sphinx_lesson_transform_colon_directives`` to
``True`` (default: ``True``), then any leading colons like this will
be transformed to backquotes transparently, which will work for any
directive.  There are some risks of false positives if a line starts
with more than three colons, but we have some heuristics to prevent
this: At least one line in the file must start with the regex
``^:::+\{[^}]+}`` for this to be used (unfortunately, we can't
filter based on whether the source is a ``.md`` file or not).
