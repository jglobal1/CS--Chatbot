#!/usr/bin/env python3
"""
Test script for FUT QA Assistant
Tests the model with sample questions
"""

import requests
import json

def test_qa_assistant():
    """Test the QA assistant with sample questions"""
    
    # Backend URL
    base_url = "http://localhost:8000"
    
    # Test questions
    test_questions = [
        "When was FUT established?",
        "What engineering programs does FUT offer?",
        "What are the admission requirements for FUT?",
        "Where is FUT's main campus located?",
        "What programming languages are taught in Computer Science?"
    ]
    
    print("🧪 Testing FUT QA Assistant...")
    print("=" * 50)
    
    # Check if backend is running
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            health_data = response.json()
            print(f"✅ Backend Status: {health_data['status']}")
            print(f"✅ Model Loaded: {health_data['model_loaded']}")
            print(f"✅ Model Type: {health_data['model_name']}")
            print("=" * 50)
        else:
            print("❌ Backend not responding")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Backend not running. Start it with: cd backend && python app.py")
        return
    
    # Test each question
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 Test {i}: {question}")
        
        try:
            response = requests.post(
                f"{base_url}/ask",
                json={"question": question}
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Answer: {data['answer']}")
                print(f"✅ Confidence: {data['confidence']:.2%}")
                print(f"✅ Model: {data['model_used']}")
            else:
                print(f"❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Testing complete!")
    print("\n💡 Tips:")
    print("- If you see 'pre-trained' model, your custom model isn't loaded yet")
    print("- If you see 'fine-tuned' model, your training was successful!")
    print("- Higher confidence scores indicate better answers")

if __name__ == "__main__":
    test_qa_assistant()
