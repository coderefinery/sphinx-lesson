# https://packaging.python.org/guides/distributing-packages-using-setuptools/
# 'wheel' may be a build-dependency, it's also dep of twine

from os.path import join, dirname
import setuptools

version_ns = { }
exec(open('sphinx_lesson/_version.py').read(), version_ns)
version = version_ns['__version__']
del version_ns

with open("README.rst", "r") as fh:
    long_description = fh.read()

requirementstxt = join(dirname(__file__), "requirements.txt")
requirements = [ line.strip() for line in open(requirementstxt, "r") if line.strip() ]

setuptools.setup(name='sphinx_lesson',
      version=version,
      description='Sphinx extension for CodeRefinery lessons',
      long_description=long_description,
      long_description_content_type="text/x-rst",  # ReST is the default
      url="https://github.com/coderefinery/sphinx-lesson",
      project_urls={
          "Documentation": "https://coderefinery.github.io/sphinx-lesson/",
          },
      author='Richard Darst',
      #author_email='',
      packages=['sphinx_lesson'],           # packages
      package_data={
          "sphinx_lesson": ['_static/*'],
          },
      #py_modules=["nbscript"],   # single modules
      keywords='sphinx-extension',
      #python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*,",
      install_requires=requirements,
      # https://pypi.org/classifiers/
      classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Extension",
        "Operating System :: OS Independent",
    ],
  )

# python setup.py sdist bdist_wheel
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# twine upload dist/*
