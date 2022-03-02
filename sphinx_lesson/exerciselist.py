import re

from docutils import nodes
from docutils.parsers.rst import Directive
import sphinx.util

DEFAULT_EXERCISELIST_CLASSES = {
    'exercise',
    'solution',
    'challenge',   # backwards compatibility
    }

class exerciselist(nodes.General, nodes.Element):
    """Node for exercise list

    Gets replaced with contents in the second pass.
    """
    pass

class ExerciselistDirective(Directive):
    def run(self):
        return [exerciselist('')]


def find_exerciselist_nodes(app, env):
    """Find all nodes for the exercise list, in order.

    Go through all documents (in toctree order) and make a list of all
    docnames.  Then, from those docnames, find all admonitions that
    match certain classes.  Store this for the next round.
    """

    env = app.builder.env

    # Find all docnames in toctree order.
    docnames = [ ]
    def process_docname(docname):
        """Process this doc and children"""
        if docname in docnames: # already visited
            return
        docnames.append(docname)
        for docname2 in env.toctree_includes.get(docname, []):  # children
            process_docname(docname2)
    root_doc = app.config.root_doc
    if root_doc not in env.toctree_includes:
        logger = sphinx.util.logging.getLogger(__name__)
        logger.error(f'sphinx_lesson.exerciselist could not find root doc {root_doc}')
        return
    process_docname(root_doc)

    # The list of all the exercises will be stored here.
    if not hasattr(env, 'sphinx_lesson_all_exercises'):
        env.sphinx_lesson_all_exercises = [ ]
    all_exercises = env.sphinx_lesson_all_exercises

    # Now go through and collect all admonitions from these docnames, in order.
    for docname in docnames:
        doctree = env.get_doctree(docname)
        for node in doctree.traverse(nodes.admonition):
            classes = node.attributes.get('classes', ())
            if DEFAULT_EXERCISELIST_CLASSES.intersection(classes):
                all_exercises.append(node)


def process_exerciselist_nodes(app, doctree, fromdocname):
    """Find 'exerciselist' directives and replace with the exercise list.
    """
    env = app.builder.env
    # List of exercises
    if not hasattr(env, 'sphinx_lesson_all_exercises'):
        env.sphinx_lesson_all_exercises = [ ]
    all_exercises = env.sphinx_lesson_all_exercises

    for exerciselist_node in doctree.traverse(exerciselist):
        content = []  # This new content in place of 'exerciselist'
        last_docname = None
        for exercise_node in all_exercises:
            # Set title of the document.  We need to make a new section with a
            # 'title' node for this.
            if exercise_node.target_docname != last_docname:
                # find the page title
                last_docname = exercise_node.target_docname
                doctree = env.get_doctree(exercise_node.target_docname)
                page_title = next(iter(doctree.traverse(nodes.title)))
                # make section with the stuff
                section = nodes.section()
                content.append(section)
                section += page_title
                slug = page_title.rawsource.replace(' ', '-').lower()
                slug = re.sub(r'[^\w\d_-]', '', slug)
                section['ids'].append(slug)

            filename = env.doc2path(exercise_node.target_docname, base=None)
            par = nodes.paragraph()

            # Create a reference
            newnode = nodes.reference(f'In {filename}:', f'In {filename}:')
            newnode['refdocname'] = exercise_node.target_docname
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, exercise_node.target_docname)
            newnode['refuri'] += '#' + exercise_node.target_id
            par += newnode
            section.append(par)
            section.append(exercise_node)

        exerciselist_node.replace_self(content)

def setup(app):
    app.add_node(exerciselist)
    app.add_directive('exerciselist', ExerciselistDirective)
    app.connect('env-check-consistency', find_exerciselist_nodes)
    app.connect('doctree-resolved', process_exerciselist_nodes)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
