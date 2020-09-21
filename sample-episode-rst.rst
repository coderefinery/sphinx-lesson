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

.. challenge:: SampleLesson-1 Getting familiar

   1. **Exercise title:** Notice the exercise set has both an ID and
      number ``SampleLesson-1`` and description of what it contains.

   2. **Create a lesson:** Similarly, each exercise has a quick
      description title ``Create a lesson`` in bold.  These titles are
      useful so that helpers (and learners...) can quickly understand
      what the point is.


.. solution::

   * **Exercise title** solution here.

   * **Create a lesson** solution to that one.


Another section
---------------

.. instructor-note::

   This is an instructor note.  It may be hidden or put to the sidebar
   in a later style.  You should use it for things that the instructor
   should see while teaching, but should be de-emphasized for the
   learners.

A subsection
~~~~~~~~~~~~

.. figure:: img/sample-image.png

   Figure caption here.


.. figure:: img/sample-image.png
   :class: with-border

   Figure caption here, which explains the content in text so that
   it's accessible to screen readers.


.. keypoints::

   - What the learner should take away
   - point 2
   - ...
