"""
Adaptive Learning System for FUT QA Assistant
Learns from user interactions and improves over time
"""

import json
import os
import re
from datetime import datetime
from typing import Dict, List, Optional
import requests

class AdaptiveLearningSystem:
    def __init__(self):
        self.learning_data_file = "learning_data.json"
        self.conversation_history = []
        self.load_learning_data()
    
    def load_learning_data(self):
        """Load existing learning data"""
        if os.path.exists(self.learning_data_file):
            with open(self.learning_data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.conversation_history = data.get('conversations', [])
        else:
            self.conversation_history = []
    
    def save_learning_data(self):
        """Save learning data"""
        data = {
            'conversations': self.conversation_history,
            'last_updated': datetime.now().isoformat()
        }
        with open(self.learning_data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    
    def detect_language_style(self, question: str) -> str:
        """Detect the language style of the question"""
        question_lower = question.lower()
        
        # Nigerian Pidgin patterns
        pidgin_patterns = [
            'naija', 'wahala', 'sha', 'o', 'abi', 'se', 'make', 'dey', 'don', 'go',
            'come', 'wan', 'fit', 'no', 'e', 'am', 'dem', 'we', 'una', 'una own'
        ]
        
        # Casual/Informal patterns
        casual_patterns = [
            'yo', 'hey', 'sup', 'whats', 'gonna', 'wanna', 'gotta', 'kinda', 'sorta'
        ]
        
        # Formal patterns
        formal_patterns = [
            'please', 'could you', 'would you', 'kindly', 'may i', 'i would like'
        ]
        
        pidgin_score = sum(1 for pattern in pidgin_patterns if pattern in question_lower)
        casual_score = sum(1 for pattern in casual_patterns if pattern in question_lower)
        formal_score = sum(1 for pattern in formal_patterns if pattern in question_lower)
        
        if pidgin_score > 2:
            return 'pidgin'
        elif casual_score > 0:
            return 'casual'
        elif formal_score > 0:
            return 'formal'
        else:
            return 'neutral'
    
    def get_adaptive_response(self, question: str, context: str = "") -> str:
        """Get adaptive response based on learning and language style"""
        language_style = self.detect_language_style(question)
        
        # Store conversation for learning
        self.conversation_history.append({
            'question': question,
            'context': context,
            'language_style': language_style,
            'timestamp': datetime.now().isoformat()
        })
        
        # Get response based on language style
        if language_style == 'pidgin':
            return self.get_pidgin_response(question, context)
        elif language_style == 'casual':
            return self.get_casual_response(question, context)
        elif language_style == 'formal':
            return self.get_formal_response(question, context)
        else:
            return self.get_neutral_response(question, context)
    
    def get_pidgin_response(self, question: str, context: str) -> str:
        """Get Nigerian Pidgin response"""
        responses = [
            "Wetin you wan know about FUT? I fit help you with information about FUT programs, courses, and everything wey concern FUT. Wetin you dey look for?",
            "Hello! I be FUT QA Assistant. I fit help you with any question about Federal University of Technology. Wetin you wan know?",
            "How far? I dey here to help you with FUT information. Wetin you dey look for about FUT?",
            "I be FUT Assistant and I fit help you with any question about FUT. Wetin you wan know about FUT programs or courses?",
            "How you dey? I be FUT QA Assistant and I dey here to help you with FUT information. Wetin you dey look for?"
        ]
        
        # Check if asking about course codes
        if any(phrase in question.lower() for phrase in ['course code', 'course codes', 'code', 'codes']):
            return "Ah, you wan know course codes for FUT? I fit help you with that! FUT get different course codes for different programs. Wetin specific course you dey look for? I fit give you the codes for Computer Science, Engineering, and other programs wey FUT get."
        
        return responses[0]  # Default response
    
    def get_casual_response(self, question: str, context: str) -> str:
        """Get casual response"""
        responses = [
            "Hey! I'm the FUT QA Assistant and I'm here to help you with any questions about Federal University of Technology. What's up?",
            "Yo! I'm the FUT QA Assistant. I can help you with info about FUT programs, courses, and everything FUT-related. What do you need?",
            "Hey there! I'm the FUT QA Assistant and I'm excited to help you learn about Federal University of Technology. What's on your mind?",
            "What's up! I'm the FUT QA Assistant and I'm here to help you with any questions about FUT. What can I do for you?",
            "Hey! I'm the FUT QA Assistant and I'm ready to help you with FUT information. What do you want to know?"
        ]
        
        # Check if asking about course codes
        if any(phrase in question.lower() for phrase in ['course code', 'course codes', 'code', 'codes']):
            return "Hey! You want to know about course codes? I can help you with that! FUT has different course codes for various programs. What specific courses are you looking for? I can give you the codes for Computer Science, Engineering, and other programs at FUT."
        
        return responses[0]  # Default response
    
    def get_formal_response(self, question: str, context: str) -> str:
        """Get formal response"""
        responses = [
            "Good day! I am the FUT QA Assistant, and I am here to assist you with any questions about Federal University of Technology. How may I help you today?",
            "Hello! I am the FUT QA Assistant, and I am pleased to help you with information about Federal University of Technology. What would you like to know?",
            "Good day! I am the FUT QA Assistant, and I am here to provide you with information about Federal University of Technology. How can I assist you?",
            "Hello! I am the FUT QA Assistant, and I am ready to help you with any questions about Federal University of Technology. What information do you need?",
            "Good day! I am the FUT QA Assistant, and I am here to assist you with information about Federal University of Technology. How may I be of service?"
        ]
        
        # Check if asking about course codes
        if any(phrase in question.lower() for phrase in ['course code', 'course codes', 'code', 'codes']):
            return "Certainly! I can provide you with information about course codes at Federal University of Technology. FUT offers various course codes for different programs. What specific courses are you interested in? I can provide you with the codes for Computer Science, Engineering, and other programs offered at FUT."
        
        return responses[0]  # Default response
    
    def get_neutral_response(self, question: str, context: str) -> str:
        """Get neutral response"""
        responses = [
            "Hello! I'm the FUT QA Assistant and I'm here to help you with questions about Federal University of Technology. How can I assist you today?",
            "Hi there! I'm the FUT QA Assistant and I'm ready to help you with information about Federal University of Technology. What would you like to know?",
            "Hello! I'm the FUT QA Assistant and I'm here to help you with any questions about FUT. What can I help you with?",
            "Hi! I'm the FUT QA Assistant and I'm excited to help you learn about Federal University of Technology. What questions do you have?",
            "Hello! I'm the FUT QA Assistant and I'm here to help you with information about Federal University of Technology. What do you need to know?"
        ]
        
        # Check if asking about course codes
        if any(phrase in question.lower() for phrase in ['course code', 'course codes', 'code', 'codes']):
            return "Hello! You're asking about course codes? I can help you with that! Federal University of Technology has various course codes for different programs. What specific courses are you looking for? I can provide you with the codes for Computer Science, Engineering, and other programs at FUT."
        
        return responses[0]  # Default response
    
    def learn_from_interaction(self, question: str, response: str, user_feedback: str = ""):
        """Learn from user interactions"""
        # This would be called after each interaction to improve responses
        learning_entry = {
            'question': question,
            'response': response,
            'user_feedback': user_feedback,
            'timestamp': datetime.now().isoformat()
        }
        
        # Store for future learning
        self.conversation_history.append(learning_entry)
        
        # Save learning data
        self.save_learning_data()
    
    def get_contextual_response(self, question: str, previous_questions: List[str] = []) -> str:
        """Get response based on conversation context"""
        # Analyze previous questions to provide contextual responses
        if previous_questions:
            # If user is asking follow-up questions, provide more specific responses
            if any('course' in q.lower() for q in previous_questions):
                if 'code' in question.lower():
                    return "Based on our conversation about courses, here are the course codes you might be looking for..."
        
        return self.get_adaptive_response(question)

# Global instance
adaptive_learning = AdaptiveLearningSystem()

def get_adaptive_response(question: str, context: str = "") -> str:
    """Get adaptive response based on learning and language style"""
    return adaptive_learning.get_adaptive_response(question, context)
