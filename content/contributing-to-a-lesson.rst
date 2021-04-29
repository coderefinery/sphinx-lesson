Quickstart: Contributing to a lesson
====================================

If you are at this page, you might want to quickly contribute to some
existing material using the ``sphinx-lesson`` format.  Luckily, this
is fairly easy:

* Get the source
* Edit the material in the ``content/`` directory
* (optional) Set up the Python environment and preview
* Send your contribution

In summary, each lesson is a Python project, with content in the
``content/`` directory.  It uses the Sphinx documentation system,
which is a popular, extendable tool.  We have only minor extensions to
make it suitable to lessons.

Instead of going through this process, you can also open an issue
instead with your proposed change, and let someone else add it.

.. highlight:: console



Get the lesson material
-----------------------

You need to consult with the lesson you would like to edit.  If this
is using the ``git`` version control system on Github, you could clone
it like this::

  $ git clone git://github.com/ORGANIZATION/LESSON.git

`CodeRefinery's git-intro lesson
<https://coderefinery.github.io/git-intro/>`__ explains more.

Edit the material
-----------------

The material is in the ``content/`` directory.  Depending on the
lesson, in may be in ReStructured Text, MyST Markdown, or Jupyter
notebooks.

ReStructured Text and MyST Markdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will probably copy existing examples, but you can also see
:doc:`our quick guide <md-and-rst>`.  The main thing to note is that
this is not unstructured Markdown, but there are particular
(non-display) **directives** and **roles** to tag blocks and inline
text.  (In fact, "markdown" is a broad concept and everyone uses some
different extensions of it).

* :doc:`md-and-rst`
* :ref:`ReStructured Text reference <sphinx:rst-primer>`
* `MyST reference <https://myst-parser.readthedocs.io/en/latest/using/syntax.html>`__
* :doc:`sphinx-lesson directives for markup <directives>`

*Do not worry about getting syntax right*.  Send your improvement, and
editing is easy and you will learn something.

Jupyter notebooks
~~~~~~~~~~~~~~~~~

Jupyter notebooks are a common format for computational narratives,
and can be natively used with Sphinx via `myst-nb
<https://myst-nb.readthedocs.io/>`__.  Note that you should use MyST
Markdown directives and roles (see previous section) in the notebook
to give structure to the material.

Again, *do not worry about getting the syntax right*.  This is the
least important part of things.



Build and test locally
----------------------

Generic: The ``requirements.txt`` file includes all Python dependencies
to build the lesson.  The lesson can be built with ``sphinx-build -M
html content/ _build``, or ``make html`` if you have Make installed.

Or in more detail:

Create a virtual environment to install the requirements (a conda
environment would work just as well)::

  $ python3 -m venv venv/
  $ source venv/bin/activate

.. note::

   if ``python3 -m venv venv/`` does not work, try with ``python -m venv venv/``

Then upgrade pip inside the virtual environment and install dependencies (it is recommended that conda base environment is deactivated)::

  $ pip install --upgrade pip
  $ pip install -r requirements.txt

You can build it using either of these commands::

  $ sphinx-build -M html content/ _build
  $ make html    # if you have make installed

And then view it with your web browser.  Remove the ``_build``
directory to force a clean rebuild (or ``make clean``).

Or you can use the **Sphinx autobuilder**, which will start a process
that rebuilds it on every change, and starts a web server to view it.
It will tell you how to access the server::

  $ sphinx-autobuild content/ _build/
  ...
  [I ...] Serving on http://127.0.0.1:8000


Sending your changes back
-------------------------

This depends on the project, but can be done using Github pull
requests.  `CodeRefinery's git-collaborative lesson
<https://coderefinery.github.io/git-collaborative/>`__ goes into
details about pull requests.


Other things to keep in mind
----------------------------

* Make sure that you have rights to submit your change.  In general,
  if you reuse anything else that already exists, explain this in your
  pull request.
* *Content and ideas are more important than markup*.  Don't worry
  about doing something wrong, that is why we have review!
* Many different people use the lessons.  Ask before doing things that
  make the lesson too specific to your use case.
