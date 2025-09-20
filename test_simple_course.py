#!/usr/bin/env python3
"""
Simple test to check if course questions use your specific dataset
"""

import requests
import time

def test_simple_course():
    """Test course questions"""
    base_url = "http://localhost:8000"
    
    print("🧪 Simple Course Test")
    print("=" * 40)
    
    # Test a simple course question
    question = "list my courses"
    print(f"📝 Testing: '{question}'")
    
    try:
        response = requests.post(f"{base_url}/ask", json={"question": question})
        
        if response.status_code == 200:
            data = response.json()
            strategy = data['model_used']
            confidence = data['confidence']
            answer = data['answer']
            
            print(f"✅ Strategy: {strategy}")
            print(f"✅ Confidence: {confidence:.2%}")
            
            # Check if response contains your specific courses
            if 'COS101' in answer and 'COS102' in answer:
                print("🎉 SUCCESS: Using YOUR specific dataset!")
                print("✅ Shows COS101, COS102, etc.")
            elif 'FCS' in answer:
                print("❌ PROBLEM: Still using generic data!")
                print("❌ Shows FCS courses instead of yours")
            else:
                print("⚠️  Mixed response")
            
            # Show preview
            preview = answer[:200] + "..." if len(answer) > 200 else answer
            print(f"📝 Answer: {preview}")
            
        else:
            print(f"❌ Error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 40)
    print("🎯 RESULT:")
    print("If you see COS101, COS102, MAT121 - FIX IS WORKING!")
    print("If you see FCS courses - STILL NEEDS FIXING!")

if __name__ == "__main__":
    test_simple_course()
