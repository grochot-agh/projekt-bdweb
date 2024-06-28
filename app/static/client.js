var socket = io();
var roomId = roomId || '';
socket.on('connect', function() {
    socket.emit('join', {room: roomId});
    console.log(roomId);
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

document.getElementById('start-game').addEventListener('click', function() {
    const startGameButton = document.getElementById('start-game');
    const roomId = startGameButton.dataset.roomId;
    socket.emit('start_game', {room: roomId});
});

socket.on('redirect_to_game', function(data) {
    console.log('hi');
    window.location.href = data.url;
});