from flask import Flask, render_template, jsonify, request
import random
import time
from redis import Redis
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Redis setup for caching
redis_cache = Redis(host='redis', port=6379)

# Rate limiting setup
limiter = Limiter(app, key_func=get_remote_address, default_limits=["5 per minute"])

# Simulate multiple servers (NGINX load balancing)
SERVERS = [f"Server-{i}" for i in range(1, 4)]
load = {server: 0 for server in SERVERS}  # Server loads

# Simulate server response
def serve_request():
    server = random.choice(SERVERS)
    load[server] += 1
    time.sleep(random.uniform(0.5, 1.5))  # Simulate processing time
    load[server] -= 1
    return server

# Cache using Redis (expiration time 10 seconds)
def get_cached_response(data):
    cached = redis_cache.get(data)
    if cached:
        return {"message": f"Cached Response: {cached.decode()}"}
    else:
        redis_cache.setex(data, 10, f"Processed {data}")
        return {"message": f"Processed {data}"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request')
@limiter.limit("10 per minute")
def handle_request():
    data = request.args.get('data', 'default')
    use_cache = request.args.get('cache') == 'true'
    
    if use_cache:
        response = get_cached_response(data)
    else:
        server = serve_request()
        response = {"message": f"Processed {data} by {server}"}

    return jsonify(response)

@app.route('/load')
def get_load():
    return jsonify(load)

if __name__ == '__main__':
    app.run(debug=True)
