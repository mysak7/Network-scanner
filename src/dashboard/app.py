import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

# Connect to Redis
try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
except Exception as e:
    print(f"Failed to connect to Redis: {e}")
    r = None

@app.route('/')
def index():
    return "Network Scanner Dashboard"

@app.route('/api/stats')
def stats():
    if not r:
        return jsonify({"error": "Redis not connected", "status": "unhealthy"}), 500
    
    try:
        # Check connection
        r.ping()
        
        last_scan = r.get('last_scan')
        if last_scan:
            data = eval(last_scan) # Simple for demo, use json.loads in production
        else:
            data = {"message": "No scan data available"}
            
        return jsonify({
            "status": "healthy",
            "redis_connection": "ok",
            "last_scan": data
        })
    except Exception as e:
        return jsonify({"error": str(e), "status": "unhealthy"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
