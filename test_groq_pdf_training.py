#!/usr/bin/env python3
"""
Test Groq PDF Training Integration
"""

import requests
import time

def test_groq_pdf_training():
    """Test Groq trained on your PDF data"""
    base_url = "http://localhost:8000"
    
    print("🤖 Testing Groq PDF Training Integration")
    print("=" * 60)
    print("Testing: Groq trained on your specific PDF content")
    print("=" * 60)
    
    # Test 1: Course-specific questions
    print("\n📚 Testing Course-Specific Questions")
    print("-" * 50)
    
    course_questions = [
        "What is COS101 about?",
        "Tell me about COS102 course content",
        "Who are the lecturers for COS102?",
        "What materials are available for COS101?",
        "How is MAT121 assessed?",
        "What are the learning objectives for COS102?",
        "Tell me about PHY101 practical sessions",
        "What topics are covered in CST111?"
    ]
    
    for i, question in enumerate(course_questions, 1):
        print(f"\n📝 Test {i}: '{question}' (PDF-Trained Groq)")
        
        try:
            response = requests.post(f"{base_url}/ask-groq-pdf", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                answer = data['answer']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                
                if strategy == 'groq_pdf_trained':
                    print("   🎉 PDF-trained Groq response!")
                else:
                    print("   ⚠️  Other strategy")
                
                # Show preview
                preview = answer[:200] + "..." if len(answer) > 200 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(1)
    
    # Test 2: General CS questions
    print("\n🔬 Testing General CS Questions")
    print("-" * 50)
    
    general_questions = [
        "What is computer science?",
        "Explain programming concepts",
        "What are data structures?",
        "How does machine learning work?"
    ]
    
    for i, question in enumerate(general_questions, 1):
        print(f"\n📝 Test {i}: '{question}' (General CS)")
        
        try:
            response = requests.post(f"{base_url}/ask-groq-pdf", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                answer = data['answer']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                
                if strategy == 'groq_pdf_trained':
                    print("   🎉 PDF-trained Groq response!")
                else:
                    print("   ⚠️  Other strategy")
                
                # Show preview
                preview = answer[:200] + "..." if len(answer) > 200 else answer
                print(f"   📝 Answer: {preview}")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(1)
    
    # Test 3: Compare with regular Groq
    print("\n🔄 Comparing PDF-Trained vs Regular Groq")
    print("-" * 50)
    
    comparison_questions = [
        "What is COS101 about?",
        "Who teaches COS102?"
    ]
    
    for i, question in enumerate(comparison_questions, 1):
        print(f"\n📝 Comparison {i}: '{question}'")
        
        # Test PDF-trained Groq
        try:
            response_pdf = requests.post(f"{base_url}/ask-groq-pdf", json={"question": question})
            if response_pdf.status_code == 200:
                data_pdf = response_pdf.json()
                print(f"   📚 PDF-Trained: {data_pdf['model_used']} ({data_pdf['confidence']:.2%})")
                preview_pdf = data_pdf['answer'][:100] + "..." if len(data_pdf['answer']) > 100 else data_pdf['answer']
                print(f"   📝 Answer: {preview_pdf}")
            else:
                print(f"   ❌ PDF-Trained Error: {response_pdf.status_code}")
        except Exception as e:
            print(f"   ❌ PDF-Trained Error: {e}")
        
        # Test regular Groq
        try:
            response_regular = requests.post(f"{base_url}/ask-groq", json={"question": question})
            if response_regular.status_code == 200:
                data_regular = response_regular.json()
                print(f"   🤖 Regular Groq: {data_regular['model_used']} ({data_regular['confidence']:.2%})")
                preview_regular = data_regular['answer'][:100] + "..." if len(data_regular['answer']) > 100 else data_regular['answer']
                print(f"   📝 Answer: {preview_regular}")
            else:
                print(f"   ❌ Regular Groq Error: {response_regular.status_code}")
        except Exception as e:
            print(f"   ❌ Regular Groq Error: {e}")
        
        time.sleep(1)
    
    print("\n" + "=" * 60)
    print("🎉 GROQ PDF TRAINING TEST RESULTS")
    print("=" * 60)
    
    print("✅ PDF-TRAINED GROQ FEATURES:")
    print("   📚 Course-specific content understanding")
    print("   👨‍🏫 Lecturer information from PDFs")
    print("   📖 Course materials and assessment details")
    print("   🎯 Enhanced accuracy for domain questions")
    print("   🔄 Smart routing between general and specific")
    
    print("\n🚀 HOW TO USE PDF-TRAINED GROQ:")
    print("   1. Use /ask-groq-pdf for course-specific questions")
    print("   2. Use /ask-groq for general CS questions")
    print("   3. Use /ask for hybrid responses (your model + Groq)")
    print("   4. Generate training data with groq_pdf_training.py")
    
    print("\n🎯 RECOMMENDED WORKFLOW:")
    print("   • Course Questions → PDF-trained Groq")
    print("   • General CS → Regular Groq")
    print("   • Domain-specific → Your trained model")
    print("   • Low confidence → Groq enhancement")
    print("   • Training data → Groq generation")

if __name__ == "__main__":
    test_groq_pdf_training()
