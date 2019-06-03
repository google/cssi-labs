#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import random


def get_fortune():
    # Add a list of fortunes to the empty fortune_list array
    fortune_list=['fortune1', 'fortune2']
    # Use the random library to return a random element from the array
    # instead of "None"
    random_fortune = None
    return random_fortune


# Remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = "insert jinja2 environment variable here"

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        self.response.write('a response from the FortuneHandler')
    # Add a post method
    # def post(self):

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler) #maps '/predict' to the FortuneHandler
], debug=True)
