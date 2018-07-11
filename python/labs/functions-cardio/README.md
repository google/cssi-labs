
# Functions Cardio

The best way to get good at something is just doing it - lots of attempts in a short span of time. This lab is all about practice. We're calling it functions cardio, but don't sweat it - this is a great chance to see what makes sense to you and what you will need some help with.

## Background

You receive a fancy new graphing calculator that allows you to write programs in Python3.  You want to make a program that contains a bunch of quick tools (functions) that will help you throughout your school day.  Let's write these functions to save them in our cool new calculator!

## Task

We detail for you five possible exercises to complete - you must **choose three** and write those functions.  Be sure to test them to make sure they work!  Here's an example of how to test a function.

#### Example: `count_spaces`

Let's say we have a function `count_spaces` that accepts one string argument, and counts the number of spaces in the argument.

We would write the function:

```python
def count_spaces(s):
    return s.count(" ")
```

And we can test the function by calling it:

```python
print(count_spaces("hello world!"))  # => 1
print(count_spaces("wow wow wow "))  # => 3
```

Notice how I put in comments the expected output (it should count 1 space, then 3 spaces).  Run the program, look at the output, and see if the output matches your expected output.  If they do, then it's good!

#### Exercise 1: `longest_word`

Write a function `longest_word` that accepts three arguments, each representing a string.  Return the longest word among  the three strings.

#### Exercise 2: `reverse_string`

Write a function `reverse_string` that accepts one argument as a string, and returns the string with its letters reversed.  For example, `"hello!"` becomes `"!olleh"`.

#### Exercise 3: `sum_to_n`

Write a function `sum_to_n` that takes one argument as an integer `num`, and returns the sum of 1 + 2 + ... + `num`.  Example: `sum_to_n(4)` returns `10` (1+2+3+4).

#### Exercise 4: `is_triangle`

Write a function `is_triangle` that takes three arguments `s1`, `s2`, `s3`, that represents the lengths of the three sides of a triangle.  This is a valid triangle if the sum of two lengths is always greater than the third. Return the special value `True` if the three arguments represent a valid triangle, or `False` if they do not.

#### Exercise 5: `roll_dice`

Write a function `roll_dice` that takes in an argument `num` representing the number of 6-sided dice to roll, and returns the sum of the `n` rolls.  Simulate rolling that number of 6-sided die using `import random` and `random.randint(1,6)` to generate a random number between 1 and 6 inclusive.  Remember that if you are rolling for 2 dice, it's not as simple as running `random.randint(2,12)`!  You must roll each die individually to maintain realistic chances - rolling a `2` is much more rare than rolling a `7`!

## Extensions

Try some of these harder ones:

#### Extension #1: `isPrime`

Write a function `isPrime` that takes in one integer as an argument and determines whether it is a prime number or not.  As a reminder, a prime number is only divisible by 1 and itself.  `isPrime` should return `true` or `false` depending on whether the number is prime.

#### Extension #2: `snake_case`

Write a function `snake_case` that takes in a string in camelCase (like you would write variables in Javascript), and converts it to snake_case, converting everything to lowercase and separating by underscores.  You can assume that each capital letter is the start of a new word.  Use string slicing to get "parts" of a word.

#### Extension #3: `get_number_input`

Write a function `get_number_input` that takes in a string as the prompt, and uses that prompt to ask the user for input using `input()`.  However, in this function, you must ensure that the user enters a number (int or float), otherwise, it must ask the question again.  Return the user's input only when they enter a valid number.  It should be able to accept negative numbers and decimal points.
