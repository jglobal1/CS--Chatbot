#!/usr/bin/env python3
"""
Test Specific Questions to see what responses we get
"""

import requests
import time

def test_specific_questions():
    """Test specific questions to see the actual responses"""
    base_url = "http://localhost:8000"
    
    print("🎯 Testing Specific Questions")
    print("=" * 60)
    
    # Test specific questions that should work
    test_questions = [
        ("What books do I need?", "Should get materials response"),
        ("Hello, I'm new here", "Should get conversational response"),
        ("What can I do after graduation?", "Should get career guidance"),
        ("What courses are available?", "Should get course listing"),
        ("Who teaches programming?", "Should get course-specific response"),
    ]
    
    for i, (question, expected) in enumerate(test_questions, 1):
        print(f"\n📝 Test {i}: '{question}'")
        print(f"   Expected: {expected}")
        
        try:
            response = requests.post(f"{base_url}/ask", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                answer_preview = data['answer'][:200] + "..." if len(data['answer']) > 200 else data['answer']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                print(f"   ✅ Response Preview: {answer_preview}")
                
                # Check if it's the generic response
                if "FUT CS Assistant - How Can I Help?" in data['answer']:
                    print("   ⚠️  Got generic response - intent analysis might not be working")
                else:
                    print("   ✅ Got specific response - intent analysis working!")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                print(f"   Response: {response.text}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)

if __name__ == "__main__":
    test_specific_questions()
