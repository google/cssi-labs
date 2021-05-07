console.log("script running!");

const button1 = document.querySelector("#button1");
const button2 = document.querySelector("#button2");
const button3 = document.querySelector("#button3");
const button4 = document.querySelector("#button4");

console.log(button1);
console.log(button2);
console.log(button3);
console.log(button4);

button1.addEventListener("click", e => {
  console.log("button 1 pressed!");
  alert("Meh-eh-eh-eh-eh!");
});

const status2 = document.querySelector("#status2");
console.log(status2);

button2.addEventListener("click", e => {
  console.log("button 2 pressed!");
  status2.innerHTML = "Thanks for petting Brodie! He looks really happy!";
});

const status3 = document.querySelector("#status3");
console.log(status3);

let carrots = 2;

button3.addEventListener("click", e => {
  console.log("button 3 pressed!");
  carrots = carrots + 1;
  status3.innerHTML = "Coco has had " + carrots + " carrots today!";
});

const zoo = document.querySelector(".container");
console.log(zoo);

button4.addEventListener("click", e => {
  console.log("button 4 pressed!");
  zoo.innerHTML = `<h1 class="title">Due to some dangerous rulebreaking, the petting zoo is temporarily closed</h1>`
});
