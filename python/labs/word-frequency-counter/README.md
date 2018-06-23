
# Word Frequency Counter

## Background

Many artificial intelligence systems can do amazing things nowadays, like translate words, or read texts and tell you whether it has a positive tone or a negative tone.  We'll be doing some basic text analysis by counting the words within a text. You are given the entire text of Jane Eyre, a classic novel spanning around 400 pages of text.

## Task

You are given a starter program, `wordfreq_starter.py`, which already contains the code that loads the book (`war-and-peace.txt`) and saves its content in a big string called `content`.  The text will already have newlines removed and everything converted to lowercase for your convenience.

In order to count the words, you will have to:
* Split `content` up by spaces using the `.split()` method
* Begin looping through each word (separated by spaces)

Your job is to use a dictionary to count the frequency of each word.  You should start by creating a dictionary for this purpose, where each key will be a word, and each value would be the count.  Then split the word up by spaces using the `.split()` string function, and then loop through!

So we would start by creating the dictionary:

```python
word_count = {}
```

And then splitting up the content by spaces using `.split()` and loop through it!

```python
word_count = {}

words = content.split(" ")
for word in words:
    # update the dictionary
    # where each key is the word and the value is the count
```

For example, if you were given the text: `I don't like bananas but bananas are good for me like other things I don't like`

Your dictionary might look something like this:
```python
{
    "I": 2,
    "don't": 2,
    "like": 3,
    "bananas": 2,
    "but": 1,
    "are": 1,
    "good": 1,
    "for": 1,
    "other": 1,
    "things": 1
}
```

Once you've created the dictionary and looped through all the words in the text, call the `get_highest_words` function, passing along the dictionary, as well as the number of words you want to see.

You can check to see if you're correct by comparing it to these results for the top 15 words:
```
: 9998
the: 7864
i: 6424
and: 6321
to: 5121
of: 4435
a: 4373
in: 2716
was: 2402
you: 2317
my: 2146
it: 1776
he: 1749
as: 1560
that: 1466
```

## Extensions

### Level 2

You may have noticed that in the results, you have empty spaces topping your list.  This is because when Python splits a string up by spaces, the string `"hi  there"` will be split up into `["hi", "", "there"]`. Can you modify your code to exclude empty spaces?

### Level 3

The words themselves aren't that meaningful, because these are called "stop words" - common words that are often filtered out before doing any natural language processing on data.

Included with the project is `stop-words.txt`, a text file with common stop words, and a function `get_stop_words()`, which is used to read that data and return the stop words as a list.

Modify your program to ignore words that are in the list of stop words so that the frequency counter becomes more meaningful.
