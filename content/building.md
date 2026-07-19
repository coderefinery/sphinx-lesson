# Building the lesson

```{highlight} console
```

You build the lesson [the normal Sphinx
ways](https://www.sphinx-doc.org/en/master/man/sphinx-build.html).
Using Sphinx directly, one would run:

```
$ sphinx-build -M html content/ _build
```

If you have `make` installed, you can:

```
$ make html
## or
$ make dirhtml

## full build
$ make clean dirhtml
```

The most common Sphinx builders are `html` (build pages ending with
.html) and `dirhtml` (build pages ending with `pagename/index.html`
for nice `your-site/pagename/` links).  When you use semantic document
links, all interlinking automatically works.

However, there are different ways to set up a Sphinx project and you
can use any of them.  CodeRefinery lessons puts the results in
`_build/`.  The {doc}`gh-action` can also automatically build a
single-HTML page, epub, and PDF file outputs because learners have
sometimes wanted these different formats.
