#!/usr/bin/env python3
"""
Test API Key Setup
"""

import requests
import time

def test_api_key():
    """Test if API key is working"""
    base_url = "http://localhost:8000"
    
    print("🔑 Testing API Key Setup")
    print("=" * 40)
    
    # Test external API status
    try:
        response = requests.get(f"{base_url}/external-api-status")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ External API Status: {data['message']}")
            print(f"✅ Available APIs: {data['available_apis']}")
            print(f"✅ OpenAI Configured: {data['openai_configured']}")
            print(f"✅ Gemini Configured: {data['gemini_configured']}")
            print(f"✅ Hugging Face Configured: {data['huggingface_configured']}")
            
            if data['openai_configured']:
                print("\n🎉 OpenAI API is configured and ready!")
            else:
                print("\n⚠️  OpenAI API not configured yet")
                
        else:
            print(f"❌ Error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test a question that should use external API
    print("\n🧪 Testing External API with a question...")
    try:
        response = requests.post(f"{base_url}/ask", json={"question": "tell me about artificial intelligence"})
        
        if response.status_code == 200:
            data = response.json()
            strategy = data['model_used']
            confidence = data['confidence']
            
            print(f"✅ Strategy: {strategy}")
            print(f"✅ Confidence: {confidence:.2%}")
            
            if strategy == 'external_api':
                print("🎉 External API is working!")
            else:
                print("⚠️  Using internal response (external API might not be configured)")
                
        else:
            print(f"❌ Error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_api_key()
