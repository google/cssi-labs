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

from google.appengine.ext import ndb

class Student(ndb.Model):
    student_id =  ndb.IntegerProperty(required=True)
    first_name =  ndb.StringProperty(required=True)
    last_name =  ndb.StringProperty(required=True)

#One to One
class Wand(ndb.Model):
    length = ndb.FloatProperty(required=True)
    material = ndb.StringProperty(required=True)
    core = ndb.StringProperty(required=True)
    owner = ndb.KeyProperty(Student)

#One to Many
class House(ndb.Model):
      name = ndb.StringProperty(required=True)
      mascot = ndb.StringProperty(required=False)
      students = ndb.KeyProperty(Student, repeated=True)
      
# Many to Many
class Course(ndb.Model):
      name = ndb.StringProperty()
      location = ndb.StringProperty()

class Enrollment(ndb.Model):
      student = ndb.KeyProperty(Student)
      course = ndb.KeyProperty(Course)

#One to Many 
#Generally, teachers teach more than one class
#While this hasn't happened yet at Hogwarts, it's feasible, so we'll make repeated = True

class Teacher(ndb.Model):
    name = ndb.StringProperty(required=True)
    years_experience = ndb.IntegerProperty(default=1)
    classes_taught = ndb.KeyProperty(Course, repeated=True)
    









