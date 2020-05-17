# pylint: disable=E701

import os

from docutils import nodes
from docutils.parsers.rst.directives.admonitions \
  import Admonition as AdmonitionDirective
from sphinx.util.docutils import SphinxDirective


class challenge(nodes.admonition):
    pass

#challenge = nodes.admonition

#nodes.challenge = challenge


# This includes a heading, to not then have
class ChallengeDirective(AdmonitionDirective, SphinxDirective):
    #node_class = docutils.nodes.caution
    #node_class = challenge
    #classes = ('task', )
    def run(self):
        # Run the normal admonition class, but add in a new class
        self.node_class = nodes.admonition
        ret = super().run()
        name = self.__class__.__name__.split('Directive')[0].lower()
        ret[0].attributes['classes'].append(name)
        return ret


# This does work, to add
from sphinx.writers.html5 import HTML5Translator
def visit_node(self, node):
    #import pdb ; pdb.set_trace()
    node.attributes['classes'] += [node.__class__.__name__]
    self.visit_admonition(node)


# Add our custom CSS to the headers.
def init_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               '_static'))
    app.config.html_static_path.append(static_path)


def setup(app):
    "Sphinx extension setup"
    app.add_node(challenge, html=(visit_node,
                                  HTML5Translator.depart_admonition))
    app.add_directive("challenge", ChallengeDirective)

#    nodes._add_node_class_names(('challenge', ))

    # Add CSS to build
    # Hint is from https://github.com/choldgraf/sphinx-copybutton/blob/master/sphinx_copybutton/__init__.py  # pylint: ignore=E501
    app.connect('builder-inited', init_static_path)
    app.add_css_file("sphinx_ext_substitution.css")
