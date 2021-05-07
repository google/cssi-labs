const getMessages = () => {
    const messagesRef = firebase.database().ref();
    messagesRef.on('value', (snapshot) => {
    const data = snapshot.val();
    findMessage(data);
    });
};

const findMessage = (messages) => {
    const passcodeAttempt = document.querySelector('#passcode').value;
    for(message in messages) {
        const messageData = messages[message];
        if(messageData.passcode === passcodeAttempt) {
            renderMessageAsHtml(messageData.message);
        };
    };
};

const renderMessageAsHtml = (message) => {
    // Hide Input Form
    const passcodeInput = document.querySelector('#passcodeInput');
    passcodeInput.style.display = 'none';
    // Render messageas HTML
    const messageDiv = document.querySelector('#message');
    messageDiv.innerHTML = message;
};
