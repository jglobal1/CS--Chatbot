#!/usr/bin/env python3
"""
Test script to verify Johnson's Training Model name is displayed correctly
"""

import requests
import json

def test_model_name_display():
    """Test that all responses show Johnson's Training Model"""
    
    print("🧪 Testing Johnson's Training Model Name Display")
    print("=" * 60)
    
    # Test questions that should show Johnson's Training Model
    test_questions = [
        "What is COS101?",
        "Who teaches Computer Science?",
        "What is artificial intelligence?",
        "Tell me about FUT",
        "What are career paths in Computer Science?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Question: {question}")
        
        try:
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
                print(f"   💬 Answer: {answer[:100]}...")
                
                # Check if it shows Johnson's Training Model
                if "Johnson's Training Model" in model_used:
                    print("   ✅ Correctly showing Johnson's Training Model")
                else:
                    print(f"   ⚠️  Showing: {model_used} (should be Johnson's Training Model)")
                    
            else:
                print(f"   ❌ Error: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            print(f"   ❌ Connection Error: Make sure the backend is running on localhost:8000")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
    
    print("\n" + "=" * 60)
    print("✅ Model name testing completed!")

def test_health_endpoint():
    """Test the health endpoint shows correct model name"""
    
    print("\n🏥 Testing Health Endpoint")
    print("=" * 40)
    
    try:
        response = requests.get("http://localhost:8000/health", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            model_name = data.get('model_name', 'Unknown')
            status = data.get('status', 'Unknown')
            model_loaded = data.get('model_loaded', False)
            
            print(f"   ✅ Status: {status}")
            print(f"   ✅ Model Loaded: {model_loaded}")
            print(f"   ✅ Model Name: {model_name}")
            
            if "Johnson's Training Model" in model_name:
                print("   ✅ Health endpoint shows Johnson's Training Model")
            else:
                print(f"   ⚠️  Health endpoint shows: {model_name}")
                
        else:
            print(f"   ❌ Error: {response.status_code} - {response.text}")
            
    except requests.exceptions.ConnectionError:
        print(f"   ❌ Connection Error: Make sure the backend is running on localhost:8000")
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
    
    print("\n" + "=" * 40)
    print("✅ Health endpoint testing completed!")

if __name__ == "__main__":
    print("🚀 Johnson's Training Model Name Test")
    print("Testing that all responses show 'Johnson's Training Model'")
    print("=" * 70)
    
    # Test main endpoint responses
    test_model_name_display()
    
    # Test health endpoint
    test_health_endpoint()
    
    print("\n🎯 Expected Results:")
    print("- All responses should show 'Johnson's Training Model'")
    print("- No more 'external_api', 'groq_pdf_enhanced', etc.")
    print("- Professional presentation for your project")
    print("\n💡 Perfect for GitHub and deployment!")
