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

from hogwarts_models import Student, Wand, House, Course, Enrollment, Teacher

def seed_data():
    ron_key = Student(student_id=423491377, first_name ="Ron", last_name = "Weasley").put()
    harry_key = Student (student_id=423491782, first_name ="Harry", last_name = "Potter").put()
    hermione_key = Student(student_id=423491249, first_name="Hermione", last_name="Granger").put()
    malfoy_key = Student(student_id=42391043, first_name="Draco", last_name="Malfoy").put()
    crabbe_key = Student(student_id=42391122, first_name="Vincent", last_name="Crabbe").put()
    goyle_key = Student(student_id=42391063, first_name="Gregory", last_name="Goyle").put()


    ron_wand=Wand(length = 14.0, material = "willow", core="unicorn", owner=ron_key)
    harry_wand=Wand(length = 11.0, material = "holly", core="phoenix feather", owner=harry_key)
    hermione_wand = Wand(length=10.75, material="vinewood", core="dragon heartstring", owner=hermione_key)

    ron_wand.put()
    harry_wand.put()
    hermione_wand.put()

    gryff = House(name="Gryffindor", mascot="Lion", students=[ron_key, harry_key, hermione_key])
    snakes = House(name="Slytherin", mascot="Snake", students=[malfoy_key, crabbe_key, goyle_key])
    hufflepuff = House(name="Hufflepuff", mascot="Badger", students=[])
    ravenclaw = House(name="Ravenclaw",  mascot="Eagle", students=[])

    gryff.put()
    snakes.put()
    hufflepuff.put()
    ravenclaw.put()

    potions = Course(name="Potions", location="dungeon")
    dada = Course(name="Defense Against the Dark Arts", location="3C")
    transfiguration = Course(name="Transfiguration", location="Class 34")
    potions_key = potions.put()
    dada_key = dada.put()
    transfiguration_key = transfiguration.put()

    #dada
    Enrollment(student=ron_key, course=dada_key).put()
    Enrollment(student=harry_key, course=dada_key).put()
    Enrollment(student=hermione_key, course=dada_key).put()

    #potions
    Enrollment(student=hermione_key, course=potions_key).put()
    Enrollment(student=ron_key, course=potions_key).put()
    Enrollment(student=malfoy_key, course=potions_key).put()
    Enrollment(student=crabbe_key, course=potions_key).put()
    Enrollment(student=goyle_key, course=potions_key).put()

    #tranfirguration
    Enrollment(student=harry_key, course=transfiguration_key).put()
    Enrollment(student=hermione_key, course=transfiguration_key).put()
    Enrollment(student=crabbe_key, course=transfiguration_key).put()
    Enrollment(student=goyle_key, course=transfiguration_key).put()

    snape = Teacher(name="Severus Snape", years_experience=5, classes_taught=[potions_key])
    snape.put()
    moody = Teacher(name="Alastor Moody", years_experience=1, classes_taught=[dada_key])
    moody.put()
    mcgonagall = Teacher(name="Minerva McGonagall", years_experience=12, classes_taught=[transfiguration_key])
    mcgonagall.put()
