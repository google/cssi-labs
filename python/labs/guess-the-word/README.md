
## Background

You've been brought on to build a game to be featured for a new game show.  The game show will be fielding a variety of games for its contestants - the one that YOU are creating is a game where you have to guess a word, letter by letter.  Sound familiar?

## Task

You will be creating a word guessing game.  A pre-set word is chosen, and the player sees how many letters are in the word - a blank spot for each letter.  The player then has to guess the letters in the word, one letter at a time. If the player guesses a correct letter, then the correct letters show in their respective spots. The letters that the player has guessed should always be visible.

For example, if the word was "programming", the player might see:

```
_ _ _ _ _ _ _ _ _ _ _
Guesses:
```

After guessing "g", "a", and "t", the player would then see:

```
_ _ _ g _ a _ _ _ _ g
Guesses: g a t
```

## Extensions

### Level 2

Implement the following:
- Have the program count the number of mistakes, and set a maximum amount.  For example, make it so that they only get 5 incorrect guesses, and if they make more than that, they lose the game.
- Have the word be randomly selected from a list of words.  This way, someone can play again and again and not know what the answer will be.
- Make it so that the player can't guess a letter they have already guessed.

### Level 3

Modify the game so that it supports phrases with spaces instead of single words.  Spaces should not have a `_` placeholder and do not have to be guessed.
