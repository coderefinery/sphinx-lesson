Deployment with Github Actions
------------------------------

In this repository, there is a ``.github/workflows/sphinx.yml`` file
that contains a Github Action that:

* Installs dependencies
* Builds the project with Sphinx
* Deploys it

  * If branch = ``master``, deploy to gethub pages normally

  * For other branches, deploy to github-pages but put the result in
    the ``branch/{branch-name}`` subdirectory.  If the branch name has
    a ``/`` in it, replace it with ``--``.

  * Keep all previous deployments, but remove branch subdirectories
    for branches that no longer exist.

This allows you to view builds from pull requests or other branches.
