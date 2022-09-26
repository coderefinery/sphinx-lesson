import re

from docutils import nodes
from docutils.parsers.rst import Directive
import sphinx.util

# Currently only sphinx-lesson admonitions can be included. Hint to fix:
# nodes.admonition to nodes.Admonition and then you have to examine the Python
# object class name.
DEFAULT_EXERCISELIST_CLASSES = {
    'exercise',
    'solution',
    'challenge',   # backwards compatibility
    'exerciselist-include',
    }

DEFAULT_EXERCISELIST_CLASSES_EXCLUDE = {
    'exerciselist-exclude',
    }

class exerciselist(nodes.General, nodes.Element):
    """Node for exercise list

    Gets replaced with contents in the second pass.
    """
    def __init__(self, *args,
                 include_classes=DEFAULT_EXERCISELIST_CLASSES,
                 exclude_classes=DEFAULT_EXERCISELIST_CLASSES_EXCLUDE):
        super().__init__(*args)
        self.include_classes = set(include_classes)
        self.exclude_classes = set(exclude_classes)

class ExerciselistDirective(Directive):
    """Run when a directive is parsed, returns the node (which is handled later)
    """
    option_spec = {'include': str, 'exclude': str}

    def run(self):
        kwargs = { }
        if 'include' in self.options:
            kwargs['include_classes'] = re.split('[ ,]+', self.options['include'])
        if 'exclude' in self.options:
            kwargs['exclude_classes'] = re.split('[ ,]+', self.options['exclude'])
        el = exerciselist('', **kwargs)
        return [el]


def is_exercise_node(node,
                     include_classes=DEFAULT_EXERCISELIST_CLASSES,
                     exclude_classes=DEFAULT_EXERCISELIST_CLASSES_EXCLUDE):
    """Should a single node be included in the exercise list?"""
    # If not an admonition, never include
    if not isinstance(node, nodes.admonition):
        return False
    # If wrong classes, exclude
    if not hasattr(node, 'attributes'):
        return False
    classes = node.attributes.get('classes', ())
    if not include_classes.intersection(classes):
        return False
    if exclude_classes.intersection(classes):
        return False
    # If parent is included, we don't need to include us.
    # TODO: higher level parents
    if (hasattr(node, 'parent')
        and is_exercise_node(
              node.parent,
              include_classes=include_classes,
              exclude_classes=exclude_classes,
       )):
        #import pdb ; pdb.set_trace()
        return False
    return True

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
    # Sphinx 4.0 renamed master_doc > root_doc
    root_doc = app.config.root_doc if hasattr(app.config, 'root_doc') else app.config.master_doc
    if root_doc not in env.toctree_includes:
        logger = sphinx.util.logging.getLogger(__name__)
        logger.error(f'sphinx_lesson.exerciselist could not find root doc {root_doc}')
        return
    process_docname(root_doc)

    # The list of all the exercises will be stored here.
    if not hasattr(env, 'sphinx_lesson_all_admonitions'):
        env.sphinx_lesson_all_admonitions = [ ]
    all_admonitions = env.sphinx_lesson_all_admonitions

    # Now go through and collect all admonitions from these docnames, in order.
    for docname in docnames:
        doctree = env.get_doctree(docname)
        for node in doctree.traverse(nodes.admonition):
            all_admonitions.append(node)


def process_exerciselist_nodes(app, doctree, fromdocname):
    """Find 'exerciselist' directives and replace with the exercise list.
    """
    env = app.builder.env
    # List of exercises
    if not hasattr(env, 'sphinx_lesson_all_admonitions'):
        env.sphinx_lesson_all_admonitions = [ ]
    all_admonitions = env.sphinx_lesson_all_admonitions

    for exerciselist_node in doctree.traverse(exerciselist):
        content = []  # This new content in place of 'exerciselist'
        last_docname = None
        for exercise_node in all_admonitions:
            # Skipp all admonitions which don't match our criteria
            if not is_exercise_node(exercise_node, include_classes=exerciselist_node.include_classes, exclude_classes=exerciselist_node.exclude_classes):
                continue
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



from sphinx.transforms import SphinxTransform
# Find the transform priority of MystReferenceResolver and be less than it.
# But don't fail if use this extension without myst_parser
try:
    from myst_parser.myst_refs import MystReferenceResolver
    # This is 8 in 2022 (thus the default value below)
    el_transform_priority = MystReferenceResolver.default_priority - 1
except ImportError:
    el_transform_priority = 8

class ExerciseListTransform(SphinxTransform):
    """Expand exerciselist nodes into the list of the exercises.

    This has to run before references are resolved
    """
    # myst_parser.myst_refs.MystReferenceResolver is priority 9
    default_priority = el_transform_priority
    def apply(self):
        doctree = self.document
        #import IPython ; IPython.embed()
        process_exerciselist_nodes(self.app, doctree, self.env.docname)



def setup(app):
    app.add_node(exerciselist)
    app.add_directive('exerciselist', ExerciselistDirective)
    app.connect('env-check-consistency', find_exerciselist_nodes)
    app.add_post_transform(ExerciseListTransform)
    return {
        'version': '0.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
