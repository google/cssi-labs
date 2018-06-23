### Ready to *bash* the repetition out of your daily command line usage? Great, so am I!

## Background
If there's one thing programmers hate, it's repetition. As computer scientists
it's our job to make the computer do as much of our work as possible. Writing
bash scripts will help us make our command line usage more efficient.

First things first, **What** is a bash script?

*GREAT* question, thankfully our friend Ryan Chadwick, over at [this great
place to find command line
tutorials](https://ryanstutorials.net/linuxtutorial/scripting.php), has an
answer for us.

 >A Bash script allows us to define a series of actions which the computer
 >will then perform without us having to enter the commands ourselves. If a
 >particular task is done often, or it is **repetitive**, then a script can be
 >a useful tool.

No repetition? **That's** what I'm talking about.

![Boom Shaka Laka](https://media.giphy.com/media/qiPJ5kow5KOT6/giphy.gif)

## Tutorial
First things first, in order to be able to run your script, you're going to
need to give your computer *permission*. Do this by running the command below.

    chmod 755 myScript.sh

Alright, time to write your first program. Head over to your myScript.sh (see
if you can open the file from the command line). Starting on line 2, write:

    echo "Hello World"

Now run:

      ./myScript.sh

in your terminal. ** TA DA ** you should see "Hello World" printed in your
terminal.

![celebration](https://media.giphy.com/media/YTbZzCkRQCEJa/giphy.gif)

Everything that you write in your bash script will run as if you had typed it
into your terminal. Let's walk through one more example before jumping into
extensions. **First** create a file for your script, this can be called
anything you want but it should have the extension .sh . **Next** make sure to
give your script permission to run by typing `chmod 755` and then the name of
your script in your terminal and pressing enter. Every time you start a new
bash script you should make sure to complete those two steps.

## Intro Challenge
Now, let's try writing a script that creates a new folder. What command do we
know creates a new folder? If you're thinking of a word that starts with a m and
ends with kdir, you're on the right track. Write the command that will create
your new folder and name it something cool in your new .sh file, then run it in
your terminal.

If it works, move on to the other challenges listed below. If you're still a
little confused try looking back at your around the world lab and thinking
about how you created new country and city folders.

Don't be afraid to use the tutorial linked above and be ready to whip out your
best googling skills. Write and run scripts that do the following:

## Main Tasks
1. Add a command to the file you created above that navigates into the folder
you're creating. (What command do we use to change directories?)
  * Date stamp your new folder name. For example, your program should create a
    folder named "2017-12-07my_super_cool_folder"
2. Prints out "My current directory is: " followed by your working directory,
and "Here is a list of everything in this directory! " followed by the contents
of your current directory.
3. Figure out how to give your bash script an input, and create a file based on
that input string. The tutorial linked earlier in the lab has some great
examples in the variables section to check out.
4. Ask the user for their name, then print out "Hi nice to meet you *insert
their name here*"
  * Try asking your user for more info and creating a customized message for
    them.
