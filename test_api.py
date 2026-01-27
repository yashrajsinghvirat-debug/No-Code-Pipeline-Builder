#!/usr/bin/env python3
"""
Test script to verify backend API is working correctly
"""

import requests
import json

# Test data
test_payload = {
    "nodes": [
        {
            "id": "customInput-1",
            "type": "customInput",
            "position": {"x": 100, "y": 100},
            "data": {"inputName": "test_input", "inputType": "Text"}
        },
        {
            "id": "customOutput-1", 
            "type": "customOutput",
            "position": {"x": 300, "y": 100},
            "data": {"outputName": "test_output", "outputType": "Text"}
        }
    ],
    "edges": [
        {
            "id": "edge-1",
            "source": "customInput-1",
            "target": "customOutput-1",
            "sourceHandle": "customInput-1-value",
            "targetHandle": "customOutput-1-value"
        }
    ]
}

def test_api():
    """Test the API endpoint"""
    url = "http://127.0.0.1:8000/pipelines/parse"
    
    try:
        print(f"Testing POST to {url}")
        print(f"Payload: {json.dumps(test_payload, indent=2)}")
        
        response = requests.post(
            url,
            json=test_payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            print(f"Response Body: {json.dumps(response.json(), indent=2)}")
            print("✅ API test successful!")
        else:
            print(f"❌ API test failed with status {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed - make sure backend is running at http://127.0.0.1:8000")
    except requests.exceptions.Timeout:
        print("❌ Request timed out")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_api()
