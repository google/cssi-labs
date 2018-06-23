]
# Movie Review Database Update

## Background

You've been contracted to do some work with IMDB, updating their movie database.  They have a few inaccurate records that need to be manually fixed.  You are given a piece of data representing the movie "Inside Out" that you need to update.

Here's the catch though, you can't edit the piece of data yourself.  It's common practice to change data in a database through individual operations, because if anything goes wrong, the operations can easily be reversed.  Your job is to write some lines of code that will update the movie record.

## Task

Using the given file `movie_reviewer.py`, Your goal is to do the following:

1. Go to the actual IMDB site for [Inside Out](http://www.imdb.com/title/tt2096673/) and identify which values in the given dictionary are inaccurate.
2. Write lines of code to update the original dictionary with the new information
3. Remove the `out_of` key-value pair, since your boss thinks its not needed since every movie is rated out of 10.
4. Add the genres with they key `genre` and the value as a list of strings
5. Print out every key-value pair in the dictionary so you can double check that it worked.

**Remember, you cannot edit the original dictionary!  Start writing your code on line 16.**

## Extensions

### Level 2

Select two more movies that you enjoyed from IMDB, and add them to the file.  Make sure all their information is accurate!  Do this under line 16.

### Level 3

Now combine all three movie data into a single array with three elements (Inside Out + 2 movies of your choice).  Ask the user to input a genre and display the highest rated movie of that genre.  To make sure this works, make sure you pick two movies that have at least one genre in common!
