#!/usr/bin/env python3
"""
Debug Response Generation
"""

import requests
import json

def debug_response_generation():
    """Debug the response generation process"""
    base_url = "http://localhost:8000"
    
    print("🔍 Debugging Response Generation")
    print("=" * 60)
    
    # Test the specific question that's failing
    question = "What can I do after graduation?"
    
    print(f"📝 Testing Question: '{question}'")
    
    try:
        # Make the request
        response = requests.post(f"{base_url}/ask", json={"question": question})
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status: {response.status_code}")
            print(f"✅ Strategy: {data.get('model_used', 'unknown')}")
            print(f"✅ Confidence: {data.get('confidence', 0):.2%}")
            print(f"✅ Full Response: {json.dumps(data, indent=2)}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"❌ Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print("\n" + "=" * 60)
    print("🔍 Testing Different Career Questions")
    
    career_questions = [
        "What can I do after graduation?",
        "What jobs are available for CS students?",
        "I want to work in tech",
        "What career opportunities are there?",
        "What jobs can I get with a CS degree?"
    ]
    
    for i, q in enumerate(career_questions, 1):
        print(f"\n📝 Career Question {i}: '{q}'")
        
        try:
            response = requests.post(f"{base_url}/ask", json={"question": q})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data.get('model_used', 'unknown')
                confidence = data.get('confidence', 0)
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                
                if "Career Opportunities" in data.get('answer', ''):
                    print("   ✅ Got career response!")
                else:
                    print("   ⚠️  Got generic response")
                    print(f"   📝 Response preview: {data.get('answer', '')[:100]}...")
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Exception: {e}")

if __name__ == "__main__":
    debug_response_generation()
