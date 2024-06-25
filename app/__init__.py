from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from config import Config

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")  # Dodaj obsługę CORS, jeśli potrzebujesz

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.game import bp as game_bp
    app.register_blueprint(game_bp, url_prefix='/game')

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    socketio.run(app, debug=True)
