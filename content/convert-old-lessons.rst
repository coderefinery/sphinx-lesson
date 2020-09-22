Converting an old lesson
========================

.. highlight: console

First strategy
--------------

Merge the two unrelated histories::

   $ git remote add template https://github.com/coderefinery/sphinx-lesson-template
   $ git fetch template
   $ git merge template/master --allow-unrelated-histories
   # Resolve any possible merge conflicts
   $ git checkout --theirs .gitignore
   $ git checkout --ours LICENSE
   $ git add .gitignore LICENSE
   $ git commit -m 'merge sphinx-lesson history to this lesson'

Clean up some misc files::

  $ git rm README.rst  # assuming we keep the README.md file
  $ git rm 0*.{rst,md}
  $ git commit -m 'remove other unrelated files'
  $ git rm jekyll-common
  $ git commit -m 'remove jekyll-common'

Move lessons::

  $ ls _episodes/
  $ mv -i _episodes/* .
  $ rm -r _episodes/
  $ git commit -m 'move episodes to main tree'

Fix up index::

  # add episodes to toctree of the main lesson:
  $ vi index.rst
  # copy other info from index.md to index.rst (one could copy the structures to index.md instead)

Do all the rest of the fixing... all the bad, non-portable,
non-relative markdown and so on.  This is the hard part.


Second strategy
---------------

::

   git remote add s-l-t https://github.com/coderefinery/sphinx-lesson-template-empty.git
   git fetch s-l-t

These are basic files to check out::

   git checkout s-l-t/master -- requirements.txt
   git checkout s-l-t/master -- .github/workflows/sphinx.yml

If you need the full template::

   git checkout s-l-t/master -- .gitignore Makefile make.bat

If you need the full template::

   git checkout s-l-t/master -- .gitignore Makefile make.bat


Set up github pages (first commit to trigger CI)::

  git checkout -b gh-pages origin/gh-pages
  git commit -m 'empty commit to trigger gh-pages' --allow-empty
  git push
