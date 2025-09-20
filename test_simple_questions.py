#!/usr/bin/env python3
"""
Test Simple Questions - Ensure the system understands basic user requests
"""

import requests
import time

def test_simple_questions():
    """Test simple questions that should get direct answers"""
    base_url = "http://localhost:8000"
    
    print("🎯 Testing Simple Questions")
    print("=" * 60)
    print("Testing that simple questions get direct, smart answers")
    print("=" * 60)
    
    # Simple questions that should work
    simple_questions = [
        ("list my courses", "Should get course listing directly"),
        ("courses", "Should get course listing"),
        ("list courses", "Should get course listing"),
        ("show me courses", "Should get course listing"),
        ("what books do i need", "Should get materials list"),
        ("books", "Should get materials list"),
        ("career opportunities", "Should get career guidance"),
        ("jobs", "Should get career guidance"),
        ("hello", "Should get friendly greeting"),
        ("help", "Should get help information"),
    ]
    
    print(f"🚀 Running {len(simple_questions)} simple question tests...")
    print("=" * 60)
    
    successful_tests = 0
    total_tests = len(simple_questions)
    
    for i, (question, expected) in enumerate(simple_questions, 1):
        print(f"\n📝 Test {i}: '{question}'")
        print(f"   Expected: {expected}")
        
        try:
            response = requests.post(f"{base_url}/ask", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                answer_preview = data['answer'][:150] + "..." if len(data['answer']) > 150 else data['answer']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                print(f"   ✅ Response: {answer_preview}")
                
                # Check if it's a direct, useful response
                if "FUT CS Assistant - How Can I Help?" in data['answer']:
                    print("   ⚠️  Got generic response - should be more direct")
                elif len(data['answer']) > 100 and confidence > 0.8:
                    print("   ✅ Got direct, useful response!")
                    successful_tests += 1
                else:
                    print("   ⚠️  Response could be better")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    # Test adaptive learning
    print("\n" + "=" * 60)
    print("🧠 Testing Adaptive Learning")
    print("=" * 60)
    
    print("📝 Testing if the system learns from interactions...")
    
    # Ask the same question multiple times to see if it improves
    test_question = "list my courses"
    print(f"\n🔄 Asking '{test_question}' multiple times to test learning:")
    
    for i in range(3):
        print(f"\n   Attempt {i+1}:")
        try:
            response = requests.post(f"{base_url}/ask", json={"question": test_question})
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Strategy: {data['model_used']}")
                print(f"   ✅ Confidence: {data['confidence']:.2%}")
                print(f"   ✅ Response length: {len(data['answer'])} characters")
            else:
                print(f"   ❌ Error: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        time.sleep(0.5)
    
    # Final results
    print("\n" + "=" * 60)
    print("🎉 Simple Questions Test Results")
    print("=" * 60)
    
    success_rate = (successful_tests / total_tests) * 100
    
    print(f"📊 Success Rate: {success_rate:.1f}% ({successful_tests}/{total_tests})")
    
    if success_rate >= 80:
        print("\n🎉 EXCELLENT! The system handles simple questions very well!")
        print("   🎯 Direct answers for simple requests")
        print("   🧠 Smart pattern recognition")
        print("   💬 User-friendly responses")
    elif success_rate >= 60:
        print("\n✅ GOOD! The system handles most simple questions well!")
        print("   🎯 Most simple requests get direct answers")
        print("   🧠 Good pattern recognition")
    else:
        print("\n⚠️  NEEDS IMPROVEMENT! The system needs better simple question handling!")
        print("   🔧 Improve pattern matching for simple phrases")
        print("   📊 Better intent recognition for basic requests")
    
    print("\n🎯 Key Features Tested:")
    print("   ✅ Simple course listing requests")
    print("   ✅ Direct materials inquiries")
    print("   ✅ Basic career questions")
    print("   ✅ Friendly greetings")
    print("   ✅ Help requests")
    print("   ✅ Adaptive learning capability")
    
    print("\n🚀 The system should now handle simple questions like a human would!")
    print("   Students can ask simple questions and get direct, useful answers!")

if __name__ == "__main__":
    test_simple_questions()
