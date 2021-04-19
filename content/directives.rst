Directives
==========

**Directives** are used to set off a certain block of text.  They can
be used as an aside or block (e.g. ``exercise``, ``instructor-note``).
If the content of the box would be long (e.g. an entire episode is a
``type-along``, or an entire section is an ``exercise``), you could use
the ``type-along`` directive to introduce the start of it but not put
all content in that directive.

Sphinx and docutils calls these type of directives **admonitions**
(and "directive" is a more general concept)



How to use
----------

Example of ``exercise``:

.. exercise::

   Some body text

.. exercise:: Custom title

   Some body text

.. exercise::

.. list-table::

   * * Markdown::

         ```{exercise}

         Some body text
         ```

       ::

         ```{exercise} Custom title

         Some body text
         ```

       ::

         ```{exercise}
         ```



     * ReST::

	 .. exercise::

	    Some body text

       ::

	 .. exercise:: Custom title

	    Some body text

       ::

	 .. exercise::


You notice these directives can have optional a custom title.  This is
an addition from regular Sphinx admonitions, and is *not* usable in
regular Sphinx admonition directives.  Also, unlike regular Sphinx
admonitions, the content in our directives is optional, if you want to
use it as a simple section header.


The ``solution`` directive begins collapsed (via `sphinx-togglebutton
<https://github.com/executablebooks/sphinx-togglebutton>`__):

.. solution::

   This is a solution

Directives are implemented in the Python package
``sphinx_lesson.directives`` and can be used independently of the rest
of ``sphinx-lesson``.



List
----

Many directives are available.

The following directives are used for exercises/solutions/homework.
They all render as green ("important" class:

* ``demo``
* ``exercise``
* ``solution`` (toggleable, default hidden)
* ``type-along`` (most of the lessons are hands-on, so this is a bit
  redundant.  Use this when emphasizing a certain section is "follow
  along", as opposed to watching or working alone.)
* ``homework``

Other miscellaneous directives:

* ``discussion``
* ``instructor-note``
* ``prerequisites``

The following are Sphinx default directives that may be especially
useful to lessons.  These do *not* accept an optional Title argument,
the title is hard-coded.

* ``see-also``
* ``note``
* ``important`` (green)
* ``warning`` (yellow)
* ``danger`` (red


The following are available, for compatibility with Carpentries styles:

* ``callout``
* ``challenge`` (alias to ``exercise``)
* ``checklist``
* ``keypoints`` (bottom of lesson)
* ``objectives`` (top of lesson)
* ``prereq`` (use ``prerequisites`` instead)
* ``solution`` (begins collapsed)
* ``testimonial``
* ``output`` (use code blocks instead)
* ``questions`` (top of lesson)



Gallery
-------

This is a demonstration of all major directives

sphinx-lesson
~~~~~~~~~~~~~

.. demo::

   demo

.. demo::

.. type-along::

   type-along

.. type-along::

.. exercise::

   exercise

.. solution::

   solution

.. homework::

   homework

.. discussion::

   discussion

.. instructor-note::

   instructor-note

.. prerequisites::

   prerequisites

Sphinx default
~~~~~~~~~~~~~~

.. note::

   note

.. important::

   important

.. seealso::

   seealso

.. warning::

   warning

.. danger::

   danger

Carpentries holdovers
~~~~~~~~~~~~~~~~~~~~~

.. questions::

   questions

.. objectives::

   objectives

.. keypoints::

   keypoints

.. callout::

   callout

.. challenge::

   challenge

.. checklist::

   checklist

.. prereq::

   prereq

.. testimonial::

   testimonial

.. output::

   output
