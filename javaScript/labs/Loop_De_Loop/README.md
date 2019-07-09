![](https://media.gettyimages.com/photos/spiral-loop-of-a-green-steel-roller-coaster-picture-id157194447)
#### Introduction
At this point in your journey with code you will have learned that loops don't just belong in roller coasters, we use them in code too! In this lab we're going to explore the differences between each iteration technique that you've learned. We're going to cover...
1. `forEach` loops
2. `for` loops
3. `while` loops

Each of these options have unique properties that make them better suited for different kinds of uses. The `script.js` file you've been given is already linked to your `index.html` file. When you open up a preview of your html file and use inspect to see the console, you should see "script is running..." printed. This is where all of the outputs of your code will go. Use `console.log` to print to the console and ensure that the code you're writing is outputting the correct results!

#### Task
1. Let's start with `forEach` loops. `forEach` loops should be used when you **know** that you want to iterate through **all** of your data. For example, if you're given an array of strings and want to capitalize every element of the array. If you look in your `script.js` file you've been given an array called `amusementParks`. It contains the names of 5 different amusement parks in the US. Write code that will iterate through the array and make the entire string uppercase, then `console.log` "NAME is a great amusement park". Since you want to do the same thing for every element in the array, you should use a `forEach` loop.

2. Now we're going to look at `for` loops. `for` loops can do the same thing as `forEach` loops, but their additional value comes from the fact that we can break out of them if we want to. In addition, we can use for loops to iterate through data structures that are not arrays. Let's see how a for loop may be helpful with an array. In your `script.js` file you're given a list of roller coaster rides. They are listed in order of increasing difficulty. You know that the hardest roller coaster you're willing to ride is called "Space Mountain". Write a for loop that iterates through the roller_coasters array and prints "I will ride NAME" for every roller coaster up to Space Mountain.
  * You'll need to use a conditional inside your for loop to check if each element is equal to "Space Mountain".
  * Once you find "Space Mountain" you should still `console.log` "I will ride Space Mountain", but then you should break out of your for loop. You can do this by using the key word `break`. Break will exit the loop you are currently in. Check out the pseudo code example below. In the example, we are moving through a for loop until we hit a condition. Once the `if` statement evaluates to `true`, we will break out of the for loop and your code will continue running below it. In your own code you won't be using the word "condition", but will instead place an actual condition that you need to test in the if statement.

    ```javascript
    for (let i = 0; i < 5; i ++){
      if (condition) {
        break;
      }
    }
    // once you break your code will continue running from here
    ```
3. Now let's use a `while` loop. The magic of while loops is that we can continue to do the same thing until a condition changes. We use while loops when the number of iterations we need to complete depends on a condition. You're given a variable height that is originally initialized to 6. Write a while loop that will continue to print "Next Customer" while height is greater than 4. This way, the line will be stopped once you reach a customer that is not tall enough to ride the ride. In each loop, after you console.log "Next Customer" set height equal to a different random number between 2 and 7. The code block below generates a random number between 3 and 22.

  ```javascript
  let number = Math.floor(Math.random() * 20) + 3;
  ```
