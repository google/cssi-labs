console.log("script running");

// Fix these querySelectors so that they each select the correct element.
const englishTile = document.querySelector("#English");
const spanishTile = document.querySelector("#Spanish");
const chineseTile = document.querySelector("#Chinese");
const tagalogTile = document.querySelector("#Tagalog");
const vietnameseTile = document.querySelector("#Vietnamese");
const arabicTile = document.querySelector("#Arabic");
const frenchTile = document.querySelector("#French");
const koreanTile = document.querySelector("#Korean");
const russianTile = document.querySelector("#Russian");

console.log(englishTile);
console.log(spanishTile);
console.log(chineseTile);
console.log(tagalogTile);
console.log(vietnameseTile);
console.log(arabicTile);
console.log(frenchTile);
console.log(koreanTile);
console.log(russianTile);

// Add the id of the input field so we can access it!
const inputField = document.querySelector("#guess");

inputField.addEventListener("change", (e) => {
  console.log("Guess submitted!");
  let guess = inputField.value;
  console.log(guess);
  if (guess === "English" || guess === "english") {
    englishTile.classList.remove("hidden");
  } else if (guess === "Spanish" || guess === "spanish") {
    spanishTile.classList.remove("hidden");
  } else if (guess === "Chinese" || guess === "chinese") {
    chineseTile.classList.remove("hidden");
  } else if (guess === "Tagalog" || guess === "tagalog") {
    tagalogTile.classList.remove("hidden");
  } else if (guess === "Vietnamese" || guess === "vietnamese") {
    vietnameseTile.classList.remove("hidden");
  } else if (guess === "Arabic" || guess === "arabic") {
    arabicTile.classList.remove("hidden");
  } else if (guess === "French" || guess === "french") {
    frenchTile.classList.remove("hidden");
  } else if (guess === "Korean" || guess === "korean") {
    koreanTile.classList.remove("hidden");
  } else if (guess === "Russian" || guess === "russian") {
    russianTile.classList.remove("hidden");
  }
  inputField.value = "";
});
