## Background

Your local art museum is having trouble finding the best way to place all of their pieces on the walls. They've asked all of the local art aficionados to submit ideas for different formats. Your best friend has made some sketches that they think will really take the museum to the next level, and they've asked you to recreate them on the computer for their final submission.

## Task

Using what you know about CSS Flexbox recreate each of the wall designs you see below. If you're not sure where to start, check out the "more details" for each wall.

Feel free to use the guide linked below as a resource!

[Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

1. **Vincent van Gogh Wall:**
This wall of the museum will be dedicated to some of van Gogh's best work. You've been given some HTML and CSS to get you started. You'll be working in the `wall-one.html` and `wall-one.css` files.

    So far, only the image with the id `vg2` has been styled in the CSS. You'll need to give each image its own ID in order to style them uniquely. Model your CSS for the remaining paintings after the code given in the file.

    At this point, your images should be in the correct order, but you may have noticed that your spacing is different. Check out the `justify-content` attribute discussed in the guide linked at the top of the lab.
<details>
 <summary>Click for more details</summary>
  <ul>
    <li>None of the pictures should grow or shrink as the size of the screen changes.</li>
    <li>The images should always be evenly spaced, no matter what the size of the screen is.</li>
    <li>The images should be in the order shown. Try to accomplish this without adjusting the order of the images in the HTML</li>
  </ul>
</details>
![Wall 1 Gif](https://media.giphy.com/media/l0HUjGaYENxkKlp8Q/giphy.gif)


2. **Claude Monet Wall:**
This wall is a bit more modern; the museum is introducing digital images that can change size as the screen changes size. Find a way to make sure your second wall acts the same way as the example below when you change the size of your preview.

    You've been given some code in your `wall-two.html` and `wall-two.css files`. Apply some general styling to the rows and images. You'll need to do some work in your HTML for this step as well.

     Next, finish the `display` property styling for the first row. Make sure to add this into your second row's styling as well.

     Finally, finish the styling for the first picture and add styling to each of the remaining images.
<details>
 <summary>Click for more details</summary>
  <ul>
    <li>Your rows and images should all be 100px tall.</li>
    <li>There should be 10px of space between the two rows. </li>
    <li>Your wall should have two rows of paintings.</li>
    <li>The ratio of the growth of image sizes on the top row should be 1:2:3 from left to right.</li>
    <li>The ratio of the growth of image sizes on the bottom row should be 3:2:1 from left to right.</li>
    <li>There should be no space between the images.</li>
    <li>All images should shrink at the same rate.</li>
  </ul>
</details>
![Wall two gif](https://media.giphy.com/media/3o752dVeKrvrvWnv0Y/giphy.gif)


3. **Paul Signac**: Rows are cool, but columns are cooler. See if you can recreate the preview with only one flex container. You've been given the images that you should be using in your `wall-three.html`. You should complete your styling for this wall in the `wall-three.css` file.
  <details>
   <summary>Click for more details</summary>
    <ul>
      <li>If you're lost on how to create a column, check out the `flex-direction` property.</li>
      <li>The first image in your column should be aligned on the right side of the screen.</li>
      <li>The second image should be centered.</li>
      <li>The third image should be left aligned.</li>
      <li>When the screen is small enough, all three images should stack on top of each other.</li>
      <li>In order to align an item in a certain way, you may want to use the `self-align` property.</li>
      <li>Items do not need to be able to grow or shrink.</li>
    </ul>
  </details>
![Wall 3 gif](https://media.giphy.com/media/3ohc1aedNONEvkXY4g/giphy.gif)


## Extension
After spending all of that time organizing art, you've decided to actually make some art of your own. See if you can recreate the Mondrian piece below. Before starting, make a plan of how you can organize the painting into different rows and columns. Keep in mind that you may have to nest rows inside of columns, inside of other rows.... Having a plan of action here is key! Each square should be its own `div`. Do your work in the `mondrian.html` and `mondrian.css` files. Best of luck, and happy (digital) painting!

![Mondrian](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Composition_A_by_Piet_Mondrian_Galleria_Nazionale_d%27Arte_Moderna_e_Contemporanea.jpg/1030px-Composition_A_by_Piet_Mondrian_Galleria_Nazionale_d%27Arte_Moderna_e_Contemporanea.jpg)
