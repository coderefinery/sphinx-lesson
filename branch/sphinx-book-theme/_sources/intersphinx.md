# Intersphinx: easy linking

There is a common problem: you want to link to documentation in other
sites, for example the documentation of `list.sort`.  Isn't it nice
to have a structured way to do this so you don't have to a) look up a
URL yourself b) risk having links break?  Well, what do you know,
Sphinx has a native solution for this: {py:mod}`Intersphinx
<sphinx.ext.intersphinx>`.

## Enable the extension

It's built into Sphinx, and in the sphinx-lesson-template `conf.py` but
commented out.  Enable it:

```python
extensions.append('sphinx.ext.intersphinx')
intersphinx_mapping = {
  'python': ('https://docs.python.org/3', None),
  }
```

Configuration details and how to link to other sites are found at
{py:mod}`the docs for intersphinx <sphinx.ext.intersphinx>`.
For most Sphinx-documented projects, use the URL of the documentation
base.  See "Usage" below for how to verify the URLs.

## Usage

Just like `:doc:` is a structured way to link to other documents,
there are other **domains** of links, such as `:py:class:`,
`:py:meth:`, and so on.  So we can link to documentation of a class
or method like this:

:::{admonition} Rendered (note the links)
The {py:class}`list` class {py:meth}`sort <list.sort>` method.
:::

```rst
# Restructured Text
The :py:class:`list` class :py:meth:`sort <list.sort>` method.
```

```md
# MyST markdown
The {py:class}`list` class {py:meth}`sort <list.sort>` method.
```

Note that this is structured information, and thus has no concept in
Markdown, only MyST "markdown".  This is, in fact, a major reason why
plain markdown is not that great for structured documentation.

## Available linking domains and roles

Of course, the domains are extendable.  Presumably, when you use
sphinx-lesson, you will be referring to other things.  The most
common roles in the Python domain are:

- `:py:mod:`: modules, e.g. {py:mod}`multiprocessing`
- `:py:func:`: modules, e.g. {py:func}`itertools.combinations`
- `:py:class:`: modules, e.g. {py:class}`list`
- `:py:meth:`: modules, e.g. {py:meth}`list.sort`
- `:py:attr:`: modules, e.g. {py:attr}`re.Pattern.groups`
- `:py:data:`: modules, e.g. {py:data}`datetime.MINYEAR`
- Also `:py:exc:`, `:py:data:`, `:py:obj:`, `::`, `::`
- There are also built-in domains for C, C++, JavaScript (see
  [the info on Sphinx domains](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html) for what the roles are).
  Others are  added by Sphinx extensions.

You can list all available reference targets at some doc using a
command line command.  You can get the URL from the conf.py file (and
use this to verify URLs before you put it in the conf.py file):

```shell
# Note we need to append `objects.inv`:
python -m sphinx.ext.intersphinx https://docs.python.org/3/objects.inv
# In conf.py: 'python': ('https://docs.python.org/3', None),
```

You usually use the fully qualified name of an object, for example
`matplotlib.pyplot.plot`.  In Python this is usually pretty obvious,
due to clear namespacing.  You'll have to look at other languages
yourself.

## See also

- [Sphinx: domains](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html) - how to
  document classes/functions to be referrable this way, and link to them.
- {py:mod}`Intersphinx <sphinx.ext.intersphinx>`.
