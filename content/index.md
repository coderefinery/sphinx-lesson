# sphinx-lesson: structured lessons with Sphinx

:::{seealso}
See a real demo lesson at
<https://coderefinery.github.io/github-without-command-line/>.
:::

sphinx-lesson is a set of Sphinx extensions and themes for creating
interactive, hands-on lessons.  It was originally made to replace the
CodeRefinery jekyll themes, but is designed to be used by others.

As the name says, it is based on the [Sphinx documentation generator](https://www.sphinx-doc.org/).  It is also inspired by and based on
[jupyter-book](https://jupyterbook.org/), but both is jupyter-book
and isn't.  It *is* because jupyter-book is based on Sphinx and
modular, we reuse all of those same Sphinx extensions which
jupyter-book has made.  It *isn't* jupyter-book because we configure
Sphinx directly, instead of wrapping it through jupyter-book
configuration and building.  Thus, we get full control and high
compatibility.

Features:

- Separate content and presentation: easy to adjust theme or control
  the parts independently.
- Based on jupyter-book, cross-compatible.
- Built with Sphinx, providing a structured, controlled output.
- Distributed as Python pip packages
- Markdown and ReStructured equally supported (yes, including all
  directives), though ReStructured Text is still a bit nicer
- Jupyter notebooks as an input format.  Can execute code (in jupyter
  and other formats, too)
- Transparent transformation of jekyll-style markdown styles into
  CommonMark with directives
- Also renders with sphinx-book-theme (theme of jupyterbook) ([preview](https://coderefinery.github.io/sphinx-lesson/branch/sphinx-book-theme/))

This is in an alpha state: we use it for lessons, but there is still
refinement work to go.

:::{prereq}
- If you know Sphinx, it helps some.  If not, it's easy to copy
- Markdown or ReStructured text
- Hosting is usually by github-pages
:::

```{toctree}
:caption: Getting started
:maxdepth: 1

getting-started
installation
contributing-to-a-lesson
building
changelog
```

```{toctree}
:caption: Basic syntax
:maxdepth: 1

md-and-rst
toctree
directives
figures
```

```{toctree}
:caption: Examples
:maxdepth: 1

sample-episode-myst
sample-episode-rst
```

```{toctree}
:caption: Advanced features
:maxdepth: 1

intersphinx
md-transforms
jupyter
executing-code
substitutions-replacements
gh-action
presentation-mode
indexing
exercise-list
convert-old-lessons
```

```{toctree}
:caption: Extras
:maxdepth: 1

cheatsheet
```

- {ref}`genindex`
- {ref}`search`
