"""Make term definition links bold
"""

from . import __version__

def setup(app):
    "Sphinx extension setup"
    app.add_css_file("term_role_formatting.css")

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
