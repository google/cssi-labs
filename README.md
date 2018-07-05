# CSSI Curriculum Labs

Welcome to the CSSI Curriculum Labs.

This repository contains the code and instructions for the student activities
and labs that complement the CSSI curriculum.

## How to download and complete these labs.

You will clone this repository to your local machine, and complete the exercises
locally. You will **not** contribute your solutions to this repository, but
you can, if you choose, create your own repository and use it to store your
solutions for later.

### Cloning the repository

To create your own local copy of this repository, use the following command:

``` shell
git clone https://github.com/google/cssi-labs
```

This will create a new folder with all the files you will need for the course.

### Writing your solutions

The main level folders divide the content by topic, inside each folder you
will find all the activities for that topic. Each lab or activity has a
`README.md` file with the instructions. You can find the same instructions in
the CSSI curriculum website shared with you by your instructors.

### Saving your solutions (optional)

If you choose to use GitHub to track your solutions, you will **not** be saving
them to Google's original repository, but you can create your own repository in
GitHub, and link it to your local copy by running

```
git remote add personal <your repository url>
```

You can find your repository URL on the GitHub web interface after you created
it.

Once you have added your remote repository, which is now named `personal`, you
can store your changes following these steps:

1. Add the files you created or modified:
```shell
git add <filenames>
```
2. Save the changes locally:
```shell
git commit -m "<insert some description of your change here>"
```
3. Push the changes to your remote repository:
```shell
git push personal
```

Don't simply run `git push`, because that will try to update our original
repository, which will reject your changes.
