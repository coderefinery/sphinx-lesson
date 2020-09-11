from ._version import __version__

def setup(app):
    "Sphinx extension setup"
    app.setup_extension('myst_nb')
    app.setup_extension('sphinx_copybutton')
    app.setup_extension(__name__+'.directives')
    app.setup_extension(__name__+'.md_transforms')

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
