"""
Intelligent Computer Science Assistant for FUT
Smart responses based on trained data and external sources
"""

import json
import os
import re
from typing import Dict, List, Optional
from datetime import datetime
import requests

class IntelligentCSAssistant:
    def __init__(self):
        self.cs_knowledge_base = self._load_cs_knowledge()
        self.course_materials = self._load_course_materials()
        self.success_tips = self._load_success_tips()
        self.external_sources = self._load_external_sources()
    
    def _load_cs_knowledge(self) -> Dict:
        """Load comprehensive CS knowledge base"""
        return {
            '100_level': {
                'courses': {
                    'COS101': {
                        'name': 'Introduction to Computer Science',
                        'description': 'Fundamental concepts of computer science, history, and applications',
                        'materials': ['Introduction to Computer Science textbook', 'Programming basics guide', 'Computer fundamentals notes'],
                        'success_tips': ['Understand basic concepts', 'Practice programming fundamentals', 'Read recommended textbooks']
                    },
                    'COS102': {
                        'name': 'Introduction to Programming',
                        'description': 'Basic programming concepts using Python',
                        'materials': ['Python programming textbook', 'Code editor (VS Code/PyCharm)', 'Online Python tutorials'],
                        'success_tips': ['Practice coding daily', 'Understand variables and data types', 'Work on programming projects']
                    },
                    'CPT121': {
                        'name': 'Introduction to Computer Hardware',
                        'description': 'Computer hardware components and maintenance',
                        'materials': ['Computer hardware textbook', 'Hardware lab manual', 'Component identification guide'],
                        'success_tips': ['Hands-on practice with hardware', 'Understand component functions', 'Study maintenance procedures']
                    },
                    'CPT122': {
                        'name': 'Computer Hardware Systems and Maintenance',
                        'description': 'Advanced hardware systems and troubleshooting',
                        'materials': ['Hardware systems textbook', 'Troubleshooting guide', 'Maintenance tools'],
                        'success_tips': ['Practice troubleshooting', 'Understand system architecture', 'Learn diagnostic procedures']
                    },
                    'MAT101': {
                        'name': 'Mathematics for Computer Science',
                        'description': 'Mathematical foundations for CS',
                        'materials': ['Discrete mathematics textbook', 'Calculus textbook', 'Mathematical problem sets'],
                        'success_tips': ['Practice mathematical problems', 'Understand discrete math concepts', 'Apply math to programming']
                    }
                },
                'success_requirements': [
                    'Attend all lectures and practical sessions',
                    'Complete all assignments on time',
                    'Participate in group projects',
                    'Use recommended textbooks and materials',
                    'Practice programming regularly',
                    'Join study groups',
                    'Seek help from lecturers when needed'
                ]
            },
            '200_level': {
                'courses': {
                    'COS201': {
                        'name': 'Data Structures and Algorithms',
                        'description': 'Fundamental data structures and algorithm design',
                        'materials': ['Data structures textbook', 'Algorithm design guide', 'Programming practice problems'],
                        'success_tips': ['Master basic data structures', 'Practice algorithm implementation', 'Understand time complexity']
                    },
                    'COS202': {
                        'name': 'Object-Oriented Programming',
                        'description': 'OOP concepts using Java or C++',
                        'materials': ['OOP textbook', 'Java/C++ programming guide', 'Design patterns book'],
                        'success_tips': ['Understand OOP principles', 'Practice inheritance and polymorphism', 'Design object-oriented solutions']
                    }
                }
            },
            'general_tips': [
                'Join CS student groups and forums',
                'Participate in coding competitions',
                'Build personal projects',
                'Learn version control (Git)',
                'Practice problem-solving',
                'Stay updated with technology trends',
                'Network with fellow students and professionals'
            ]
        }
    
    def _load_course_materials(self) -> Dict:
        """Load comprehensive course materials"""
        return {
            'essential_software': [
                'Visual Studio Code',
                'Python IDLE',
                'Git',
                'Chrome/Firefox browser',
                'PDF reader',
                'Text editor (Notepad++)'
            ],
            'recommended_books': [
                'Introduction to Computer Science - Comprehensive Guide',
                'Python Programming for Beginners',
                'Data Structures and Algorithms in Python',
                'Computer Hardware Maintenance Guide',
                'Mathematics for Computer Science'
            ],
            'online_resources': [
                'Coursera CS courses',
                'edX Computer Science',
                'Khan Academy Programming',
                'GeeksforGeeks',
                'Stack Overflow',
                'GitHub for code examples'
            ],
            'practical_tools': [
                'Laptop with good specifications',
                'External hard drive for backups',
                'USB flash drives',
                'Notebook for taking notes',
                'Calculator for mathematics',
                'Internet connection for research'
            ]
        }
    
    def _load_success_tips(self) -> Dict:
        """Load success tips for CS students"""
        return {
            'academic_success': [
                'Attend all lectures and take detailed notes',
                'Complete assignments before deadlines',
                'Form study groups with classmates',
                'Ask questions during lectures',
                'Use office hours to clarify doubts',
                'Practice coding regularly',
                'Read beyond the syllabus'
            ],
            'practical_skills': [
                'Learn to use IDEs effectively',
                'Master version control with Git',
                'Practice debugging techniques',
                'Build personal projects',
                'Contribute to open source projects',
                'Learn multiple programming languages',
                'Understand software development lifecycle'
            ],
            'career_preparation': [
                'Build a strong portfolio',
                'Create a professional LinkedIn profile',
                'Participate in hackathons',
                'Join professional CS organizations',
                'Attend tech meetups and conferences',
                'Learn about industry trends',
                'Develop soft skills'
            ]
        }
    
    def _load_external_sources(self) -> Dict:
        """Load external knowledge sources"""
        return {
            'programming_resources': [
                'Codecademy',
                'FreeCodeCamp',
                'W3Schools',
                'MDN Web Docs',
                'Python.org documentation'
            ],
            'cs_communities': [
                'Stack Overflow',
                'GitHub',
                'Reddit r/programming',
                'Dev.to',
                'Medium CS articles'
            ],
            'fut_specific': [
                'FUT CS department website',
                'FUT library resources',
                'FUT CS student portal',
                'FUT CS faculty contacts',
                'FUT CS lab schedules'
            ]
        }
    
    def get_smart_response(self, question: str, context: str = "") -> str:
        """Get intelligent response based on question analysis"""
        question_lower = question.lower()
        
        # Course code queries
        if any(phrase in question_lower for phrase in ['course code', 'course codes', 'list course', 'show course']):
            return self._get_course_codes_response(question)
        
        # Materials queries
        elif any(phrase in question_lower for phrase in ['materials', 'books', 'software', 'tools', 'what do i need']):
            return self._get_materials_response(question)
        
        # Success tips queries
        elif any(phrase in question_lower for phrase in ['success', 'pass', 'excel', 'tips', 'advice', 'how to']):
            return self._get_success_tips_response(question)
        
        # Specific course queries
        elif any(phrase in question_lower for phrase in ['cos101', 'cos102', 'cpt121', 'cpt122', 'mat101']):
            return self._get_specific_course_response(question)
        
        # General CS queries
        elif any(phrase in question_lower for phrase in ['computer science', 'cs', 'programming', 'coding']):
            return self._get_general_cs_response(question)
        
        # Level-specific queries
        elif any(phrase in question_lower for phrase in ['100l', '100 level', 'first year', 'freshman']):
            return self._get_100_level_response(question)
        
        else:
            return self._get_general_response(question)
    
    def _get_course_codes_response(self, question: str) -> str:
        """Get comprehensive course codes response"""
        response = "📚 **FUT Computer Science Course Codes**\n\n"
        
        # 100 Level courses
        response += "**100 LEVEL COURSES:**\n"
        for code, details in self.cs_knowledge_base['100_level']['courses'].items():
            response += f"• {code}: {details['name']}\n"
        
        # 200 Level courses
        response += "\n**200 LEVEL COURSES:**\n"
        for code, details in self.cs_knowledge_base['200_level']['courses'].items():
            response += f"• {code}: {details['name']}\n"
        
        response += "\n💡 **Need more details about any specific course? Just ask!**"
        return response
    
    def _get_materials_response(self, question: str) -> str:
        """Get comprehensive materials response"""
        response = "📖 **Essential Materials for CS Students**\n\n"
        
        # Essential software
        response += "**🖥️ ESSENTIAL SOFTWARE:**\n"
        for software in self.course_materials['essential_software']:
            response += f"• {software}\n"
        
        # Recommended books
        response += "\n**📚 RECOMMENDED BOOKS:**\n"
        for book in self.course_materials['recommended_books']:
            response += f"• {book}\n"
        
        # Online resources
        response += "\n**🌐 ONLINE RESOURCES:**\n"
        for resource in self.course_materials['online_resources']:
            response += f"• {resource}\n"
        
        # Practical tools
        response += "\n**🛠️ PRACTICAL TOOLS:**\n"
        for tool in self.course_materials['practical_tools']:
            response += f"• {tool}\n"
        
        return response
    
    def _get_success_tips_response(self, question: str) -> str:
        """Get success tips response"""
        response = "🎯 **Success Tips for CS Students**\n\n"
        
        # Academic success
        response += "**📚 ACADEMIC SUCCESS:**\n"
        for tip in self.success_tips['academic_success']:
            response += f"• {tip}\n"
        
        # Practical skills
        response += "\n**💻 PRACTICAL SKILLS:**\n"
        for tip in self.success_tips['practical_skills']:
            response += f"• {tip}\n"
        
        # Career preparation
        response += "\n**🚀 CAREER PREPARATION:**\n"
        for tip in self.success_tips['career_preparation']:
            response += f"• {tip}\n"
        
        return response
    
    def _get_specific_course_response(self, question: str) -> str:
        """Get specific course information"""
        question_lower = question.lower()
        
        # Find the course code in the question
        course_code = None
        for code in ['COS101', 'COS102', 'CPT121', 'CPT122', 'MAT101']:
            if code.lower() in question_lower:
                course_code = code
                break
        
        if course_code:
            course_info = self.cs_knowledge_base['100_level']['courses'].get(course_code, {})
            if course_info:
                response = f"📚 **{course_code} - {course_info['name']}**\n\n"
                response += f"**Description:** {course_info['description']}\n\n"
                
                response += "**📖 Materials Needed:**\n"
                for material in course_info['materials']:
                    response += f"• {material}\n"
                
                response += "\n**💡 Success Tips:**\n"
                for tip in course_info['success_tips']:
                    response += f"• {tip}\n"
                
                return response
        
        return "I can help you with specific course information. Please mention the course code (e.g., COS101, COS102, CPT121, CPT122, MAT101)."
    
    def _get_100_level_response(self, question: str) -> str:
        """Get 100 level specific response"""
        response = "🎓 **100 Level CS Success Guide**\n\n"
        
        response += "**📚 CORE COURSES:**\n"
        for code, details in self.cs_knowledge_base['100_level']['courses'].items():
            response += f"• {code}: {details['name']}\n"
        
        response += "\n**✅ SUCCESS REQUIREMENTS:**\n"
        for requirement in self.cs_knowledge_base['100_level']['success_requirements']:
            response += f"• {requirement}\n"
        
        response += "\n**💡 GENERAL TIPS:**\n"
        for tip in self.cs_knowledge_base['general_tips']:
            response += f"• {tip}\n"
        
        return response
    
    def _get_general_cs_response(self, question: str) -> str:
        """Get general CS response"""
        response = "💻 **Computer Science at FUT**\n\n"
        response += "**🎯 WHAT YOU'LL LEARN:**\n"
        response += "• Programming fundamentals\n"
        response += "• Data structures and algorithms\n"
        response += "• Computer hardware and systems\n"
        response += "• Software development\n"
        response += "• Problem-solving skills\n"
        response += "• Mathematical foundations\n\n"
        
        response += "**🚀 CAREER OPPORTUNITIES:**\n"
        response += "• Software Developer\n"
        response += "• Data Scientist\n"
        response += "• System Administrator\n"
        response += "• Cybersecurity Specialist\n"
        response += "• IT Consultant\n"
        response += "• Web Developer\n\n"
        
        response += "**💡 SUCCESS TIPS:**\n"
        for tip in self.cs_knowledge_base['general_tips']:
            response += f"• {tip}\n"
        
        return response
    
    def _get_general_response(self, question: str) -> str:
        """Get general response"""
        return "I'm here to help you with Computer Science at FUT! I can assist with:\n\n• Course codes and descriptions\n• Required materials and books\n• Success tips and advice\n• Specific course information\n• Study strategies\n• Career guidance\n\nWhat would you like to know?"

# Global instance
intelligent_cs_assistant = IntelligentCSAssistant()

def get_intelligent_cs_response(question: str, context: str = "") -> str:
    """Get intelligent CS response"""
    return intelligent_cs_assistant.get_smart_response(question, context)
