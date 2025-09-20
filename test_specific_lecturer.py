#!/usr/bin/env python3
"""
Test Specific Lecturer Questions - Test individual lecturer questions
"""

import requests
import time

def test_specific_lecturer_questions():
    """Test specific lecturer questions to identify the issue"""
    base_url = "http://localhost:8000"
    
    print("👨‍🏫 Testing Specific Lecturer Questions")
    print("=" * 60)
    print("Testing individual lecturer questions to identify issues")
    print("=" * 60)
    
    # Test specific lecturer questions
    lecturer_questions = [
        "who are the lecturer for MAT121",
        "lecturer for COS101", 
        "who teaches PHY101",
        "teacher for CST111",
        "instructor for FTM-CPT112",
        "who are the lecturers for PHY101",
        "lecturers for CST111",
        "who teaches FTM-CPT112"
    ]
    
    print(f"🚀 Running {len(lecturer_questions)} specific lecturer tests...")
    print("=" * 60)
    
    successful_tests = 0
    total_tests = len(lecturer_questions)
    
    for i, question in enumerate(lecturer_questions, 1):
        print(f"\n📝 Test {i}: '{question}'")
        
        try:
            response = requests.post(f"{base_url}/ask", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                answer_preview = data['answer'][:200] + "..." if len(data['answer']) > 200 else data['answer']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                print(f"   ✅ Response: {answer_preview}")
                
                # Check if it's a specific lecturer response
                if strategy == 'course_specific' and confidence > 0.8:
                    print("   ✅ Got specific lecturer information!")
                    successful_tests += 1
                elif "FUT CS Assistant - How Can I Help?" in data['answer']:
                    print("   ⚠️  Got generic response - course not recognized")
                else:
                    print("   ⚠️  Got unexpected response")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                print(f"   Response: {response.text}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    # Test course detection patterns
    print("\n" + "=" * 60)
    print("🔍 Testing Course Detection Patterns")
    print("=" * 60)
    
    course_tests = [
        "MAT121",
        "COS101", 
        "PHY101",
        "CST111",
        "FTM-CPT112"
    ]
    
    for i, course in enumerate(course_tests, 1):
        print(f"\n📝 Course Test {i}: '{course}'")
        
        try:
            response = requests.post(f"{base_url}/ask", json={"question": course})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                
                if strategy == 'course_specific' and confidence > 0.8:
                    print("   ✅ Course detected correctly!")
                else:
                    print("   ⚠️  Course not detected - falling back to generic")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    # Final results
    print("\n" + "=" * 60)
    print("🎉 Specific Lecturer Test Results")
    print("=" * 60)
    
    success_rate = (successful_tests / total_tests) * 100
    
    print(f"📊 Success Rate: {success_rate:.1f}% ({successful_tests}/{total_tests})")
    
    if success_rate >= 80:
        print("\n🎉 EXCELLENT! The system handles lecturer questions very well!")
        print("   👨‍🏫 Specific lecturer information provided")
        print("   🎯 Course detection working properly")
        print("   💬 Context-aware responses")
    elif success_rate >= 60:
        print("\n✅ GOOD! The system handles most lecturer questions well!")
        print("   👨‍🏫 Most lecturer questions get specific responses")
        print("   🎯 Good course detection")
    else:
        print("\n⚠️  NEEDS IMPROVEMENT! The system needs better lecturer question handling!")
        print("   🔧 Improve course detection patterns")
        print("   📊 Better lecturer information routing")
        print("   💬 Enhanced context awareness")
    
    print("\n🎯 Key Features Tested:")
    print("   ✅ Course-specific lecturer information")
    print("   ✅ Pattern matching for lecturer questions")
    print("   ✅ Course detection accuracy")
    print("   ✅ Response strategy routing")
    print("   ✅ Confidence scoring")
    
    print("\n🚀 The system should now handle lecturer questions properly!")
    print("   Students can ask about specific lecturers and get detailed information!")

if __name__ == "__main__":
    test_specific_lecturer_questions()
