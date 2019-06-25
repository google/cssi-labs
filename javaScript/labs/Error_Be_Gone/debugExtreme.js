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

const addElement = (array, newElement) = > {
  array = array.push(newElement);
  return array;
};

const printElements = (array) => {
  for(let i = 0; i <= array.length; i ++){
    console.log(array(i));
  }
};

const createWord(arrayOfLetters){
  return arrayofletters.join(" ");
};

const conditionalAdd = (number1, number2) => {
  if(number2 < 5){
    let add = 1
  } else{
    const add = 2
  }
  return number1 + add;
};

// Test Functions
const arr = [1,2,3,4,5,];
//Expected Output: 6 should be added onto arr, arr with 6 in it should be printed
console.log(addElement(arr,6))

// Expected Output: all elements of arr should print
printElements(arr)

const letters = ["b", "u", "g", "s"];
// Expected Output: bugs
console.log(createWord(letters));

// Expected Output: 7
console.log(conditionalAdd(6));
