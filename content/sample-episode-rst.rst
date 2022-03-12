Sample episode in ReST
======================

.. questions::

   - How does a typical lesson page look?
   - Questions list questions to get the interest of learners
   - point 2
   - ...

.. objectives::

   - Show a complete lesson page with all of the most common
     structures.
   - Objectives list what you get out of the page (not just what
     you do)
   - point 2
   - ...


Topic introduction here

You really want to browse this page alongside the source of it, to see
how this is implemented.  See the links at the to right of the page.



This is a section
-----------------

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


Exercise: the general topic
---------------------------

Exercises get their own section, so that they can be linked and found
in the table of contents.

.. exercise:: 1.1 Exercise title

   1. Notice the exercise set has both an ID and
      number ``SampleLesson-1`` and description of what it contains.

.. solution::

   * Solution here.


.. exercise:: 1.2 Create a lesson

   2. Similarly, each exercise has a quick description title ``Create
      a lesson`` in bold.  These titles are useful so that helpers
      (and learners...) can quickly understand what the point is.

.. solution::

   * Solution to that one.


.. exercise:: Exercise with embedded solution

   2. Similarly, each exercise has a quick description title ``Create
      a lesson`` in bold.  These titles are useful so that helpers
      (and learners...) can quickly understand what the point is.

   .. solution::

      * Solution to that one.

.. exercise:: Exercise with embedded solution

   3. Exercise with a :doc:`link <index>`, or :ref:`internal reference
      <exerciselist_recommendations>`.



Another section
---------------

.. instructor-note::

   This is an instructor note.  It may be hidden or put to the sidebar
   in a later style.  You should use it for things that the instructor
   should see while teaching, but should be de-emphasized for the
   learners.


These tab synchronize with those above:

.. tabs::

   .. code-tab:: py

      import cmath
      a = 10 / 2

   .. code-tab:: r R

      library(x)
      a <- 10 / 2



A subsection
~~~~~~~~~~~~

.. figure:: img/sample-image.png

   Figure caption here.


.. figure:: img/sample-image.png
   :class: with-border

   Figure caption here, which explains the content in text so that
   it's accessible to screen readers.


Other directives
----------------

.. important::

   Test

.. warning::

   Test

.. seealso::

   Test


See also
--------

* Upstream information
* Another course



.. keypoints::

   - What the learner should take away
   - point 2
   - ...
