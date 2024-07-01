from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app import db, socketio
from app.game import bp
from app.game.forms import CreateRoomForm, JoinRoomForm
from app.models import User, Room, room_users
from textblob import Word

def is_english_word(word):
    return Word(word).spellcheck()[0][1] == 1.0



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

import datetime  # Upewnij się, że moduł datetime jest poprawnie zaimportowany
import random
import string

@bp.route('/play_game/<int:room_id>')
@login_required
def play_game(room_id):
    room = Room.query.get_or_404(room_id)
    if current_user not in room.users:
        return redirect(url_for('game.room', room_id=room_id))
    
    random_number = random.randint(3, 8)
    first_random_letter = random.choice(string.ascii_lowercase)
    second_random_letter = random.choice(string.ascii_lowercase)

    start_time = request.args.get('start_time', datetime.datetime.now().isoformat())
    return render_template('game2.html', room=room, start_time=start_time, random_number = random_number,
                           first_random_letter = first_random_letter, second_random_letter=second_random_letter)


@bp.route('/end_game/<int:room_id>')
@login_required
def end_game(room_id):
    room = Room.query.get_or_404(room_id)
    return redirect(url_for('game.room', room_id=room_id))

@bp.route('/home')
def home():
    return render_template('home.html')

@bp.route('/instruction')
def instruction():
    return render_template('instruction.html')

@bp.route('/about')
def about():
    return render_template('about.html')


from flask_socketio import join_room

@socketio.on('join')
def handle_join(data):
    room_id = data['room']
    join_room(room_id)
    room = Room.query.get(room_id)
    socketio.emit('user_update', {'users': [{'username': user.username, 'points': user.points} for user in room.users]}, to=room_id)

from flask_socketio import leave_room

@socketio.on('leave')
def handle_leave(data):
    room_id = data['room']
    leave_room(room_id)
    room = Room.query.get(room_id)
    if room:
        room.users.remove(current_user)
    current_user.points = 0
    db.session.commit()
    if(room):
        socketio.emit('user_update', {'users': [{'username': user.username, 'points': user.points} for user in room.users]}, to=room_id)
        if current_user == room.owner:
            socketio.emit('redirect_to_home', {'url': url_for('game.home')}, to=room_id)
            db.session.delete(room)
            db.session.commit()
        

@socketio.on('start_game')
def handle_start_game(data):
    room_id = data['room']
    print(f"Start game for room {room_id}")
    socketio.emit('redirect_to_game', {'url': url_for('game.play_game', room_id=room_id)}, to=room_id)

@socketio.on('submit_points')
def handle_submit_points(data):
    time_percentage = float(data['timePercentage'])
    answer = data['answer']
    letter_number = int(data['random_number'])
    first_required_letter = data['first_random_letter']
    second_required_letter = data['second_random_letter']
    print(is_english_word(answer))
    if is_english_word(answer) and len(answer) == letter_number and first_required_letter in answer and second_required_letter in answer:
        current_user.points += int(time_percentage*100)
    db.session.commit()