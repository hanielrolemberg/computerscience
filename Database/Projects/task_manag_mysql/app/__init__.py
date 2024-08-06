from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import redis
from flask_session import Session

db = SQLAlchemy()
migrate = Migrate()
server_session = Session()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://teste:teste@localhost/task_manager'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True
    app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379')

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)
    server_session.init_app(app)

    # Registrar Blueprints ou Rotas
    from .routes import main
    app.register_blueprint(main)

    return app
