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

  - Making good summaries is really an important skill for organizing
    anything - give this the attention it needs.

  - Think of an exercise leader or helper coming to help someone, seeing
    the exercise, and needing to help someone: not just what to do,
    but what the core lesson and task is, so that they can focus on
    giving the right help (and telling the learners what they don't
    need to worry about).

  - Context can be both in the exercise title and in the exercise body
    itself.

- Name the exercises well.  Best is to think of it like a version
  control commit: an imperative sentence stating what the person will
  do in the exercise.  For example::

    Make your first git commit
    Resolve the conflict

- In the title, include any other important information (see below)::

    Create a setup.py file for your package (15 min)
    (optional) Install your package in editable mode using ``pip install -e`` (5 min)
    (advanced) Also create packaging using pyproject.toml and compare (20 min)

- Consider giving your exercises permanent identifiers.  They are not
  auto-numbered yet for a reason (what happens when more exercises are
  added/removed?), but if you give them an ID, they will be findable
  even later.  Suggestion is ``Episodetopic-N``::

    Basic-1: Verify git is installed
    Basic-2: Initialize the repository
    Conflicts-2: Create a new branch for the other commit.
    Internals-1: (advanced): Inspect individual objects with ``git cat-file``

  - It could include not just what you do, but a bit about why you are
    doing it and what you are learning.

- The list includes only ``exercise``, ``type-along``, and ``solution``.  For
  backwards compatibility, ``challenge`` is also included.

- Optional or advanced exercises should clearly state it in the
  exercise title, since people will browse the list separate from the
  main lesson material.


Example
-------

This section contains the exercise list of sphinx-lesson.  Note that
the directives occur many times in random contexts, so many of them
don't really make sense.  Keep in mind how to ensure that your cases
are better.

.. exerciselist::
