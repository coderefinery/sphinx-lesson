# Markdown transforms

To ease the transition from other Markdown dialects(like the one used
in software-carpentry), we implement some transformations in sphinx.
These are implemented in the `sphinx_lessons.md_transforms` Python
package and are implemented using regular expressions, so they are a
bit fragile.

## Code fences

Code fence syntax is translated to CommonMark.  Input:

````
```
blah
```
{: output}
````

Output:

````
```{output}
blah
```
````

## Block quotes

Transform CSS styles into MyST directives (implemented as code
fences.  Input:

```
> ## some-heading
> text
> text
{: .block-class}
```

Output:

````
```{block-class} some-heading
text
text
```
````

The `block-class` is the directive name (we maintain compatibility
with old jekyll-common)

## Raw HTML images

Raw HTML isn't a good idea in portable formats.  Plus, in the old
jekyll formats, bad relative path handling caused absolute paths to be
embedded a lot.Transform this:

```
<img src="/path/to/img.png">
```

into this:

````
```{figure} /path/to/img.png
```
````

Exclude any possible `{{ ... }}` template variables used to
semi-hard code absolute paths.
