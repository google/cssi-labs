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

const uglyCode =(arr, num)=>{
if(arr.length == 0) return "array length is zero"
else{

if(arr.length > 5) for(var i = 0; i < arr.length; i++) arr[i]=num
}

return arr

}

let array=[0,0,0,0,0,0]
console.log(
  uglyCode(array,5))
