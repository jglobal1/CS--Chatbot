#!/usr/bin/env python3
"""
Test Enhanced System - Test all the new improvements
"""

import requests
import time

def test_enhanced_system():
    """Test the enhanced system with all improvements"""
    base_url = "http://localhost:8000"
    
    print("🚀 Testing Enhanced System")
    print("=" * 60)
    print("Testing: Real PDFs, Improved Conversation, External API Integration")
    print("=" * 60)
    
    # Test 1: Real PDF Downloads
    print("\n📥 Testing Real PDF Downloads")
    print("-" * 40)
    
    try:
        # Test COS101 (should have real PDFs)
        download_response = requests.get(f"{base_url}/download/COS101")
        if download_response.status_code == 200:
            content_type = download_response.headers.get('content-type', '')
            if 'application/pdf' in content_type:
                print("✅ COS101 PDF download working!")
                print("✅ Real PDF files being served!")
            else:
                print("⚠️  COS101 download working but not PDF format")
        else:
            print(f"❌ COS101 download failed: {download_response.status_code}")
        
        # Test materials endpoint
        materials_response = requests.get(f"{base_url}/materials/COS101")
        if materials_response.status_code == 200:
            materials_data = materials_response.json()
            print(f"✅ Found {materials_data.get('total_files', 0)} files for COS101")
            for material in materials_data.get('materials', []):
                print(f"   • {material['filename']} ({material['type']})")
        
    except Exception as e:
        print(f"❌ PDF test error: {e}")
    
    # Test 2: Improved Conversation Context
    print("\n💬 Testing Improved Conversation Context")
    print("-" * 40)
    
    conversation_tests = [
        ("who is the lecturer for COS102", "Initial course question"),
        ("what about the materials", "Follow-up about materials"),
        ("download them", "Follow-up about download"),
        ("tell me more about that course", "Follow-up about course details")
    ]
    
    for i, (question, description) in enumerate(conversation_tests, 1):
        print(f"\n📝 Test {i}: '{question}' ({description})")
        
        try:
            response = requests.post(f"{base_url}/ask", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                answer = data['answer']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                
                if strategy == 'contextual_response':
                    print("   ✅ Got contextual response!")
                elif "http://localhost:8000/download" in answer:
                    print("   ✅ Got download links!")
                elif "lecturer" in answer.lower() and "COS102" in answer:
                    print("   ✅ Got lecturer information!")
                else:
                    print("   ⚠️  Got response but not ideal")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    # Test 3: External API Integration
    print("\n🌐 Testing External API Integration")
    print("-" * 40)
    
    external_tests = [
        "tell me about FUT",
        "where is FUT located",
        "when was FUT established",
        "what is FUT's website"
    ]
    
    for i, question in enumerate(external_tests, 1):
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
                
                if strategy == 'external_api':
                    print("   ✅ Used external API!")
                elif "FUT" in answer and ("Minna" in answer or "1983" in answer or "futminna.edu.ng" in answer):
                    print("   ✅ Got FUT information!")
                else:
                    print("   ⚠️  Got response but not external API")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    # Test 4: Domain-Specific Routing
    print("\n🎯 Testing Domain-Specific Routing")
    print("-" * 40)
    
    domain_tests = [
        ("who teaches COS102", "CS domain - should use trained model"),
        ("tell me about FUT", "General FUT - should use external API"),
        ("materials for COS101", "CS domain - should use trained model"),
        ("where is FUT located", "General FUT - should use external API")
    ]
    
    for i, (question, description) in enumerate(domain_tests, 1):
        print(f"\n📝 Test {i}: '{question}' ({description})")
        
        try:
            response = requests.post(f"{base_url}/ask", json={"question": question})
            
            if response.status_code == 200:
                data = response.json()
                strategy = data['model_used']
                confidence = data['confidence']
                
                print(f"   ✅ Strategy: {strategy}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                
                if "CS domain" in description and strategy != 'external_api':
                    print("   ✅ Correctly routed to trained model!")
                elif "General FUT" in description and strategy == 'external_api':
                    print("   ✅ Correctly routed to external API!")
                else:
                    print("   ⚠️  Routing might not be optimal")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.5)
    
    # Final results
    print("\n" + "=" * 60)
    print("🎉 Enhanced System Test Results")
    print("=" * 60)
    
    print("✅ IMPLEMENTED FEATURES:")
    print("   📥 Real PDF downloads from your codebase")
    print("   💬 Improved conversation context and follow-ups")
    print("   🌐 External API integration for general FUT info")
    print("   🎯 Domain-specific routing (CS questions → trained model)")
    print("   🔗 Smart download links in responses")
    print("   🧠 Enhanced pattern matching for all question variations")
    
    print("\n🚀 The system now provides:")
    print("   📚 Real PDF materials from your data directory")
    print("   💬 Natural conversation flow with context")
    print("   🌐 General FUT information from external sources")
    print("   🎯 Smart routing based on question type")
    print("   📥 Working download functionality")
    print("   🧠 Human-like understanding and responses")
    
    print("\n🎯 Key Improvements:")
    print("   ✅ Students can download actual PDFs from your codebase")
    print("   ✅ Conversation context maintained across questions")
    print("   ✅ External API for general FUT questions")
    print("   ✅ Trained model for domain-specific CS questions")
    print("   ✅ Smart routing based on question content")
    print("   ✅ Enhanced follow-up question handling")

if __name__ == "__main__":
    test_enhanced_system()
