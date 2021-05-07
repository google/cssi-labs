let search = document.getElementById('search');
search.addEventListener("keyup", function(event) {
  // On Enter keystroke
  if (event.keyCode === 13) {
    // // Cancel the default action, if needed
    // event.preventDefault();
    if (!firebase.apps.length) {
        firebase.initializeApp(firebaseConfig);
    }
    else {
        firebase.app(); // if already initialized, use that one
    }
    
    // Capture the search string, convert to lowercase
    const searchStr = search.value.toLowerCase();

    const bookList = firebase.database().ref('books');
    bookList.on('value', (snapshot) => {
        const books = snapshot.val();
        const bookArray = Object.entries(books);
        const findBookByTitle = bookArray.find(arr => {
            const bookTitle = arr[1].title;
            const bookTitleLowercase = bookTitle.toLowerCase();
            console.log(searchStr, bookTitle)
            return searchStr === bookTitleLowercase;
        })
        const imgEle = document.getElementById('coverImg');
        const message = document.getElementById('bookContent');
console.log(findBookByTitle)        
        if(!findBookByTitle) {
            imgEle.setAttribute('src', 'https://media.giphy.com/media/14uQ3cOFteDaU/giphy.gif');
            message.innerHTML = `<strong>Sorry we weren't able to find that title! Try searching for another one.</strong>`;
            message.classList.add('has-text-centered')
        }
        else {
            const bookInfo = findBookByTitle[1];
            imgEle.setAttribute('src', bookInfo.cover_img);
            const formattedHTML = formatHTML(bookInfo);
            message.innerHTML = formattedHTML;
        }
      });
  }
});

const formatHTML = (info) => {
    let innerHTML = '';
    innerHTML += `<strong>Author:</strong> ${info.author}`;
    innerHTML += `<br>`;
    innerHTML += `<strong>Title:</strong> ${info.title}`;
    innerHTML += `<br>`;
    innerHTML += `<strong><a href="https://www.google.com/search?q=${info.title}&tbm=shop">Purchase This Book</a></strong>`
    return innerHTML;
}