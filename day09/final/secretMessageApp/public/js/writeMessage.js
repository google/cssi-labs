const submitMessage = () => {
    const passcodeInput = document.querySelector('#passcode').value;
    const messageInput = document.querySelector('#message').value;
    
    firebase.database().ref().push({
        passcode: passcodeInput,
        message: messageInput
    });
};