## Sequence
1. [Setup](#setup)
2. [Query Challenge](query-challenge)
3. [Query Data to Views](query-data-to-views)

### Setup
Clear the current datastore and run it with the admin interactive console
enabled:

  `dev_appserver.py  app.yaml --clear_datastore=yes --enable_console=True`

Add the Hogwarts data to your app's datastore by using your browser to go to
`http://localhost:8080/seed-data`.


### Query Challenge
Open up the interactive console.

Delete any existing code and add the following:
```
#in interactive console
from google.appengine.ext import ndb
import hogwarts_models

print hogwarts_models.Student.query().fetch()
```
Use print statements to find:
- the mascot of Ravenclaw
- the number of `Courses` in Datastore
- the teacher with the most least amount of teaching experience
- the student enrolled in the most classes
- the material of Harry's Wand

### Query Data to Views
Using the `HouseHandler` and `houselist.html` template as a model, add a new
view that shows all of the wands of students at Hogwarts, their details, and the
names of their owners.

If you finish early, continue to build out the Hogwarts app. For a stretch
challenge, you can modify some of the models to include images as well.
