var socket = io();
var roomId = roomId || '';

socket.on('connect', function() {
    socket.emit('join', {room: roomId});
    console.log('joined: ' + roomId)
});

socket.on('user_update', function(data) {
    console.log(data);
    const usersTable = document.getElementById('users-table');
    usersTable.innerHTML = '';
    data.users.forEach(user => {
        const row = `<tr><td>${user.username}</td><td>${user.points}</td></tr>`;
        usersTable.innerHTML += row;
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var startGameButton = document.getElementById('start-game');
    if (startGameButton) {
        startGameButton.addEventListener('click', function() {
            console.log(roomId);
            socket.emit('start_game', {room: roomId});
        });
    }
});

socket.on('redirect_to_game', function(data) {
    localStorage.setItem('timeLeft', 30);
    localStorage.setItem('formSubmitted', 'false');
    window.location.href = data.url;
    
});

