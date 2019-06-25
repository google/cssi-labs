
#### Introduction
In this lab we're going to look at how we can use arrays to hold data. You're given a recipe for the best apple pie in the world, but it's your job to use array methods to group all of the instructions together.

**Recipe**
1. Heat oven to 425ºF. Prepare Double-Crust Pastry.
2. Mix sugar, flour, cinnamon, nutmeg and salt in large bowl.
3. Stir in apples.
4. Turn into pastry-lined pie plate. Dot with butter. Trim overhanging edge of pastry 1/2 inch from rim of plate.
5. Roll other round of pastry. Fold into fourths and cut slits so steam can escape.
6. Unfold top pastry over filling; trim overhanging edge 1 inch from rim of plate.
7. Fold and roll top edge under lower edge, pressing on rim to seal; flute as desired.
8. Cover edge with 3-inch strip of aluminum foil to prevent excessive browning. Remove foil during last 15 minutes of baking.
9. Bake 40 to 50 minutes or until crust is brown and juice begins to bubble through slits in crust. Serve warm if desired.

#### Tasks
Your HTML and JavaScript files are linked, so the outputs of your code will be in the console of your HTML page!
1. Begin by creating an empty array called "recipe" in your `script.js` file.
2. Write a function `addInstructions` that takes an array as an input and pushes all of the recipe instructions into the `recipe` array in the proper order. Each instruction should be inserted as a string. The function should return the array.
3. Write a function `checkStep` that takes an input of the step that the person using your recipe wants to double check and the array they want to look in. Remember that step numbers begin at 1, but indices begin at 0. So, step number 1 has an index of zero in your array. Access the correct element of the array and return it.
4. Write a function `checkLength` that takes an input of an array and returns the length of the array.
5. Write a function called `publishRecipe` that takes an array as input. Use a `forEach` loop to print out every step in the array. Each step should start on a new line.
  - Extension: Figure out how to print the step number before each step. So, for example you should print "Step 1: Heat oven to 425ºF. Prepare Double-Crust Pastry." on the first iteration.

#### Extension
Let's begin incorporating the DOM. Write a function `publishRecipeToPage`. This will do a similar method to your `publishRecipe` function, but instead of printing each instruction to the console, you will display them in `index.html`. You may want to look online and figure out how to create new elements and append them to your html.
This function should be called when you click on the button on the page. Your JavaScript file is already linked to the page and your HTML has a button in it that is waiting to be pressed!
