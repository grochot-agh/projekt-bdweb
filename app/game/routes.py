from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app import db, socketio
from app.game import bp
from app.game.forms import CreateRoomForm, JoinRoomForm
from app.models import User, Room

@bp.route('/create_room', methods=['GET', 'POST'])
@login_required
def create_room():
    form = CreateRoomForm()
    if form.validate_on_submit():
        room = Room(name=form.name.data)
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
