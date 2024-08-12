# Presentation mode

:::{note}
This is a technical demo, included by default to make it easy to
use.  It may be removed in a future release.
:::

Using [minipres](https://github.com/coderefinery/sphinx-minipres),
any web page can be turned into a presentation.  As usual, there is
nothing very specific to sphinx-lesson about this, but currently
minipres is only tested on `sphinx_rtd_theme`, but theoretically can
work on others.

Using minipres, you only have to write one page: the material your
students read.  Then, you hide the unnecessary elements (table of
contents), focus on one section, and provide a quick way to jump
between sections.  Then you can get the focused attention of a
presentation and the readability of a single page.

How it works:

- Add `?minipres` to the URL of any page, and it goes into
  presentation mode.
- Add `?plain` to the URL of any page to go to plain mode.

In presentation mode:

- The sidebars are removed (this is the only thing that happens in
  `plain` mode).
- Extra space is added between each section (HTML headings), so that
  you focus on one section at a time
- The **left/right arrow keys** scroll between sections.

Examples:

```{eval-rst}
- `View this page as an example of minipres <../sample-episode-rst/?minipres>`__.
- `View this page in "plain" mode <../sample-episode-rst/?plain>`__.
```
