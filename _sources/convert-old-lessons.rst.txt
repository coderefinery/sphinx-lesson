Converting an old lesson
========================

.. highlight: console


Convert a Jekyll lesson
-----------------------

This brings in the necessary files

Add the template lesson as a new remote::

   git remote add s-l-t https://github.com/coderefinery/sphinx-lesson-template.git
   git fetch s-l-t

Check out some basic files into your working directory.  Warning: if
you add a ``.github/workflows/sphinx.yml`` file, even a push to a
branch will **override github pages**::

   git checkout s-l-t/main -- requirements.txt
   git checkout s-l-t/main -- .github/workflows/sphinx.yml

If you need more Sphinx files::

   git checkout s-l-t/main -- content/conf.py
   git checkout s-l-t/main -- .gitignore Makefile make.bat

If you need the full content (only ``index.rst`` for now)::

   git checkout s-l-t/main -- content/

(if jekyll conversion) Move content over::

  git mv _episodes/* content/

(if jekyll conversion) Copy stuff from ``index.md`` into ``content/index.rst``.

(if jekyll conversion) Remove old jekyll stuff::

  git rm jekyll-common/ index.md _config.yml Gemfile .gitmodules

Set up github pages (first commit to trigger CI), see :doc:`installation`::

  git checkout -b gh-pages origin/gh-pages
  git commit -m 'empty commit to trigger gh-pages' --allow-empty
  git push

Do all the rest of the fixing... all the bad, non-portable,
non-relative markdown and so on.  This is the hard part.  Common
problems:

* Non-consecutive section headings
* Multiple top-level section headings (there should be one top-level
  section heading that is the page title)
* Weird relative links (most work though)


You can also update your local view of the default branch::

  git remote set-head origin --auto



Joint history
-------------

This option joins the histories of the two repositories, so that you
could merge from the template repository to keep your files up to
date.  **This may not currently work**, and also may not have any
value (but is kept here for reference until later).

Merge the two unrelated histories::

   $ git remote add template https://github.com/coderefinery/sphinx-lesson-template
   $ git fetch template
   $ git merge template/main --allow-unrelated-histories
   # Resolve any possible merge conflicts
   $ git checkout --theirs .gitignore
   $ git checkout --ours LICENSE
   $ git add .gitignore LICENSE
   $ git commit -m 'merge sphinx-lesson history to this lesson'

Then proceed like the previous section shows.
