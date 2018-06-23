
# Pluralize-It

## Background

Do you know all the ways that you can convert a word from its singular form to its plural?  There are actually quite a few rules that might surprise you.  You can have one goose and one moose, but get one more of each and you've got two geese and two moose.  What?

Luckily, we'll be tackling the simpler rules in this program where we ask the user to enter a (singular-form) word and we'll tell them what it is, "pluralized".

## Getting Started

Just like in the last lab, you'll need to use the `touch pluralizer.py` command to create the script file, and then once it's built, you'll need to run the `python pluralizer.py` command in order to execute the script.

## Task

Ask the user for a number, then a word, then print out a phrase that depends on the number and the word.

You should pluralize the word by adding an "s" to the end whenenver they enter a number that is 0 or greater than 1.

You'll need to implement an `if`/`else` statement in your code, since you don't want to pluralize the word in every instance!

Examples:

```
In: 0
In: bat
Out: 0 bats
```

```
In: 1
In: cat
Out: 1 cat
```

```
In: 4
In: dog
Out: 4 dogs
```

## Extensions

### Level 2

Not every word is made into plural form by adding an 's' at the end.  Come up with 4 words that have special rules when it comes to making them plural.

Example: plural of "catch" is "catches".

In your code, if the user enters one of the special 4 words, instead implement the special rule.  If the word isn't one of the special 4 words, just add an 's' to the end like you did in Level 1.

Here you will have to begin using `elif` statements in addition to `if`/`else`.

### Level 3

Let's implement some more advanced rules:

| Word ends in:   | Becomes:     | Example            |
|:---------------:|:------------:|:------------------:|
| -ife            | -ives        | life -> lives      |
| -sh/ch          | -shes/ches   | bush -> bushes <br> church -> churches|
| -us             | -i           | cactus -> cacti    |
| -ay/oy/ey/uy    | -ays/oys/eys/uys | guy -> guys <br> toy -> toys <br> key -> keys <br> way -> ways         |
|                 |              | way -> ways        |
| -y              | -ies         | fly -> flies       |
| everything else | add -s       | hat -> hats        |

To do this, you'll have to use string slicing.  The following table provides the shortcuts for common tools you might need:

| Syntax        | Meaning                                     |
|---------------|---------------------------------------------|
| `word[:x]`    | The first `x` letters of `word`             |
| `word[:-x]`   | All of `word` except the last `x` letters   |
| `word[x:]`    | All of `word` except the first `x` letters  |
| `word[-x:]`   | The last `x` letters of `word`              |

Here are a few examples:

```python
word = "computerz"
print(word[:5])  # prints "compu"
print(word[:-1])  # prints "computer"
print(word[4:])  # prints "uterz"
print(word[-3:])  # prints "erz"
```
You'll need a series of conditional `if`/`elif`/`else` statements to handle each rule.  Make sure you're careful with your ordering, since some of these rules overlap!
