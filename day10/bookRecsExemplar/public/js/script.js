const handleSubmitSurvey = () => {
    if (!firebase.apps.length) {
        firebase.initializeApp(firebaseConfig);
    }
    else {
        firebase.app(); // if already initialized, use that one
    }

    const genre = getGenre();
    const series = getSeriesPref();
    const emotion = getEmotion();
    let shuffledBooks;
    // Get books from DB
    const getBookRec = firebase.database().ref('books').orderByChild('series');
    getBookRec.on('value', (snapshot) => {
        const allBooks = snapshot.val();
        console.log(allBooks)

        const allBooksArray = Object.entries(allBooks);
        // Filter books based on survey results
        const allRecommendations = allBooksArray.filter(book => {
            // book[0] is the title of the book, book[1] is all of the data associated with it
            const bookData = book[1];
            const bookGenre = bookData.genre;
            const bookEmotion = bookData.emotions;

            // Firebase RTBD does not support booleans, converts all text to strings
            // console.log(bookData.series)
            const seriesBoolToStr = bookData.series.toString();
            return seriesBoolToStr === series && bookGenre.includes(genre) && bookEmotion.includes(emotion);
        });
        shuffledBooks = shuffleBookRecs(allRecommendations);
        const bookRecommendation = shuffledBooks[0][1];
        document.getElementById('coverImg').setAttribute('src', bookRecommendation.cover_img);
        return shuffledBooks;  
    })
}

const getGenre = () => {
    const genre = document.getElementById('genre').value;
    return genre;
}

const getSeriesPref = () => {
    const seriesSelection = document.getElementsByName('series');
    let series;

    for (let i = 0; i < seriesSelection.length; i++) {
        if (seriesSelection[i].checked) {
            series = seriesSelection[i].value;
            // only one radio can be logically checked, don't check the rest
            break;
        }
    }
    return series;
}

const getEmotion = () => {
    const emotion = document.getElementById('emotion').value;
    return emotion;   
}

const shuffleBookRecs = (books) => {
    let shuffledBooks = [];
    for(let i = books.length; i > 0; i--) {
        const randomNum = Math.random() 
        const randomFloat = randomNum * books.length         
        const randomIdx = Math.floor(randomFloat)
        shuffledBooks.push(books[randomIdx])
        books.splice(randomIdx, 1)
    }
    console.log(shuffledBooks)
    return shuffledBooks;
}

const handleAddBook = () => {
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const cover = document.getElementById('cover').value;
    const emotions = document.getElementById('emotions').value;
    const genres = document.getElementById('genres').value
    const series = getSeriesPref();

    const emotionsArray = emotions.split(',');
    const genresArray = genres.split(',')

    firebase.database().ref('books').push({
        author: author,
        title: title, 
        cover_img: cover,
        emotions: emotionsArray,
        genre: genresArray,
        series: series
    });
}