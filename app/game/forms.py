from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Room

class CreateRoomForm(FlaskForm):
    name = StringField('Room Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Create Room')

    def validate_name(self, name):
        room = Room.query.filter_by(name=name.data).first()
        if room is not None:
            raise ValidationError('Please use a different room name.')

class JoinRoomForm(FlaskForm):
    name = StringField('Room Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Join Room')
