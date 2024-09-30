from flask import Flask
from redis import Redis
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

def create_app():
    app = Flask(__name__)

    # Redis configuration
    redis_host = os.getenv('REDIS_HOST', 'localhost')
    redis_port = os.getenv('REDIS_PORT', 6379)
    app.redis_cache = Redis(host=redis_host, port=redis_port)

    # Rate limiting setup
    app.limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["5 per minute"]
    )

    # Import routes from app.py
    with app.app_context():
        from . import app as routes  # Import your app.py routes
        return app
