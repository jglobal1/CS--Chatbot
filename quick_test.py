#!/usr/bin/env python3
"""
Quick test to verify both CS-specific and general question routing works
"""

import requests
import json

def test_routing():
    """Test both CS-specific and general question routing"""
    
    print("🧪 Quick Routing Test")
    print("=" * 40)
    
    # Test CS-specific question (should use your dataset)
    cs_question = "What is COS101 about?"
    print(f"\n1. CS Question: {cs_question}")
    
    try:
        response = requests.post(
            "http://localhost:8000/ask",
            json={"question": cs_question},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            model_used = data.get('model_used', 'Unknown')
            print(f"   Model: {model_used}")
            
            if 'external_api' in model_used.lower():
                print("   ⚠️  WARNING: Using external API for CS question!")
            else:
                print("   ✅ Using specific dataset for CS question")
        else:
            print(f"   ❌ Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
    
    # Test general question (should use external API)
    general_question = "What is artificial intelligence?"
    print(f"\n2. General Question: {general_question}")
    
    try:
        response = requests.post(
            "http://localhost:8000/ask",
            json={"question": general_question},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            model_used = data.get('model_used', 'Unknown')
            print(f"   Model: {model_used}")
            
            if 'external_api' in model_used.lower():
                print("   ✅ Using external API for general question")
            else:
                print(f"   ℹ️  Using {model_used} for general question")
        else:
            print(f"   ❌ Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
    
    print("\n" + "=" * 40)
    print("✅ Test completed!")
    print("\nExpected Results:")
    print("- CS questions (COS101, COS102) should use your specific dataset")
    print("- General questions should use external APIs")
    print("- No more generic FCS course info for your specific courses")

if __name__ == "__main__":
    test_routing()
