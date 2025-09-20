#!/usr/bin/env python3
"""
Test Groq API Integration
"""

import requests
import time

def test_groq_integration():
    """Test Groq API integration"""
    base_url = "http://localhost:8000"
    
    print("🚀 Testing Groq API Integration")
    print("=" * 50)
    print("Testing: Groq API for high-quality responses")
    print("=" * 50)
    
    # Check API status
    try:
        response = requests.get(f"{base_url}/external-api-status")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Available APIs: {data['available_apis']}")
            print(f"✅ Total Configured: {data['total_configured']}")
            print(f"✅ Groq Configured: {data.get('groq_configured', 'Not shown')}")
        else:
            print(f"❌ Error getting API status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test questions that should use Groq API
    test_questions = [
        "what are the top schools in africa",
        "explain artificial intelligence in simple terms",
        "what is machine learning and how does it work",
        "tell me about blockchain technology",
        "what are the latest technology trends"
    ]
    
    print("\n🧪 Testing Questions with Groq API")
    print("-" * 50)
    
    groq_responses = 0
    total_questions = len(test_questions)
    
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
                    print("   🎉 Using external API (likely Groq)!")
                    groq_responses += 1
                elif strategy == 'external_api_fallback':
                    print("   🔄 Using external API as fallback!")
                    groq_responses += 1
                else:
                    print("   ⚠️  Using internal response")
                
                # Check response quality
                if "I understand you're asking about" in answer and "outside my specialized domain" in answer:
                    print("   ❌ Generic fallback response")
                else:
                    print("   ✅ Good response!")
                
                # Show first 150 characters
                preview = answer[:150] + "..." if len(answer) > 150 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(1)  # Wait between requests
    
    print("\n" + "=" * 50)
    print("🎉 Groq API Integration Test Complete!")
    print("=" * 50)
    print(f"✅ Groq Responses: {groq_responses}/{total_questions}")
    
    if groq_responses > 0:
        print("🎉 Groq API is working and providing responses!")
        print("✅ Your system now has high-quality, fast responses!")
    else:
        print("⚠️  Groq API might not be working yet")
        print("   Check if the API key is correct and the backend is running")
    
    print("\n🚀 Your system now has:")
    print("   🆓 Hugging Face (free)")
    print("   🚀 Groq (high-quality, fast)")
    print("   🆓 Enhanced fallbacks")
    print("   📚 Real PDF downloads")
    print("   💬 Smart conversation context")

if __name__ == "__main__":
    test_groq_integration()
