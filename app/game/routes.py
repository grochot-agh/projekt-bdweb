from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from flask_socketio import SocketIO, leave_room, send, emit
from app import db, socketio
from app.game import bp
from app.game.forms import CreateRoomForm, JoinRoomForm
from app.models import User, Room

@bp.route('/create_room', methods=['GET', 'POST'])
@login_required
def create_room():
    form = CreateRoomForm()
    if form.validate_on_submit():
        room = Room(name=form.name.data, owner=current_user)
        room.set_password(form.password.data)
        room.users.append(current_user)
        db.session.add(room)
        db.session.commit()
        flash('Room created successfully!')
        return redirect(url_for('game.room', room_id=room.id))
    return render_template('create_room.html', form=form)


@bp.route('/join_room', methods=['GET', 'POST'])
@login_required
def join_room():
    form = JoinRoomForm()
    if form.validate_on_submit():
        room = Room.query.filter_by(name=form.name.data).first()
        if room and room.check_password(form.password.data):
            if len(room.users) < 10:
                room.users.append(current_user)
                db.session.commit()
                flash('Joined room successfully!')
                return redirect(url_for('game.room', room_id=room.id))
            else:
                flash('Room is full!')
        else:
            flash('Invalid room name or password!')
    return render_template('join_room.html', form=form)

@bp.route('/room/<int:room_id>')
@login_required
def room(room_id):
    room = Room.query.get_or_404(room_id)
    return render_template('room.html', room=room)

@socketio.on('start_game')
def handle_start_game(data):
    room_id = data['room']
    print(data)
    # Tutaj można dodać logikę biznesową dotyczącą rozpoczęcia gry
    print(f"Received 'start_game' event for room ID: {room_id}")
    print("ok")
    # Emitowanie zdarzenia 'redirect_to_game'
    emit('redirect_to_game', {'url': url_for('game.play_game', room_id=room_id)})

@bp.route('/play_game/<int:room_id>')
@login_required
def play_game(room_id):
    room = Room.query.get_or_404(room_id)
    if current_user not in room.users:
        return redirect(url_for('game.room', room_id=room_id))
    return render_template('game.html', room=room)

@bp.route('/end_game/<int:room_id>')
@login_required
def end_game(room_id):
    room = Room.query.get_or_404(room_id)
    if current_user not in room.users:
        return redirect(url_for('game.room', room_id=room_id))

    # Example logic to update points
    for user in room.users:
        user.points += 10  # Example increment
    db.session.commit()

    return redirect(url_for('game.room', room_id=room_id))

@bp.route('/home')
def home():
    return render_template('home.html')


from flask_socketio import join_room

@socketio.on('join')
def handle_join(data):
    room_id = data['room']
    print(room_id)
    room = Room.query.get(room_id)
    join_room(room_id)
    send(f'{current_user.username} has entered the room.', room=room_id)
    emit('user_update', {'users': [{'username': user.username, 'points': user.points} for user in room.users]}, room=room_id)
    print('end')

@socketio.on('leave')
def handle_leave(data):
    room_id = data['room']
    leave_room(room_id)
    send(f'{current_user.username} has left the room.', room=room_id)
    room = Room.query.get(room_id)
    emit('user_update', {'users': [{'username': user.username, 'points': user.points} for user in room.users]}, room=room_id)

