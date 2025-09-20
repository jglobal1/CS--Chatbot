#!/usr/bin/env python3
"""
Test Real OpenAI Integration
"""

import requests
import time

def test_real_openai():
    """Test real OpenAI API integration"""
    base_url = "http://localhost:8000"
    
    print("🤖 Testing Real OpenAI Integration")
    print("=" * 50)
    print("Testing: Actual OpenAI API calls for general questions")
    print("=" * 50)
    
    # Test questions that should get real OpenAI responses
    test_questions = [
        "whats the latest technology",
        "explain artificial intelligence",
        "what is machine learning",
        "tell me about blockchain",
        "how does neural networks work"
    ]
    
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
                    print("   🎉 Using OpenAI API!")
                elif strategy == 'external_api_fallback':
                    print("   🔄 Using OpenAI as fallback!")
                else:
                    print("   ⚠️  Using internal response")
                
                # Check if it's a real response or generic fallback
                if "I understand you're asking about" in answer and "outside my specialized domain" in answer:
                    print("   ⚠️  Still getting generic fallback response")
                else:
                    print("   ✅ Got real OpenAI response!")
                
                # Show first 200 characters of answer
                preview = answer[:200] + "..." if len(answer) > 200 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(2)  # Wait between requests to avoid rate limits
    
    print("\n" + "=" * 50)
    print("🎉 Real OpenAI Integration Test Complete!")
    print("=" * 50)
    
    if "real OpenAI response" in str(locals()):
        print("✅ OpenAI API is working and providing real responses!")
    else:
        print("⚠️  OpenAI API might still be falling back to generic responses")
        print("   Check the backend logs for any API errors")

if __name__ == "__main__":
    test_real_openai()
