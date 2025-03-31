# Getting started

## From a template repository

You can get started by making a Sphinx project and configuring the
extension.  We recommend you use the sphinx-lesson-template repository
(<https://github.com/coderefinery/sphinx-lesson-template>).

This template repository is updated with new copies of base files as
the lesson develops - you might want to check back for them, later.

## Convert an existing jekyll lesson

See {doc}`convert-old-lessons`.  This hasn't been used in years so may
be out of date.

## From scratch

See the next page, {doc}`installation`, for raw Python packages to
install and how to configure a arbitrary Sphinx project.

## Github Pages initial commit

The included Github Actions file will automatically push to Github
Pages, but due to some quirk/bugs in gh-pages *the very first
non-human gh-pages push won't enable Github Pages*.  So, you have to
do one push yourself (or go to settings and disable-enable gh-pages
the first time).

You can make an empty commit to gh-pages this way, which will trigger
the gh-pages deployment (and everything will be automatic after that):

```
git checkout -b gh-pages origin/gh-pages
git commit -m 'empty commit to trigger gh-pages' --allow-empty
git push
```

## Demo lessons

This guide can't currently stand alone.  It is probably good to look
at and copy from existing lessons for some things:

- Python for Scientific Computing uses many of the features:
  <https://aaltoscicomp.github.io/python-for-scicomp/> .
- Github without the command line is a complete lesson using the
  theme: <https://coderefinery.github.io/github-without-command-line/> .
