"""
Dynamic Intelligence System for FUT QA Assistant
ChatGPT 3.0+ level intelligence with dynamic data fetching
"""

import json
import os
import re
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import requests

class DynamicIntelligence:
    def __init__(self):
        self.knowledge_base = self._load_comprehensive_knowledge()
        self.course_database = self._load_course_database()
        self.external_sources = self._load_external_sources()
        self.conversation_context = []
        self.learning_data = []
    
    def _load_comprehensive_knowledge(self) -> Dict:
        """Load comprehensive knowledge base"""
        return {
            'fut_general': {
                'established': '1983',
                'location': 'Minna, Niger State, Nigeria',
                'motto': 'Technology for Development',
                'type': 'Federal University',
                'accreditation': 'National Universities Commission (NUC)',
                'website': 'https://fut.edu.ng',
                'email': 'info@fut.edu.ng',
                'phone': '+234-66-222-000'
            },
            'sict_school': {
                'name': 'School of Information and Communication Technology',
                'departments': ['Computer Science', 'Cyber Security', 'Information Technology', 'Telecommunications Engineering'],
                'programs': ['B.Sc Computer Science', 'B.Sc Cyber Security', 'B.Sc Information Technology', 'B.Eng Telecommunications'],
                'facilities': ['Computer Laboratories', 'Network Laboratory', 'Software Development Lab', 'Hardware Maintenance Lab', 'Research Laboratory']
            },
            'admission_requirements': {
                'utme': 'Minimum of 180 in UTME',
                'olevel': 'Five credits including Mathematics and English',
                'subjects': 'Mathematics, English, Physics, Chemistry, and any other science subject',
                'direct_entry': 'A-level, OND, HND, or equivalent qualifications',
                'cut_off_mark': '180 and above'
            }
        }
    
    def _load_course_database(self) -> Dict:
        """Load comprehensive course database"""
        return {
            '100_level': {
                'COS101': {
                    'name': 'Introduction to Computer Science',
                    'description': 'Fundamental concepts of computer science, history, and applications',
                    'credits': 3,
                    'prerequisites': 'None',
                    'materials': [
                        'Introduction to Computer Science textbook',
                        'Programming basics guide',
                        'Computer fundamentals notes',
                        'Online CS resources'
                    ],
                    'success_tips': [
                        'Understand basic concepts thoroughly',
                        'Practice programming fundamentals',
                        'Read recommended textbooks',
                        'Join study groups',
                        'Ask questions during lectures'
                    ],
                    'assessment': 'Continuous Assessment (30%) + Examination (70%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Weekly lab sessions'
                },
                'COS102': {
                    'name': 'Introduction to Programming',
                    'description': 'Basic programming concepts using Python',
                    'credits': 3,
                    'prerequisites': 'COS101',
                    'materials': [
                        'Python programming textbook',
                        'Code editor (VS Code/PyCharm)',
                        'Online Python tutorials',
                        'Programming practice problems'
                    ],
                    'success_tips': [
                        'Practice coding daily',
                        'Understand variables and data types',
                        'Work on programming projects',
                        'Use online coding platforms',
                        'Debug your code regularly'
                    ],
                    'assessment': 'Continuous Assessment (40%) + Examination (60%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Weekly programming labs'
                },
                'CPT121': {
                    'name': 'Introduction to Computer Hardware',
                    'description': 'Computer hardware components and maintenance',
                    'credits': 3,
                    'prerequisites': 'None',
                    'materials': [
                        'Computer hardware textbook',
                        'Hardware lab manual',
                        'Component identification guide',
                        'Hardware tools'
                    ],
                    'success_tips': [
                        'Hands-on practice with hardware',
                        'Understand component functions',
                        'Study maintenance procedures',
                        'Practice troubleshooting',
                        'Join hardware study groups'
                    ],
                    'assessment': 'Continuous Assessment (35%) + Examination (65%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Weekly hardware labs'
                },
                'CPT122': {
                    'name': 'Computer Hardware Systems and Maintenance',
                    'description': 'Advanced hardware systems and troubleshooting',
                    'credits': 3,
                    'prerequisites': 'CPT121',
                    'materials': [
                        'Hardware systems textbook',
                        'Troubleshooting guide',
                        'Maintenance tools',
                        'System diagnostic software'
                    ],
                    'success_tips': [
                        'Practice troubleshooting',
                        'Understand system architecture',
                        'Learn diagnostic procedures',
                        'Work with different hardware',
                        'Document maintenance procedures'
                    ],
                    'assessment': 'Continuous Assessment (30%) + Examination (70%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Weekly maintenance labs'
                },
                'MAT101': {
                    'name': 'Mathematics for Computer Science',
                    'description': 'Mathematical foundations for CS',
                    'credits': 3,
                    'prerequisites': 'O\'Level Mathematics',
                    'materials': [
                        'Discrete mathematics textbook',
                        'Calculus textbook',
                        'Mathematical problem sets',
                        'Scientific calculator'
                    ],
                    'success_tips': [
                        'Practice mathematical problems',
                        'Understand discrete math concepts',
                        'Apply math to programming',
                        'Use mathematical software',
                        'Join math study groups'
                    ],
                    'assessment': 'Continuous Assessment (30%) + Examination (70%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Weekly problem-solving sessions'
                }
            },
            '200_level': {
                'COS201': {
                    'name': 'Data Structures and Algorithms',
                    'description': 'Fundamental data structures and algorithm design',
                    'credits': 3,
                    'prerequisites': 'COS102',
                    'materials': [
                        'Data structures textbook',
                        'Algorithm design guide',
                        'Programming practice problems',
                        'Algorithm visualization tools'
                    ],
                    'success_tips': [
                        'Master basic data structures',
                        'Practice algorithm implementation',
                        'Understand time complexity',
                        'Solve coding problems',
                        'Use algorithm visualization tools'
                    ]
                },
                'COS202': {
                    'name': 'Object-Oriented Programming',
                    'description': 'OOP concepts using Java or C++',
                    'credits': 3,
                    'prerequisites': 'COS102',
                    'materials': [
                        'OOP textbook',
                        'Java/C++ programming guide',
                        'Design patterns book',
                        'IDE (IntelliJ/Eclipse)'
                    ],
                    'success_tips': [
                        'Understand OOP principles',
                        'Practice inheritance and polymorphism',
                        'Design object-oriented solutions',
                        'Learn design patterns',
                        'Build OOP projects'
                    ]
                }
            }
        }
    
    def _load_external_sources(self) -> Dict:
        """Load external knowledge sources"""
        return {
            'programming_resources': [
                'Codecademy - Interactive programming courses',
                'FreeCodeCamp - Free coding bootcamp',
                'W3Schools - Web development tutorials',
                'MDN Web Docs - Web development reference',
                'Python.org - Official Python documentation',
                'GeeksforGeeks - Programming tutorials',
                'Stack Overflow - Programming Q&A'
            ],
            'cs_communities': [
                'Stack Overflow - Programming community',
                'GitHub - Code repository and collaboration',
                'Reddit r/programming - CS discussions',
                'Dev.to - Developer community',
                'Medium CS articles - Technical writing',
                'HackerRank - Coding challenges',
                'LeetCode - Algorithm practice'
            ],
            'fut_specific': [
                'FUT CS department website',
                'FUT library resources',
                'FUT CS student portal',
                'FUT CS faculty contacts',
                'FUT CS lab schedules',
                'FUT CS student groups'
            ]
        }
    
    def analyze_question_intent(self, question: str) -> Dict:
        """Analyze question intent and determine response type"""
        question_lower = question.lower()
        
        # Check for unrelated questions
        unrelated_keywords = [
            'cooking', 'recipe', 'food', 'restaurant', 'travel', 'hotel', 'weather',
            'sports', 'football', 'basketball', 'music', 'movie', 'entertainment',
            'fashion', 'shopping', 'beauty', 'health', 'medical', 'politics',
            'religion', 'dating', 'relationship', 'personal', 'private'
        ]
        
        if any(keyword in question_lower for keyword in unrelated_keywords):
            return {
                'type': 'unrelated',
                'confidence': 0.9,
                'response_type': 'boundary'
            }
        
        # Check for course-specific questions
        course_codes = ['COS101', 'COS102', 'CPT121', 'CPT122', 'MAT101', 'COS201', 'COS202']
        for code in course_codes:
            if code.lower() in question_lower:
                return {
                    'type': 'course_specific',
                    'course_code': code,
                    'confidence': 0.95,
                    'response_type': 'course_detail'
                }
        
        # Check for general CS questions
        cs_keywords = [
            'computer science', 'cs', 'programming', 'coding', 'software',
            'hardware', 'algorithm', 'data structure', 'database', 'network',
            'cybersecurity', 'information technology', 'it'
        ]
        
        if any(keyword in question_lower for keyword in cs_keywords):
            return {
                'type': 'cs_general',
                'confidence': 0.85,
                'response_type': 'cs_guidance'
            }
        
        # Check for FUT-specific questions
        fut_keywords = [
            'fut', 'federal university', 'minna', 'admission', 'requirements',
            'campus', 'facilities', 'programs', 'courses', 'university'
        ]
        
        if any(keyword in question_lower for keyword in fut_keywords):
            return {
                'type': 'fut_general',
                'confidence': 0.8,
                'response_type': 'fut_info'
            }
        
        # Check for materials/resources questions
        material_keywords = [
            'materials', 'books', 'software', 'tools', 'resources', 'what do i need',
            'equipment', 'supplies', 'textbooks', 'laptop', 'computer'
        ]
        
        if any(keyword in question_lower for keyword in material_keywords):
            return {
                'type': 'materials',
                'confidence': 0.85,
                'response_type': 'materials_guide'
            }
        
        # Check for success/advice questions
        success_keywords = [
            'success', 'pass', 'excel', 'tips', 'advice', 'how to', 'help',
            'guidance', 'strategy', 'study', 'learn', 'improve'
        ]
        
        if any(keyword in question_lower for keyword in success_keywords):
            return {
                'type': 'success_advice',
                'confidence': 0.8,
                'response_type': 'success_guide'
            }
        
        # Default to general response
        return {
            'type': 'general',
            'confidence': 0.5,
            'response_type': 'general_help'
        }
    
    def get_dynamic_response(self, question: str, context: str = "") -> str:
        """Get dynamic intelligent response"""
        intent = self.analyze_question_intent(question)
        
        # Store conversation context
        self.conversation_context.append({
            'question': question,
            'intent': intent,
            'timestamp': datetime.now().isoformat()
        })
        
        # Generate response based on intent
        if intent['type'] == 'unrelated':
            return self._get_boundary_response(question)
        elif intent['type'] == 'course_specific':
            return self._get_course_specific_response(question, intent['course_code'])
        elif intent['type'] == 'cs_general':
            return self._get_cs_general_response(question)
        elif intent['type'] == 'fut_general':
            return self._get_fut_general_response(question)
        elif intent['type'] == 'materials':
            return self._get_materials_response(question)
        elif intent['type'] == 'success_advice':
            return self._get_success_advice_response(question)
        else:
            return self._get_general_response(question)
    
    def _get_boundary_response(self, question: str) -> str:
        """Handle unrelated questions"""
        return """🚫 **I'm a specialized FUT Computer Science Assistant**

I'm designed specifically to help FUT Computer Science students with:
• Course information and codes
• Study materials and resources
• Academic success tips
• Programming and CS guidance
• FUT-specific information

I can't help with topics like cooking, travel, entertainment, or other non-academic subjects.

**How can I help you with your CS studies at FUT?**"""
    
    def _get_course_specific_response(self, question: str, course_code: str) -> str:
        """Get detailed course-specific response"""
        course_info = None
        
        # Search in 100 level
        if course_code in self.course_database['100_level']:
            course_info = self.course_database['100_level'][course_code]
            level = '100 Level'
        # Search in 200 level
        elif course_code in self.course_database['200_level']:
            course_info = self.course_database['200_level'][course_code]
            level = '200 Level'
        
        if course_info:
            response = f"📚 **{course_code} - {course_info['name']}**\n"
            response += f"**Level:** {level}\n"
            response += f"**Credits:** {course_info['credits']}\n"
            response += f"**Prerequisites:** {course_info['prerequisites']}\n\n"
            
            response += f"**📖 Description:**\n{course_info['description']}\n\n"
            
            response += "**📚 Materials Needed:**\n"
            for material in course_info['materials']:
                response += f"• {material}\n"
            
            response += "\n**💡 Success Tips:**\n"
            for tip in course_info['success_tips']:
                response += f"• {tip}\n"
            
            response += f"\n**📊 Assessment:** {course_info['assessment']}\n"
            response += f"**👨‍🏫 Office Hours:** {course_info['lecturer_office_hours']}\n"
            response += f"**🔬 Practical Sessions:** {course_info['practical_sessions']}\n"
            
            return response
        
        return f"❌ **Course {course_code} not found in our database.**\n\nPlease check the course code or ask about available courses."
    
    def _get_cs_general_response(self, question: str) -> str:
        """Get general CS guidance"""
        response = "💻 **Computer Science at FUT**\n\n"
        
        response += "**🎯 WHAT YOU'LL LEARN:**\n"
        response += "• Programming fundamentals (Python, Java, C++)\n"
        response += "• Data structures and algorithms\n"
        response += "• Computer hardware and systems\n"
        response += "• Software development and engineering\n"
        response += "• Database design and management\n"
        response += "• Network and cybersecurity\n"
        response += "• Problem-solving and critical thinking\n\n"
        
        response += "**🚀 CAREER OPPORTUNITIES:**\n"
        response += "• Software Developer/Engineer\n"
        response += "• Data Scientist/Analyst\n"
        response += "• System Administrator\n"
        response += "• Cybersecurity Specialist\n"
        response += "• IT Consultant\n"
        response += "• Web Developer\n"
        response += "• Mobile App Developer\n"
        response += "• AI/ML Engineer\n\n"
        
        response += "**💡 SUCCESS STRATEGIES:**\n"
        response += "• Practice coding regularly\n"
        response += "• Build personal projects\n"
        response += "• Join CS communities\n"
        response += "• Participate in hackathons\n"
        response += "• Learn version control (Git)\n"
        response += "• Stay updated with technology trends\n"
        response += "• Network with professionals\n"
        response += "• Contribute to open source projects\n\n"
        
        response += "**🌐 RECOMMENDED RESOURCES:**\n"
        for resource in self.external_sources['programming_resources'][:5]:
            response += f"• {resource}\n"
        
        return response
    
    def _get_fut_general_response(self, question: str) -> str:
        """Get FUT general information"""
        response = "🏛️ **Federal University of Technology, Minna**\n\n"
        
        fut_info = self.knowledge_base['fut_general']
        response += f"**Established:** {fut_info['established']}\n"
        response += f"**Location:** {fut_info['location']}\n"
        response += f"**Motto:** {fut_info['motto']}\n"
        response += f"**Type:** {fut_info['type']}\n"
        response += f"**Accreditation:** {fut_info['accreditation']}\n\n"
        
        response += "**📞 CONTACT INFORMATION:**\n"
        response += f"• Website: {fut_info['website']}\n"
        response += f"• Email: {fut_info['email']}\n"
        response += f"• Phone: {fut_info['phone']}\n\n"
        
        response += "**🎓 ADMISSION REQUIREMENTS:**\n"
        admission = self.knowledge_base['admission_requirements']
        response += f"• UTME Score: {admission['utme']}\n"
        response += f"• O'Level: {admission['olevel']}\n"
        response += f"• Subjects: {admission['subjects']}\n"
        response += f"• Direct Entry: {admission['direct_entry']}\n"
        response += f"• Cut-off Mark: {admission['cut_off_mark']}\n\n"
        
        response += "**🏫 SCHOOL OF ICT (SICT):**\n"
        sict = self.knowledge_base['sict_school']
        response += f"• Name: {sict['name']}\n"
        response += "• Departments:\n"
        for dept in sict['departments']:
            response += f"  - {dept}\n"
        response += "• Programs:\n"
        for program in sict['programs']:
            response += f"  - {program}\n"
        response += "• Facilities:\n"
        for facility in sict['facilities']:
            response += f"  - {facility}\n"
        
        return response
    
    def _get_materials_response(self, question: str) -> str:
        """Get materials and resources response"""
        response = "📚 **Essential Materials for CS Students**\n\n"
        
        response += "**💻 HARDWARE REQUIREMENTS:**\n"
        response += "• Laptop/Desktop Computer (8GB RAM minimum)\n"
        response += "• External Monitor (optional but recommended)\n"
        response += "• USB Drive for file storage\n"
        response += "• Headphones for online learning\n"
        response += "• Stable Internet Connection\n\n"
        
        response += "**🛠️ SOFTWARE TOOLS:**\n"
        response += "• Code Editor: VS Code, PyCharm, or IntelliJ IDEA\n"
        response += "• Python IDE: Anaconda or Jupyter Notebook\n"
        response += "• Version Control: Git and GitHub Desktop\n"
        response += "• Database: MySQL, PostgreSQL, or SQLite\n"
        response += "• Virtual Machine: VirtualBox or VMware\n"
        response += "• Office Suite: Microsoft Office or LibreOffice\n\n"
        
        response += "**📖 RECOMMENDED TEXTBOOKS:**\n"
        response += "• Introduction to Computer Science\n"
        response += "• Python Programming for Beginners\n"
        response += "• Data Structures and Algorithms\n"
        response += "• Computer Hardware and Maintenance\n"
        response += "• Discrete Mathematics for CS\n"
        response += "• Software Engineering Principles\n\n"
        
        response += "**🌐 ONLINE RESOURCES:**\n"
        for resource in self.external_sources['programming_resources'][:5]:
            response += f"• {resource}\n"
        
        return response
    
    def _get_success_advice_response(self, question: str) -> str:
        """Get success advice response"""
        response = "🎯 **Success Strategies for CS Students**\n\n"
        
        response += "**📚 ACADEMIC EXCELLENCE:**\n"
        response += "• Attend all lectures and practical sessions\n"
        response += "• Take detailed notes and review them regularly\n"
        response += "• Practice coding daily, even for 30 minutes\n"
        response += "• Form study groups with classmates\n"
        response += "• Ask questions during lectures and office hours\n"
        response += "• Complete assignments before deadlines\n"
        response += "• Prepare thoroughly for examinations\n\n"
        
        response += "**💻 PRACTICAL SKILLS:**\n"
        response += "• Build personal programming projects\n"
        response += "• Contribute to open source projects on GitHub\n"
        response += "• Participate in coding competitions\n"
        response += "• Learn multiple programming languages\n"
        response += "• Understand version control (Git)\n"
        response += "• Practice problem-solving on platforms like LeetCode\n"
        response += "• Build a portfolio of your work\n\n"
        
        response += "**🌐 NETWORKING & COMMUNITY:**\n"
        response += "• Join CS student organizations\n"
        response += "• Attend tech meetups and conferences\n"
        response += "• Connect with alumni and professionals\n"
        response += "• Participate in hackathons\n"
        response += "• Join online CS communities\n"
        response += "• Follow tech blogs and stay updated\n\n"
        
        response += "**⏰ TIME MANAGEMENT:**\n"
        response += "• Create a study schedule and stick to it\n"
        response += "• Prioritize tasks based on importance and urgency\n"
        response += "• Take regular breaks to avoid burnout\n"
        response += "• Balance academics with personal life\n"
        response += "• Set realistic goals and track progress\n"
        response += "• Use productivity tools and apps\n\n"
        
        response += "**🚀 CAREER PREPARATION:**\n"
        response += "• Research career paths in CS\n"
        response += "• Build a professional LinkedIn profile\n"
        response += "• Create a strong resume highlighting projects\n"
        response += "• Practice technical interviews\n"
        response += "• Consider internships and co-op programs\n"
        response += "• Stay updated with industry trends\n"
        
        return response
    
    def _get_general_response(self, question: str) -> str:
        """Get general help response"""
        return """🤖 **FUT CS Assistant - How Can I Help?**

I'm your intelligent assistant for Computer Science at Federal University of Technology, Minna. I can help you with:

**📚 ACADEMIC SUPPORT:**
• Course information and codes
• Study materials and resources
• Success tips and strategies
• Programming guidance

**🏫 FUT INFORMATION:**
• University details and history
• Admission requirements
• Campus facilities
• Academic programs

**💻 CS GUIDANCE:**
• Career opportunities
• Learning resources
• Technical support
• Study strategies

**Ask me anything about:**
• Specific courses (COS101, COS102, CPT121, etc.)
• Materials you need for CS
• How to succeed in your studies
• FUT programs and requirements
• Programming help and resources

**What would you like to know?**"""
    
    def fetch_external_data(self, query: str) -> Optional[str]:
        """Fetch data from external sources (simulated)"""
        # In a real implementation, this would connect to:
        # - FUT website API
        # - Course catalog database
        # - Academic calendar
        # - Faculty directory
        # - Library resources
        
        # For now, return None to use local knowledge
        return None
    
    def learn_from_interaction(self, question: str, response: str, feedback: Optional[str] = None):
        """Learn from user interactions"""
        interaction = {
            'question': question,
            'response': response,
            'feedback': feedback,
            'timestamp': datetime.now().isoformat()
        }
        self.learning_data.append(interaction)
        
        # In a real implementation, this would:
        # - Update the knowledge base
        # - Improve response patterns
        # - Adjust confidence scores
        # - Store successful interactions
    
    def get_conversation_summary(self) -> str:
        """Get summary of current conversation"""
        if not self.conversation_context:
            return "No conversation history available."
        
        summary = f"**Conversation Summary ({len(self.conversation_context)} interactions):**\n\n"
        
        for i, context in enumerate(self.conversation_context[-5:], 1):  # Last 5 interactions
            summary += f"{i}. **Question:** {context['question'][:50]}...\n"
            summary += f"   **Intent:** {context['intent']['type']}\n"
            summary += f"   **Time:** {context['timestamp']}\n\n"
        
        return summary

# Initialize the dynamic intelligence system
dynamic_intelligence = DynamicIntelligence()
