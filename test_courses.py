#!/usr/bin/env python3
"""
Test Course Information
"""

import requests
import json

def test_courses():
    """Test course information"""
    try:
        response = requests.post('http://localhost:8000/ask', json={'question': 'What courses are available for 100 level CS students?'})
        if response.status_code == 200:
            data = response.json()
            print("✅ SUCCESS!")
            print(f"Strategy: {data['model_used']}")
            print(f"Confidence: {data['confidence']:.2%}")
            print("\n📚 COURSE INFORMATION:")
            print(data['answer'])
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_courses()
