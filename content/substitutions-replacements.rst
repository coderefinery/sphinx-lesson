Substitutions and replacement variables
=======================================


Like most languages, ReST and MyST both have direct ways to substitute
variables to locally customize lessons.  While this works for simple
cases, this can quickly become difficult to manage with the "master
copy" of possibly important content being separated from the main
body, and keeping the substitutions up to date.

`sphinx_ext_substitution
<https://github.com/NordicHPC/sphinx_ext_substitution>`__ tries to
solve these problems by keeping the default values within the document
and providing tools to manage the substitution as the context changes
over time.  It is tested with ReST and should work with MyST as well.
