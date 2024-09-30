from flask import current_app as app, render_template, jsonify, request
import random
import time

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
    cached = app.redis_cache.get(data)
    if cached:
        return {"message": f"Cached Response: {cached.decode()}"}
    else:
        app.redis_cache.setex(data, 10, f"Processed {data}")
        return {"message": f"Processed {data}"}

# Home route to render the index HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle incoming requests and demonstrate caching/load balancing
@app.route('/request')
@app.limiter.limit("10 per minute")
def handle_request():
    data = request.args.get('data', 'default')
    use_cache = request.args.get('cache') == 'true'
    
    # Check if caching is enabled and process accordingly
    if use_cache:
        response = get_cached_response(data)
    else:
        server = serve_request()
        response = {"message": f"Processed {data} by {server}"}

    return jsonify(response)

# Route to get current server loads (for visualization)
@app.route('/load')
def get_load():
    return jsonify(load)
