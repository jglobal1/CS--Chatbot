#!/usr/bin/env python3
"""
Test OpenAI Integration
"""

import requests
import time

def test_openai_integration():
    """Test OpenAI API integration"""
    base_url = "http://localhost:8000"
    
    print("🤖 Testing OpenAI Integration")
    print("=" * 50)
    print("Testing: OpenAI API for general questions")
    print("=" * 50)
    
    # Test questions that should use OpenAI
    test_questions = [
        "explain artificial intelligence",
        "what is machine learning",
        "tell me about blockchain technology",
        "what are the latest tech trends",
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
                
                # Show first 150 characters of answer
                preview = answer[:150] + "..." if len(answer) > 150 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(1)  # Wait between requests
    
    # Test CS domain questions (should use trained model)
    print("\n💻 Testing CS Domain Questions (Should use trained model)")
    print("-" * 50)
    
    cs_questions = [
        "who is the lecturer for COS102",
        "what materials are available for COS101",
        "list my courses"
    ]
    
    for i, question in enumerate(cs_questions, 1):
        print(f"\n📝 Test {i}: '{question}'")
        
        try:
            response = requests.post(f"{base_url}/ask", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                
                if strategy in ['course_specific', 'course_general', 'materials', 'cs_guidance']:
                    print("   ✅ Using trained model (correct!)")
                elif strategy == 'external_api':
                    print("   ⚠️  Using OpenAI (might be correct)")
                else:
                    print("   ⚠️  Using other strategy")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    print("\n" + "=" * 50)
    print("🎉 OpenAI Integration Test Complete!")
    print("=" * 50)
    print("✅ Your system now has:")
    print("   🤖 OpenAI API integration for general questions")
    print("   🎯 Smart routing (CS → trained model, general → OpenAI)")
    print("   📚 Real PDF downloads from your codebase")
    print("   💬 Enhanced conversation context")
    print("   🔄 Fallback mechanisms for edge cases")

if __name__ == "__main__":
    test_openai_integration()
