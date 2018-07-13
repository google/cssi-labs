![](https://media.gettyimages.com/photos/mature-woman-inserting-credit-card-into-local-french-cash-machine-picture-id723498437)
#### Introduction
As the newest intern at the biggest bank in the world, you're determined to prove yourself. As the weeks continue you begin to realize that your bank's business could improve drastically if many of the processes that customers use were automated. As a result you decide to write some functions to show your boss. Your first priority should be to write working code, but style matters when you're planning on showing your code to others, so be mindful and use best practices! Since we're just starting out in JavaScript right now we're going to focus on building out the functions and code we need for a single bank account. In the future, you'll be introduced to more tools that will allow you to build out more bank accounts and push this same idea even further.

You should also be testing your own code as you go. In order to test your code, call the functions you write and console.log the values returned. You'll be able to see these outputs in the console when you open up the live preview of the html page. The files are linked for you, but you can double check by opening up the html file, using inspect mode to see the console, and making sure that "script is running" is printed. Check out the example code below for help:

First, write your actual function.
```javascript
//First write the function
function testMe(a){
  return a + 4;
}
```

Next, you'll call the function and console.log the value returned. Remember, you won't see values that are returned, you need to print them for the values to actually appear in your console. You can do this two ways...

One: Call the function and save the returned value in a variable, then console.log the variable.
```javascript
let result = testMe(5);
console.log(result);
```
Two: Do this all in one line as shown below
```javascript
console.log(testMe(5));
```
Here is a screenshot of what you would see in your console after running either of these code blocks.
<!-- Insert image -->

Test your functions with different inputs to make sure they're returning the correct things!

![](https://media.gettyimages.com/photos/closeup-of-benjamin-franklins-portrait-on-the-one-hundred-dollar-bill-picture-id636176028)
#### Tasks
A lot of the tasks below will include some new information. You've been given some starter code in your script.js file. Open up your file and take a look at it. You should see that you have two global variables defined for you, balance and customer_name. There are also three functions that are defined and will need to be filled in by you as you move through this lab. Happy coding!

1. First things first, your customer needs to be able to create their account. You're going to write a function called openAccount that takes an input of your customers name. Your function should set the global customer_name variable equal to this input and the global balance variable equal to 0. Have your function return "NAME has opened a new account with a balance of $0." Replace NAME with the input. You're given some code to get you started with this function in your script.js file.

2. What if someone comes in with $100 right off the bat that they want to open their account with? Let's account for this situation by adding another input to our openAccount function. This input should be a starting balance. If a starting balance is given, set balance equal to that. Otherwise, the default value for the input should be zero. The code below is an example of a different function that has an input b with a default value. Apply the same ideas shown below to the code you add into script.js.
```javascript
function useDefaults(a, b = 0){
  return a + b;
}
useDefaults(2); //this will return 2
useDefaults(2, 3); //this will return 5
```
3. Write a deposit function that takes an input of how much money you want to deposit and adds it to your balance. This function should return "NAME has deposited VALUE. NAME 's total balance is $BALANCE'"

4. Now that you have money in the bank, you need to be able to withdraw. Write a function that takes the amount you want to withdraw as an input, and subtracts that number from your global balance variable. The function should return "NAME has withdrawn AMOUNT. NAME has $BALANCE remaining."

5. Some of you may have started to ask yourselves what happens if you try to withdraw from an empty bank account? Or what if you try to withdraw more money than you have? These kinds of examples are often called **edge cases**, essentially they are the situations that are most likely to break your code. Strong code accounts for all of these edge cases. Use conditionals to check if the amount you're trying to withdraw is larger than your current balance. If it is, return "Sorry, NAME, you do not have enough money in your account. You need DIFFERENCE more dollars." DIFFERENCE should be the amount of money you need to deposit to make this transaction possible. If you don't have enough money, balance should stay the same.

6. Write code that will create a new account with a starting balance of $300, deposit $50, and then withdraw $500. Use console.log as shown in the introduction to test each function call.

#### Extension
![](https://media.gettyimages.com/photos/vault-door-picture-iddv631022b)

Let's add some security measures to our code. Create a global variable named logged_in that is initialized to false. This variable will keep track of whether or not your user has logged in. Create another global variable called password.
* Update your createAccount function to take a password input that sets the global variable.
* Write a logIn function that takes your name and password as inputs. If the name and password match your global variables, update logged_in to true and return "NAME has logged in." Otherwise, return "Incorrect log in" and set logged_in to false.
* Write a logOut function that takes no inputs, but sets logged_out to false and returns "NAME has logged out."
* Update your withdraw and deposit functions so that you cannot withdraw or deposit if you are not logged in. If you are not logged in both functions should return "User must log in." and should not change any values.
