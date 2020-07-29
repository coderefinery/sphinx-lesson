# pylint: disable=E701

import os
import re

from docutils import nodes
from docutils.parsers.rst.directives.admonitions \
  import Admonition as AdmonitionDirective
from sphinx.util.docutils import SphinxDirective
from sphinx.util.logging import getLogger

LOG = getLogger('sphinx-lesson')



def transform_code_fences(app, docname, source):
    """Transform a code fence when read.

    Changes:
    ```
    blah
    ```
    {: output}

    Into this:
    ```{output}
    blah
    ```
    """
    if not app.config.sphinx_lesson_transform_code_fences:
        return
    print(docname)
    content = source[0]
    LOG.debug(content)
    code_fence_re = re.compile(
        r'^(?P<before>```.*?)(?P<content>\n.*?)(?P<after>^``` ?\n)(?:\{:(?P<class>[^}\n]+)\}$)?',
        re.DOTALL|re.MULTILINE,
)
    def sub_fence(m):
        if m.group('class'):
            print("matched:", m.group(0))
            print("class:", m.group('class'))
            return m.group('before') + '{%s}'%m.group('class').strip() + m.group('content') + m.group('after')
        else:
            return m.group(0)

    newcontent = code_fence_re.sub(sub_fence, content)
    LOG.debug(newcontent)
    source[0] = newcontent

def setup(app):
    "Sphinx extension setup"
    app.setup_extension('myst_nb')
    # Code frence transformation
    app.add_config_value('sphinx_lesson_transform_code_fences', True, 'env')
    app.connect('source-read', transform_code_fences)
