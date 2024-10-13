# Building the lesson

```{highlight} console
```

It is built the normal Sphinx ways.  Using Sphinx directly, one would
run:

```
$ sphinx-build -M html content/ _build
```

If you have `make` installed, you can:

```
$ make html
## or
$ make dirhtml
## full build
$ make clean html
```

However, there are different ways to set up a Sphinx project.
CodeRefinery lessons puts the results in `_build/`.
