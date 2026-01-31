import os
import time
import redis
import random
import datetime

# Configuration
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
SCAN_NETWORK = os.getenv('SCAN_NETWORK', '192.168.1.0/24')

def main():
    print(f"Starting scanner for network: {SCAN_NETWORK}")
    print(f"Connecting to Redis at: {REDIS_HOST}")
    
    try:
        r = redis.Redis(host=REDIS_HOST, port=6379, db=0)
        
        # Simulate scanning
        devices_found = random.randint(1, 10)
        print(f"Scan complete. Found {devices_found} devices.")
        
        # Store results
        scan_data = {
            'timestamp': datetime.datetime.now().isoformat(),
            'network': SCAN_NETWORK,
            'devices_count': devices_found,
            'status': 'success'
        }
        
        r.set('last_scan', str(scan_data))
        print("Results stored in Redis.")
        
    except Exception as e:
        print(f"Error during scan: {e}")

if __name__ == "__main__":
    main()
