"""Add some sphinx-docutils directives related to lessons.
"""
# pylint: disable=E701

import os

from docutils import nodes
from docutils.parsers.rst.directives.admonitions \
  import Admonition as AdmonitionDirective
from sphinx.util.docutils import SphinxDirective
from sphinx.util.logging import getLogger

from . import __version__
LOG = getLogger(__name__)


def class_name_to_slug(name):
    """Strip Directive and turn name into slug

    Example:
      Hands_OnDirective --> hands-on
    """
    return name.split('Directive')[0].lower().replace('_', '-')


# This includes a heading, to not then have
class _BaseCRDirective(AdmonitionDirective, SphinxDirective):
    """A directive to handle CodeRefinery styles
    """
    # node_class = challenge
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    extra_classes = [ ]
    allow_empty = True

    @classmethod
    def get_cssname(cls):
        """Return the CSS class name and Sphinx directive name.

        - Remove 'Directive' from the name of the class
        - All lowercase
        - '_' replaced with '-'
        """
        return class_name_to_slug(cls.__name__)
    @classmethod
    def cssname(cls):
          warnings.warn(
            "You should use `get_cssname` (#71, 2021-08-22) and update old code to use it. This may be removed someday.\n" ,
            category=FutureWarning,
            stacklevel=2)
            return get_cssname(cls)

    def run(self):
        """Run the normal admonition class, but add in a new features.

        title_text: some old classes had a title which was added at the
        CSS level. If this is set, then this title will be added by the
        directive.
        """
        name = self.get_cssname()
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
        ret[0].attributes['classes'].extend(self.extra_classes)
        return ret

    def assert_has_content(self):
        """Allow empty directive blocks.

        This override skips the content check, if self.allow_empty is set
        to True.  This adds the admonition-no-content to the CSS
        classes, which reduces a bit of the empty space.  This is a hack
        of docutils, and may need fixing later on.
        """
        if not self.allow_empty:
            return super().assert_has_content()
        if not self.content:
            #if not hasattr(self, 'extra_classes'):
            #    self.extra_classes = [ ]
            self.extra_classes = list(self.extra_classes) + ['admonition-no-content']
        return


# These are the priamirly recommend directives
class DemoDirective(_BaseCRDirective):
    title_text = "Demo"
class Type_AlongDirective(_BaseCRDirective):
    extra_classes = ['important']
class ExerciseDirective(_BaseCRDirective):
    extra_classes = ['important']
class SolutionDirective(_BaseCRDirective):
    extra_classes = ['important', 'dropdown'] #'toggle-shown' = visible by default
class HomeworkDirective(_BaseCRDirective):
    extra_classes = ['important']
class Instructor_NoteDirective(_BaseCRDirective):
    title_text = "Instructor note"
class PrerequisitesDirective(_BaseCRDirective):
    title_text = "Prerequisites"
class DiscussionDirective(_BaseCRDirective):
    extra_classes = ['attention']

# These are hold-over for carpentries
class QuestionsDirective(_BaseCRDirective):
    """Used at top of lesson for questions which will be answered"""
    pass
class ObjectivesDirective(_BaseCRDirective):
    """Used at top of lesson"""
    pass
class KeypointsDirective(_BaseCRDirective):
    """Used at bottom of lesson"""
    pass
class CalloutDirective(_BaseCRDirective): pass
ChallengeDirective = ExerciseDirective
class ChecklistDirective(_BaseCRDirective): pass
PrereqDirective = PrerequisitesDirective
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


def setup(app):
    "Sphinx extension setup"
    app.setup_extension('myst_nb')
    for name, obj in globals().items():
        #print(name, obj)
        if (name.endswith('Directive')
            and issubclass(obj, _BaseCRDirective)
            and not name.startswith('_')):
            #print(name, obj.get_cssname())
            directive_name = class_name_to_slug(name)
            app.add_directive(directive_name, obj)

    # Add CSS to build
    # Hint is from https://github.com/choldgraf/sphinx-copybutton/blob/master/sphinx_copybutton/__init__.py  # pylint: ignore=E501
    app.connect('builder-inited', init_static_path)
    app.add_css_file("sphinx_lesson.css")

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
