# pylint: disable=E701

import os
import re

from docutils import nodes
from docutils.parsers.rst.directives.admonitions \
  import Admonition as AdmonitionDirective
from sphinx.util.docutils import SphinxDirective
from sphinx.util.logging import getLogger

LOG = getLogger(__name__)



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
    LOG.debug('transform_code_fences: beginning %s', docname)
    content = source[0]
    LOG.debug(content)
    code_fence_re = re.compile(
        r'^(?P<before>```.*?)(?P<content>\n.*?)(?P<after>^``` ?\n)(?:\{:(?P<class>[^}\n]+)\}$)?',
        re.DOTALL|re.MULTILINE,
        )
    def sub_fence(m):
        if m.group('class'):
            LOG.debug("matched: %s", m.group(0))
            LOG.debug("class: %s", m.group('class'))
            return m.group('before') + '{%s}'%m.group('class').strip() + m.group('content') + m.group('after')
        else:
            return m.group(0)

    newcontent = code_fence_re.sub(sub_fence, content)
    LOG.debug(newcontent)
    source[0] = newcontent

def transform_block_quotes(app, docname, source):
    """
    Transform this:

    > ## some-heading
    > text
    > text
    {: .block-class}

    into this:

    ```{block-class} some-heading
    text
    text
    ```

    """
    if not app.config.sphinx_lesson_transform_block_quotes:
        return
    LOG.debug('sphinx_lesson: transform_block_quotes: %s', docname)
    content = source[0]
    LOG.debug(content)

    block_quote_re = re.compile(
        r'(?P<heading>> ?#+[^\n]*$\n)?(?P<content>(?:>[^\n]*$\n)+)\{: +(?P<class>[^\}]+)\}',
        re.DOTALL|re.MULTILINE,
    )

    def sub_block(m):
        """Handle each detected block quote"""
        if m.group('class'):
            LOG.debug("matched: %s", m.group(0))
            LOG.debug("class: %s", m.group('class'))
            # Extract the class, remove leading characters
            class_ = m.group('class')
            class_ = re.sub('^[ .]*', '', class_)
            # heading: tranform explicit heading into directive heading
            if m.group('heading'):
                heading = m.group('heading')
                heading = ' ' + re.sub('^[ >#]*', '', heading)
            else:
                heading = ''
            # content: remove one leading '>' character
            contentlines = m.group('content').split('\n')
            contentlines = [ re.sub('^> ?', '', line) for line in contentlines ]

            LOG.debug(contentlines)
            return ("```{%s}%s\n"%(class_, heading)
                    + '\n'.join(contentlines)
                    + "```"
                    )

        else:
            return m.group(0)

    newcontent = block_quote_re.sub(sub_block, content)
    LOG.debug(newcontent)
    source[0] = newcontent


def setup(app):
    "Sphinx extension setup"
    app.setup_extension('myst_nb')
    # Code frence transformation
    app.add_config_value('sphinx_lesson_transform_code_fences', True, 'env')
    app.add_config_value('sphinx_lesson_transform_block_quotes', True, 'env')
    app.connect('source-read', transform_code_fences)
    app.connect('source-read', transform_block_quotes)
