Directives
==========

We have the following directives available:

* ``callout``
* ``challenge``
* ``checklist``
* ``discussion``
* ``keypoints``
* ``objectives``
* ``prereq``
* ``solution`` (begins collapsed)
* ``testimonial``
* ``output``
* ``questions``
* ``instructor-note``


Example of ``challenge``:

.. challenge::

   Some body text

.. list-table::

   * * Markdown::

         ```{challenge}

         Some body text
         ```

     * ReST::

	 .. challenge::

	    Some body text


The ``solution`` directive begins collapsed (via `sphinx-togglebutton
<https://github.com/executablebooks/sphinx-togglebutton>`__:

.. solution::

   This is a solution

Directives are implemented in the Python package
``sphinx_lesson.directives`` and can be used independently of the rest
of ``sphinx-lesson``.
