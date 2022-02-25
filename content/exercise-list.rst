Exercise list
=============

The ``exercise-list`` directive inserts a list of all exercises.  This
can be useful as an overall summary of the entire lesson flow,
onboarding new instructors and helpers, and more.

ReST::

  .. exerciselist::

MyST::

  ```{exerciselist}```

Note that it includes the page names, links to the exercises, and the
exercise directive contents itself.  Note that the context is missing,
so it is important to give a good name to the exercise so that it
makes sense to a reader.  An example of an exercise with a title::

  .. exercise:: Demonstrate basic addition

     What is 1+1?

This feature is new as of early 2022, there may be possible problems
in it still - please report.



Example
-------

This section contains the exercise list of sphinx-lesson.  Note that
the directives occur many times in random contexts, so many of them
don't really make sense.  Keep in mind how to ensure that your cases
are better.

.. exerciselist::
