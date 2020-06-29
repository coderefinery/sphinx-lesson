# pylint: disable=E701

import os
import re

from docutils import nodes
from docutils.parsers.rst.directives.admonitions \
  import Admonition as AdmonitionDirective
from sphinx.util.docutils import SphinxDirective
from sphinx.util.logging import getLogger

LOG = getLogger('sphinx-lesson')


# class challenge(nodes.admonition):
#     pass

# This includes a heading, to not then have
class _BaseCRDirective(AdmonitionDirective, SphinxDirective):
    """A directive to handle CodeRefinery styles
    """
    # node_class = challenge
    required_arguments = 0

    @classmethod
    def cssname(cls):
        return cls.__name__.split('Directive')[0].lower()

    def run(self):
        """Run the normal admonition class, but add in a new features.

        title_text: some old classes had a title which was added at the
        CSS level. If this is set, then this title will be added by the
        directive.
        """
        name = self.__class__.__name__.split('Directive')[0].lower()
        self.node_class = nodes.admonition
        # Some jekyll-common nodes have CSS-generated titles, some don't.  The
        # Admonition class requires a title.  Add one if missing.  The title is
        # the first argument to the directive.
        if len(self.arguments) == 0:
            if hasattr(self, 'title_text'):
                self.arguments = [self.title_text]
            else:
                self.arguments = [name]
        # Run the upstream directive
        ret = super().run()
        # Set CSS classes
        ret[0].attributes['classes'].append(name)
        return ret


class CalloutDirective(_BaseCRDirective): pass
class ChallengeDirective(_BaseCRDirective): pass
class ChecklistDirective(_BaseCRDirective): pass
class DiscussionDirective(_BaseCRDirective): pass
class KeypointsDirective(_BaseCRDirective): pass
class ObjectivesDirective(_BaseCRDirective): pass
class PrereqDirective(_BaseCRDirective): pass
#    title_text = "Prerequisites"
class SolutionDirective(_BaseCRDirective): pass
class TestimonialDirective(_BaseCRDirective): pass
class OutputDirective(_BaseCRDirective):
    title_text = 'Output'

# This does work, to add
# from sphinx.writers.html5 import HTML5Translator
# def visit_node(self, node):
#     #import pdb ; pdb.set_trace()
#     node.attributes['classes'] += [node.__class__.__name__]
#     self.visit_admonition(node)


# Add our custom CSS to the headers.
def init_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               '_static'))
    #print('sphinx_lesson static path:', static_path)
    app.config.html_static_path.append(static_path)

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
#    app.add_node(challenge, html=(visit_node,
#                                  HTML5Translator.depart_admonition))
    for name, obj in globals().items():
        #print(name, obj)
        if (name.endswith('Directive')
            and issubclass(obj, _BaseCRDirective)
            and not name.startswith('_')):
            #print(name, obj.cssname())
            app.add_directive(obj.cssname(), obj)

#    nodes._add_node_class_names(('challenge', ))

    # Add CSS to build
    # Hint is from https://github.com/choldgraf/sphinx-copybutton/blob/master/sphinx_copybutton/__init__.py  # pylint: ignore=E501
    app.connect('builder-inited', init_static_path)
    app.add_css_file("sphinx_coderefinery.css")
    #app.add_css_file("lesson.css")
    # Code frence transformation
    app.add_config_value('sphinx_lesson_transform_code_fences', True, 'env')
    app.connect('source-read', transform_code_fences)
