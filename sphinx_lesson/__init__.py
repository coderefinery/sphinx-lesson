from ._version import __version__

def setup(app):
    "Sphinx extension setup"
    app.setup_extension('myst_nb')
    app.setup_extension(__name__+'.directives')
    app.setup_extension(__name__+'.md_transforms')

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
