from flask import Flask
from redis import Redis

def create_app():
    app = Flask(__name__)

    # Configuração do Redis
    app.redis = Redis(host='localhost', port=6379, db=0)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
