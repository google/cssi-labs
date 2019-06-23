// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

const generateGif = document.querySelector('button');
const output = document.querySelector('#output');

const fetchGif = () => {
  // TODO: replace the next line with your API key
  const apiKey = 'GgFZf48OO1lfS1C4hm9gMI0jt2sMIaFS';
  fetch(`http://api.giphy.com/v1/gifs/search?api_key=${apiKey}&q=hello&limit=1`)
    .then((data) => {
      return data.json();
    })
    .then((json) => {
      // display the json in the console for inspection
      console.log(json);
      // TODO: call the processJsonResponse function, passing along the data

    });
};

// TODO: complete the function below
const processJsonResponse = (jsonData) => {
  // TODO: parse the data and grab the "downsized url" from the images object

  // TODO: create an HTML string representing an img tag linking to the url above

  // TODO: append the HTML string to the end of the #output div tag.

};

/*
Challenges:
- modify the API call to instead search for a random gif
- modify the API call to select 10 gifs at a time, then have the
  processJsonResponse function choose one at random
- add an <input> tag and allow the user to choose the query for searching.
*/
generateGif.addEventListener('click', fetchGif);
