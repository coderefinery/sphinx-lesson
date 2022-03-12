Exercise list
=============

The ``exercise-list`` directive inserts a list of all exercises.  This
can be useful as an overall summary of the entire lesson flow,
onboarding new instructors and helpers, and more.

ReST::

  .. exerciselist::

MyST::

  ```{exerciselist}```


This feature is new as of early 2022, there may be possible problems
in it still - please report.



.. _exerciselist_recommendations:

Recommendations to make a useful list
-------------------------------------

- Context is important!  Give your exercises a name other than the
  default of "Exercise", so that someone quickly scanning the exercise
  list can follow the overall flow.

  - It could include not just what you do, but a bit about why you are
    doing it and what you are learning.

  - Think of an exercise leader or helper coming to help someone, seeing
    the exercise, and needing to help someone: not just what to do,
    but what the core lesson and task is, so that they can focus on
    giving the right help (and telling the learners what they don't
    need to worry about).

  Example:

  .. exercise:: Demonstrate basic operators

     What is 1+1?


- The list includes only ``exercise``, ``type-along``, and ``solution``.  For
  backwards compatibility, ``challenge`` is also included.



Example
-------

This section contains the exercise list of sphinx-lesson.  Note that
the directives occur many times in random contexts, so many of them
don't really make sense.  Keep in mind how to ensure that your cases
are better.

.. exerciselist::
