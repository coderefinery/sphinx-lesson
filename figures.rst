Figures
=======

The ``figure`` directive inserts an image and also provides a caption
and other material.

* The path is the relative or absolute path *within the sphinx source
  directory*.

* You can give optional CSS classes, ``with-border`` gives it a black
  border.  Remove this if you don't want it - the examples below
  include it.

.. figure:: img/sample-image.png
   :class: with-border

   This is the caption.


In ReST, this is::

    .. figure:: img/sample-image.png
       :class: with-border

       This is the caption.



In MyST Markdown, this is::

   ```{figure} img/sample-image.png
   ---
   class: with-border
   ---

   This is the figure caption.
   ```


When adding figures, optimize for narrow columns.  First off, many
themes keep it in a small column but even if not, learners will
usually need to keep the text in a small column anyway, to share the
screen with their workspace.  If you are ``690`` or less, then
sphinx_rtd_theme has no image scaling.  ``600`` or less may be best.
If larger, then they may be scaled down (in some themes) or scroll
left (others).
