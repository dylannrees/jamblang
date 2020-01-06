# Jamb

Jamb is an experimental version of [Jelly][1], a tacit golfing language written by Dennis Mitchell. New features include variable depth atoms and automatic argument swapping for some dyads.

## New features in Jamb and differences from Jelly

### Ions

Atoms can now have variable depth. Previously, the only way to overload atoms was by doing it within each atom's call. Now, atoms can have a list of "sub-atoms" called ions each of which have their own vectorization depths and calls.

For example, the first ion of the atom `»` is to return the greater of it's two arguments at depth zero on both sides. This works when the two arguments are of the same type, but errors when given a string and an integer. This was the atom's only behavior in Jelly. In Jamb, when the first ion errors, the second ion is tried. If given `abc` and `5` as its arguments, the atom will then change it's left argument's depth to one and try to left pad it to length equal to the right argument. E.g. `“abc”»5` will return `'  abc'` (`“abc”»` looks like the string `“abc”` is being shifted to the right). Equivalently, `«` right pads.

At the point in Jelly at which Jamb diverged, there was only one single byte dyad that had depths **1** and **0**, so it was not possible to overload existing single byte atoms to include both a left padding atom and a right padding atom without taking up unused bytes.

### Argument swapping for dyads

Dyads can now be given `swapargs = True`, which specifies that when a dyad errors with left and right arguments **x** and **y**, Jamb should attempt to apply the atom with two arguments switched. This means that when using the left padding ion of `»`, you'll never need to write `»@` because both `“abc”»5` and `5»“abc”` return the same thing.

  - Should this be default behavior for all dyadic links?

### More changes

- `@` now turns monads into dyads which use the right argument. Dyadic behavior is unchanged. This frees `}`.
- ``` ` ``` now turns monads into dyads which use the left argument. Dyadic behavior is unchanged. This frees `{`.
- `Ɱ` now works for monads and is equivalent  to `<monad>@Ɱ` in Jamb or `<monad>}Ɱ` in Jelly. Additionally, `<nilad>Ɱ` is a dyad which replaces each item in it's right argument with `<nilad>`. E.g. `5Ɱ3` yields `[5, 5, 5]`.
- `<link>Ƒ` now vectorizes at the same depth as `<link>`.
- `ɲ` is a new "not" quick the applies the logical NOT operator to the result of the link it consumes at the same depth. This was an idea Dennis had at one point but was never implemented in Jelly. This allows for greater than or equal to, for example, as `<ɲ`.
- `)` now begins a three character string literal, similar to `⁾`. I mostly added this so I could add another quine: `))ṢżżṢ`. This feature might not survive in the end.
- `ɱ` has replaced `)` and is equivalent to `µ€`
- To call links at certain a certain index, use `Ð¢`, `ÐÇ` and `Ðç` instead of Jelly's `£`, `Ŀ` and `ŀ`. I had never seen these used in a golfing context so didn't think they deserved single byte tokens.
- `Ŀ` is now prepend zero, or **[0..z]** for integers.
- `Ż` is now all permutations of **z**.
- There are also new atoms and quicks which won't necessarily be added here. Jamb has its own atoms/quicks/etc. pages so all features can be documented somewhere.

[1]: https://github.com/DennisMitchell/jellylanguage
