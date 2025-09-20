"""
Conversational response handler for FUT QA Assistant
Provides human-like responses for conversational inputs
"""

def get_conversational_response(question):
    """Get appropriate conversational response"""
    
    question_lower = question.lower().strip()
    
    # Greeting responses
    if question_lower in ["hi", "hello", "hey"]:
        return "Hello! I'm the FUT QA Assistant. I'm here to help you with questions about Federal University of Technology. How can I assist you today?"
    
    # How are you responses
    if "how are you" in question_lower:
        return "I'm doing fantastic, thank you for asking! I'm the FUT QA Assistant and I'm excited to help you learn about Federal University of Technology. What questions do you have for me today?"
    
    # What's up responses
    if "what's up" in question_lower or "whats up" in question_lower:
        return "Hey there! I'm doing great, thanks for asking! I'm the FUT QA Assistant and I'm here to help you with any questions about Federal University of Technology. What can I help you with today?"
    
    # Help responses
    if "what can you help" in question_lower or "what do you do" in question_lower:
        return "I can help you with information about FUT's academic programs, admission requirements, campus facilities, student life, engineering courses, technology programs, and much more! I'm here to make your FUT journey easier. What specific information are you looking for?"
    
    # About yourself responses
    if "tell me about yourself" in question_lower or "who are you" in question_lower:
        return "I'm the FUT QA Assistant, your friendly guide to Federal University of Technology! I'm designed to help students, prospective students, and visitors with information about FUT's academic programs, campus life, student services, and university resources. I'm excited to help you learn about FUT!"
    
    # Default conversational response
    return None
