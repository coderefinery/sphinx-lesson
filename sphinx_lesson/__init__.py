"""Sphinx extension for CodeRefinery lessons"""
from ._version import __version__

def setup(app):
    "Sphinx extension setup"
    app.setup_extension('myst_nb')
    app.setup_extension('sphinx_copybutton')
    app.setup_extension('sphinx_minipres')
    app.setup_extension('sphinx_togglebutton')
    app.setup_extension(__name__+'.directives')
    app.setup_extension(__name__+'.md_transforms')
    app.setup_extension(__name__+'.exerciselist')
    app.setup_extension(__name__+'.term_role_formatting')

    if 'pdf' not in app.tags:
        # sphinx_tabs does not support the PDF builder. Use it for other builds.
        app.setup_extension('sphinx_tabs.tabs')
    else:
        # Use imgmath to render math without javascript in PDF builds
        app.setup_extension("sphinx.ext.imgmath")
        # Render tab groups as a list instead of tabs in PDF builds
        app.setup_extension("sphinx_pyppeteer_builder.tabs")

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
