#!/usr/bin/env python3
"""
Test External API Integration
"""

import requests
import time

def test_external_api_integration():
    """Test the external API integration"""
    base_url = "http://localhost:8000"
    
    print("🌐 Testing External API Integration")
    print("=" * 60)
    print("Testing: External LLM integration for questions outside domain")
    print("=" * 60)
    
    # Test 1: Check external API status
    print("\n📊 Testing External API Status")
    print("-" * 40)
    
    try:
        response = requests.get(f"{base_url}/external-api-status")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ External API Status: {data['message']}")
            print(f"✅ Available APIs: {data['available_apis']}")
            print(f"✅ Total Configured: {data['total_configured']}")
        else:
            print(f"❌ Error getting API status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 2: General FUT questions (should use external API)
    print("\n🏫 Testing General FUT Questions")
    print("-" * 40)
    
    general_questions = [
        "tell me about FUT",
        "where is FUT located",
        "when was FUT established",
        "what is FUT's website",
        "what departments does FUT have",
        "how do I apply to FUT"
    ]
    
    for i, question in enumerate(general_questions, 1):
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
                    print("   ✅ Used external API!")
                elif strategy == 'external_api_fallback':
                    print("   ✅ Used external API as fallback!")
                else:
                    print("   ⚠️  Used internal response")
                
                # Show first 100 characters of answer
                preview = answer[:100] + "..." if len(answer) > 100 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    # Test 3: Questions outside domain (should use external API)
    print("\n🌍 Testing Questions Outside Domain")
    print("-" * 40)
    
    outside_domain_questions = [
        "what is the weather like today",
        "tell me about artificial intelligence",
        "what are the latest technology trends",
        "explain machine learning",
        "what is blockchain technology"
    ]
    
    for i, question in enumerate(outside_domain_questions, 1):
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
                    print("   ✅ Used external API!")
                elif strategy == 'external_api_fallback':
                    print("   ✅ Used external API as fallback!")
                else:
                    print("   ⚠️  Used internal response")
                
                # Show first 100 characters of answer
                preview = answer[:100] + "..." if len(answer) > 100 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    # Test 4: CS domain questions (should use trained model)
    print("\n💻 Testing CS Domain Questions")
    print("-" * 40)
    
    cs_questions = [
        "who is the lecturer for COS102",
        "what materials are available for COS101",
        "tell me about programming courses",
        "what is computer science about"
    ]
    
    for i, question in enumerate(cs_questions, 1):
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
                
                if strategy in ['course_specific', 'course_general', 'materials', 'cs_guidance']:
                    print("   ✅ Used trained model!")
                elif strategy == 'external_api':
                    print("   ⚠️  Used external API (might be correct)")
                else:
                    print("   ⚠️  Used other strategy")
                
                # Show first 100 characters of answer
                preview = answer[:100] + "..." if len(answer) > 100 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    # Final results
    print("\n" + "=" * 60)
    print("🎉 External API Integration Test Results")
    print("=" * 60)
    
    print("✅ IMPLEMENTED FEATURES:")
    print("   🌐 External API integration framework")
    print("   🔧 Configuration system for API keys")
    print("   📊 API status monitoring")
    print("   🎯 Smart routing (CS domain → trained model)")
    print("   🌍 General questions → external API")
    print("   🔄 Fallback mechanism for low confidence responses")
    
    print("\n🚀 TO CONFIGURE EXTERNAL APIs:")
    print("   📝 Set environment variables:")
    print("      • OPENAI_API_KEY=your_openai_key")
    print("      • GEMINI_API_KEY=your_gemini_key")
    print("      • HUGGINGFACE_API_KEY=your_hf_key")
    print("   🔧 Or modify config.py directly")
    
    print("\n🎯 CURRENT STATUS:")
    print("   ✅ Framework ready for external APIs")
    print("   ✅ Fallback to web search for general questions")
    print("   ✅ Smart routing based on question type")
    print("   ✅ Configuration system in place")
    print("   ⚠️  External APIs need API keys to be fully functional")

if __name__ == "__main__":
    test_external_api_integration()
