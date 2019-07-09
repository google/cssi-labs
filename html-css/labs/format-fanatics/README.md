### Ready to grind out some grid-full page formats?
![](https://media.giphy.com/media/gdM6D5CAc1puw/giphy.gif)

## Background
You've been asked to create a family scrapbook for your parent's upcoming
birthday. With your knowledge of CS, you decide to bring scrapbooks into the
modern age and digitize the process.

## Task
You'll be given several page formats and asked to recreate them. We'll use
`div`s labeled with the content that will fill them, for example, "Photo",
"Caption", and "Title". Once you're finished, feel free to replace these with
actual content.

This [guide about Grid
layout](https://css-tricks.com/snippets/css/complete-guide-grid/) might be
helpful as you work through the lab.

1. Format One:
You'll recreate the format below in the `format_one.html` and `format_one.css`
files. You may notice that there is already some styling done for you in
`basic.css`. For now, ignore this as it isn't related to the css grid skills
that we're practicing.

    ![](https://media.giphy.com/media/3ohs4AiUTpVfnKV0ze/giphy.gif)

2. Format Two:
Recreate this format in the `format_two.css` and `format_two.html`. You'll need
to use the `span` property to get all of the columns looking the way you want
them. In order to have your page border look correct you'll need to span in both
the column and row direction.

    ![](https://media.giphy.com/media/3o7WIEF2KAorL474VW/giphy.gif)

  Now that you've used your css grid skills to make this look nice, take a look
  at the `basic.css`. Meander your eyes on down to line 4 and **shocker**, what
  do we see?

  ```css
  display: flex;
  ```
  ![](https://media.giphy.com/media/12BxzBy3K0lsOs/giphy.gif)

No doubt, you feel betrayed right now. "But I thought this was a css grid
lab??". Yes, it is, but the real benefit of these things come when they are
used **together**. Often, flexbox will be the easier choice when styling
individual elements and trying to align content, while css-grid will allow
you to easily create bigger picture page formats. Parse through the
`basic.css` code and try to understand the gist of what is going on.

3. Format Three:
Watch the behavior of the mock-up below as you expand the width of the page.
Check out the `auto-fill` vs `auto-fit` and `minmax` properties to achieve this
effect. Remember, all of the rows should be 100px, no matter how many rows you
end up with.

    ![](https://media.giphy.com/media/xUOwGj6l4EyEzJWp44/giphy.gif)

4. Format Four: Putting it all together
This will be a messages page, where family members can write happy birthday
messages and sign the scrap book. However, some family members have requested
more space for writing.

    ![](https://media.giphy.com/media/26DNca9t7TFLwLfKU/giphy.gif)

You've been given a general format in the `format_four.html` and
`format_four.css` files. You'll need to replace the large "messages" block with
15 or more individual message blocks. The class of each box should signify
which kind of family member has written the box.

  - **Siblings:** Span 2 columns, but one row
  - **Aunts and Uncles:** Span 1 column, but two rows
  - **Grandparents:** Span 2 columns and two rows
  - **Cousins and friends:** One row, and one column

## Extension
Look back at the extension in the museum-manager flexbox lab. Try to recreate
the same (or a different) Mondrian using CSS Grid instead. If you've worked in
both, think about which one you thought was easier to use and what aspects of
the features were more and less helpful.
