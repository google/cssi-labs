![](https://media.gettyimages.com/photos/closeup-of-clock-against-blue-background-picture-id763270575)
#### Introduction
You have realized that you and your family have been running late for... **everything**. You've decided to write some alarm clock functions to help everyone out. Currently your script.js file is linked to your html file. If you open up your index.html page and look in the console, you'll be able to see the output of your code. Before you get started do this and make sure "script is running" is printed into the console.

#### Task
You'll be writing each of the functions given below and testing them yourselves. Let's go over a quick recap on how we do this. A basic alarm function that takes in a message and returns it is shown below.
```javascript
function Basic_Alarm(alarmMessage){
  return alarmMessage;
}
```
In order to test this function, and print it's output to the console, we would add the following line to our code **below** the function.
```javascript
console.log(Basic_Alarm("My alarm!"));
```
If we run our script and see the correct output, then we know our function is working and can move onto the next one! Try this out on the tasks below...

1. Write a function called My_Alarm. The function should take in an input of a string with the time you need to wake up. The output of the function should be "Hey, *NAME*, wake up! It's **\*insert time***". Instead of NAME your function should have your name.

2. Write a function called Mom_Alarm. The function should take in an input of a string with the time you need to wake up. The output of the function should be "Hey, Mom, wake up! It's **\*insert time***"

3. You may have noticed that the two functions above seem very similar. In an effort to avoid repeating code, let's make a new function called Family_Alarm. This function should take in **two** inputs, a string with the time you need to wakeup AND the person you are trying to wake up. The function should return "Hey, **\*insert person***, wake up! It's **\*insert time***"

4. Write a function called Important_Alarm that takes in a message and returns it in all uppercase. For example, if the input is "wake up, wake up, wake UP!!" The function will return "WAKE UP, WAKE UP, WAKE UP!!".

5. Write a Snooze_Alarm function. This should take in a number time, such as 1, 2, 3,.. etc., add one to it, and then return the string "The alarm for **\*insert original time*** has been changed to **\*insert new time***"

#### Extension
* Write an alarm that takes in the number of people it needs to wake up and prints "Wake up!" that number of times. Check out what kind of built in javascript string functions may let you do this.
