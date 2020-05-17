# Markdown example

## markdown format from old lessons, that doesn't work.

> ## Sample block in old markdown format, that doesn't work
>
> What do you think will be the outcome if you
> stage a file and then edit it and stage it again, do this several times and
> at the end perform a commit? (think of focusing several scenes and pressing the
> shoot button only at the end)
{: .challenge}


## myst_parser block directive format

```{admonition} Sample block in new format
---
class: challenge
---

This has a CSS class of "challenge", and I think it might even share
the normal ReST directive class, so that we only have to program
`challenge` once!

What do you think will be the outcome if you
stage a file and then edit it and stage it again, do this several times and
at the end perform a commit? (think of focusing several scenes and pressing the
shoot button only at the end)
```

## This format is not implemented yet

(so you see nothing here in the html, but it is in the source)

```{challenge}
## This doesn't work

What do you think will be the outcome if you
stage a file and then edit it and stage it again, do this several times and
at the end perform a commit? (think of focusing several scenes and pressing the
shoot button only at the end)
```

