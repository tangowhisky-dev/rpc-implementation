#!/usr/bin/env python3
"""
Test timeout functionality
"""

import requests
from requests.exceptions import Timeout

def test_timeout():
    """Test the timeout functionality"""
    print("Testing timeout functionality...")
    
    try:
        # This should timeout after 2 seconds
        response = requests.post(
            "http://localhost:8081/slow",
            json={"x": 1, "y": 2},
            timeout=2
        )
        print("ERROR: Request should have timed out!")
    except Timeout:
        print("✓ Request timed out (as expected)")
    except Exception as e:
        print(f"Connection failed (server not running): {e}")

if __name__ == '__main__':
    test_timeout()
