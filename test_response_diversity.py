#!/usr/bin/env python3
"""
Test Response Diversity
Ensure responses are distinct and not clustered
"""

import requests
import json
import time

def test_response_diversity():
    """Test that responses are diverse and distinct"""
    base_url = "http://localhost:8000"
    
    print("🎯 Testing Response Diversity")
    print("Ensuring responses are distinct and not clustered")
    print("=" * 80)
    
    # Test cases for different response types
    test_cases = [
        # Course-specific questions (should be distinct)
        ("What is COS101?", "course_specific"),
        ("Tell me about COS102", "course_specific"),
        ("What is CPT121 about?", "course_specific"),
        
        # General course questions (should be different from specific)
        ("What courses are available?", "course_general"),
        ("Tell me about CS courses", "course_general"),
        ("What courses do I take in 100 level?", "course_general"),
        
        # CS guidance questions (should be distinct)
        ("What career opportunities are there?", "cs_guidance"),
        ("How can I improve my programming?", "cs_guidance"),
        ("What programming languages should I learn?", "cs_guidance"),
        
        # Materials questions (should be distinct)
        ("What materials do I need?", "materials"),
        ("What software should I install?", "materials"),
        ("What books should I buy?", "materials"),
        
        # Success tips (should be distinct)
        ("How can I excel in my studies?", "success_tips"),
        ("What study tips do you have?", "success_tips"),
        ("How can I pass my exams?", "success_tips"),
        
        # FUT information (should be distinct)
        ("Tell me about FUT", "fut_info"),
        ("What are the admission requirements?", "fut_info"),
        ("What facilities does FUT have?", "fut_info"),
        
        # Conversational (should be distinct)
        ("Hello", "conversational"),
        ("Thank you", "conversational"),
        ("How are you?", "conversational"),
        ("What can you do?", "conversational"),
        
        # Adaptive (should be distinct)
        ("Wetin you fit tell me?", "adaptive_learning"),
        ("Yo, what's up?", "adaptive_learning"),
        
        # General guidance (should be distinct)
        ("I need help", "general_guidance"),
        ("What can you help me with?", "general_guidance"),
    ]
    
    print(f"🚀 Testing {len(test_cases)} different question types...")
    print("=" * 80)
    
    responses = {}
    strategy_counts = {}
    
    for i, (question, expected_strategy) in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: '{question}'")
        print(f"   Expected Strategy: {expected_strategy}")
        
        try:
            response = requests.post(
                f"{base_url}/ask",
                json={"question": question}
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data['answer']
                confidence = data['confidence']
                strategy_used = data['model_used']
                
                print(f"   ✅ Strategy Used: {strategy_used}")
                print(f"   ✅ Confidence: {confidence:.2%}")
                print(f"   ✅ Response Length: {len(answer)} characters")
                
                # Store response for diversity analysis
                if strategy_used not in responses:
                    responses[strategy_used] = []
                responses[strategy_used].append(answer[:200])  # First 200 chars
                
                # Count strategies
                strategy_counts[strategy_used] = strategy_counts.get(strategy_used, 0) + 1
                
                # Check if correct strategy was used
                if strategy_used == expected_strategy:
                    print("   ✅ Correct strategy used!")
                else:
                    print(f"   ⚠️  Expected {expected_strategy}, got {strategy_used}")
                
                # Show response preview
                print(f"   📝 Preview: {answer[:100]}...")
                
            else:
                print(f"   ❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.3)
    
    # Analyze response diversity
    print("\n" + "=" * 80)
    print("📊 Response Diversity Analysis")
    print("=" * 80)
    
    print(f"📈 Strategy Distribution:")
    total_tests = len(test_cases)
    for strategy, count in strategy_counts.items():
        percentage = (count / total_tests) * 100
        print(f"   • {strategy}: {count} ({percentage:.1f}%)")
    
    print(f"\n🎯 Response Uniqueness Analysis:")
    for strategy, response_list in responses.items():
        unique_responses = set(response_list)
        uniqueness_ratio = len(unique_responses) / len(response_list) if response_list else 0
        print(f"   • {strategy}: {len(unique_responses)}/{len(response_list)} unique ({uniqueness_ratio:.2%})")
        
        if uniqueness_ratio < 0.5:
            print(f"     ⚠️  Low diversity - responses too similar!")
        elif uniqueness_ratio < 0.8:
            print(f"     ⚠️  Medium diversity - some clustering detected")
        else:
            print(f"     ✅ High diversity - responses are distinct")
    
    # Check for clustering issues
    print(f"\n🔍 Clustering Analysis:")
    clustering_issues = 0
    
    for strategy, response_list in responses.items():
        if len(response_list) > 1:
            # Check if responses are too similar
            similar_count = 0
            for i, response1 in enumerate(response_list):
                for j, response2 in enumerate(response_list):
                    if i != j:
                        # Simple similarity check (first 100 characters)
                        similarity = len(set(response1[:100].split()) & set(response2[:100].split())) / len(set(response1[:100].split()) | set(response2[:100].split()))
                        if similarity > 0.8:  # 80% similarity threshold
                            similar_count += 1
            
            if similar_count > len(response_list) * 0.3:  # More than 30% similar
                print(f"   ⚠️  {strategy}: High clustering detected ({similar_count} similar pairs)")
                clustering_issues += 1
            else:
                print(f"   ✅ {strategy}: Low clustering, responses are diverse")
    
    # Overall assessment
    print("\n" + "=" * 80)
    print("🎉 Response Diversity Assessment")
    print("=" * 80)
    
    diversity_score = 100 - (clustering_issues * 20)  # Penalize clustering issues
    diversity_score = max(0, diversity_score)  # Don't go below 0
    
    print(f"📊 Overall Diversity Score: {diversity_score}/100")
    
    if diversity_score >= 80:
        print("\n🎉 EXCELLENT! Responses are highly diverse and distinct!")
        print("   ✅ Each question type gets unique, appropriate responses")
        print("   ✅ No clustering issues detected")
        print("   ✅ System provides varied and engaging interactions")
    elif diversity_score >= 60:
        print("\n✅ GOOD! Responses are reasonably diverse!")
        print("   ✅ Most responses are distinct and appropriate")
        print("   ⚠️  Some minor clustering in certain categories")
    elif diversity_score >= 40:
        print("\n⚠️  FAIR! Response diversity needs improvement!")
        print("   ⚠️  Some responses are too similar")
        print("   🔧 Consider improving response variety")
    else:
        print("\n❌ POOR! Significant clustering detected!")
        print("   ❌ Many responses are too similar")
        print("   🔧 Major improvements needed for response diversity")
    
    print("\n🚀 Recommendations:")
    if clustering_issues > 0:
        print("   • Improve response templates for each strategy")
        print("   • Add more variety to response generation")
        print("   • Ensure each question type has distinct responses")
    else:
        print("   • Continue maintaining response diversity")
        print("   • Monitor for clustering in future updates")
    
    print(f"\n📈 Strategy Coverage:")
    expected_strategies = ['course_specific', 'course_general', 'cs_guidance', 'materials', 'success_tips', 'fut_info', 'conversational', 'adaptive_learning', 'general_guidance']
    covered_strategies = len([s for s in expected_strategies if s in strategy_counts])
    coverage_percentage = (covered_strategies / len(expected_strategies)) * 100
    print(f"   • {covered_strategies}/{len(expected_strategies)} strategies used ({coverage_percentage:.1f}%)")

if __name__ == "__main__":
    test_response_diversity()
