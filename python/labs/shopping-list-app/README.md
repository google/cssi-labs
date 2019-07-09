
![](/images/shopping-list.png)

## Background

You are going to write a program that keeps track of a running shopping list for the user.  The file `shopping_list_starter.py` is provided for you as a template.

## Task

Your program should allow for the following functionality:
- add an item to the list
- remove an item from the list (assume the item is already there)
- show all items on the list (printed in a list format)
- exit the program

You should start by writing the conditionals.  Remember to use `append()` to add an item to a list and `remove()` to remove an item from a list.

The program will repeatedly ask the user to choose one of the above options until the user chooses to exit the program.

## Extensions

### Level 2

Your program should allow for the following functionality:
- add an item to the list.
- remove an item from the list (**do not assume the item is already there**).
- **check to see if an item is on the list**.
- show all items on the list (printed in a list format).
- exit the program.

Similar to above, the program will repeatedly ask the user to choose one of these options.

When removing an item from the list, you should check to make sure the item is actually on the list to avoid an error.  Don't forget that you can use `item in list` to check if `item` is in `list`.

### Level 3

All of the above, plus any number of the following features:

- Prevent duplicates: before adding an item to the list, first make sure that it doesn't already exist in the list.
- Ask to remove: before removing an item to the list, ask the user if they are sure they want to remove the item from the list.
- Advanced checking: when checking for an item, if the item is not in the list, ask if they would like to add it.  If it is in the list, ask if they want to remove it.
- Multiple entries: when adding an item to the list, allow the user to add multiple items in one line separated by commas (using `split()` to separate and `strip()` to remove whitespace - both are string functions).  For example, the user typing in `"eggs, milk, bread"` should add three individual items to the list - `eggs`, `milk`, and `bread`.

## Skills you may need

Remember to use Python List methods, such as `append()` and `remove()`!

The most difficult part of this project is probably managing all the different options.  Use `while` loops, `for` loops, and `if/else` statements to their full potential here.  Have a different block of code for each possible option and keep your code organized!
