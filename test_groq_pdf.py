#!/usr/bin/env python3
"""
Test script to verify Groq PDF integration works correctly
This tests whether Groq can answer questions using your PDF data
"""

import requests
import json

def test_groq_pdf_integration():
    """Test Groq with PDF data for various question types"""
    
    print("🧪 Testing Groq PDF Integration")
    print("=" * 50)
    
    # Test questions that should use PDF data
    test_questions = [
        # Lecturer questions
        "Who are the lecturers teaching COS101?",
        "Who teaches COS102 at FUT?",
        "What are the names of lecturers for Computer Science courses?",
        "Who is teaching Front End Web Development?",
        
        # Course questions
        "What is COS101 about?",
        "Tell me about COS102 course",
        "What does CPT112 cover?",
        "What is the content of PHY101?",
        
        # Career questions
        "What career paths are available in Computer Science?",
        "What industries can Computer Science graduates work in?",
        "What are the essential skills for Computer Science students?",
        
        # General CS questions
        "What is Computer Science?",
        "How can I balance academics with other responsibilities?",
        "What edge does Computer Science have over other departments?",
        
        # Specific FUT questions
        "What courses are offered in the Computer Science department at FUT?",
        "Who are the current lecturers in the CS department?",
        "What are the Computer Science courses at FUT Minna?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Question: {question}")
        
        try:
            # Test the main endpoint (should use Groq with PDF data for CS questions)
            response = requests.post(
                "http://localhost:8000/ask",
                json={"question": question},
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data.get('answer', 'No answer')
                model_used = data.get('model_used', 'Unknown')
                confidence = data.get('confidence', 0)
                
                print(f"   ✅ Model Used: {model_used}")
                print(f"   📊 Confidence: {confidence:.2f}")
                print(f"   💬 Answer: {answer[:150]}...")
                
                # Check if it's using the right model
                if 'groq_pdf' in model_used.lower():
                    print("   ✅ Using Groq with PDF data")
                elif 'unified' in model_used.lower():
                    print("   ℹ️  Using unified intelligence")
                elif 'external_api' in model_used.lower():
                    print("   ℹ️  Using external API")
                else:
                    print(f"   ℹ️  Using {model_used}")
                    
            else:
                print(f"   ❌ Error: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            print(f"   ❌ Connection Error: Make sure the backend is running on localhost:8000")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("✅ Groq PDF integration testing completed!")

def test_direct_groq_pdf():
    """Test the direct Groq PDF endpoint"""
    
    print("\n🔬 Testing Direct Groq PDF Endpoint")
    print("=" * 50)
    
    test_questions = [
        "Who teaches COS101?",
        "What are the career paths in Computer Science?",
        "What skills are essential for Computer Science students?",
        "Who are the lecturers in the CS department?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Direct Groq PDF Question: {question}")
        
        try:
            response = requests.post(
                "http://localhost:8000/ask-groq-pdf",
                json={"question": question},
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data.get('answer', 'No answer')
                model_used = data.get('model_used', 'Unknown')
                confidence = data.get('confidence', 0)
                
                print(f"   ✅ Model Used: {model_used}")
                print(f"   📊 Confidence: {confidence:.2f}")
                print(f"   💬 Answer: {answer[:150]}...")
                
                # Check if it contains specific information from PDF
                if any(name in answer for name in ['Umar Alkali', 'Sadiu Ahmed', 'Benjamin Alenoghen', 'Aku Ibrahim']):
                    print("   ✅ Contains specific lecturer names from PDF data")
                elif any(course in answer for course in ['COS101', 'COS102', 'CPT112', 'PHY101']):
                    print("   ✅ Contains specific course information from PDF data")
                else:
                    print("   ℹ️  Generic response (may not be using PDF data)")
                    
            else:
                print(f"   ❌ Error: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            print(f"   ❌ Connection Error: Make sure the backend is running on localhost:8000")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("✅ Direct Groq PDF testing completed!")

if __name__ == "__main__":
    print("🚀 Groq PDF Integration Test")
    print("Testing whether Groq can answer questions using your PDF data")
    print("=" * 70)
    
    # Test main endpoint with Groq PDF integration
    test_groq_pdf_integration()
    
    # Test direct Groq PDF endpoint
    test_direct_groq_pdf()
    
    print("\n🎯 Test Summary:")
    print("- CS questions should use Groq with PDF data")
    print("- Lecturer questions should return specific names from PDF")
    print("- Career questions should use PDF career information")
    print("- General questions can use external APIs")
    print("\n💡 Look for specific lecturer names and course details in responses!")
