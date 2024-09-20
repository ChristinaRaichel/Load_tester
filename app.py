from flask import Flask, request, jsonify, render_template
import random
import time
import redis

app = Flask(__name__)

load_data = []

cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate_load', methods=['POST'])
def simulate_load():
    load_value = request.json.get('load', 1)
    time.sleep(load_value)  # Simulate load
    load_data.append(load_value)
    return jsonify({"status": "success", "load": load_value})

@app.route('/load_status_with_cache')
def load_status():
    cached_data = cache.get('load_data')
    if cached_data:
        return jsonify(cached_data)
    else:
        return jsonify(load_data)

@app.route('/load_status')
def load_status():
    cached_data = cache.get('load_data')
    if cached_data:
        return jsonify(cached_data)
    else:
        return jsonify(load_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)