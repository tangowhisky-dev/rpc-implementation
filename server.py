#!/usr/bin/env python3
"""
Simple RPC Server
Provides add and multiply endpoints via HTTP JSON API
"""

from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/add', methods=['POST'])
def add():
    """Add two numbers"""
    try:
        data = request.get_json()
        if not data or 'x' not in data or 'y' not in data:
            return jsonify({'error': 'Missing x or y parameters'}), 400
        
        x = data['x']
        y = data['y']
        result = x + y
        
        logger.info(f"Adding {x} + {y} = {result}")
        return jsonify({'result': result})
    
    except Exception as e:
        logger.error(f"Error in add endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/multiply', methods=['POST'])
def multiply():
    """Multiply two numbers"""
    try:
        data = request.get_json()
        if not data or 'x' not in data or 'y' not in data:
            return jsonify({'error': 'Missing x or y parameters'}), 400
        
        x = data['x']
        y = data['y']
        result = x * y
        
        logger.info(f"Multiplying {x} * {y} = {result}")
        return jsonify({'result': result})
    
    except Exception as e:
        logger.error(f"Error in multiply endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    logger.info("Starting RPC Server on port 8080...")
    app.run(host='0.0.0.0', port=8080, debug=False)
