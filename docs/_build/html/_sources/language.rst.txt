###############
  language.py
###############

Implements a specific ConLang for a series of books.
This includes a few grammar rules and lexicon rules to create words.

Background
==========

This is a for a specific Epic Fantasy series.
It implements an imperial trade language shared by a handful of kingdoms all under control of the "Western Empire."

The essential language has a relatively simple structure.

Sentences have forms like VP NP NP, VP NP PP, VP NP PP NP PP.
The verb is always first.
Nouns follow, generally decorated with prepositions.

There are some additional grammar rules for noun phrases to inject determiners to help keep the subjects and objects stright.

..  code-block::

    NP -> Det Nominal ;
    Nominal -> Nominal Noun ;

A transliteration of "Kill the mage" would look like this:

    "go-Kill you mage-the"

There's a verb, "go-Kill", and two nouns, "you" and "mage-the".

Verbs:

-   Present tense is the base form of verbs.

-   Imperative gets a "go-" prefix.

-   Present participle ("-ing" in English) gets a "now-" prefix.

-   Past ("-ed" in English) gets a "did-" prefix.

There's no person conjugation. It's a separate word and comes right after the verb.

Generally, the ConLang lacks intransitive verbs. "did-Bark the dog at something."
"did-See myself the man." "did-Give the dog to a man." "did-Say the man did-Bark the dog at something."

Nouns determiners (this, that, the, any, all, etc.) are suffixed onto the noun.

Implementation
==============

..  automodule:: language

Part 1 -- Lexicon
-----------------

To create words, we use a simple weighted choice random selection.

..  autofunction:: language.weighted_choice

A :py:class:`language.WordMaker` builds words from a specific set of digraph frequencies.

..  autoclass:: language.WordMaker
    :members:
    :undoc-members:
    :special-members: __init__
    :member-order: bysource

Two seed-generating functions to build a :py:class:`language.WordMaker`  instance.

..  autofunction:: language.naive_seed

..  autofunction:: language.hash_seed

Part 2 -- Grammar
------------------

..  autoclass:: language.Tag
    :members:
    :undoc-members:
    :member-order: bysource

Example of tagged input:

    >>> from language import Tag

    >>> src = '(S (VP (TV kill) (NP (DET the) (NP mage))))'
    >>> t = Tag.from_text(src)
    >>> t.clean()
    'kill the mage'


..  autoclass:: language.TransformRule
    :members:
    :undoc-members:
    :member-order: bysource

Example of a transformation:

    >>> from language import TransformRule

    >>> rule1 = TransformRule("(S (NP $n) (VP $v $n2))", "(S (VP $v) (NP $n) (PP a $n2))")
    >>> s1 = Tag.from_text("(S (NP I) (VP am (NP groot)))")
    >>> xform_s1.clean()
    'am I a groot'

