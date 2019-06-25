
![](https://media.gettyimages.com/photos/puppies-in-a-basket-picture-id739281687)
#### Introduction
It's time for Puppies.

As you may know, giphy.com is a website with a large database of gifs. We can access those gifs through their API. The API provides us with direct access to the data behind everything you can see on their website. By using a designated access point to this database, we can search for things and receive tons of data from the website pretty easily. We've already used the access point to get a large object full of puppies, and we saved the response for you to play with.

If you go check out `puppies.js` you'll see a large, complex object called `dataObject`. Inside of `dataObject`, you'll see there is a key called `data`. The value associated with this key is an array. Each element of that array is another object... and so on.

You'll be combining your knowledge of, well, everything to create an amazing puppy gif generator.

#### Tasks
**Pre Task:** Let's begin by making sure that all of our files are linked correctly. Since `puppies.js` is loaded in the html file before `script.js`, we can use the global variables from `puppies.js` in `script.js`. Currently, `script.js` contains a statement:

```javascript
console.log(dataObject);
```
Open up a live preview of the html page and check out your console. You should see an object printed. Use the arrow to expand the object until you can see all of the levels. If you hover your mouse over a key, you'll see the path you need to use to access it. For example, hovering your mouse over the first gif's `rating` displays `.data["0"].rating`.

This means that in order to access the first gif's rating, we need to type:
```javascript
  const firstGifRating = dataObject.data["0"].rating;
```
1. Add a button into the html page. When you click on the button, `console.log` the image URL for the first gif. This URL is inside of the `images` key, under the original attribute. Use the trick discussed above to figure out how to access this value.

2. Now, when you click on the button create a new `img` element with a source equal to the URL you console logged in task 2. If you do this successfully, you should see the gif displayed on the page. Check out these [examples](https://www.w3schools.com/jsref/met_document_createelement.asp) for ways of creating new elements and adding them to the DOM.

3. Once you have that working, use a `forEach` loop so that clicking on the button results in all 10 dog gifs being printed. Think carefully about what array you want to loop through and how to access that from `dataObject`. You'll need to create a new element for each gif and set the `src` to the correct link each time. Set the height and width of each gif to be 200px. Give each of these images a class of "gif".

4. Add to the task you completed above by making the title of each gif appear as well.

5. Create a new button. When you click on this button, select all elements on the page with the class "gif" and delete them.

6. Create a third button. When you click on this button, display a random gif from the `dataObject`. Pay attention to the way in which you need to access each element of the array, as well as the bounds of the array indices. The button from the previous task should clear all of these gifs as well.

7. Get rid of your third button. Instead of displaying a random gif when you click a button, display a random gif each time your mouse moves.

#### Extension
Instead of displaying a random gif each time your mouse moves, do this each time you click *anywhere* in your window. Set the properties of this new gif such that it appears in the same location you clicked on the page.

Use style attributes to nicely style the elements you're adding onto the page. For example, when you use the button that displays all gifs, make the gifs display in rows with the title underneath the respective gif. Set the size of each gif so this looks nice.

Make it so that the button that displays all of the gifs will only do this once. After you click it the first time it won't work again until you use the clear button to get rid of all of the puppies.
