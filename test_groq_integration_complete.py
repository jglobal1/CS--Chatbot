#!/usr/bin/env python3
"""
Test Complete Groq Integration
"""

import requests
import time

def test_groq_integration_complete():
    """Test complete Groq integration"""
    base_url = "http://localhost:8000"
    
    print("🚀 Testing Complete Groq Integration")
    print("=" * 60)
    print("Testing: Hybrid responses, direct Groq, and training data generation")
    print("=" * 60)
    
    # Test 1: Check API status
    print("\n📊 Testing API Status")
    print("-" * 40)
    
    try:
        response = requests.get(f"{base_url}/external-api-status")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Available APIs: {data['available_apis']}")
            print(f"✅ Groq Configured: {data.get('groq_configured', 'Not shown')}")
            print(f"✅ Total Configured: {data['total_configured']}")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 2: Direct Groq endpoint
    print("\n🤖 Testing Direct Groq Endpoint")
    print("-" * 40)
    
    test_questions = [
        "what is computer science",
        "explain programming concepts",
        "what are data structures"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 Test {i}: '{question}' (Direct Groq)")
        
        try:
            response = requests.post(f"{base_url}/ask-groq", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                answer = data['answer']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                
                if strategy == 'groq_direct':
                    print("   🎉 Direct Groq response!")
                else:
                    print("   ⚠️  Other strategy")
                
                # Show preview
                preview = answer[:150] + "..." if len(answer) > 150 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(1)
    
    # Test 3: Hybrid responses
    print("\n🔄 Testing Hybrid Responses")
    print("-" * 40)
    
    hybrid_questions = [
        "who is the lecturer for COS102",
        "what materials are available for COS101",
        "tell me about programming courses"
    ]
    
    for i, question in enumerate(hybrid_questions, 1):
        print(f"\n📝 Test {i}: '{question}' (Hybrid)")
        
        try:
            response = requests.post(f"{base_url}/ask", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                answer = data['answer']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                
                if strategy == 'hybrid_groq_enhanced':
                    print("   🎉 Hybrid Groq enhanced response!")
                elif strategy in ['course_specific', 'course_general', 'materials']:
                    print("   ✅ Your trained model response")
                else:
                    print("   ⚠️  Other strategy")
                
                # Show preview
                preview = answer[:150] + "..." if len(answer) > 150 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(1)
    
    print("\n" + "=" * 60)
    print("🎉 Complete Groq Integration Test Results")
    print("=" * 60)
    
    print("✅ GROQ INTEGRATION FEATURES:")
    print("   🤖 Direct Groq endpoint (/ask-groq)")
    print("   🔄 Hybrid responses (Your model + Groq)")
    print("   📚 Enhanced training data generation")
    print("   🎯 Smart routing with Groq fallback")
    print("   📥 Real PDF downloads")
    print("   💬 Enhanced conversation context")
    
    print("\n🚀 HOW TO USE GROQ FOR TRAINING:")
    print("   1. Run: python generate_training_data_with_groq.py")
    print("   2. Use generated data to retrain your model")
    print("   3. Combine your domain knowledge with Groq's general knowledge")
    print("   4. Use hybrid responses for best results")
    
    print("\n🎯 RECOMMENDED WORKFLOW:")
    print("   • CS Domain Questions → Your trained model")
    print("   • Low confidence responses → Groq enhancement")
    print("   • General questions → Direct Groq")
    print("   • Generate training data → Groq API")
    print("   • Real materials → Your PDF database")

if __name__ == "__main__":
    test_groq_integration_complete()
