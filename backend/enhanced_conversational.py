"""
Enhanced Conversational Handler for FUT QA Assistant
Uses open-source APIs and advanced conversational patterns
"""

import requests
import json
import random
from typing import Optional

class EnhancedConversationalHandler:
    def __init__(self):
        self.conversational_patterns = self._load_conversational_patterns()
        self.fut_context = self._get_fut_context()
    
    def _load_conversational_patterns(self):
        """Load conversational response patterns"""
        return {
            "greetings": [
                "Hello! I'm the FUT QA Assistant, your friendly guide to Federal University of Technology. I'm here to help you with questions about FUT's programs, campus life, and student services. How can I assist you today?",
                "Hi there! I'm the FUT QA Assistant and I'm excited to help you learn about Federal University of Technology. What would you like to know about FUT?",
                "Hey! I'm the FUT QA Assistant, your helpful companion for all things Federal University of Technology. I'm here to make your FUT journey easier. What can I help you with?"
            ],
            "how_are_you": [
                "I'm doing fantastic, thank you for asking! I'm the FUT QA Assistant and I'm excited to help you learn about Federal University of Technology. What questions do you have for me today?",
                "I'm doing great, thanks! I'm the FUT QA Assistant and I'm here to help you with any questions about Federal University of Technology. What would you like to know?",
                "I'm doing excellent, thank you! I'm the FUT QA Assistant and I'm ready to help you with information about Federal University of Technology. What can I assist you with?"
            ],
            "whats_up": [
                "Hey there! I'm doing great, thanks for asking! I'm the FUT QA Assistant and I'm here to help you with any questions about Federal University of Technology. What can I help you with today?",
                "Hey! I'm doing fantastic, thanks! I'm the FUT QA Assistant and I'm excited to help you learn about Federal University of Technology. What would you like to know?",
                "Hey there! I'm doing excellent, thanks! I'm the FUT QA Assistant and I'm ready to help you with information about Federal University of Technology. What can I assist you with?"
            ],
            "help_requests": [
                "I can help you with information about FUT's academic programs, admission requirements, campus facilities, student life, engineering courses, technology programs, and much more! I'm here to make your FUT journey easier. What specific information are you looking for?",
                "I can assist you with details about FUT's academic programs, admission requirements, campus facilities, student life, engineering courses, technology programs, and much more! I'm here to help you succeed at FUT. What would you like to know?",
                "I can provide information about FUT's academic programs, admission requirements, campus facilities, student life, engineering courses, technology programs, and much more! I'm here to make your FUT experience better. What specific information do you need?"
            ],
            "about_self": [
                "I'm the FUT QA Assistant, your friendly guide to Federal University of Technology! I'm designed to help students, prospective students, and visitors with information about FUT's academic programs, campus life, student services, and university resources. I'm excited to help you learn about FUT!",
                "I'm the FUT QA Assistant, your helpful companion for Federal University of Technology! I'm here to assist students, prospective students, and visitors with information about FUT's academic programs, campus life, student services, and university resources. I'm excited to help you discover FUT!",
                "I'm the FUT QA Assistant, your knowledgeable guide to Federal University of Technology! I'm designed to help students, prospective students, and visitors with information about FUT's academic programs, campus life, student services, and university resources. I'm excited to help you explore FUT!"
            ]
        }
    
    def _get_fut_context(self):
        """Get FUT context for conversational responses"""
        return {
            "university_name": "Federal University of Technology (FUT)",
            "focus": "technology and engineering education",
            "programs": "engineering, technology, and applied sciences",
            "services": "academic resources, course materials, and institutional information"
        }
    
    def get_conversational_response(self, question: str) -> Optional[str]:
        """Get enhanced conversational response"""
        
        question_lower = question.lower().strip()
        
        # Greeting responses
        if question_lower in ["hi", "hello", "hey"]:
            return random.choice(self.conversational_patterns["greetings"])
        
        # How are you responses
        if "how are you" in question_lower:
            return random.choice(self.conversational_patterns["how_are_you"])
        
        # What's up responses
        if "what's up" in question_lower or "whats up" in question_lower:
            return random.choice(self.conversational_patterns["whats_up"])
        
        # Help requests
        if any(phrase in question_lower for phrase in ["what can you help", "what do you do", "what can you do", "help me"]):
            return random.choice(self.conversational_patterns["help_requests"])
        
        # About yourself
        if any(phrase in question_lower for phrase in ["tell me about yourself", "who are you", "what are you"]):
            return random.choice(self.conversational_patterns["about_self"])
        
        # Casual conversation starters
        if any(phrase in question_lower for phrase in ["good morning", "good afternoon", "good evening"]):
            return f"Good {question_lower.split()[1]}! I'm the FUT QA Assistant and I'm here to help you with questions about Federal University of Technology. How can I assist you today?"
        
        # Thank you responses
        if "thank you" in question_lower or "thanks" in question_lower:
            return "You're very welcome! I'm the FUT QA Assistant and I'm here to help you with any other questions about Federal University of Technology. What else can I assist you with?"
        
        # Goodbye responses
        if any(phrase in question_lower for phrase in ["bye", "goodbye", "see you", "farewell"]):
            return "Goodbye! It was great helping you today. I'm the FUT QA Assistant and I'm always here to help with questions about Federal University of Technology. Have a wonderful day!"
        
        # Weather/small talk
        if any(phrase in question_lower for phrase in ["weather", "nice day", "beautiful day"]):
            return "I'm the FUT QA Assistant and I'm here to help you with questions about Federal University of Technology. While I can't check the weather, I can definitely help you with information about FUT's programs, campus life, and student services. What would you like to know?"
        
        # Default conversational response for other casual inputs
        if len(question_lower.split()) <= 3 and not any(academic_word in question_lower for academic_word in ["program", "course", "admission", "campus", "student", "university", "fut"]):
            return "I'm the FUT QA Assistant and I'm here to help you with questions about Federal University of Technology. I can provide information about FUT's academic programs, campus life, student services, and much more. What would you like to know about FUT?"
        
        return None
    
    def get_openai_style_response(self, question: str) -> Optional[str]:
        """Get OpenAI-style conversational response (fallback)"""
        try:
            # This would integrate with an open-source conversational API
            # For now, we'll use our enhanced patterns
            return self.get_conversational_response(question)
        except Exception as e:
            print(f"Error with conversational API: {e}")
            return self.get_conversational_response(question)

# Global instance
conversational_handler = EnhancedConversationalHandler()

def get_conversational_response(question: str) -> Optional[str]:
    """Get enhanced conversational response"""
    return conversational_handler.get_conversational_response(question)
