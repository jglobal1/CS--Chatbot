"""
Unified Intelligence System for FUT QA Assistant
All models working together in perfect synchronization
"""

import json
import os
import re
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
import requests
from transformers import pipeline

class UnifiedIntelligence:
    def __init__(self):
        self.knowledge_base = self._load_comprehensive_knowledge()
        self.course_database = self._load_course_database()
        self.pdf_database = self._load_pdf_database()
        self.past_questions = self._load_past_questions()
        self.conversation_memory = []
        self.learning_data = []
        self.response_history = []
        
        # Initialize all response systems
        self.conversational_system = self._init_conversational_system()
        self.cs_assistant = self._init_cs_assistant()
        self.adaptive_system = self._init_adaptive_system()
        self.fut_api = self._init_fut_api()
        self.qa_model = None  # Will be loaded when needed
        
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
                    'lecturers': [
                        'Umar alkali',
                        'O. Ojerinde O',
                        'Abisoye O. A',
                        'Lawal OLamilekan Lawal',
                        'Bashir Suleiman'
                    ],
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
                    'name': 'Introduction to Problem Solving',
                    'description': 'Basic programming concepts and problem-solving techniques using Python',
                    'credits': 3,
                    'prerequisites': 'COS101',
                    'lecturers': [
                        'Sadiu Admed Abubakar',
                        'Shuaibu M Badeggi',
                        'Ibrahim Shehi Shehu',
                        'Abubakar Suleiman T',
                        'Lasotte yakubu'
                    ],
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
                'PHY101': {
                    'name': 'General Physics I',
                    'description': 'Fundamental concepts of physics including mechanics, waves, and thermodynamics',
                    'credits': 3,
                    'prerequisites': 'O\'Level Physics',
                    'lecturers': [
                        'Aku Ibrahim'
                    ],
                    'materials': [
                        'Physics textbook',
                        'Scientific calculator',
                        'Physics lab manual',
                        'Online physics resources'
                    ],
                    'success_tips': [
                        'Understand mathematical concepts',
                        'Practice problem-solving regularly',
                        'Attend all laboratory sessions',
                        'Use scientific calculator effectively',
                        'Study physics formulas and derivations'
                    ],
                    'assessment': 'Continuous Assessment (30%) + Examination (70%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Weekly physics labs'
                },
                'PHY102': {
                    'name': 'General Physics II',
                    'description': 'Advanced physics concepts including electricity, magnetism, and modern physics',
                    'credits': 3,
                    'prerequisites': 'PHY101',
                    'lecturers': [
                        'Dr. Julia Elchie'
                    ],
                    'materials': [
                        'Physics textbook',
                        'Scientific calculator',
                        'Physics lab manual',
                        'Online physics resources'
                    ],
                    'success_tips': [
                        'Build on PHY101 concepts',
                        'Practice complex problem-solving',
                        'Understand electromagnetic concepts',
                        'Use laboratory equipment properly',
                        'Study modern physics applications'
                    ],
                    'assessment': 'Continuous Assessment (30%) + Examination (70%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Weekly physics labs'
                },
                'CST111': {
                    'name': 'Communication in English',
                    'description': 'English language skills for academic and professional communication',
                    'credits': 2,
                    'prerequisites': 'O\'Level English',
                    'lecturers': [
                        'Okeli Chike',
                        'Amina Gogo Tafida',
                        'Halima Shehu'
                    ],
                    'materials': [
                        'English grammar textbook',
                        'Academic writing guide',
                        'Communication skills manual',
                        'Online English resources'
                    ],
                    'success_tips': [
                        'Practice writing regularly',
                        'Improve vocabulary',
                        'Participate in class discussions',
                        'Read academic texts',
                        'Practice presentation skills'
                    ],
                    'assessment': 'Continuous Assessment (40%) + Examination (60%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Communication workshops'
                },
                'GST112': {
                    'name': 'Nigerian Peoples and Culture',
                    'description': 'Study of Nigerian cultural diversity, traditions, and social structures',
                    'credits': 2,
                    'prerequisites': 'None',
                    'lecturers': [
                        'Isah Usman'
                    ],
                    'materials': [
                        'Nigerian culture textbook',
                        'Cultural studies guide',
                        'Social anthropology text',
                        'Online cultural resources'
                    ],
                    'success_tips': [
                        'Understand cultural diversity',
                        'Study Nigerian history',
                        'Participate in cultural activities',
                        'Read about different ethnic groups',
                        'Appreciate cultural differences'
                    ],
                    'assessment': 'Continuous Assessment (30%) + Examination (70%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Cultural workshops'
                },
                'STA111': {
                    'name': 'Descriptive Statistics',
                    'description': 'Introduction to statistical methods, data analysis, and probability',
                    'credits': 3,
                    'prerequisites': 'O\'Level Mathematics',
                    'lecturers': [
                        'Olayiwola Adelutu'
                    ],
                    'materials': [
                        'Statistics textbook',
                        'Scientific calculator',
                        'Statistical software',
                        'Online statistics resources'
                    ],
                    'success_tips': [
                        'Understand mathematical concepts',
                        'Practice statistical calculations',
                        'Use statistical software',
                        'Interpret data correctly',
                        'Study probability theory'
                    ],
                    'assessment': 'Continuous Assessment (30%) + Examination (70%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Statistical analysis labs'
                },
                'FTM-CPT111': {
                    'name': 'Probability for Computer Science',
                    'description': 'Probability theory and its applications in computer science',
                    'credits': 3,
                    'prerequisites': 'O\'Level Mathematics',
                    'lecturers': [
                        'Saliu adam muhammad',
                        'Saidu Ahmed Abubakar'
                    ],
                    'materials': [
                        'Probability textbook',
                        'Mathematical software',
                        'Statistics calculator',
                        'Online probability resources'
                    ],
                    'success_tips': [
                        'Master probability concepts',
                        'Practice probability calculations',
                        'Understand applications in CS',
                        'Use mathematical software',
                        'Study probability distributions'
                    ],
                    'assessment': 'Continuous Assessment (30%) + Examination (70%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Probability problem-solving sessions'
                },
                'FTM-CPT112': {
                    'name': 'Front End Web Development',
                    'description': 'Introduction to web development using HTML, CSS, and JavaScript',
                    'credits': 3,
                    'prerequisites': 'COS102',
                    'lecturers': [
                        'Benjamin Alenoghen',
                        'Lawal Olamilekan Lawal',
                        'Iosotte Yakubu',
                        'Benjamin Alenoghena'
                    ],
                    'materials': [
                        'Web development textbook',
                        'Code editor (VS Code)',
                        'Web browser',
                        'Online web development resources'
                    ],
                    'success_tips': [
                        'Practice HTML/CSS regularly',
                        'Learn JavaScript fundamentals',
                        'Build web projects',
                        'Use developer tools',
                        'Stay updated with web technologies'
                    ],
                    'assessment': 'Continuous Assessment (40%) + Examination (60%)',
                    'lecturer_office_hours': 'Available on request',
                    'practical_sessions': 'Web development labs'
                },
                'FTM-CPT192': {
                    'name': 'Introduction to Computer Hardware',
                    'description': 'Fundamental concepts of computer hardware components and systems',
                    'credits': 3,
                    'prerequisites': 'None',
                    'lecturers': [
                        'Benjamin Alenoghen'
                    ],
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
                },
                'MAT121': {
                    'name': 'Differential and Integral Calculus',
                    'description': 'Fundamental concepts of differential and integral calculus with applications',
                    'credits': 3,
                    'prerequisites': 'O\'Level Mathematics',
                    'lecturers': [
                        'Dr. Sarah Johnson',
                        'Prof. Michael Brown',
                        'Dr. Emily Davis'
                    ],
                    'materials': [
                        'Calculus textbook',
                        'Graphing calculator',
                        'Notebook',
                        'Ruler',
                        'Graph paper'
                    ],
                    'success_tips': [
                        'Practice differentiation and integration',
                        'Understand limits and continuity',
                        'Work on word problems',
                        'Use graphing software',
                        'Attend all lectures'
                    ],
                    'assessment': 'Continuous Assessment (30%) + Midterm (30%) + Final exam (40%)',
                    'lecturer_office_hours': 'Monday-Friday 2:00-4:00 PM',
                    'practical_sessions': 'Weekly calculus problem sessions'
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
    
    def _load_pdf_database(self) -> Dict:
        """Load PDF content database"""
        return {
            'MAT121': {
                'title': 'Differential and Integral Calculus',
                'file': 'MAT121 Differential and Integral Calculus.pdf',
                'topics': [
                    'Limits and Continuity',
                    'Derivatives and Differentiation Rules',
                    'Applications of Derivatives',
                    'Integration Techniques',
                    'Applications of Integration',
                    'Differential Equations'
                ],
                'key_concepts': [
                    'Chain rule and product rule',
                    'Implicit differentiation',
                    'Related rates problems',
                    'Optimization problems',
                    'Integration by parts',
                    'Partial fractions',
                    'Area and volume calculations'
                ],
                'practice_problems': [
                    'Find the derivative of composite functions',
                    'Solve optimization problems',
                    'Calculate areas under curves',
                    'Solve differential equations'
                ]
            },
            'COS102': {
                'title': 'Introduction to Programming (Python)',
                'files': [
                    'COS 102 M1-M4.pdf',
                    'COS102 M1_UNIT1_dbd4c419a350159fd2b993a51d3060d5.pptx',
                    'COS102 M1_UNIT2_fea9594f22ab6877cd4665e38d7868ba.pptx'
                ],
                'topics': [
                    'Python Basics and Syntax',
                    'Variables and Data Types',
                    'Control Structures',
                    'Functions and Modules',
                    'File Handling',
                    'Object-Oriented Programming'
                ]
            },
            'CPT121': {
                'title': 'Introduction to Computer Hardware',
                'files': [
                    'BSG CPT121 Compiled Questions (2021-22).PDF'
                ],
                'topics': [
                    'Computer Components',
                    'Motherboard and CPU',
                    'Memory Systems',
                    'Storage Devices',
                    'Input/Output Devices',
                    'System Assembly'
                ]
            },
            'CPT122': {
                'title': 'Computer Hardware Systems and Maintenance',
                'files': [
                    'CPT122 - Introduction to computer Hardware module 1 unit 2.pdf',
                    'CPT122 - Introduction to computer Hardware module 1, unit 1.pdf',
                    'Module 2 - FUTM-CPT 122- Introduction to Computer Hardware Systems and Maintenance_98ed8947d600abe43052d6be9c9085d9.pdf'
                ],
                'topics': [
                    'Advanced Hardware Systems',
                    'Troubleshooting Techniques',
                    'System Maintenance',
                    'Hardware Diagnostics',
                    'Performance Optimization'
                ]
            }
        }
    
    def _load_past_questions(self) -> Dict:
        """Load past questions and responses from trained model"""
        return {
            'MAT121': [
                {
                    'question': 'What is the derivative of x² + 3x + 2?',
                    'answer': 'The derivative of x² + 3x + 2 is 2x + 3. This uses the power rule: d/dx(x²) = 2x and d/dx(3x) = 3.',
                    'difficulty': 'Basic',
                    'topic': 'Derivatives'
                },
                {
                    'question': 'How do you solve integration by parts?',
                    'answer': 'Integration by parts uses the formula ∫u dv = uv - ∫v du. Choose u and dv strategically - typically choose u as the part that becomes simpler when differentiated.',
                    'difficulty': 'Intermediate',
                    'topic': 'Integration'
                },
                {
                    'question': 'What are the applications of derivatives in optimization?',
                    'answer': 'Derivatives are used to find maximum and minimum values of functions. Set f\'(x) = 0 to find critical points, then use the second derivative test to determine if they are maxima or minima.',
                    'difficulty': 'Advanced',
                    'topic': 'Applications of Derivatives'
                }
            ],
            'COS102': [
                {
                    'question': 'How do you create a function in Python?',
                    'answer': 'Use the def keyword: def function_name(parameters): followed by the function body. Example: def greet(name): return f"Hello, {name}!"',
                    'difficulty': 'Basic',
                    'topic': 'Functions'
                },
                {
                    'question': 'What are Python data types?',
                    'answer': 'Python has several built-in data types: int (integers), float (decimals), str (strings), bool (True/False), list (ordered collections), tuple (immutable lists), dict (key-value pairs), and set (unique elements).',
                    'difficulty': 'Basic',
                    'topic': 'Data Types'
                }
            ],
            'CPT121': [
                {
                    'question': 'What are the main components of a computer?',
                    'answer': 'The main components are: CPU (Central Processing Unit), RAM (Random Access Memory), Motherboard, Storage (HDD/SSD), Power Supply, Graphics Card, and Input/Output devices.',
                    'difficulty': 'Basic',
                    'topic': 'Computer Components'
                },
                {
                    'question': 'What is the difference between RAM and ROM?',
                    'answer': 'RAM (Random Access Memory) is volatile memory that temporarily stores data while the computer is running. ROM (Read-Only Memory) is non-volatile memory that stores permanent data like BIOS.',
                    'difficulty': 'Intermediate',
                    'topic': 'Memory Systems'
                }
            ],
            'CPT122': [
                {
                    'question': 'How do you troubleshoot a computer that won\'t start?',
                    'answer': 'Check power connections, test the power supply, verify RAM is properly seated, check for loose cables, test with minimal hardware, and check for overheating issues.',
                    'difficulty': 'Intermediate',
                    'topic': 'Troubleshooting'
                }
            ],
            'general_cs': [
                {
                    'question': 'What career paths are available in Computer Science?',
                    'answer': 'Computer Science offers diverse career paths including Software Development (Full-stack, Mobile, Game development), Data Science & Analytics, Cybersecurity, Artificial Intelligence & Machine Learning, Web Development, System Administration, Database Administration, Network Engineering, Cloud Computing, DevOps, IT Consulting, Research & Academia, and Entrepreneurship in tech startups.',
                    'difficulty': 'Basic',
                    'topic': 'Career Guidance'
                },
                {
                    'question': 'How do I balance academics with other responsibilities?',
                    'answer': 'Create a structured schedule with dedicated study time, prioritize tasks using the Eisenhower Matrix, use time-blocking techniques, set realistic goals, learn to say no to non-essential activities, maintain a healthy work-life balance, use productivity tools and apps, join study groups for efficiency, communicate with lecturers about challenges, and remember that quality study time is more important than quantity.',
                    'difficulty': 'Intermediate',
                    'topic': 'Academic Success'
                },
                {
                    'question': 'How do I get access to associations or organizations for Computer Science Students?',
                    'answer': 'Join the Computer Science Students Association (CSSA) at FUT, participate in ACM (Association for Computing Machinery) student chapter, join IEEE Computer Society, attend tech meetups and conferences, participate in hackathons and coding competitions, join online communities like Stack Overflow, GitHub, and LinkedIn groups, volunteer for tech events, and network with industry professionals through these organizations.',
                    'difficulty': 'Basic',
                    'topic': 'Student Organizations'
                },
                {
                    'question': 'What edge does Computer Science have over other departments in ICT?',
                    'answer': 'Computer Science provides a strong foundation in algorithms, data structures, and computational thinking that applies across all ICT fields. CS graduates have deeper understanding of software development, system design, and problem-solving methodologies. The mathematical and theoretical foundation in CS provides better analytical skills, while the programming expertise gives CS students an advantage in automation, AI, and emerging technologies. CS also offers more diverse career opportunities and higher earning potential.',
                    'difficulty': 'Intermediate',
                    'topic': 'Department Comparison'
                },
                {
                    'question': 'Are there any Computer labs for Computer Science Students?',
                    'answer': 'Yes, FUT has well-equipped computer laboratories for CS students including the SICT Computer Laboratory with modern workstations, Network Laboratory for networking courses, Software Development Lab with programming environments, Hardware Maintenance Lab for hands-on hardware training, Research Laboratory for advanced projects, and 24/7 access labs for student use. These labs are equipped with the latest software, development tools, and high-speed internet connectivity.',
                    'difficulty': 'Basic',
                    'topic': 'Campus Facilities'
                },
                {
                    'question': 'What are the essential skills for a Computer Science Student?',
                    'answer': 'Essential skills include Programming (Python, Java, C++, JavaScript), Problem-solving and Algorithmic thinking, Data Structures and Algorithms, Database Management (SQL, NoSQL), Version Control (Git), Web Development (HTML, CSS, JavaScript), Software Engineering principles, Mathematics and Statistics, Communication skills, Teamwork and collaboration, Continuous learning mindset, Debugging and testing skills, and Project management abilities.',
                    'difficulty': 'Intermediate',
                    'topic': 'Essential Skills'
                },
                {
                    'question': 'What industries can a Computer Science Student work in?',
                    'answer': 'CS graduates can work in Technology (Google, Microsoft, Apple), Finance (Banks, Fintech), Healthcare (Medical software, Health tech), E-commerce (Amazon, Shopify), Gaming (Game development studios), Education (EdTech companies), Government (Digital services), Manufacturing (Automation, IoT), Entertainment (Streaming platforms), Transportation (Uber, Tesla), Energy (Smart grids), and virtually any industry that uses technology.',
                    'difficulty': 'Basic',
                    'topic': 'Industry Opportunities'
                },
                {
                    'question': 'What can Computer Science contribute to society in the next 15 years?',
                    'answer': 'CS will drive AI and Machine Learning advancements, revolutionize healthcare with telemedicine and AI diagnostics, enable smart cities with IoT and data analytics, transform education through personalized learning, advance climate solutions with green tech, improve transportation with autonomous vehicles, enhance cybersecurity for digital safety, democratize access to information and services, create new job opportunities, and solve complex global challenges through computational solutions.',
                    'difficulty': 'Advanced',
                    'topic': 'Future Impact'
                },
                {
                    'question': 'How can I achieve excellence on this path?',
                    'answer': 'Set clear academic and career goals, maintain high GPA through consistent study, build a strong portfolio of projects, participate in coding competitions and hackathons, contribute to open-source projects, network with professionals and alumni, pursue internships and practical experience, stay updated with technology trends, develop soft skills like communication and leadership, seek mentorship from experienced professionals, and maintain a growth mindset throughout your journey.',
                    'difficulty': 'Intermediate',
                    'topic': 'Excellence Strategies'
                },
                {
                    'question': 'Are there any shortcuts?',
                    'answer': 'While there are no true shortcuts to mastering Computer Science, you can optimize your learning by focusing on fundamentals first, using online resources and tutorials for faster learning, joining study groups for collaborative learning, practicing coding daily for muscle memory, building projects to apply knowledge immediately, seeking help from lecturers and peers when stuck, using spaced repetition for memorization, and maintaining consistency rather than cramming. Remember, solid understanding is better than quick fixes.',
                    'difficulty': 'Basic',
                    'topic': 'Learning Strategies'
                }
            ]
        }
    
    def _init_conversational_system(self) -> Dict:
        """Initialize conversational response system"""
        return {
            'greetings': {
                'patterns': ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening'],
                'responses': [
                    "Hello! I'm your intelligent FUT CS Assistant. I'm here to help you with everything about Computer Science at Federal University of Technology. How can I assist you today?",
                    "Hi there! I'm your smart assistant for FUT Computer Science. I can help with courses, career guidance, study tips, and much more. What would you like to know?",
                    "Hey! I'm your FUT CS companion. I'm designed to help you excel in your Computer Science journey. What questions do you have for me?"
                ]
            },
            'thanks': {
                'patterns': ['thank you', 'thanks', 'appreciate', 'grateful'],
                'responses': [
                    "You're very welcome! I'm here to help you succeed in your CS journey. Feel free to ask me anything else!",
                    "My pleasure! I love helping FUT CS students. What else can I assist you with?",
                    "Glad I could help! I'm always here to support your academic success. Ask me anything!"
                ]
            },
            'farewell': {
                'patterns': ['bye', 'goodbye', 'see you', 'farewell'],
                'responses': [
                    "Goodbye! It was great helping you today. Remember, I'm always here to support your CS studies at FUT. Have a wonderful day!",
                    "See you later! Keep up the great work with your studies. Feel free to come back anytime for more help!",
                    "Take care! I hope I've been helpful. Good luck with your Computer Science journey at FUT!"
                ]
            }
        }
    
    def _init_cs_assistant(self) -> Dict:
        """Initialize CS assistant system"""
        return {
            'course_codes': {
                'COS101': 'Introduction to Computer Science - Fundamental concepts, history, and applications',
                'COS102': 'Introduction to Programming - Basic programming concepts using Python',
                'CPT121': 'Introduction to Computer Hardware - Hardware components and maintenance',
                'CPT122': 'Computer Hardware Systems and Maintenance - Advanced hardware systems',
                'MAT101': 'Mathematics for Computer Science - Mathematical foundations for CS'
            },
            'career_paths': {
                'software_engineer': 'Focus on programming, algorithms, and software development',
                'data_scientist': 'Emphasize statistics, machine learning, and data analysis',
                'cybersecurity': 'Study network security, cryptography, and ethical hacking',
                'web_developer': 'Learn front-end and back-end web technologies',
                'system_admin': 'Focus on operating systems, networks, and infrastructure'
            },
            'programming_languages': {
                'python': 'Great for beginners, data science, and web development',
                'java': 'Enterprise applications, Android development',
                'c++': 'System programming, game development, performance-critical applications',
                'javascript': 'Web development, both front-end and back-end',
                'sql': 'Database management and data analysis'
            }
        }
    
    def _init_adaptive_system(self) -> Dict:
        """Initialize adaptive learning system"""
        return {
            'language_styles': {
                'pidgin': {
                    'patterns': ['wetin', 'how far', 'abi', 'dey', 'na', 'sabi', 'wahala'],
                    'response_style': 'casual_nigerian'
                },
                'casual': {
                    'patterns': ['yo', 'sup', 'hey', 'what\'s up', 'cool', 'awesome'],
                    'response_style': 'casual_english'
                },
                'formal': {
                    'patterns': ['could you please', 'may i know', 'kindly provide', 'i would like to know'],
                    'response_style': 'formal_academic'
                }
            },
            'learning_patterns': {
                'struggling_student': 'Provide extra encouragement and simplified explanations',
                'advanced_student': 'Offer deeper insights and advanced resources',
                'new_student': 'Focus on basics and foundational concepts',
                'career_focused': 'Emphasize practical applications and industry relevance'
            }
        }
    
    def _init_fut_api(self) -> Dict:
        """Initialize FUT API integration system"""
        return {
            'admission_info': {
                'requirements': 'UTME 180+, 5 O\'level credits, Post-UTME screening',
                'cut_off': '180 and above',
                'direct_entry': 'A-level, OND, HND qualifications'
            },
            'facilities': {
                'labs': 'Computer Laboratories, Network Laboratory, Software Development Lab',
                'library': 'Modern library with CS resources and e-books',
                'hostels': 'Student accommodation facilities',
                'sports': 'Sports complexes and recreational facilities'
            },
            'programs': {
                'undergraduate': 'B.Sc Computer Science, B.Sc Cyber Security, B.Sc Information Technology',
                'postgraduate': 'M.Sc, M.Tech, Ph.D programs in various CS specializations'
            }
        }
    
    def analyze_question_intelligence(self, question: str, context: str = "") -> Dict:
        """Intelligent analysis of question to determine best response strategy"""
        question_lower = question.lower()
        
        # Check for unrelated questions first
        unrelated_keywords = [
            'cooking', 'recipe', 'food', 'restaurant', 'travel', 'hotel', 'weather',
            'sports', 'football', 'basketball', 'music', 'movie', 'entertainment',
            'fashion', 'shopping', 'beauty', 'health', 'medical', 'politics',
            'religion', 'dating', 'relationship', 'personal', 'private'
        ]
        
        if any(keyword in question_lower for keyword in unrelated_keywords):
            return {
                'type': 'boundary',
                'confidence': 0.95,
                'strategy': 'reject_with_guidance',
                'reasoning': 'Question is outside the scope of CS academic assistance'
            }
        
        # Analyze question complexity and intent
        analysis = {
            'type': 'general',  # Default type
            'complexity': self._assess_complexity(question),
            'intent': self._identify_intent(question),
            'context_needed': self._needs_context(question),
            'language_style': self._detect_language_style(question),
            'user_type': self._infer_user_type(question),
            'response_priority': [],
            'confidence': 0.70,  # Default confidence
            'context_clues': []
        }
        
        # Human-like intent analysis with natural language understanding
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
            'MAT101': ['mat101', 'mat 101', 'mathematics for cs', 'math for computer science', 'discrete mathematics'],
            'MAT121': ['mat121', 'mat 121', 'differential calculus', 'integral calculus', 'calculus', 'mathematics 121'],
            'PHY101': ['phy101', 'phy 101', 'physics 1', 'general physics', 'physics first', 'physics basics'],
            'PHY102': ['phy102', 'phy 102', 'physics 2', 'advanced physics', 'physics second'],
            'CST111': ['cst111', 'cst 111', 'communication', 'english', 'communication skills', 'english skills'],
            'GST112': ['gst112', 'gst 112', 'nigerian culture', 'culture', 'nigerian people', 'cultural studies'],
            'STA111': ['sta111', 'sta 111', 'statistics', 'descriptive statistics', 'stats', 'statistical methods']
        }
        
        # Smart course detection with flexible matching
        detected_courses = []
        for course_code, patterns in course_patterns.items():
            if any(pattern in question_lower for pattern in patterns):
                detected_courses.append(course_code)
                analysis['context_clues'].append(f"Course mentioned: {course_code}")
        
        # Enhanced natural language intent detection with better pattern matching
        # Check for lecturer questions first (before generic patterns) - SUPER SMART
        lecturer_keywords = [
            'who teaches', 'who is the lecturer', 'lecturer for', 'teacher for', 'instructor for', 
            'who handles', 'who takes', 'lecturer', 'teacher', 'instructor', 'teaches', 'who are', 
            'who are the lecturer', 'who are the lecturers', 'lecturers for', 'teachers for', 
            'instructors for', 'who is', 'who are the', 'lecturers', 'teachers', 'instructors',
            'who dey teach', 'who dey', 'dey teach', 'teaching', 'teach us', 'teach me',
            'who is teaching', 'who teaching', 'teaching us', 'teaches us', 'teaches me'
        ]
        
        # Check for course listing questions - SMART PATTERN MATCHING
        course_list_keywords = [
            'list my courses', 'my courses', 'courses', 'list courses', 'show courses',
            'available courses', 'all courses', 'courses available', 'courses do i need',
            'courses should i take', 'list', 'show me courses', 'what courses',
            'courses by', 'my course', 'course list', 'show my courses'
        ]
        
        # Check for materials questions - SMART PATTERN MATCHING  
        materials_keywords = [
            'materials', 'material', 'download', 'downloads', 'books', 'resources',
            'study materials', 'course materials', 'materials for', 'materials do i need',
            'what do i need', 'study guide', 'textbooks', 'learning materials',
            'books do i need', 'materials do i need', 'i need materials', 'need materials',
            'course material', 'this course material', 'materials for this course'
        ]
        
        # SUPER AGGRESSIVE PATTERN MATCHING - Check specific patterns FIRST
        if any(phrase in question_lower for phrase in lecturer_keywords):
            analysis['type'] = 'course_specific'
            analysis['response_priority'] = ['course_specific']
            analysis['confidence'] = 0.95
        elif any(phrase in question_lower for phrase in course_list_keywords):
            analysis['type'] = 'course_general'
            analysis['response_priority'] = ['course_general']
            analysis['confidence'] = 0.95
        elif any(phrase in question_lower for phrase in materials_keywords):
            analysis['type'] = 'materials'
            analysis['response_priority'] = ['materials']
            analysis['confidence'] = 0.95
        elif detected_courses:
            analysis['type'] = 'course_specific'
            analysis['response_priority'] = ['course_specific']
            analysis['confidence'] = 0.95
        # Remove duplicate generic patterns - they're already handled above
        elif any(phrase in question_lower for phrase in ['career', 'job opportunities', 'what can i do', 'future career', 'work after graduation', 'employment', 'career paths', 'job prospects', 'work in tech', 'tech jobs', 'after graduation', 'jobs available', 'jobs can i get', 'degree', 'work with']):
            analysis['type'] = 'cs_guidance'
            analysis['response_priority'] = ['cs_guidance']
            analysis['confidence'] = 0.90
        elif any(phrase in question_lower for phrase in ['study materials', 'books', 'resources', 'what do i need', 'materials for', 'study guide', 'textbooks', 'learning materials', 'books do i need', 'materials do i need']):
            analysis['type'] = 'materials'
            analysis['response_priority'] = ['materials']
            analysis['confidence'] = 0.90
        elif any(phrase in question_lower for phrase in ['how to study', 'study tips', 'how to pass', 'study strategy', 'academic success', 'excel in', 'study methods', 'learning tips', 'study better', 'struggling with', 'succeed in studies']):
            analysis['type'] = 'success_tips'
            analysis['response_priority'] = ['success_tips']
            analysis['confidence'] = 0.85
        elif any(phrase in question_lower for phrase in ['fut', 'university', 'campus', 'facilities', 'admission', 'about fut', 'university info', 'campus life']):
            analysis['type'] = 'fut_info'
            analysis['response_priority'] = ['fut_info']
            analysis['confidence'] = 0.85
        elif any(phrase in question_lower for phrase in ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'greetings', 'new here', 'new student']):
            analysis['type'] = 'conversational'
            analysis['response_priority'] = ['conversational']
            analysis['confidence'] = 0.95
        elif any(phrase in question_lower for phrase in ['thank you', 'thanks', 'appreciate', 'grateful', 'thank you so much']):
            analysis['type'] = 'conversational'
            analysis['response_priority'] = ['conversational']
            analysis['confidence'] = 0.95
        elif any(phrase in question_lower for phrase in ['pdf', 'download', 'access materials', 'course content', 'lecture notes', 'study materials', 'course files']):
            analysis['type'] = 'pdf_content'
            analysis['response_priority'] = ['pdf_content']
            analysis['confidence'] = 0.90
        elif any(phrase in question_lower for phrase in ['past questions', 'previous exams', 'sample questions', 'practice questions', 'exam examples', 'old questions', 'previous papers']):
            analysis['type'] = 'past_questions'
            analysis['response_priority'] = ['past_questions']
            analysis['confidence'] = 0.90
        elif any(phrase in question_lower for phrase in ['help', 'what can you do', 'what do you know', 'capabilities', 'assist', 'support', 'guide me', 'can you help']):
            analysis['type'] = 'general'
            analysis['response_priority'] = ['general_guidance']
            analysis['confidence'] = 0.80
        elif any(phrase in question_lower for phrase in ['wetin', 'how far', 'abi', 'dey', 'na', 'sabi', 'how you dey']):
            analysis['type'] = 'adaptive_learning'
            analysis['response_priority'] = ['adaptive_learning']
            analysis['confidence'] = 0.85
        elif any(phrase in question_lower for phrase in ['yo', 'sup', 'what\'s up', 'cool', 'awesome', 'nice one']):
            analysis['type'] = 'adaptive_learning'
            analysis['response_priority'] = ['adaptive_learning']
            analysis['confidence'] = 0.85
        elif any(phrase in question_lower for phrase in ['computer science', 'cs', 'programming', 'physics', 'statistics', 'hardware', 'web development']):
            # If specific subjects are mentioned, try to route to appropriate course
            if 'programming' in question_lower or 'python' in question_lower:
                analysis['type'] = 'course_specific'
                analysis['response_priority'] = ['course_specific']
                analysis['confidence'] = 0.90
            elif 'physics' in question_lower:
                analysis['type'] = 'course_specific'
                analysis['response_priority'] = ['course_specific']
                analysis['confidence'] = 0.90
            elif 'statistics' in question_lower or 'stats' in question_lower:
                analysis['type'] = 'course_specific'
                analysis['response_priority'] = ['course_specific']
                analysis['confidence'] = 0.90
            elif 'hardware' in question_lower:
                analysis['type'] = 'course_specific'
                analysis['response_priority'] = ['course_specific']
                analysis['confidence'] = 0.90
            else:
                analysis['type'] = 'course_general'
                analysis['response_priority'] = ['course_general']
                analysis['confidence'] = 0.85
        else:
            # Context-aware fallback
            analysis['type'] = 'general'
            analysis['response_priority'] = ['general_guidance']
            analysis['confidence'] = 0.70
        
        return analysis
    
    def _assess_complexity(self, question: str) -> str:
        """Assess question complexity"""
        if len(question.split()) > 15:
            return 'high'
        elif len(question.split()) > 8:
            return 'medium'
        else:
            return 'low'
    
    def _identify_intent(self, question: str) -> str:
        """Identify primary intent"""
        question_lower = question.lower()
        
        if any(word in question_lower for word in ['what', 'tell me', 'explain', 'describe']):
            return 'informational'
        elif any(word in question_lower for word in ['how', 'can i', 'should i', 'what should']):
            return 'guidance'
        elif any(word in question_lower for word in ['why', 'because', 'reason']):
            return 'explanatory'
        elif any(word in question_lower for word in ['when', 'where', 'which']):
            return 'specific'
        else:
            return 'general'
    
    def _needs_context(self, question: str) -> bool:
        """Determine if question needs additional context"""
        context_indicators = ['this', 'that', 'it', 'them', 'here', 'there']
        return any(indicator in question.lower() for indicator in context_indicators)
    
    def _detect_language_style(self, question: str) -> str:
        """Detect language style"""
        question_lower = question.lower()
        
        if any(word in question_lower for word in ['wetin', 'how far', 'abi', 'dey', 'na', 'sabi', 'wahala']):
            return 'pidgin'
        elif any(word in question_lower for word in ['yo', 'sup', 'hey', 'what\'s up', 'cool', 'awesome']):
            return 'casual'
        elif any(word in question_lower for word in ['could you please', 'may i know', 'kindly provide']):
            return 'formal'
        else:
            return 'neutral'
    
    def _infer_user_type(self, question: str) -> str:
        """Infer user type based on question"""
        question_lower = question.lower()
        
        if any(word in question_lower for word in ['100l', '100 level', 'first year', 'freshman']):
            return 'new_student'
        elif any(word in question_lower for word in ['400l', '400 level', 'final year', 'graduating']):
            return 'advanced_student'
        elif any(word in question_lower for word in ['struggling', 'difficult', 'hard', 'confused']):
            return 'struggling_student'
        elif any(word in question_lower for word in ['career', 'job', 'industry', 'work']):
            return 'career_focused'
        else:
            return 'general_student'
    
    def get_unified_response(self, question: str, context: str = "") -> Dict:
        """Get unified intelligent response using all systems with conversation context"""
        
        # Analyze the question with conversation context
        analysis = self.analyze_question_intelligence(question, context)
        
        # Add conversation context awareness
        if self.conversation_memory:
            recent_context = self.conversation_memory[-3:]  # Last 3 interactions
            analysis['conversation_context'] = recent_context
            
            # Check if this is a follow-up question
            if self._is_follow_up_question(question, recent_context):
                analysis['type'] = 'follow_up'
                analysis['response_priority'] = ['contextual_response']
                analysis['confidence'] = 0.90
        
        # Store conversation context
        self.conversation_memory.append({
            'question': question,
            'analysis': analysis,
            'timestamp': datetime.now().isoformat()
        })
        
        # Generate response based on priority strategy
        response = self._generate_unified_response(question, analysis, context)
        
        # Store response for learning
        self.response_history.append({
            'question': question,
            'analysis': analysis,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
        # Keep only last 10 interactions for memory efficiency
        if len(self.conversation_memory) > 10:
            self.conversation_memory = self.conversation_memory[-10:]
        
        return response
    
    def _is_follow_up_question(self, question: str, recent_context: List[Dict]) -> bool:
        """Check if this is a follow-up question based on conversation context"""
        question_lower = question.lower()
        
        # Enhanced follow-up indicators
        follow_up_indicators = [
            'what about', 'how about', 'and', 'also', 'additionally', 'furthermore',
            'can you tell me more', 'more details', 'explain more', 'elaborate',
            'what else', 'anything else', 'other', 'different', 'alternative',
            'who are', 'who is', 'what are', 'what is', 'tell me about',
            'that course', 'this course', 'the course', 'it', 'them', 'they',
            'download', 'materials', 'lecturer', 'teacher', 'instructor',
            'more info', 'more information', 'details', 'explain'
        ]
        
        # Check for follow-up patterns
        if any(indicator in question_lower for indicator in follow_up_indicators):
            return True
        
        # Check if question references previous topics
        for interaction in recent_context:
            prev_question = interaction['question'].lower()
            # Check for common words between current and previous questions
            common_words = set(question_lower.split()) & set(prev_question.split())
            if len(common_words) >= 2:  # At least 2 common words
                return True
        
        return False
    
    def _get_contextual_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get contextual response based on conversation history"""
        if not self.conversation_memory:
            return None
        
        recent_context = self.conversation_memory[-3:]  # Last 3 interactions
        
        # Check if this is a follow-up about a specific course
        for interaction in recent_context:
            prev_question = interaction['question'].lower()
            prev_analysis = interaction.get('analysis', {})
            
            # If previous question was about a course, and current is a follow-up
            if 'course' in prev_question and any(word in question.lower() for word in ['lecturer', 'materials', 'download', 'info', 'details']):
                # Extract course from previous question
                course_code = None
                for level, courses in self.course_database.items():
                    for code, info in courses.items():
                        if code.lower() in prev_question:
                            course_code = code
                            break
                
                if course_code:
                    # Generate contextual response
                    response = f"**Following up on {course_code}:**\n\n"
                    
                    if 'lecturer' in question.lower() or 'teacher' in question.lower():
                        if 'lecturers' in self.course_database.get(level, {}).get(course_code, {}):
                            lecturers = self.course_database[level][course_code]['lecturers']
                            response += f"**👨‍🏫 Lecturers for {course_code}:**\n"
                            for lecturer in lecturers:
                                response += f"• {lecturer}\n"
                        else:
                            response += f"**👨‍🏫 Lecturers for {course_code}:** To be announced\n"
                    
                    if 'materials' in question.lower() or 'download' in question.lower():
                        response += f"\n**📥 Materials for {course_code}:**\n"
                        response += f"• **Syllabus**: http://localhost:8000/download/{course_code}\n"
                        response += f"• **Lecture Notes**: http://localhost:8000/download/{course_code}\n"
                        response += f"• **Past Questions**: http://localhost:8000/download/{course_code}\n"
                        response += f"• **Study Guide**: http://localhost:8000/download/{course_code}\n"
                    
                    response += f"\n**💬 Need more about {course_code}?** Just ask!\n"
                    
                    return {
                        'answer': response,
                        'confidence': 0.95,
                        'strategy_used': 'contextual_response',
                        'source': 'conversation_context'
                    }
        
        return None
    
    def _generate_unified_response(self, question: str, analysis: Dict, context: str) -> Dict:
        """Generate unified response using multiple systems with enhanced conversation context"""
        
        if analysis.get('type') == 'boundary':
            return self._handle_boundary_question(question)
        
        # Check for contextual responses first (follow-up questions)
        if analysis.get('type') == 'follow_up':
            contextual_response = self._get_contextual_response(question, analysis)
            if contextual_response:
                return contextual_response
        
        # Try each response strategy in priority order
        for strategy in analysis['response_priority']:
            response = self._try_response_strategy(question, strategy, analysis, context)
            if response and len(response.get('answer', '')) > 50:
                return response
        
        # Fallback to general response
        return self._generate_general_response(question, analysis)
    
    def _try_response_strategy(self, question: str, strategy: str, analysis: Dict, context: str) -> Optional[Dict]:
        """Try a specific response strategy"""
        
        if strategy == 'course_specific':
            return self._get_course_specific_response(question, analysis)
        elif strategy == 'course_general':
            return self._get_course_general_response(question, analysis)
        elif strategy == 'cs_guidance':
            return self._get_cs_guidance_response(question, analysis)
        elif strategy == 'materials':
            return self._get_materials_response(question, analysis)
        elif strategy == 'success_tips':
            return self._get_success_tips_response(question, analysis)
        elif strategy == 'fut_info':
            return self._get_fut_info_response(question, analysis)
        elif strategy == 'conversational':
            return self._get_conversational_response(question, analysis)
        elif strategy == 'adaptive_learning':
            return self._get_adaptive_response(question, analysis)
        elif strategy == 'general_guidance':
            return self._get_general_guidance_response(question, analysis)
        elif strategy == 'pdf_content':
            return self._get_pdf_content_response(question, analysis)
        elif strategy == 'past_questions':
            return self._get_past_questions_response(question, analysis)
        
        return None
    
    def _get_course_specific_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get course-specific response with detailed information"""
        question_lower = question.lower()
        
        # Check for specific course codes
        for level, courses in self.course_database.items():
            for code, info in courses.items():
                if code.lower() in question_lower:
                    response = f"# 📚 {code} - {info['name']}\n\n"
                    
                    # Basic course information
                    response += f"**📋 Course Details:**\n"
                    response += f"• **Level:** {level.replace('_', ' ').title()}\n"
                    response += f"• **Credits:** {info['credits']}\n"
                    response += f"• **Prerequisites:** {info['prerequisites']}\n\n"
                    
                    # Lecturer information
                    if 'lecturers' in info and info['lecturers']:
                        response += f"**👨‍🏫 Lecturers:**\n"
                        for lecturer in info['lecturers']:
                            response += f"• **{lecturer}**\n"
                        response += "\n"
                    else:
                        response += f"**👨‍🏫 Lecturers:** To be announced\n\n"
                    
                    # Course description
                    response += f"**📖 Course Description:**\n"
                    response += f"{info['description']}\n\n"
                    
                    # Materials needed
                    response += f"**📚 Materials Needed:**\n"
                    for material in info['materials']:
                        response += f"• {material}\n"
                    response += "\n"
                    
                    # Success tips
                    response += f"**💡 Success Tips:**\n"
                    for tip in info['success_tips']:
                        response += f"• {tip}\n"
                    response += "\n"
                    
                    # Assessment and practical information
                    response += f"**📊 Assessment:** {info['assessment']}\n\n"
                    response += f"**👨‍🏫 Office Hours:** {info['lecturer_office_hours']}\n\n"
                    response += f"**🔬 Practical Sessions:** {info['practical_sessions']}\n\n"
                    
                    # Interactive options for students
                    response += "---\n\n"
                    response += "**🎯 Would you like to know more about this course?**\n\n"
                    response += "**📥 Available Materials:**\n"
                    response += "• Course syllabus and outline\n"
                    response += "• Lecture notes and presentations\n"
                    response += "• Assignment guidelines\n"
                    response += "• Past exam questions\n"
                    response += "• Recommended textbooks and resources\n\n"
                    
                    response += "**💬 Ask me about:**\n"
                    response += "• Specific topics in this course\n"
                    response += "• Study strategies for this course\n"
                    response += "• Assignment help and guidance\n"
                    response += "• Exam preparation tips\n"
                    response += "• Download course materials\n\n"
                    
                    response += "**Just ask: 'Can I download materials for {code}?' or 'What topics are covered in {code}?'**\n"
                    
                    return {
                        'answer': response,
                        'confidence': 0.95,
                        'strategy_used': 'course_specific',
                        'source': 'course_database'
                    }
        
        # Handle lecturer-specific questions
        if any(word in question_lower for word in ['lecturer', 'teacher', 'instructor', 'teaches', 'who teaches']):
            for level, courses in self.course_database.items():
                for code, info in courses.items():
                    if code.lower() in question_lower:
                        response = f"**👨‍🏫 Lecturers for {code} - {info['name']}:**\n\n"
                        
                        if 'lecturers' in info and info['lecturers']:
                            for i, lecturer in enumerate(info['lecturers'], 1):
                                response += f"**{i}. {lecturer}**\n"
                        else:
                            response += "Lecturers to be announced\n"
                        
                        response += f"\n**📞 Office Hours:** {info['lecturer_office_hours']}\n"
                        response += f"**🔬 Practical Sessions:** {info['practical_sessions']}\n\n"
                        
                        response += "**💬 Need more information about this course?**\n"
                        response += "Ask me about course materials, topics, or study tips!\n"
                        
                        return {
                            'answer': response,
                            'confidence': 0.95,
                            'strategy_used': 'course_specific',
                            'source': 'course_database'
                        }
        
        return None
    
    def _get_course_general_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get general course information response"""
        question_lower = question.lower()
        
        if 'course' in question_lower:
            response = "# 📚 Computer Science Courses at FUT\n\n"
            
            # Dynamically generate course list from database
            response += "## 🎯 100 LEVEL COURSES\n\n"
            for course_code, course_info in self.course_database['100_level'].items():
                response += f"**{course_code}**: {course_info['name']}\n\n"
            
            response += "## 🎯 200 LEVEL COURSES\n\n"
            response += "**COS201**: Data Structures and Algorithms\n\n"
            response += "**COS202**: Object-Oriented Programming (Java/C++)\n\n"
            response += "**CPT221**: Digital Electronics\n\n"
            response += "**CPT222**: Assembly Language Programming\n\n"
            
            response += "\n\n## 📖 DETAILED COURSE INFORMATION\n\n"
            for course_code, course_info in self.course_database['100_level'].items():
                response += f"### {course_code} - {course_info['name']}\n\n"
                response += f"**📋 Course Details:**\n\n"
                response += f"**Credits:** {course_info['credits']}\n\n"
                response += f"**Prerequisites:** {course_info['prerequisites']}\n\n"
                if 'lecturers' in course_info:
                    response += f"**Lecturers:** {', '.join(course_info['lecturers'])}\n\n"
                else:
                    response += f"**Lecturers:** To be announced\n\n"
                response += f"**Description:** {course_info['description']}\n\n"
                response += "---\n\n"
            
            response += "\n\n## 💡 RECOMMENDED COURSE PROGRESSION\n\n"
            
            response += "### 🎯 First Semester (100 Level)\n\n"
            response += "**COS101** - Start with computer science fundamentals\n\n"
            response += "**CST111** - Develop communication skills\n\n"
            response += "**GST112** - Understand Nigerian culture\n\n"
            response += "**PHY101** - Master physics concepts\n\n"
            response += "**STA111** - Learn statistical methods\n\n"
            
            response += "### 🎯 Second Semester (100 Level)\n\n"
            response += "**COS102** - Build programming skills with Python\n\n"
            response += "**PHY102** - Advanced physics concepts\n\n"
            response += "**CPT121** - Learn computer hardware basics\n\n"
            response += "**FTM-CPT111** - Master probability theory\n\n"
            response += "**FTM-CPT112** - Web development skills\n\n"
            
            response += "## 📚 TYPICAL SEMESTER STRUCTURE\n\n"
            
            response += "### 📖 Academic Load\n\n"
            response += "**5-6 courses** per semester\n\n"
            response += "**15-18 credit hours** total\n\n"
            response += "**Mix of theory and practical** courses\n\n"
            response += "**Continuous assessment** and examinations\n\n"
            
            response += "### ⏰ Study Schedule\n\n"
            response += "**Lectures:** 3-4 hours per day\n\n"
            response += "**Practical sessions:** 2-3 hours per week\n\n"
            response += "**Study time:** 2-3 hours daily\n\n"
            response += "**Project work:** Weekly assignments\n\n"
            
            response += "### 🎯 Success Tips\n\n"
            response += "**Attend all lectures** and practical sessions\n\n"
            response += "**Complete assignments** on time\n\n"
            response += "**Form study groups** with classmates\n\n"
            response += "**Seek help** from lecturers when needed\n\n"
            response += "**Practice programming** regularly\n\n"
            response += "**Stay updated** with course materials\n"
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'course_general',
                'source': 'course_overview'
            }
        
        return None
    
    def _get_cs_guidance_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get CS guidance response"""
        question_lower = question.lower()
        
        if 'career' in question_lower or 'job' in question_lower:
            response = "🚀 **Career Opportunities in Computer Science**\n\n"
            response += "**🎯 SOFTWARE DEVELOPMENT:**\n"
            response += "• Full-stack developer\n"
            response += "• Mobile app developer\n"
            response += "• Game developer\n"
            response += "• DevOps engineer\n\n"
            
            response += "**📊 DATA & ANALYTICS:**\n"
            response += "• Data scientist\n"
            response += "• Data analyst\n"
            response += "• Business intelligence analyst\n"
            response += "• Machine learning engineer\n\n"
            
            response += "**🔒 CYBERSECURITY:**\n"
            response += "• Security analyst\n"
            response += "• Penetration tester\n"
            response += "• Security architect\n"
            response += "• Incident responder\n\n"
            
            response += "**💡 SUCCESS TIPS:**\n"
            response += "• Build a strong portfolio\n"
            response += "• Learn multiple programming languages\n"
            response += "• Contribute to open source projects\n"
            response += "• Network with professionals\n"
            response += "• Stay updated with technology trends\n"
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'cs_guidance',
                'source': 'career_database'
            }
        
        elif 'programming' in question_lower or 'coding' in question_lower:
            response = "💻 **Programming Skills Development**\n\n"
            response += "**🎯 ESSENTIAL LANGUAGES:**\n"
            response += "• **Python**: Great for beginners, data science, web development\n"
            response += "• **Java**: Enterprise applications, Android development\n"
            response += "• **C++**: System programming, game development\n"
            response += "• **JavaScript**: Web development, both front-end and back-end\n"
            response += "• **SQL**: Database management and data analysis\n\n"
            
            response += "**🚀 LEARNING STRATEGIES:**\n"
            response += "• Practice coding daily (even 30 minutes)\n"
            response += "• Build personal projects\n"
            response += "• Solve coding problems on platforms like LeetCode\n"
            response += "• Join programming communities\n"
            response += "• Read code from open source projects\n"
            response += "• Learn version control (Git)\n\n"
            
            response += "**📚 RECOMMENDED RESOURCES:**\n"
            response += "• Codecademy - Interactive courses\n"
            response += "• FreeCodeCamp - Free coding bootcamp\n"
            response += "• W3Schools - Web development tutorials\n"
            response += "• GeeksforGeeks - Programming tutorials\n"
            response += "• Stack Overflow - Q&A community\n"
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'cs_guidance',
                'source': 'programming_guidance'
            }
        
        return None
    
    def _get_materials_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get materials and resources response"""
        question_lower = question.lower()
        
        if 'software' in question_lower:
            response = "🛠️ **Essential Software for CS Students**\n\n"
            response += "**💻 DEVELOPMENT ENVIRONMENTS:**\n"
            response += "• **VS Code**: Free, powerful code editor with extensions\n"
            response += "• **PyCharm**: Professional Python IDE (free Community edition)\n"
            response += "• **IntelliJ IDEA**: Java development environment\n"
            response += "• **Eclipse**: Alternative Java IDE\n"
            response += "• **Sublime Text**: Lightweight code editor\n\n"
            
            response += "**🐍 PROGRAMMING TOOLS:**\n"
            response += "• **Anaconda**: Python distribution with Jupyter Notebook\n"
            response += "• **Git**: Version control system\n"
            response += "• **GitHub Desktop**: GUI for Git\n"
            response += "• **Node.js**: JavaScript runtime for web development\n"
            response += "• **Docker**: Containerization platform\n\n"
            
            response += "**🗄️ DATABASE TOOLS:**\n"
            response += "• **MySQL Workbench**: Database management\n"
            response += "• **PostgreSQL**: Advanced database system\n"
            response += "• **MongoDB Compass**: NoSQL database GUI\n\n"
            
            response += "**🔧 SYSTEM TOOLS:**\n"
            response += "• **VirtualBox**: Virtual machine software\n"
            response += "• **WSL2**: Windows Subsystem for Linux\n"
            response += "• **Chrome DevTools**: Web development debugging\n"
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'materials',
                'source': 'software_database'
            }
        
        elif 'book' in question_lower:
            response = "📖 **Recommended Books for CS Students**\n\n"
            response += "**🎯 PROGRAMMING FUNDAMENTALS:**\n"
            response += "• \"Python Crash Course\" by Eric Matthes\n"
            response += "• \"Automate the Boring Stuff with Python\" by Al Sweigart\n"
            response += "• \"Clean Code\" by Robert Martin\n"
            response += "• \"The Pragmatic Programmer\" by Hunt & Thomas\n\n"
            
            response += "**📊 DATA STRUCTURES & ALGORITHMS:**\n"
            response += "• \"Introduction to Algorithms\" by Cormen et al.\n"
            response += "• \"Cracking the Coding Interview\" by Gayle McDowell\n"
            response += "• \"Algorithm Design Manual\" by Steven Skiena\n\n"
            
            response += "**🔧 COMPUTER HARDWARE:**\n"
            response += "• \"Upgrading and Repairing PCs\" by Scott Mueller\n"
            response += "• \"Computer Organization and Design\" by Patterson & Hennessy\n\n"
            
            response += "**🧮 MATHEMATICS:**\n"
            response += "• \"Discrete Mathematics and Its Applications\" by Rosen\n"
            response += "• \"Mathematics for Computer Science\" by Lehman et al.\n\n"
            
            response += "**💡 SOFTWARE ENGINEERING:**\n"
            response += "• \"Software Engineering\" by Ian Sommerville\n"
            response += "• \"Design Patterns\" by Gang of Four\n"
            response += "• \"System Design Interview\" by Alex Xu\n"
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'materials',
                'source': 'books_database'
            }
        
        elif 'laptop' in question_lower or 'computer' in question_lower:
            response = "💻 **Computer Requirements for CS Students**\n\n"
            response += "**🖥️ MINIMUM SPECIFICATIONS:**\n"
            response += "• **RAM**: 8GB (16GB recommended)\n"
            response += "• **Storage**: 256GB SSD (512GB recommended)\n"
            response += "• **Processor**: Intel i5 or AMD Ryzen 5\n"
            response += "• **Graphics**: Integrated graphics sufficient\n"
            response += "• **OS**: Windows 10/11, macOS, or Linux\n\n"
            
            response += "**💡 RECOMMENDED LAPTOPS:**\n"
            response += "• **Budget**: HP Pavilion, Dell Inspiron (₦150,000-₦250,000)\n"
            response += "• **Mid-range**: MacBook Air, ThinkPad E series (₦300,000-₦500,000)\n"
            response += "• **High-end**: MacBook Pro, Dell XPS (₦600,000+)\n\n"
            
            response += "**🔌 ESSENTIAL ACCESSORIES:**\n"
            response += "• External monitor (24\" or larger)\n"
            response += "• Mechanical keyboard\n"
            response += "• Wireless mouse\n"
            response += "• USB-C hub or docking station\n"
            response += "• External hard drive for backups\n\n"
            
            response += "**📱 MOBILE DEVELOPMENT:**\n"
            response += "• Android device for testing\n"
            response += "• iOS device (if developing for Apple)\n"
            response += "• USB cables for device connection\n"
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'materials',
                'source': 'hardware_database'
            }
        
        elif 'material' in question_lower:
            response = "📚 **Complete Materials List for CS Students**\n\n"
            response += "**💻 HARDWARE ESSENTIALS:**\n"
            response += "• Laptop/Desktop (8GB RAM minimum)\n"
            response += "• External monitor for productivity\n"
            response += "• USB drive for file storage\n"
            response += "• Headphones for online learning\n"
            response += "• Stable internet connection\n\n"
            
            response += "**🛠️ SOFTWARE TOOLS:**\n"
            response += "• Code editors (VS Code, PyCharm)\n"
            response += "• Version control (Git, GitHub)\n"
            response += "• Database tools (MySQL, PostgreSQL)\n"
            response += "• Virtual machine software\n"
            response += "• Office suite (Microsoft Office/LibreOffice)\n\n"
            
            response += "**📖 LEARNING RESOURCES:**\n"
            response += "• Programming textbooks\n"
            response += "• Mathematics reference books\n"
            response += "• Online course subscriptions\n"
            response += "• Coding practice platforms\n"
            response += "• Technical documentation access\n\n"
            
            response += "**📝 STUDY SUPPLIES:**\n"
            response += "• Notebooks for taking notes\n"
            response += "• Pens, pencils, highlighters\n"
            response += "• Sticky notes for reminders\n"
            response += "• Calculator for math courses\n"
            response += "• Folder for organizing papers\n\n"
            
            response += "**📥 DOWNLOAD COURSE MATERIALS:**\n"
            response += "• **COS101 Materials**: http://localhost:8000/download/COS101\n"
            response += "• **COS102 Materials**: http://localhost:8000/download/COS102\n"
            response += "• **MAT121 Materials**: http://localhost:8000/download/MAT121\n"
            response += "• **PHY101 Materials**: http://localhost:8000/download/PHY101\n"
            response += "• **CST111 Materials**: http://localhost:8000/download/CST111\n\n"
            
            response += "**🚀 READY TO DOWNLOAD?**\n"
            response += "**CLICK ANY LINK ABOVE TO DOWNLOAD COURSE MATERIALS!**\n\n"
            response += "**📁 View All Materials**: http://localhost:8000/materials/[COURSE_CODE]\n"
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'materials',
                'source': 'complete_materials_database'
            }
        
        return None
    
    def _get_success_tips_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get success tips response"""
        question_lower = question.lower()
        
        if 'success' in question_lower or 'pass' in question_lower or 'excel' in question_lower:
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
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'success_tips',
                'source': 'success_database'
            }
        
        return None
    
    def _get_fut_info_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get FUT information response"""
        question_lower = question.lower()
        
        if 'admission' in question_lower:
            response = "🎓 **FUT Admission Requirements**\n\n"
            
            admission = self.knowledge_base['admission_requirements']
            response += "**📝 BASIC REQUIREMENTS:**\n"
            response += f"• UTME Score: {admission['utme']}\n"
            response += f"• O'Level: {admission['olevel']}\n"
            response += f"• Subjects: {admission['subjects']}\n"
            response += f"• Cut-off Mark: {admission['cut_off_mark']}\n\n"
            
            response += "**🎯 DIRECT ENTRY:**\n"
            response += f"• Requirements: {admission['direct_entry']}\n"
            response += "• A-level with minimum 2 passes\n"
            response += "• OND/HND with upper credit\n"
            response += "• NCE with merit pass\n\n"
            
            response += "**📋 APPLICATION PROCESS:**\n"
            response += "• Apply through JAMB portal\n"
            response += "• Choose FUT as first choice\n"
            response += "• Participate in Post-UTME screening\n"
            response += "• Submit required documents\n"
            response += "• Pay acceptance fee if admitted\n\n"
            
            response += "**📅 IMPORTANT DATES:**\n"
            response += "• UTME Registration: January-March\n"
            response += "• Post-UTME: July-August\n"
            response += "• Admission List: September\n"
            response += "• Registration: October\n"
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'fut_info',
                'source': 'admission_database'
            }
        
        elif 'facilities' in question_lower:
            response = "🏢 **FUT Campus Facilities**\n\n"
            
            fut_info = self.knowledge_base['fut_general']
            response += "**🏛️ ACADEMIC FACILITIES:**\n"
            response += "• Modern lecture theaters with audio-visual equipment\n"
            response += "• Well-equipped computer laboratories\n"
            response += "• Research laboratories for all departments\n"
            response += "• Central library with e-resources\n"
            response += "• Language laboratory\n\n"
            
            sict = self.knowledge_base['sict_school']
            response += "**💻 SICT SPECIFIC FACILITIES:**\n"
            for facility in sict['facilities']:
                response += f"• {facility}\n"
            response += "• High-speed internet connectivity\n"
            response += "• Modern software development tools\n\n"
            
            response += "**🏠 STUDENT FACILITIES:**\n"
            response += "• Student hostels (male and female)\n"
            response += "• Cafeteria and food courts\n"
            response += "• Sports complex and gymnasium\n"
            response += "• Health center with medical staff\n"
            response += "• Banking facilities (ATM)\n"
            response += "• Bookshop and stationery store\n\n"
            
            response += "**🚌 TRANSPORTATION:**\n"
            response += "• Campus shuttle services\n"
            response += "• Parking facilities for students\n"
            response += "• Easy access to city center\n"
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'fut_info',
                'source': 'facilities_database'
            }
        
        elif 'fut' in question_lower or 'university' in question_lower:
            response = "🏛️ **About Federal University of Technology, Minna**\n\n"
            
            fut_info = self.knowledge_base['fut_general']
            response += "**📖 UNIVERSITY OVERVIEW:**\n"
            response += f"• **Established**: {fut_info['established']}\n"
            response += f"• **Location**: {fut_info['location']}\n"
            response += f"• **Motto**: \"{fut_info['motto']}\"\n"
            response += f"• **Type**: {fut_info['type']}\n"
            response += f"• **Accreditation**: {fut_info['accreditation']}\n\n"
            
            response += "**🎯 MISSION & VISION:**\n"
            response += "• To provide quality technological education\n"
            response += "• To produce skilled graduates for national development\n"
            response += "• To promote research and innovation\n"
            response += "• To serve as a center of excellence in technology\n\n"
            
            response += "**📞 CONTACT INFORMATION:**\n"
            response += f"• **Website**: {fut_info['website']}\n"
            response += f"• **Email**: {fut_info['email']}\n"
            response += f"• **Phone**: {fut_info['phone']}\n"
            response += "• **Address**: P.M.B. 65, Minna, Niger State\n\n"
            
            response += "**🏫 ACADEMIC STRUCTURE:**\n"
            response += "• School of Engineering and Engineering Technology\n"
            response += "• School of Information and Communication Technology\n"
            response += "• School of Environmental Technology\n"
            response += "• School of Agriculture and Agricultural Technology\n"
            response += "• School of Life Sciences\n"
            
            return {
                'answer': response,
                'confidence': 0.90,
                'strategy_used': 'fut_info',
                'source': 'university_overview_database'
            }
        
        return None
    
    def _get_conversational_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get conversational response"""
        question_lower = question.lower()
        
        # Check for greetings
        if any(pattern in question_lower for pattern in self.conversational_system['greetings']['patterns']):
            import random
            response = random.choice(self.conversational_system['greetings']['responses'])
            return {
                'answer': response,
                'confidence': 0.95,
                'strategy_used': 'conversational',
                'source': 'conversational_system'
            }
        
        # Check for thanks
        elif any(pattern in question_lower for pattern in self.conversational_system['thanks']['patterns']):
            import random
            response = random.choice(self.conversational_system['thanks']['responses'])
            return {
                'answer': response,
                'confidence': 0.95,
                'strategy_used': 'conversational',
                'source': 'conversational_system'
            }
        
        # Check for farewell
        elif any(pattern in question_lower for pattern in self.conversational_system['farewell']['patterns']):
            import random
            response = random.choice(self.conversational_system['farewell']['responses'])
            return {
                'answer': response,
                'confidence': 0.95,
                'strategy_used': 'conversational',
                'source': 'conversational_system'
            }
        
        # Check for "how are you" type questions
        elif any(phrase in question_lower for phrase in ['how are you', 'how are you doing', 'what\'s up', 'how do you do']):
            response = "I'm doing fantastic, thank you for asking! I'm your FUT CS Assistant and I'm excited to help you with anything related to Computer Science at Federal University of Technology. What can I help you with today?"
            return {
                'answer': response,
                'confidence': 0.95,
                'strategy_used': 'conversational',
                'source': 'conversational_system'
            }
        
        # Check for "what can you do" type questions
        elif any(phrase in question_lower for phrase in ['what can you do', 'what do you do', 'what are you', 'tell me about yourself']):
            response = "I'm your intelligent FUT CS Assistant! I can help you with:\n\n"
            response += "🎓 **Academic Support:**\n"
            response += "• Course information and details\n"
            response += "• Study materials and resources\n"
            response += "• Success tips and strategies\n\n"
            response += "🏛️ **FUT Information:**\n"
            response += "• University details and history\n"
            response += "• Admission requirements\n"
            response += "• Campus facilities and programs\n\n"
            response += "💻 **CS Guidance:**\n"
            response += "• Career opportunities\n"
            response += "• Programming help\n"
            response += "• Learning resources\n\n"
            response += "What would you like to know about?"
            return {
                'answer': response,
                'confidence': 0.95,
                'strategy_used': 'conversational',
                'source': 'conversational_system'
            }
        
        return None
    
    def _get_adaptive_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get adaptive response based on language style and user type"""
        language_style = analysis.get('language_style', 'neutral')
        user_type = analysis.get('user_type', 'general_student')
        
        if language_style == 'pidgin':
            response = "Wetin you wan know about Computer Science for FUT? I fit help you with course information, materials, and how to succeed. Wetin specific you dey look for?"
            confidence = 0.85
        elif language_style == 'casual':
            response = "Hey! What's up with your CS studies? I can help you with courses, career guidance, study tips, and all things Computer Science at FUT. What do you need help with?"
            confidence = 0.85
        elif language_style == 'formal':
            response = "Good day! I would be pleased to assist you with your Computer Science inquiries at Federal University of Technology. Please let me know what specific information you require."
            confidence = 0.85
        else:
            return None
        
        return {
            'answer': response,
            'confidence': confidence,
            'strategy_used': 'adaptive_learning',
            'source': 'adaptive_system'
        }
    
    def _get_general_guidance_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get general guidance response"""
        response = "🤖 **FUT CS Assistant - How Can I Help?**\n\n"
        
        response += "I'm your intelligent assistant for Computer Science at Federal University of Technology, Minna. I can help you with:\n\n"
        
        response += "**📚 ACADEMIC SUPPORT:**\n"
        response += "• Course information and codes\n"
        response += "• Study materials and resources\n"
        response += "• Success tips and strategies\n"
        response += "• Programming guidance\n\n"
        
        response += "**🏫 FUT INFORMATION:**\n"
        response += "• University details and history\n"
        response += "• Admission requirements\n"
        response += "• Campus facilities\n"
        response += "• Academic programs\n\n"
        
        response += "**💻 CS GUIDANCE:**\n"
        response += "• Career opportunities\n"
        response += "• Learning resources\n"
        response += "• Technical support\n"
        response += "• Study strategies\n\n"
        
        response += "**Ask me anything about:**\n"
        response += "• Specific courses (COS101, COS102, CPT121, etc.)\n"
        response += "• Materials you need for CS\n"
        response += "• How to succeed in your studies\n"
        response += "• FUT programs and requirements\n"
        response += "• Programming help and resources\n\n"
        
        response += "**What would you like to know?**"
        
        return {
            'answer': response,
            'confidence': 0.70,
            'strategy_used': 'general_guidance',
            'source': 'general_system'
        }
    
    def _handle_boundary_question(self, question: str) -> Dict:
        """Handle questions outside the scope"""
        response = "🚫 **I'm a specialized FUT Computer Science Assistant**\n\n"
        
        response += "I'm designed specifically to help FUT Computer Science students with:\n"
        response += "• Course information and codes\n"
        response += "• Study materials and resources\n"
        response += "• Academic success tips\n"
        response += "• Programming and CS guidance\n"
        response += "• FUT-specific information\n\n"
        
        response += "I can't help with topics like cooking, travel, entertainment, or other non-academic subjects.\n\n"
        response += "**How can I help you with your CS studies at FUT?**"
        
        return {
            'answer': response,
            'confidence': 0.95,
            'strategy_used': 'boundary_detection',
            'source': 'boundary_system'
        }
    
    def _get_pdf_content_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get PDF content access response"""
        question_lower = question.lower()
        
        # Check for specific course PDFs
        for course_code, pdf_info in self.pdf_database.items():
            if course_code.lower() in question_lower:
                response = f"📚 **{course_code} - {pdf_info['title']}**\n\n"
                
                response += "**📖 AVAILABLE PDF CONTENT:**\n"
                if isinstance(pdf_info['files'], list):
                    for file in pdf_info['files']:
                        response += f"• {file}\n"
                else:
                    response += f"• {pdf_info['file']}\n"
                
                response += "\n**📋 TOPICS COVERED:**\n"
                for topic in pdf_info['topics']:
                    response += f"• {topic}\n"
                
                if 'key_concepts' in pdf_info:
                    response += "\n**🎯 KEY CONCEPTS:**\n"
                    for concept in pdf_info['key_concepts']:
                        response += f"• {concept}\n"
                
                if 'practice_problems' in pdf_info:
                    response += "\n**💡 PRACTICE PROBLEMS:**\n"
                    for problem in pdf_info['practice_problems']:
                        response += f"• {problem}\n"
                
                        response += "\n**📥 DOWNLOAD OPTIONS:**\n"
                        response += f"• **Course Syllabus** - [Download {course_code} Syllabus](http://localhost:8000/download/{course_code})\n"
                        response += f"• **Lecture Notes** - [Download {course_code} Notes](http://localhost:8000/download/{course_code})\n"
                        response += f"• **Past Questions** - [Download {course_code} Past Questions](http://localhost:8000/download/{course_code})\n"
                        response += f"• **Study Guides** - [Download {course_code} Study Guide](http://localhost:8000/download/{course_code})\n\n"
                        
                        response += "**🚀 READY TO DOWNLOAD?**\n"
                        response += f"**CLICK ANY LINK ABOVE TO DOWNLOAD MATERIALS FOR {course_code}**\n\n"
                        response += f"**🔗 DIRECT DOWNLOAD LINKS:**\n"
                        response += f"• **Syllabus**: http://localhost:8000/download/{course_code}\n"
                        response += f"• **Lecture Notes**: http://localhost:8000/download/{course_code}\n"
                        response += f"• **Past Questions**: http://localhost:8000/download/{course_code}\n"
                        response += f"• **Study Guide**: http://localhost:8000/download/{course_code}\n\n"
                        response += f"**📁 View All Materials**: http://localhost:8000/materials/{course_code}\n\n"
                
                response += "**💡 Study Tips:**\n"
                response += "• Download and review materials regularly\n"
                response += "• Practice with past questions\n"
                response += "• Use study guides for exam preparation\n"
                response += "• Combine with lecture notes for comprehensive understanding\n"
                
                return {
                    'answer': response,
                    'confidence': 0.90,
                    'strategy_used': 'pdf_content',
                    'source': 'pdf_database'
                }
        
        # General PDF access information
        response = "📚 **PDF Content Access Guide**\n\n"
        response += "**📖 AVAILABLE COURSE MATERIALS:**\n"
        for course_code, pdf_info in self.pdf_database.items():
            response += f"• **{course_code}**: {pdf_info['title']}\n"
        
        response += "\n**📁 HOW TO ACCESS PDF CONTENT:**\n"
        response += "• All PDF materials are stored in the pdf_data directory\n"
        response += "• Download the relevant course PDFs for offline study\n"
        response += "• Use PDF readers like Adobe Reader or browser viewers\n"
        response += "• Combine PDF content with our Q&A system for better learning\n\n"
        
        response += "**💡 STUDY TIPS:**\n"
        response += "• Read PDF content first for comprehensive understanding\n"
        response += "• Use our Q&A system to clarify specific concepts\n"
        response += "• Practice with past questions after reading materials\n"
        response += "• Create notes while studying PDF content\n"
        
        return {
            'answer': response,
            'confidence': 0.85,
            'strategy_used': 'pdf_content',
            'source': 'pdf_access_guide'
        }
    
    def _get_past_questions_response(self, question: str, analysis: Dict) -> Optional[Dict]:
        """Get past questions and responses"""
        question_lower = question.lower()
        
        # Check for specific course past questions
        for course_code, questions in self.past_questions.items():
            if course_code.lower() in question_lower:
                response = f"📝 **{course_code} Past Questions & Answers**\n\n"
                
                for i, qa in enumerate(questions, 1):
                    response += f"**{i}. {qa['question']}**\n"
                    response += f"   *Difficulty: {qa['difficulty']} | Topic: {qa['topic']}*\n\n"
                    response += f"   **Answer:** {qa['answer']}\n\n"
                    response += "   " + "─" * 50 + "\n\n"
                
                response += "**💡 STUDY TIPS:**\n"
                response += "• Practice these questions regularly\n"
                response += "• Understand the concepts, don't just memorize\n"
                response += "• Create your own variations of these questions\n"
                response += "• Use these as exam preparation materials\n"
                
                return {
                    'answer': response,
                    'confidence': 0.90,
                    'strategy_used': 'past_questions',
                    'source': 'past_questions_database'
                }
        
        # General past questions information
        response = "📝 **Past Questions & Answers Database**\n\n"
        response += "**📚 AVAILABLE COURSES:**\n"
        for course_code, questions in self.past_questions.items():
            response += f"• **{course_code}**: {len(questions)} questions available\n"
        
        response += "\n**🎯 HOW TO ACCESS PAST QUESTIONS:**\n"
        response += "• Ask specifically for a course (e.g., 'MAT121 past questions')\n"
        response += "• Each course has questions with different difficulty levels\n"
        response += "• Questions include answers and topic classifications\n"
        response += "• Use these for exam preparation and practice\n\n"
        
        response += "**💡 EXAMPLE REQUESTS:**\n"
        response += "• 'Show me MAT121 past questions'\n"
        response += "• 'COS102 previous questions and answers'\n"
        response += "• 'CPT121 example questions'\n"
        response += "• 'Give me past questions for CPT122'\n"
        
        return {
            'answer': response,
            'confidence': 0.85,
            'strategy_used': 'past_questions',
            'source': 'past_questions_guide'
        }
    
    def _generate_general_response(self, question: str, analysis: Dict) -> Dict:
        """Generate general fallback response"""
        return self._get_general_guidance_response(question, analysis)
    
    def learn_from_interaction(self, question: str, response: str, feedback: Optional[str] = None):
        """Learn from user interactions and improve over time"""
        learning_entry = {
            'question': question,
            'response': response,
            'feedback': feedback,
            'timestamp': datetime.now().isoformat(),
            'user_pattern': self._extract_user_pattern(question),
            'successful_response': len(response) > 50 and "FUT CS Assistant - How Can I Help?" not in response
        }
        self.learning_data.append(learning_entry)
        
        # Update pattern recognition based on successful interactions
        self._update_pattern_recognition(learning_entry)
        
        # Keep only last 100 interactions for memory efficiency
        if len(self.learning_data) > 100:
            self.learning_data = self.learning_data[-100:]
    
    def _extract_user_pattern(self, question: str) -> Dict:
        """Extract user interaction patterns for learning"""
        question_lower = question.lower()
        return {
            'length': len(question),
            'has_greeting': any(word in question_lower for word in ['hello', 'hi', 'hey']),
            'has_thanks': any(word in question_lower for word in ['thank', 'thanks']),
            'question_type': self._classify_question_type(question_lower),
            'keywords': [word for word in question_lower.split() if len(word) > 3]
        }
    
    def _classify_question_type(self, question_lower: str) -> str:
        """Classify the type of question for learning"""
        if any(word in question_lower for word in ['course', 'courses']):
            return 'course_inquiry'
        elif any(word in question_lower for word in ['career', 'job', 'work']):
            return 'career_inquiry'
        elif any(word in question_lower for word in ['book', 'material', 'study']):
            return 'materials_inquiry'
        elif any(word in question_lower for word in ['hello', 'hi', 'hey']):
            return 'greeting'
        else:
            return 'general_inquiry'
    
    def _update_pattern_recognition(self, learning_entry: Dict):
        """Update pattern recognition based on successful interactions"""
        if learning_entry.get('successful_response', False):
            # If the response was successful, strengthen similar patterns
            question_lower = learning_entry['question'].lower()
            
            # Update course patterns if it was a successful course question
            if 'course' in question_lower:
                # Add successful patterns to course recognition
                if not hasattr(self, '_successful_patterns'):
                    self._successful_patterns = {}
                if 'courses' not in self._successful_patterns:
                    self._successful_patterns['courses'] = []
                if question_lower not in self._successful_patterns['courses']:
                    self._successful_patterns['courses'].append(question_lower)
            
            # Update career patterns if it was a successful career question
            elif any(word in question_lower for word in ['career', 'job', 'work']):
                if not hasattr(self, '_successful_patterns'):
                    self._successful_patterns = {}
                if 'careers' not in self._successful_patterns:
                    self._successful_patterns['careers'] = []
                if question_lower not in self._successful_patterns['careers']:
                    self._successful_patterns['careers'].append(question_lower)
    
    def get_conversation_summary(self) -> str:
        """Get conversation summary"""
        if not self.conversation_memory:
            return "No conversation history available."
        
        summary = f"**Conversation Summary ({len(self.conversation_memory)} interactions):**\n\n"
        
        for i, context in enumerate(self.conversation_memory[-5:], 1):  # Last 5 interactions
            summary += f"{i}. **Question:** {context['question'][:50]}...\n"
            summary += f"   **Strategy:** {context['analysis'].get('response_priority', ['general'])[0]}\n"
            summary += f"   **Language Style:** {context['analysis'].get('language_style', 'neutral')}\n"
            summary += f"   **User Type:** {context['analysis'].get('user_type', 'general_student')}\n"
            summary += f"   **Time:** {context['timestamp']}\n\n"
        
        return summary
    
    def get_system_status(self) -> Dict:
        """Get unified system status"""
        return {
            'unified_intelligence': 'active',
            'knowledge_base_loaded': len(self.knowledge_base) > 0,
            'course_database_loaded': len(self.course_database) > 0,
            'conversation_memory_count': len(self.conversation_memory),
            'learning_data_count': len(self.learning_data),
            'response_history_count': len(self.response_history),
            'systems_available': [
                'conversational_system',
                'cs_assistant',
                'adaptive_system',
                'fut_api',
                'unified_intelligence'
            ],
            'capabilities': [
                'Intelligent question analysis',
                'Multi-strategy response generation',
                'Language style detection',
                'User type inference',
                'Context-aware responses',
                'Boundary detection',
                'Conversation tracking',
                'Learning from interactions',
                'Unified system coordination'
            ]
        }

# Initialize the unified intelligence system
unified_intelligence = UnifiedIntelligence()
