#!/usr/bin/env python3
"""
Test script for deployed Render.com service
Replace YOUR_RENDER_URL with your actual Render URL
"""

import requests
import sys

def test_deployed_service(base_url):
    """Test the deployed RPC service"""
    print(f"Testing deployed service at: {base_url}")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            print("✅ Health check passed")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return
    
    # Test add endpoint
    try:
        response = requests.post(
            f"{base_url}/add",
            json={"x": 2, "y": 3},
            timeout=10
        )
        if response.status_code == 200:
            result = response.json()['result']
            print(f"✅ add(2,3) = {result}")
        else:
            print(f"❌ Add test failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Add test error: {e}")
    
    # Test multiply endpoint
    try:
        response = requests.post(
            f"{base_url}/multiply",
            json={"x": 4, "y": 5},
            timeout=10
        )
        if response.status_code == 200:
            result = response.json()['result']
            print(f"✅ multiply(4,5) = {result}")
        else:
            print(f"❌ Multiply test failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Multiply test error: {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        # Remove trailing slash if present
        url = url.rstrip('/')
        test_deployed_service(url)
    else:
        print("Usage: python test_deployed.py https://rpc-implementation.onrender.com")
        print("Example: python test_deployed.py https://rpc-implementation.onrender.com")
