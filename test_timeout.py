#!/usr/bin/env python3
"""
Test script to verify timeout functionality
"""

import time
from flask import Flask

app = Flask(__name__)

@app.route('/slow', methods=['POST'])
def slow_endpoint():
    """Endpoint that takes longer than 2 seconds to respond"""
    time.sleep(3)  # Sleep for 3 seconds
    return {'result': 'slow response'}

if __name__ == '__main__':
    print("Starting slow test server on port 8081...")
    app.run(host='0.0.0.0', port=8081, debug=False)
