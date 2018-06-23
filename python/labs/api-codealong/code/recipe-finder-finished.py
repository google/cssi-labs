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

ingredients = []

enter_more = input("Do you have any specific ingredients to enter? [y|n]:").lower()

while enter_more == "y":
    ingredients.append(input("What is the ingredient? One word only please:").lower())
    enter_more = input("Do you have any more ingredients to enter? [y|n]:").lower()

recipe_type = input("What kind of recipe do you want to find?")

# Write your code below!

ingredient_string = ",".join(ingredients)

import requests

url = "http://www.recipepuppy.com/api/?i=%s&q=%s" % (ingredient_string, recipe_type)
res = requests.get(url)
print(type(res.status_code))

recipes = res.json()["results"]

print("Your results:")
for i in range(len(recipes)):
    recipe = recipes[i]
    print("%s: %s" % (i, recipe["title"]))

choice = int(input("Choose a recipe (number): "))

print("Great choice!  You can find that recipe here:")
print(recipes[choice]["href"])