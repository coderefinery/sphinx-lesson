Sample episode in ReST
======================

.. questions::

   - What syntax is used to make a lesson?
   - How do you structure a lesson effectively for teaching?

   ``questions`` are at the top of a lesson and provide a starting
   point for what you might learn.  It is usually a bulleted list.
   (The history is a holdover from carpentries-style lessons, and is
   not required.)

.. objectives::

   - Show a complete lesson page with all of the most common
     structures.
   - ...

   This is also a holdover from the carpentries-style.  It could
   usually be left off.


A first paragraph really motivating *why* you would need the material
presented on this page, and why it is exciting.  Don't go into details.

Then, another paragraph going into the big picture of *what* you will
do and *how* you will do it.  Not details, but enough so that someone
knows the overall path.

[For the syntax of ReST, you really want to browse this page alongside the
source of it, to see how this is implemented.  See the links at the to
right of the page.]



Section titles should be enough to understand the page
------------------------------------------------------

The first paragraph of each section should again summarize what you
will do in it.

Top-level section titles are the map through the page and should make
sense together.

This is text.

A code block with preceeding paragraph::

  import multiprocessing

* A bullet list

* Bullet list

  * Sub-list::

      code block (note indention)

  .. note::

     directive within a list (note indention)

.. tabs::

   .. code-tab:: py

      import bisect
      a = 1 + 2

   .. code-tab:: r R

      library(x)
      a <- 1 + 2

.. discussion:: This is a `discussion` directive

   Discussion content.


Exercise: [the general topic]
-----------------------------

These exercises will show basic exercise conventions.  It might be
useful for the first paragraph of a multi-exercise section to tie them
together to the overall point, but that isn't necessary.

[Exercises get their own section, so that they can be linked and found
in the table of contents.]

.. exercise:: ReST-1 Imperative statement of what will happen in the exercise.

   An intro paragraph about the exercise, if not obvious.  Expect that
   learners and exercise leaders will end up here without having
   browsed the lesson above.  Make sure that they understand the
   general idea of what is going on and *why* the exercise exists
   (what the learning objective is roughly, for example there is a big
   difference between making a commit and focusing on writing a good
   commit message and knowing the command line arguments!)

   1. Bullet list if multiple parts.
   2. Despite the names, most exercises are not really "exercises" in
      that the are difficult.  Most are rather direct applications of
      what has been learned (unless they are ``(advanced)``).
   3. When writing the exercise steps, try to make it clear enough
      that a helper/exercise leader who knows the general tools
      somewhat well (but doesn't know the lesson) can lead the
      exercise just by looking at the text in the box.

      - Of course that's not always possible, sometimes they actually
	are difficult.

.. solution::

   * Solution here.


.. exercise:: (optional) ReST-2 Imperative statement of what will happen in the exercise.

   1. Optional exercises are prefixed with ``(optional)``
   2. It's better to have more exercises be optional than many that
      are made optional ad-hoc.  Every instructor may do something
      different, but it's better to seem like you are covering all the
      main material than seem like you are skipping parts.

.. solution::

   * Solution to that one.


.. exercise:: (optional) ReST-3: Exercise with embedded solution

   1. This exercise has the solution within its box itself.  This is a
      stylistic difference more than anything.

   .. solution::

      * Solution to that one.

.. exercise:: (advanced) ReST-4: Exercise with embedded solution

   1. ``(advanced)`` is the tag for things which really require
      figuring out stuff on your own.  Can also be ``(advanced,
      optional)`` but that's sort of implied.
   2. This also demonstrates an exercise with a :doc:`link <index>`,
      or :ref:`internal reference <exerciselist_recommendations>`.



This entire section is an exercise
----------------------------------

.. admonition:: Exercise leader setup
   :class: dropdown

   This admonition is a drop-down and can be used for instructor or
   exercise-leader specific setup.  (see also / compare with
   ``instructor-note``.

.. exercise:: In this section, we will [do something]

   Standard intro paragraph of the exercise.

   Describe how this exercise is following everything that is in this
   section.

Do this.

Then do that.

And so on.



Another section
---------------

.. instructor-note::

   This is an instructor note.  It may be hidden, collapsed, or put to
   the sidebar in a later style.  You should use it for things that
   the instructor should see while teaching, but should be
   de-emphasized for the learners.  Still, we don't hide them for
   learners (instructors often present from the same view.)


These tab synchronize with those above:

.. tabs::

   .. code-tab:: py

      import cmath
      a = 10 / 2

   .. code-tab:: r R

      library(x)
      a <- 10 / 2

.. admonition:: Advanced info that should be hidden
   :class: dropdown

   Any advanced information can be hidden behind any admonition by
   adding a ``dropdown`` class to it (syntax: ``:class: dropdown`` as
   first line separated by a space).

   This can be useful for advanced info that should not be show in the
   main body of text..




A subsection
~~~~~~~~~~~~

Subsections are fine, use them as you want.  But make sure the main
sections tell the story and provide a good table of contents to the
episode.

.. figure:: img/sample-image.png

   Figure caption here.


.. figure:: img/sample-image.png
   :class: with-border

   Figure caption here, which explains the content in text so that
   it's accessible to screen readers.


Other directives
----------------

.. seealso::

   A reference to something else.  Usually used at the top of a
   section or page to highlight that the main source of information is
   somewhere else.  Regular-importance "see also" is usually at a
   section at the bottom of the page or an a regular paragraph text.

.. important::

   This is used for things that should be highlighted to prevent
   significant confusion.  It's not *that* often used.

.. warning::

   Something which may result in data loss, security, or massive
   confusion.  It's not *that* often used.



What's next?
------------

Pointers to what someone can learn about next to expand on this topic,
if relevant.



Summary
-------

A summary of what you learned.



See also
--------

A "see also" section is good practice to show that you have researched
the topic well and your lesson becomes a hub pointing to the other
best possible resources.

* Upstream information
* Another course



.. keypoints::

   - What the learner should take away
   - point 2
   - ...

   This is another holdover from the carpentries style.  This perhaps
   is better done in a "summary" section.
