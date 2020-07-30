# pylint: disable=E701

import os

from docutils import nodes
from docutils.parsers.rst.directives.admonitions \
  import Admonition as AdmonitionDirective
from sphinx.util.docutils import SphinxDirective
from sphinx.util.logging import getLogger

LOG = getLogger(__name__)


# class challenge(nodes.admonition):
#     pass

# This includes a heading, to not then have
class _BaseCRDirective(AdmonitionDirective, SphinxDirective):
    """A directive to handle CodeRefinery styles
    """
    # node_class = challenge
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True

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
                self.arguments = [name.title()]
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
class PrereqDirective(_BaseCRDirective):
    title_text = "Prerequisites"
class SolutionDirective(_BaseCRDirective): pass
class TestimonialDirective(_BaseCRDirective): pass
class OutputDirective(_BaseCRDirective):
    title_text = 'Output'
class QuestionsDirective(_BaseCRDirective): pass

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
    app.add_css_file("sphinx_lesson.css")

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
