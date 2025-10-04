#!/usr/bin/env python3
"""
RPC Client
Makes requests to the RPC server with timeout handling
"""

import requests
import json
import sys
from requests.exceptions import Timeout, RequestException

class RPCClient:
    def __init__(self, base_url="http://localhost:8080", timeout=2):
        self.base_url = base_url
        self.timeout = timeout
    
    def _make_request(self, endpoint, x, y):
        """Make a request to the server with timeout handling"""
        url = f"{self.base_url}/{endpoint}"
        payload = {"x": x, "y": y}
        
        try:
            response = requests.post(
                url, 
                json=payload, 
                timeout=self.timeout,
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                return response.json()['result']
            else:
                print(f"Server error: {response.status_code} - {response.text}")
                return None
                
        except Timeout:
            print("Request timed out")
            return None
        except RequestException as e:
            print(f"Request failed: {e}")
            return None
    
    def add(self, x, y):
        """Call the add endpoint"""
        return self._make_request("add", x, y)
    
    def multiply(self, x, y):
        """Call the multiply endpoint"""
        return self._make_request("multiply", x, y)

def main():
    # Default to localhost, but allow override via command line
    server_url = "http://localhost:8080"
    if len(sys.argv) > 1:
        server_url = sys.argv[1]
    
    print(f"Connecting to RPC server at: {server_url}")
    client = RPCClient(server_url)
    
    # Test cases
    test_cases = [
        ("add", 2, 3),
        ("multiply", 4, 5),
        ("add", 10, -5),
        ("multiply", 7, 8),
        ("add", 0, 100)
    ]
    
    print("\n=== RPC Client Test Results ===")
    
    for operation, x, y in test_cases:
        if operation == "add":
            result = client.add(x, y)
            if result is not None:
                print(f"add({x},{y}) = {result}")
            else:
                print(f"add({x},{y}) = FAILED")
        
        elif operation == "multiply":
            result = client.multiply(x, y)
            if result is not None:
                print(f"multiply({x},{y}) = {result}")
            else:
                print(f"multiply({x},{y}) = FAILED")

if __name__ == '__main__':
    main()
