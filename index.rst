Test sphinx lesson
==================

In this lesson, we learn how to make a CodeRefinery lesson using
sphinx.  It is designed to replace the Jekyll-based software carepntry
templates.  The source is on `github
<https://github.com/coderefinery/sphinx-test-lesson>`__.


.. prereq:: Required software

   * prereq1
   * prereq2

   This has the css class 'prereq', and like all blocks is implemented
   like::

     .. prereq::

	* prereq1
	* prereq2


The following directives are implemented:

* ``callout``
* ``challenge``
* ``checklist``
* ``discussion``
* ``keypoints``
* ``objectives``
* ``prereq``
* ``solution``
* ``testimonial``

All that remains is some proper CSS

.. toctree::
   :maxdepth: 2
   :caption: Episodes

   01_intro
   02_rst_tests
   03_md_tests
   04_executing
   05_jupyter

.. toctree::
   :caption: Other material

   cheatsheet
   guide


* :ref:`genindex`
* :ref:`search`
