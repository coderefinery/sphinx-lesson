# Indexing

An index lets you efficiently look up any topic.  In the age of
full-text search, you are right to wonder what the point of indexes
are.  They could be seen as companion of cheatsheet: instead of
searching and hoping you find the hright place, you can index the
actual locations to which one would refer.

As you might expect, there is nothing special to in sphinx-lesson
about indexing: see the Sphinx documentation on {rst:dir}`index`.

```{index} ! Index
```

## Basic concepts

**Headings** are the terms which can be looked up in the index.  When
choosing headings, consider:

- What is useful to a reader to locate
- How would a reader look it up? For example, `commit` or
  `committing` is useful, but `how to commit` is not.  Phrase it
  with the most important terms first (big-endian)
- And index can have sub-entries.  For example, under the entry
  `git`, there can be subentries for each git command, such as
  `commit`.

## Syntax

:::{seealso}
The Sphinx documentation on {rst:dir}`index`.
:::

```{highlight} rst
```

The `index` directive and role are the main ways to add index
entries.  The semicolon (`;`) character separates entries and
subentries.

```{index} pair: index; ReST
```

Index a block with the directive, with ReST:

```
.. index:: commit; amend
```

Or ReST, multiple:

```
.. index::
   commit
   commit; message
   pair: commit; amend
```

MyST:

````
```{index} commit; amend
```

```{index}
commit
commit; mesage
pair: commit; amend
```
````

Or index a single term with the role:

```
This sentence has an index entry for :index:`commit`.  If you want the
indexed term to be different, standard syntax applies such as
:index:`loop variables <pair: commit; amend>`.
```

```{index} pair: index; MyST
```

MyST:

```
Simple entry: {index}`commit`
Pair entry: {index}`loop variables <pair: commit; amend>`
```

```{index} index; single index; pair index; see index; seealso
```

There are different styles:

- `TERM`, same as below
- `single: TERM` (the default): create just a single entry
- `pair: TERM; TERM`: create entries for `x; y` and `y; x`
- `see: TOPIC; OTHER`: creates a "see other" entry for "topic".
- `seealso: TOPIC; OTHER`: creates a "seealso" entry, like above

## Glossaries

If you make a glossary using the {rst:dir}`glossary directive
<glossary>`, the terms automatically get added to the index

## See also

- {rst:dir}`index` directive
- Sphinx {rst:dir}`glossary`
