
## Background

If you've never played with mad libs before, you're in for a treat.  What is a mad lib, you might ask?  It's an interactive story that lets you, the user, choose a bunch of words, which are then inserted into a story, making for a hilariously nonsensical piece of art.  You'll be programming a simple version of a mad libs program here.

## Getting Started

You'll need to create a new file in this directory. The command `touch mystory.py` should work! You don't have to name it "mystory.py", but whatever filename you choose must end in a `.py` file extension so that it is designated a Python script.

Once that file exits, you'll code your story-script in the file. To run it, the command is `python mystory.py`, although if you named it something else, you'll swap the filename "mystory.py" with whatever filename you chose.

## Task

To make a mad libs game, you have to do a few things:
1. Write a generic story.
2. Take out specific words from that story.
3. Ask the user for words with specific parts of speech that correspond to the removed words.
4. Re-tell the story with the user's inputted words.

For the sake of simplicity, let's make a short story that's two sentences long.  You can come up with one on your own, or use this one that is given:

```
The (noun1) jumped over a (adjective1) (noun2).  Then the (noun2) decided to stop being so (adjective1) and take up a hobby: (verb1-ing).
```

The program would ask the user to enter something for `noun1`, `noun2`, `adjective1`, and `verb1`, then print the story out with the user's entered words.

When asking for nouns, be sure to specify whether you want plural or singular!  When asking for verbs, be sure to specify whether it should be present, past, or future tense, and whether it should end in -ing or not.


## Extensions

Make the story longer!  Or ask for a name, and repeatedly refer to the name.  If you've explored conditionals in Python, maybe you can even ask for their gender and use proper personal pronouns (him/her/them, he/she/they, etc).
