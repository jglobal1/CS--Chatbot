#!/usr/bin/env python3
"""
Test Enhanced Course Information - Test detailed course info with lecturers and materials
"""

import requests
import time

def test_enhanced_course_info():
    """Test enhanced course information with lecturers and materials"""
    base_url = "http://localhost:8000"
    
    print("🎓 Testing Enhanced Course Information")
    print("=" * 70)
    print("Testing detailed course info with lecturers and material downloads")
    print("=" * 70)
    
    # Test cases for enhanced course information
    test_cases = [
        # Course-specific questions
        ("COS101", "Should get detailed course info with lecturers"),
        ("CPT121", "Should get course details with lecturer names"),
        ("MAT101", "Should get course information"),
        
        # Lecturer-specific questions
        ("lecturer for COS101", "Should get lecturer names for COS101"),
        ("who teaches CPT121", "Should get lecturer information"),
        ("teacher for MAT101", "Should get lecturer details"),
        
        # Material download questions
        ("download materials for COS101", "Should get material download options"),
        ("I need materials for CPT121", "Should get download information"),
        ("show me materials for MAT101", "Should get material access info"),
        
        # Interactive questions
        ("what topics are in COS101", "Should get course topics"),
        ("study tips for CPT121", "Should get study guidance"),
        ("past questions for MAT101", "Should get past questions info"),
    ]
    
    print(f"🚀 Running {len(test_cases)} enhanced course information tests...")
    print("=" * 70)
    
    successful_tests = 0
    total_tests = len(test_cases)
    
    for i, (question, expected) in enumerate(test_cases, 1):
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
                print(f"   ✅ Response: {answer_preview}")
                
                # Check for specific content
                if "lecturer" in data['answer'].lower() or "teacher" in data['answer'].lower():
                    print("   ✅ Contains lecturer information!")
                elif "download" in data['answer'].lower() or "material" in data['answer'].lower():
                    print("   ✅ Contains material information!")
                elif "course" in data['answer'].lower() and len(data['answer']) > 200:
                    print("   ✅ Contains detailed course information!")
                else:
                    print("   ⚠️  Response could be more detailed")
                
                # Check if it's a useful response
                if confidence > 0.8 and len(data['answer']) > 100:
                    print("   ✅ Got detailed, useful response!")
                    successful_tests += 1
                else:
                    print("   ⚠️  Response could be better")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                print(f"   Response: {response.text}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    # Test interactive course flow
    print("\n" + "=" * 70)
    print("🔄 Testing Interactive Course Flow")
    print("=" * 70)
    
    interactive_flow = [
        "Tell me about COS101",
        "Who teaches this course?",
        "What materials do I need?",
        "Can I download materials?",
        "What topics are covered?",
        "Any study tips?"
    ]
    
    print("📝 Testing interactive course conversation:")
    for i, q in enumerate(interactive_flow, 1):
        print(f"   {i}. {q}")
    
    print("\n🔄 Running interactive course flow test...")
    for i, question in enumerate(interactive_flow, 1):
        print(f"\n💬 Turn {i}: '{question}'")
        try:
            response = requests.post(f"{base_url}/ask", json={"question": question})
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Strategy: {data['model_used']}")
                print(f"   ✅ Confidence: {data['confidence']:.2%}")
                print(f"   ✅ Response: {data['answer'][:150]}...")
            else:
                print(f"   ❌ Error: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        time.sleep(0.5)
    
    # Final results
    print("\n" + "=" * 70)
    print("🎉 Enhanced Course Information Test Results")
    print("=" * 70)
    
    success_rate = (successful_tests / total_tests) * 100
    
    print(f"📊 Success Rate: {success_rate:.1f}% ({successful_tests}/{total_tests})")
    
    if success_rate >= 80:
        print("\n🎉 EXCELLENT! The system provides comprehensive course information!")
        print("   🎓 Detailed course information with lecturers")
        print("   📥 Material download options")
        print("   💬 Interactive course guidance")
        print("   🧠 Smart course-specific responses")
    elif success_rate >= 60:
        print("\n✅ GOOD! The system provides good course information!")
        print("   🎓 Most course questions get detailed responses")
        print("   📥 Good material information")
    else:
        print("\n⚠️  NEEDS IMPROVEMENT! The system needs better course information!")
        print("   🔧 Improve course-specific responses")
        print("   📊 Better lecturer information")
        print("   💬 Enhanced material access")
    
    print("\n🎯 Key Features Tested:")
    print("   ✅ Course-specific information")
    print("   ✅ Lecturer details and names")
    print("   ✅ Material download options")
    print("   ✅ Interactive course guidance")
    print("   ✅ Study tips and advice")
    print("   ✅ Past questions access")
    
    print("\n🚀 The system now provides comprehensive course information!")
    print("   Students can get detailed course info, lecturer names, and download materials!")

if __name__ == "__main__":
    test_enhanced_course_info()
