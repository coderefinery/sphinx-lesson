# Deployment with Github Actions

In sphinx-lesson-template (and this lesson...), there is a
`.github/workflows/sphinx.yml` file that contains a Github Action.
There is nothing special about this, but it's simple and all in one
file.  It does:

- Installs dependencies

- Builds the project with Sphinx (`dirhtml` builder)

- Deploys it

  - If branch = `main`, deploy to github pages normally
  - For other branches, deploy to github-pages but put the result in
    the `branch/{branch-name}` subdirectory.  If the branch name has
    a `/` in it, replace it with `--`.
  - Keep all previous deployments, but remove branch subdirectories
    for branches that no longer exist.

- There are also versions that can be built:

  - A one-page HTML version at `/singlehtml/`. This is built by
   default.
  - A epub version built and stored at
    `{organization_name}-{repo_name}.epub`.  This is built by default
    since it's easy and fast.
  - A PDF version built and stored at
    `{organization_name}-{repo_name}.epub`.  This is not built by
    default since it requires extra dependencies (including Chromium)
    to be installed and takes much longer.

This allows you to view builds from pull requests or other branches.

## Usage

It is recommended to copy from
[sphinx-lesson-template](https://github.com/coderefinery/sphinx-lesson-template/),
since that is the primary copy that is updated with all of the latest developments.

Direct link:
<https://github.com/coderefinery/sphinx-lesson-template/blob/main/.github/workflows/sphinx.yml>
