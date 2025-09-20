#!/usr/bin/env python3
"""
Simple Intent Test - Test the intent analysis logic directly
"""

def test_intent_patterns():
    """Test the intent analysis patterns directly"""
    print("🧠 Testing Intent Analysis Patterns")
    print("=" * 60)
    
    # Test questions
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
    
    # Course patterns (from the system)
    course_patterns = {
        'COS101': ['cos101', 'cos 101', 'introduction to computer science', 'computer science intro', 'cs intro', 'computer science basics'],
        'COS102': ['cos102', 'cos 102', 'introduction to programming', 'python', 'programming intro', 'problem solving', 'programming basics'],
        'PHY101': ['phy101', 'phy 101', 'physics 1', 'general physics', 'physics first', 'physics basics'],
        'PHY102': ['phy102', 'phy 102', 'physics 2', 'advanced physics', 'physics second'],
        'CST111': ['cst111', 'cst 111', 'communication', 'english', 'communication skills', 'english skills'],
        'GST112': ['gst112', 'gst 112', 'nigerian culture', 'culture', 'nigerian people', 'cultural studies'],
        'STA111': ['sta111', 'sta 111', 'statistics', 'descriptive statistics', 'stats', 'statistical methods'],
        'CPT121': ['cpt121', 'cpt 121', 'computer hardware', 'hardware intro', 'hardware basics', 'computer components'],
        'CPT122': ['cpt122', 'cpt 122', 'hardware systems', 'hardware maintenance', 'advanced hardware', 'computer maintenance'],
        'FTM-CPT111': ['ftm-cpt111', 'ftm cpt111', 'probability', 'math for cs', 'probability theory', 'mathematical probability'],
        'FTM-CPT112': ['ftm-cpt112', 'ftm cpt112', 'web development', 'frontend', 'html css javascript', 'web programming'],
        'FTM-CPT192': ['ftm-cpt192', 'ftm cpt192', 'computer hardware systems', 'hardware systems', 'computer systems'],
        'MAT101': ['mat101', 'mat 101', 'mathematics for cs', 'math for computer science', 'discrete mathematics']
    }
    
    # Intent patterns
    intent_patterns = {
        'course_general': ['what courses', 'list courses', 'show courses', 'available courses', 'all courses', 'courses available', 'courses do i need', 'courses should i take'],
        'course_specific': ['who teaches', 'who is the lecturer', 'lecturer for', 'teacher for', 'instructor for', 'who handles', 'who takes', 'programming course', 'physics course', 'hardware course'],
        'cs_guidance': ['career', 'job opportunities', 'what can i do', 'future career', 'work after graduation', 'employment', 'career paths', 'job prospects', 'work in tech', 'tech jobs'],
        'materials': ['study materials', 'books', 'resources', 'what do i need', 'materials for', 'study guide', 'textbooks', 'learning materials', 'books do i need', 'materials do i need'],
        'success_tips': ['how to study', 'study tips', 'how to pass', 'study strategy', 'academic success', 'excel in', 'study methods', 'learning tips', 'study better', 'struggling with', 'succeed in studies'],
        'conversational': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'greetings', 'new here', 'new student', 'thank you', 'thanks', 'appreciate', 'grateful', 'thank you so much']
    }
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 Question {i}: '{question}'")
        question_lower = question.lower()
        
        # Check course patterns
        detected_courses = []
        for course_code, patterns in course_patterns.items():
            if any(pattern in question_lower for pattern in patterns):
                detected_courses.append(course_code)
        
        # Check intent patterns
        detected_intent = None
        for intent, patterns in intent_patterns.items():
            if any(pattern in question_lower for pattern in patterns):
                detected_intent = intent
                break
        
        # Check subject mentions
        subject_mentions = []
        if 'computer science' in question_lower or 'cs' in question_lower:
            subject_mentions.append('computer science')
        if 'programming' in question_lower or 'python' in question_lower:
            subject_mentions.append('programming')
        if 'physics' in question_lower:
            subject_mentions.append('physics')
        if 'statistics' in question_lower or 'stats' in question_lower:
            subject_mentions.append('statistics')
        if 'hardware' in question_lower:
            subject_mentions.append('hardware')
        
        print(f"   🎯 Detected Courses: {detected_courses}")
        print(f"   🎯 Detected Intent: {detected_intent}")
        print(f"   🎯 Subject Mentions: {subject_mentions}")
        
        # Determine expected response
        if detected_courses:
            expected = "course_specific"
        elif detected_intent:
            expected = detected_intent
        elif subject_mentions:
            expected = "course_specific" if any(subject in ['programming', 'physics', 'statistics', 'hardware'] for subject in subject_mentions) else "course_general"
        else:
            expected = "general_guidance"
        
        print(f"   ✅ Expected Response: {expected}")
        
        # Check if this matches what we expect
        if expected in ['course_specific', 'course_general', 'cs_guidance', 'materials', 'success_tips', 'conversational']:
            print("   ✅ Should work correctly")
        else:
            print("   ⚠️  Might fall back to general")

if __name__ == "__main__":
    test_intent_patterns()
