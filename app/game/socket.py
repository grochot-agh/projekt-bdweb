from app import socketio, db
from flask_socketio import join_room, leave_room, send, emit
from flask_login import current_user
from app.models import Room

@socketio.on('join')
def handle_join(data):
    room_id = data['room']
    room = Room.query.get(room_id)
    join_room(room_id)
    send(f'{current_user.username} has entered the room.', room=room_id)
    emit('user_update', {'users': [{'username': user.username, 'points': user.points} for user in room.users]}, room=room_id)

@socketio.on('leave')
def handle_leave(data):
    room_id = data['room']
    leave_room(room_id)
    send(f'{current_user.username} has left the room.', room=room_id)
    room = Room.query.get(room_id)
    emit('user_update', {'users': [{'username': user.username, 'points': user.points} for user in room.users]}, room=room_id)
