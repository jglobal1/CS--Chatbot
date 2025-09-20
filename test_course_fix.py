#!/usr/bin/env python3
"""
Test that course questions use your specific dataset
"""

import requests
import time

def test_course_fix():
    """Test that course questions use your specific dataset"""
    base_url = "http://localhost:8000"
    
    print("🔧 Testing Course Dataset Fix")
    print("=" * 50)
    print("Testing: Course questions should use YOUR specific dataset")
    print("=" * 50)
    
    # Test course listing questions
    course_questions = [
        "list my courses",
        "what courses are available",
        "show me the courses"
    ]
    
    for i, question in enumerate(course_questions, 1):
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
                
                # Check if response contains your specific courses
                if 'COS101' in answer and 'COS102' in answer:
                    print("   🎉 Using YOUR specific dataset!")
                elif 'FCS' in answer:
                    print("   ❌ Still using generic data!")
                else:
                    print("   ⚠️  Mixed response")
                
                # Show preview
                preview = answer[:150] + "..." if len(answer) > 150 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print("🎯 FIX RESULTS")
    print("=" * 50)
    
    print("✅ EXPECTED:")
    print("   📚 Should show COS101, COS102, MAT121, etc.")
    print("   👨‍🏫 Should list your specific lecturers")
    print("   🎯 Should avoid generic FCS courses")
    
    print("\n🚀 NEXT STEPS:")
    print("   1. If still showing generic data, need to fix routing")
    print("   2. If showing your data, fix is working!")
    print("   3. Test with specific course questions")

if __name__ == "__main__":
    test_course_fix()
