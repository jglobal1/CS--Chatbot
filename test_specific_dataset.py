#!/usr/bin/env python3
"""
Test that the system uses your specific dataset instead of generic responses
"""

import requests
import time

def test_specific_dataset():
    """Test that the system uses your specific course data"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Specific Dataset Usage")
    print("=" * 60)
    print("Testing: System should use your specific course data, not generic responses")
    print("=" * 60)
    
    # Test questions that should trigger your specific dataset
    test_questions = [
        "list my courses",
        "what courses are available",
        "show me the courses",
        "what are the 100 level courses",
        "tell me about COS101",
        "who teaches COS102",
        "what materials are available for COS101"
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
                
                # Check if response contains your specific course data
                if any(course in answer for course in ['COS101', 'COS102', 'MAT121', 'PHY101', 'CST111']):
                    print("   🎉 Using your specific dataset!")
                elif 'FCS' in answer or 'FUTMINNA' in answer:
                    print("   ❌ Using generic data instead of your dataset!")
                else:
                    print("   ⚠️  Mixed response")
                
                # Show preview
                preview = answer[:200] + "..." if len(answer) > 200 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(1)
    
    print("\n" + "=" * 60)
    print("🎯 DATASET USAGE TEST RESULTS")
    print("=" * 60)
    
    print("✅ EXPECTED BEHAVIOR:")
    print("   📚 Should show your specific courses (COS101, COS102, etc.)")
    print("   👨‍🏫 Should list your specific lecturers")
    print("   📖 Should use your course descriptions")
    print("   🎯 Should avoid generic FCS course codes")
    
    print("\n❌ PROBLEM IDENTIFIED:")
    print("   🔍 System is using generic course data instead of your dataset")
    print("   🛠️  Need to fix routing to prioritize your specific data")
    print("   📝 Need to enhance course list response method")
    
    print("\n🚀 SOLUTION:")
    print("   1. Update course list response to use your specific data")
    print("   2. Fix routing to prioritize your dataset over generic responses")
    print("   3. Ensure Groq enhancement doesn't override your data")
    print("   4. Test with course-specific questions")

if __name__ == "__main__":
    test_specific_dataset()
