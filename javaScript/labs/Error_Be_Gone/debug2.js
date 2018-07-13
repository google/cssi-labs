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

function checkNumEven(number){
  if(number%2=0){
    return true;
  }
  else{
    return false;
  }
}

function checkStringEqualNum(numberString, numberInt){
  if(numberString === numberInt){
    return true;
  }
  return false;
}

function getFirstElement(array){
  return array(1);
}

// Test Functions

// Expected output: true
console.log(checkStringEqualNum("10",10));

// Expected output: false
console.log(checkNumEven(3));

let arr = ["first", "not first"];
// Expected output first
console.log(getFirstElement(arr));
