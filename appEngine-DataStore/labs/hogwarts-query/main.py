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

import webapp2
import os
import jinja2
from hogwarts_models import Student, Wand, House, Course, Enrollment, Teacher
from seed_hogwarts_db import seed_data

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to Hogwarts' Online Portal")

class HouseHandler(webapp2.RequestHandler):
    def get(self):
        hogwarts_houses = House.query().order(House.name).fetch()
        start_template = jinja_env.get_template("templates/houselist.html")
        self.response.write(start_template.render({'house_info' : hogwarts_houses}))

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/houses', HouseHandler),
    ('/seed-data', LoadDataHandler)
], debug=True)
