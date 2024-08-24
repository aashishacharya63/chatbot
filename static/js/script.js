document.getElementById('send-btn').addEventListener('click', function() {
    var userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== "") {
        displayMessage(userInput, 'user');
        fetch('/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                data.data.forEach(movie => {
                    displayMessage(`Title: ${movie.title}\nGenre: ${movie.genre}\nOverview: ${movie.overview}\nRating: ${movie.vote_average}`, 'bot');
                });
            } else {
                displayMessage(data.message, 'bot');
            }
        });
        document.getElementById('user-input').value = "";
    }
});

function displayMessage(message, sender) {
    var chatBox = document.getElementById('chat-box');
    var messageElement = document.createElement('div');
    messageElement.className = sender;
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
