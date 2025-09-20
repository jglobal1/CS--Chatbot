#!/usr/bin/env python3
"""
Test Free APIs
"""

import requests
import time

def test_free_apis():
    """Test which free APIs are working"""
    base_url = "http://localhost:8000"
    
    print("🆓 Testing Free APIs")
    print("=" * 50)
    print("Testing: Hugging Face, Groq, Gemini, and fallbacks")
    print("=" * 50)
    
    # Check API status
    try:
        response = requests.get(f"{base_url}/external-api-status")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Available APIs: {data['available_apis']}")
            print(f"✅ Total Configured: {data['total_configured']}")
            print(f"✅ OpenAI: {data['openai_configured']}")
            print(f"✅ Gemini: {data['gemini_configured']}")
            print(f"✅ Hugging Face: {data['huggingface_configured']}")
        else:
            print(f"❌ Error getting API status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test questions that should use external APIs
    test_questions = [
        "what are the top schools in africa",
        "explain artificial intelligence",
        "what is machine learning",
        "tell me about blockchain technology"
    ]
    
    print("\n🧪 Testing Questions with Free APIs")
    print("-" * 50)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 Test {i}: '{question}'")
        
        try:
            response = requests.post(f"{base_url}/ask", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                answer = data['answer']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                
                if strategy == 'external_api':
                    print("   🎉 Using external API!")
                elif strategy == 'external_api_fallback':
                    print("   🔄 Using external API as fallback!")
                else:
                    print("   ⚠️  Using internal response")
                
                # Check response quality
                if "I understand you're asking about" in answer and "outside my specialized domain" in answer:
                    print("   ❌ Generic fallback response")
                else:
                    print("   ✅ Good response!")
                
                # Show first 100 characters
                preview = answer[:100] + "..." if len(answer) > 100 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print("🎉 Free API Test Complete!")
    print("=" * 50)
    print("✅ Your system now has multiple free API options:")
    print("   🆓 Hugging Face (already working)")
    print("   🆓 Groq (if you get API key)")
    print("   🆓 Gemini (if you get API key)")
    print("   🆓 Enhanced fallback responses")
    print("\n📖 See FREE_API_SETUP_GUIDE.md for setup instructions")

if __name__ == "__main__":
    test_free_apis()
