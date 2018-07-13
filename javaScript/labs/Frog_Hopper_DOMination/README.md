
### Introduction
In this lab you'll be recreating some of the functionality of the frogger game you may remember from your childhood. You've been given the html and css to create a board with lily pads and a frog on your screen. As you work through the tasks below you'll move closer and closer to having your very own fully functional frogger game!

![Frog image link: https://www.gettyimages.com/detail/photo/frog-bathtub-stopper-royalty-free-image/172183896](https://media.gettyimages.com/photos/frog-bathtub-stopper-picture-id172183896)
### Tasks

Complete the tasks below in order! You'll be coding in your script.js file, but feel free to check out the html and css file for any information on styling and classes/ids. You may notice that some styling has been done inline in the HTML file. This is used for the purposes of this lab, but you should try to avoid using this in the future.


1. Let's begin by adding an event listener to our frog. Check our your work from the Color Buttons lab for an idea of how to begin. When you click on the frog you should print "hop" to the console.
<details>
 <summary>Not sure where to start?</summary>
  <ul>
    <li> Begin by using a query selector to grab the frog from your html.</li>
    <li> Save it in a variable in your script.js file. </li>
    <li> Add an event handler to your frog variable, write a function that prints "hop" to your console.</li>
  </ul>
</details>


2. Now that you've grabbed your frog from the html and create an event listener, let's take it a step further. After printing "hop" to your console, try moving the frog onto the second lily pad. The code below would take care of the horizontal movement. Copy the code below into your click function for your frog and check out what it does. Now try doing a similar thing to take care of the necessary vertical movement.
<!-- Insert code block  -->
```javascript
frog.addEventListener('click', e=>{
  frog.style.left = "33.5%";
});
```

3. You may have noticed that the first lily pad is "glowing" with a yellow border. Figure out what class the first lily pad has that causes it to "glow". Use the classList property to make the second lily pad glow when your frog lands on it.

4. Now use the classList property to make your first lily pad stop glowing once your frog has moved on to the second lily pad.

5. When your mouse is over your frog, increase the size slightly (to about 80px by 80px). It should return to normal size when your mouse leaves it.

7. When you click on the space bar, reset the game to how it was originally.

### Extensions
* Now that you have your frog hopping from the first lily pad to the second, find a way to make it continue to hop along the path each time you click on it. Take a look at the ids and consider how you can use a counter variable to keep track of which lily pad you're on. Consider what data type you'll need as a counter, what data type you'll need for the id, and how to convert between the two of them.
* When you reach the last lily pad create a header element and add it to your document. It should say, "Congratulations, you won!"
* Make one of the lily pads a tricky jump by making it blink every second. It should alternate between being visible and being invisible.
    * Take this a step further, if you land on the lily pad while it is invisible, you should lose the game. You decide what that means.
