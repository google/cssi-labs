#### Introduction
Now that you've written some JavaScript and become comfortable with the language, you've decided to try to make some money by correcting other people's code. You offer two services:
1. Debugging
  - In these cases you help people locate errors in their code. If this code does run, it will likely return incorrect answers. Look for syntax errors, like a missing parenthesis or using the wrong number of equal signs, as well as gaps in logic that might result in an incorrect output.

2. Style Correction
  - This kind of code will run correctly, but will be extremely hard to read. Use the Google style guide to ensure that the code's style is as solid as the logic behind it.

#### Tasks
Complete the tasks below and successfully correct all of the broken code you've been given. Before you get started, check out the tips and tricks for debugging below! In order to get started open up a live preview of the html file. The page is empty, but if you check out the console, you'll see that the code from `debug1.js` is running.

<details>
 <summary>If you get stuck, click here for tips and tricks.</summary>
  <ul>
    <li>Error messages are your friend here. Run the code as many times as you need to see where your errors are.</li>
    <li>Debug in chunks! At the end of each file is a section commented "Test Functions". Comment out all function calls except for one so you can debug a single function at a time. This will make your job **much** easier.</li>
    <li>Print statements are also extremely helpful when debugging. Place `console.log`s throughout your code to see what variables are holding what and how far your code is getting before it stops running.</li>
    <li>Be conscious of data types as well as what values certain built-in functions actually return.</li>
    <li>No code is safe! Don't assume that the code underneath the "Test Functions" comment is correct...</li>
  </ul>
</details>
<br>

You'll know that you've correctly found and squashed all bugs once you can run these files and get the correct output. Remember, you run the code by refreshing the page in your browser.

1. Begin by opening up your `debug1.js` file. You can run this by opening `index.html` in your browser. You'll notice that when you run this code you get some errors. This is because this code is broken! It's your job to fix all of the errors throughout the code. Look through each function using error messages and placing print statements if you need them in order to debug the code. You'll know you're finished when your code runs successfully.

2. Now that you've warmed up your debugging skills, it's time to work through `debug2.js`. Go into the index.html file and comment out the first script tag. Uncomment the line that links `debug2.js`. Now when you open up the html page, `debug2.js` will be running in the console.

3. Now that you've learned how to make sure your code works, it's time to learn how to make code readable. Ugly code is hard to understand, which makes it difficult to work with other people when you're coding. Open up your `index.html` file again and uncomment the `style.js` script tag. Make sure all other script tags are commented out. Open up the file `style.js`. If you run the code (it will run automatically when you refresh the html page and check out the console), you'll see that it works. I know, I was shocked too. Use the [Google style guide](https://google.github.io/styleguide/jsguide.html) to fix this code. Do your best to work through the file without looking at the answers, but feel free to expand the section below to check your work once you've finished.

<details>
 <summary>Click here for the solution to the style challenge.</summary>
 ```javascript
 const uglyCode = (arr, num) => {
   if (arr.length == 0) {
     return "array length is zero";
   } else {
     if (arr.length > 5) {
       for (let i = 0; i < arr.length; i++) {
         arr[i] = num;
       }
     }
   }
   return arr;
 }

 const array = [0,0,0,0,0,0];
 console.log(uglyCode(array, 5));
 ```
</details>
<br>

#### Extension
Ready to really challenge your debugging skills? Open up `debugExtreme.js` and get the code working! Make sure to have the correct script tag uncommented in your html file. Feel free to work with another partner that has finished all the tasks. This code is **hard**, so enjoy the struggle and take your time walking through each section of code!
