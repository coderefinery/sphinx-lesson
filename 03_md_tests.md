# Markdown example

## Native markdown blocks

This is a native challenge block, using myst_parser and sphinx directives

```{challenge} This is a challenge

This has css class `challenge`.

What do you think will be the outcome if you
stage a file and then edit it and stage it again, do this several times and
at the end perform a commit? (think of focusing several scenes and pressing the
shoot button only at the end)
```

It is implemented as:

```
   ```{challenge} This is a challenge

   content
   >```
```

TODO: how to have nested code fences - the `>` shouldn't be above but
I can't make them nested?


## markdown format from old lessons, that doesn't work with myst_parser

> ## Sample block in old markdown format, that doesn't work
>
> What do you think will be the outcome if you
> stage a file and then edit it and stage it again, do this several times and
> at the end perform a commit? (think of focusing several scenes and pressing the
> shoot button only at the end)
{: .challenge}
