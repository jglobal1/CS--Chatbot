#!/usr/bin/env python3
"""
Test the exact question from the screenshot
"""

import requests
import time

def test_screenshot_question():
    """Test the exact question from the screenshot"""
    base_url = "http://localhost:8000"
    
    print("🔍 Testing Screenshot Question")
    print("=" * 50)
    print("Testing: 'what are the top schools in africa'")
    print("=" * 50)
    
    question = "what are the top schools in africa"
    
    try:
        response = requests.post(f"{base_url}/ask", json={"question": question})
        
        if response.status_code == 200:
            data = response.json()
            strategy = data['model_used']
            confidence = data['confidence']
            answer = data['answer']
            
            print(f"✅ Strategy: {strategy}")
            print(f"✅ Confidence: {confidence:.2%}")
            print(f"📝 Full Answer: {answer}")
            
            # Check if it's the generic fallback
            if "I understand you're asking about" in answer and "outside my specialized domain" in answer:
                print("\n❌ STILL GETTING GENERIC FALLBACK!")
                print("The system is not using the improved responses.")
            else:
                print("\n✅ Got improved response!")
                
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test a few more questions to see the pattern
    print("\n" + "=" * 50)
    print("🧪 Testing More Questions")
    print("=" * 50)
    
    test_questions = [
        "what are the best universities in nigeria",
        "tell me about harvard university", 
        "what is the weather like today"
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
                
                if "I understand you're asking about" in answer:
                    print("   ❌ Generic fallback response")
                else:
                    print("   ✅ Improved response")
                
                # Show first 100 characters
                preview = answer[:100] + "..." if len(answer) > 100 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)

if __name__ == "__main__":
    test_screenshot_question()
