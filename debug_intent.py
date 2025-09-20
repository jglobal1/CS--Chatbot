#!/usr/bin/env python3
"""
Debug Intent Analysis
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from unified_intelligence import UnifiedIntelligence

def debug_intent_analysis():
    """Debug the intent analysis to see what's happening"""
    print("🔍 Debugging Intent Analysis")
    print("=" * 50)
    
    # Initialize the system
    intelligence = UnifiedIntelligence()
    
    # Test questions that should be understood
    test_questions = [
        "What is computer science about?",
        "Who teaches programming?",
        "I need help with physics",
        "What about statistics?",
        "Tell me about hardware courses",
        "What can I do after graduation?",
        "How do I study better?",
        "What books do I need?",
        "Hello, I'm new here",
        "Thanks for the help"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 Question {i}: '{question}'")
        
        try:
            # Analyze the question
            analysis = intelligence.analyze_question_intelligence(question)
            
            print(f"   🎯 Type: {analysis.get('type', 'unknown')}")
            print(f"   🎯 Priority: {analysis.get('response_priority', [])}")
            print(f"   🎯 Confidence: {analysis.get('confidence', 0):.2%}")
            print(f"   🎯 Context Clues: {analysis.get('context_clues', [])}")
            
            # Try to get a response
            response = intelligence.get_unified_response(question)
            print(f"   ✅ Strategy: {response.get('model_used', 'unknown')}")
            print(f"   ✅ Confidence: {response.get('confidence', 0):.2%}")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    debug_intent_analysis()
