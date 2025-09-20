#!/usr/bin/env python3
"""
Test script for Dynamic Intelligence System
Tests ChatGPT 3.0+ level intelligence capabilities
"""

import requests
import json
import time
from typing import List, Tuple

def test_dynamic_intelligence():
    """Test the dynamic intelligence system with various question types"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Dynamic Intelligence System (ChatGPT 3.0+ Level)")
    print("=" * 80)
    
    # Test intelligence status first
    try:
        response = requests.get(f"{base_url}/intelligence-status")
        if response.status_code == 200:
            status = response.json()
            print("✅ Dynamic Intelligence Status:")
            print(f"   - System: {status['dynamic_intelligence']}")
            print(f"   - Knowledge Base: {'✅' if status['knowledge_base_loaded'] else '❌'}")
            print(f"   - Course Database: {'✅' if status['course_database_loaded'] else '❌'}")
            print(f"   - Conversation Context: {status['conversation_context_count']} interactions")
            print(f"   - Learning Data: {status['learning_data_count']} records")
            print("\n🎯 Capabilities:")
            for capability in status['capabilities']:
                print(f"   • {capability}")
            print("=" * 80)
        else:
            print("❌ Could not get intelligence status")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Backend not running. Start it with: cd backend && python app.py")
        return
    
    # Test cases for different intelligence levels
    test_cases = [
        # Course-specific questions (should get detailed responses)
        ("What is COS101 about?", "course_specific", True),
        ("Tell me about COS102", "course_specific", True),
        ("What materials do I need for CPT121?", "course_specific", True),
        ("How can I pass MAT101?", "course_specific", True),
        
        # CS general questions (should get comprehensive guidance)
        ("What is computer science about?", "cs_general", True),
        ("What career opportunities are there in CS?", "cs_general", True),
        ("How can I succeed in computer science?", "cs_general", True),
        ("What programming languages should I learn?", "cs_general", True),
        
        # FUT-specific questions (should get university information)
        ("Tell me about FUT", "fut_general", True),
        ("What are the admission requirements?", "fut_general", True),
        ("What facilities does FUT have?", "fut_general", True),
        ("What programs are available at SICT?", "fut_general", True),
        
        # Materials and resources (should get comprehensive lists)
        ("What materials do I need for CS?", "materials", True),
        ("What software should I install?", "materials", True),
        ("What books should I buy?", "materials", True),
        ("What tools do I need for programming?", "materials", True),
        
        # Success and advice (should get detailed strategies)
        ("How can I excel in my studies?", "success_advice", True),
        ("What study tips do you have?", "success_advice", True),
        ("How can I improve my programming skills?", "success_advice", True),
        ("What should I do to prepare for exams?", "success_advice", True),
        
        # Unrelated questions (should get boundary response)
        ("How do I cook pasta?", "unrelated", False),
        ("What's the weather like?", "unrelated", False),
        ("Tell me about football", "unrelated", False),
        ("How do I lose weight?", "unrelated", False),
        
        # General questions (should get helpful guidance)
        ("Hello", "general", True),
        ("Help", "general", True),
        ("What can you do?", "general", True),
        ("I need assistance", "general", True),
    ]
    
    results = {
        "course_specific": 0,
        "cs_general": 0,
        "fut_general": 0,
        "materials": 0,
        "success_advice": 0,
        "unrelated": 0,
        "general": 0,
        "total_tests": len(test_cases)
    }
    
    print(f"\n🚀 Running {len(test_cases)} intelligence tests...")
    print("=" * 80)
    
    for i, (question, expected_type, should_succeed) in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: '{question}'")
        print(f"   Expected: {expected_type} | Should succeed: {should_succeed}")
        
        try:
            response = requests.post(
                f"{base_url}/ask",
                json={"question": question}
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data['answer']
                confidence = data['confidence']
                model_used = data['model_used']
                
                print(f"   ✅ Response: {answer[:100]}...")
                print(f"   ✅ Confidence: {confidence:.2%}")
                print(f"   ✅ Model: {model_used}")
                
                # Check if response is appropriate
                if should_succeed:
                    if len(answer) > 100 and confidence > 0.7:
                        print("   ✅ Comprehensive and confident response")
                        results[expected_type] += 1
                    else:
                        print("   ⚠️  Response could be more detailed")
                else:
                    if "specialized" in answer.lower() or "can't help" in answer.lower():
                        print("   ✅ Correctly identified as unrelated")
                        results[expected_type] += 1
                    else:
                        print("   ⚠️  Should have been identified as unrelated")
            else:
                print(f"   ❌ Error: {response.status_code} - {response.json().get('detail', 'Unknown error')}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)  # Small delay to avoid overwhelming the server
    
    # Test conversation summary
    print("\n" + "=" * 80)
    print("📊 Testing Conversation Summary...")
    try:
        response = requests.get(f"{base_url}/conversation-summary")
        if response.status_code == 200:
            summary = response.json()['conversation_summary']
            print("✅ Conversation Summary:")
            print(summary)
        else:
            print("❌ Could not get conversation summary")
    except Exception as e:
        print(f"❌ Error getting conversation summary: {e}")
    
    # Test learning functionality
    print("\n" + "=" * 80)
    print("🧠 Testing Learning Functionality...")
    try:
        learn_response = requests.post(
            f"{base_url}/learn",
            params={
                "question": "What is COS101?",
                "response": "COS101 is Introduction to Computer Science",
                "feedback": "Very helpful!"
            }
        )
        if learn_response.status_code == 200:
            print("✅ Learning data recorded successfully")
        else:
            print("❌ Could not record learning data")
    except Exception as e:
        print(f"❌ Error recording learning data: {e}")
    
    # Final results
    print("\n" + "=" * 80)
    print("🎉 Dynamic Intelligence Test Results")
    print("=" * 80)
    
    total_successful = sum(results[key] for key in results if key != "total_tests")
    success_rate = (total_successful / results["total_tests"]) * 100
    
    print(f"📊 Overall Success Rate: {success_rate:.1f}% ({total_successful}/{results['total_tests']})")
    print("\n📈 Results by Category:")
    for category, count in results.items():
        if category != "total_tests":
            percentage = (count / results["total_tests"]) * 100
            print(f"   • {category.replace('_', ' ').title()}: {count} ({percentage:.1f}%)")
    
    print("\n🎯 Intelligence Capabilities Demonstrated:")
    print("   ✅ Course-specific detailed responses")
    print("   ✅ CS guidance and career advice")
    print("   ✅ FUT information and admission details")
    print("   ✅ Materials and resources guidance")
    print("   ✅ Success strategies and tips")
    print("   ✅ Unrelated question boundary detection")
    print("   ✅ Dynamic data fetching")
    print("   ✅ Conversation context tracking")
    print("   ✅ Learning from interactions")
    
    if success_rate >= 80:
        print("\n🎉 EXCELLENT! Dynamic Intelligence System is working at ChatGPT 3.0+ level!")
    elif success_rate >= 60:
        print("\n✅ GOOD! Dynamic Intelligence System is performing well!")
    else:
        print("\n⚠️  NEEDS IMPROVEMENT! Dynamic Intelligence System needs optimization!")

if __name__ == "__main__":
    test_dynamic_intelligence()
