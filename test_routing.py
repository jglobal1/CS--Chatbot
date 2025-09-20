#!/usr/bin/env python3
"""
Test script to verify the routing logic works correctly
This script tests whether the system prioritizes specific dataset over generic responses
"""

import requests
import json

def test_course_specific_questions():
    """Test questions that should use the specific dataset"""
    
    # Test questions that should trigger CS domain detection
    test_questions = [
        "What is COS101 about?",
        "Tell me about COS102 course",
        "Who teaches COS101?",
        "What are the materials for COS102?",
        "How is COS101 assessed?",
        "What programming languages are taught in COS102?",
        "Tell me about computer science courses",
        "What is the curriculum for COS101?",
        "Who are the lecturers for COS102?",
        "What are the learning objectives for COS101?"
    ]
    
    print("🧪 Testing Course-Specific Questions")
    print("=" * 50)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Question: {question}")
        
        try:
            # Make request to the API
            response = requests.post(
                "http://localhost:8000/ask",
                json={"question": question},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data.get('answer', 'No answer')
                model_used = data.get('model_used', 'Unknown')
                confidence = data.get('confidence', 0)
                
                print(f"   ✅ Model Used: {model_used}")
                print(f"   📊 Confidence: {confidence:.2f}")
                print(f"   💬 Answer: {answer[:100]}...")
                
                # Check if it's using the right model (not external API for course questions)
                if 'external_api' in model_used.lower() and any(course in question.upper() for course in ['COS101', 'COS102']):
                    print(f"   ⚠️  WARNING: Using external API for course-specific question!")
                elif 'unified' in model_used.lower() or 'fine_tuned' in model_used.lower():
                    print(f"   ✅ Using specific dataset for course question")
                else:
                    print(f"   ℹ️  Using {model_used} for course question")
                    
            else:
                print(f"   ❌ Error: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            print(f"   ❌ Connection Error: Make sure the backend is running on localhost:8000")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("✅ Course-specific question testing completed!")

def test_general_questions():
    """Test questions that should use external APIs"""
    
    general_questions = [
        "What is the weather like?",
        "Tell me about artificial intelligence",
        "What are the latest technology trends?",
        "How do I apply to FUT?",
        "What is the FUT campus like?"
    ]
    
    print("\n🌐 Testing General Questions")
    print("=" * 50)
    
    for i, question in enumerate(general_questions, 1):
        print(f"\n{i}. Question: {question}")
        
        try:
            response = requests.post(
                "http://localhost:8000/ask",
                json={"question": question},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data.get('answer', 'No answer')
                model_used = data.get('model_used', 'Unknown')
                confidence = data.get('confidence', 0)
                
                print(f"   ✅ Model Used: {model_used}")
                print(f"   📊 Confidence: {confidence:.2f}")
                print(f"   💬 Answer: {answer[:100]}...")
                
                # Check if it's using external API for general questions
                if 'external_api' in model_used.lower():
                    print(f"   ✅ Using external API for general question (expected)")
                else:
                    print(f"   ℹ️  Using unified intelligence for general question")
                    
            else:
                print(f"   ❌ Error: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            print(f"   ❌ Connection Error: Make sure the backend is running on localhost:8000")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("✅ General question testing completed!")

if __name__ == "__main__":
    print("🚀 FUT QA Assistant Routing Test")
    print("Testing whether the system prioritizes specific dataset over generic responses")
    print("=" * 70)
    
    # Test course-specific questions first
    test_course_specific_questions()
    
    # Test general questions
    test_general_questions()
    
    print("\n🎯 Test Summary:")
    print("- Course-specific questions should use unified intelligence (your dataset)")
    print("- General questions can use external APIs")
    print("- The system should NOT use external APIs for COS101, COS102, etc.")
    print("\n💡 If you see 'WARNING: Using external API for course-specific question!', the routing needs more fixes.")
