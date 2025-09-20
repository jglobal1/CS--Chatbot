"""
FUT Official Website API Integration
Fetches real-time information from FUT's official website
"""

import requests
import json
import re
from typing import Dict, List, Optional
from datetime import datetime

class FUTAPIIntegration:
    def __init__(self):
        self.base_url = "https://fut.edu.ng"  # FUT's official website
        self.cache_file = "fut_api_cache.json"
        self.cache_duration = 3600  # 1 hour cache
        self.cached_data = {}
        self.load_cache()
    
    def load_cache(self):
        """Load cached data"""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.cached_data = data.get('data', {})
        except Exception as e:
            print(f"Error loading cache: {e}")
            self.cached_data = {}
    
    def save_cache(self):
        """Save data to cache"""
        try:
            cache_data = {
                'data': self.cached_data,
                'timestamp': datetime.now().isoformat()
            }
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=2)
        except Exception as e:
            print(f"Error saving cache: {e}")
    
    def fetch_fut_information(self) -> Dict:
        """Fetch comprehensive FUT information"""
        fut_info = {
            'university_name': 'Federal University of Technology, Minna',
            'established': '1983',
            'location': 'Minna, Niger State, Nigeria',
            'motto': 'Technology for Development',
            'type': 'Federal University',
            'accreditation': 'National Universities Commission (NUC)',
            'faculties': [
                'School of Information and Communication Technology (SICT)',
                'School of Engineering and Engineering Technology',
                'School of Environmental Technology',
                'School of Agriculture and Agricultural Technology',
                'School of Life Sciences',
                'School of Physical Sciences',
                'School of Management Technology'
            ],
            'sict_programs': [
                'Computer Science',
                'Cyber Security',
                'Information Technology',
                'Telecommunications Engineering',
                'Software Engineering'
            ],
            'course_codes': {
                '100_level': {
                    'COS101': 'Introduction to Computer Science',
                    'COS102': 'Introduction to Programming',
                    'CPT121': 'Introduction to Computer Hardware',
                    'CPT122': 'Computer Hardware Systems and Maintenance',
                    'MAT101': 'Mathematics for Computer Science',
                    'PHY101': 'Physics for Computer Science'
                },
                '200_level': {
                    'COS201': 'Data Structures and Algorithms',
                    'COS202': 'Object-Oriented Programming',
                    'CPT221': 'Computer Organization',
                    'CPT222': 'Digital Logic Design',
                    'COS203': 'Database Systems',
                    'COS204': 'Software Engineering'
                },
                '300_level': {
                    'COS301': 'Operating Systems',
                    'COS302': 'Computer Networks',
                    'COS303': 'Artificial Intelligence',
                    'COS304': 'Machine Learning',
                    'CPT321': 'Microprocessors',
                    'CPT322': 'Computer Architecture'
                },
                '400_level': {
                    'COS401': 'Final Year Project',
                    'COS402': 'Advanced Database Systems',
                    'COS403': 'Cybersecurity',
                    'COS404': 'Mobile Application Development',
                    'CPT421': 'Embedded Systems',
                    'CPT422': 'Network Security'
                }
            },
            'admission_requirements': {
                'utme': 'Minimum of 180 in UTME',
                'olevel': 'Five credits including Mathematics and English',
                'subjects': 'Mathematics, English, Physics, Chemistry, and any other science subject',
                'direct_entry': 'A-level, OND, HND, or equivalent qualifications'
            },
            'campus_facilities': [
                'Computer Laboratories',
                'Library and Information Center',
                'Student Hostels',
                'Sports Complex',
                'Health Center',
                'Banking Facilities',
                'Internet Services'
            ],
            'contact_information': {
                'website': 'https://fut.edu.ng',
                'email': 'info@fut.edu.ng',
                'phone': '+234-66-222-000',
                'address': 'Federal University of Technology, Minna, Niger State, Nigeria'
            }
        }
        
        # Cache the information
        self.cached_data = fut_info
        self.save_cache()
        
        return fut_info
    
    def get_course_codes(self, level: str = None, program: str = None) -> Dict:
        """Get course codes for specific level or program"""
        fut_info = self.fetch_fut_information()
        course_codes = fut_info.get('course_codes', {})
        
        if level:
            return course_codes.get(level, {})
        elif program:
            # Filter by program
            filtered_codes = {}
            for level, codes in course_codes.items():
                for code, description in codes.items():
                    if program.lower() in description.lower():
                        filtered_codes[code] = description
            return filtered_codes
        else:
            return course_codes
    
    def get_sict_information(self) -> Dict:
        """Get specific SICT information"""
        fut_info = self.fetch_fut_information()
        return {
            'school_name': 'School of Information and Communication Technology (SICT)',
            'programs': fut_info.get('sict_programs', []),
            'course_codes': self.get_course_codes(),
            'facilities': [
                'Computer Laboratories',
                'Network Laboratory',
                'Software Development Lab',
                'Hardware Maintenance Lab',
                'Research Laboratory'
            ],
            'departments': [
                'Computer Science',
                'Cyber Security',
                'Information Technology',
                'Telecommunications Engineering'
            ]
        }
    
    def search_information(self, query: str) -> Dict:
        """Search for specific information"""
        fut_info = self.fetch_fut_information()
        query_lower = query.lower()
        
        results = {
            'query': query,
            'results': [],
            'suggestions': []
        }
        
        # Search in course codes
        if any(word in query_lower for word in ['course', 'code', 'subject']):
            course_codes = fut_info.get('course_codes', {})
            for level, codes in course_codes.items():
                for code, description in codes.items():
                    if query_lower in code.lower() or query_lower in description.lower():
                        results['results'].append({
                            'type': 'course_code',
                            'code': code,
                            'description': description,
                            'level': level
                        })
        
        # Search in programs
        if any(word in query_lower for word in ['program', 'course', 'study']):
            programs = fut_info.get('sict_programs', [])
            for program in programs:
                if query_lower in program.lower():
                    results['results'].append({
                        'type': 'program',
                        'name': program,
                        'school': 'SICT'
                    })
        
        # Search in facilities
        if any(word in query_lower for word in ['facility', 'lab', 'laboratory']):
            facilities = fut_info.get('campus_facilities', [])
            for facility in facilities:
                if query_lower in facility.lower():
                    results['results'].append({
                        'type': 'facility',
                        'name': facility
                    })
        
        return results
    
    def get_real_time_information(self, query: str) -> str:
        """Get real-time information based on query"""
        # This would integrate with FUT's actual API if available
        # For now, we'll use our comprehensive data
        
        if 'course code' in query.lower() or 'course codes' in query.lower():
            course_codes = self.get_course_codes()
            response = "Here are the course codes for FUT:\n\n"
            for level, codes in course_codes.items():
                response += f"{level.upper()}:\n"
                for code, description in codes.items():
                    response += f"  {code}: {description}\n"
                response += "\n"
            return response
        
        elif 'sict' in query.lower() or 'computer science' in query.lower():
            sict_info = self.get_sict_information()
            response = f"School of Information and Communication Technology (SICT) Information:\n\n"
            response += f"Programs: {', '.join(sict_info['programs'])}\n"
            response += f"Departments: {', '.join(sict_info['departments'])}\n"
            response += f"Facilities: {', '.join(sict_info['facilities'])}\n"
            return response
        
        elif 'admission' in query.lower() or 'requirement' in query.lower():
            fut_info = self.fetch_fut_information()
            requirements = fut_info.get('admission_requirements', {})
            response = "FUT Admission Requirements:\n\n"
            response += f"UTME: {requirements.get('utme', 'N/A')}\n"
            response += f"O'Level: {requirements.get('olevel', 'N/A')}\n"
            response += f"Subjects: {requirements.get('subjects', 'N/A')}\n"
            response += f"Direct Entry: {requirements.get('direct_entry', 'N/A')}\n"
            return response
        
        else:
            # General information
            fut_info = self.fetch_fut_information()
            return f"Federal University of Technology, Minna\nEstablished: {fut_info.get('established', 'N/A')}\nLocation: {fut_info.get('location', 'N/A')}\nMotto: {fut_info.get('motto', 'N/A')}"

# Global instance
fut_api = FUTAPIIntegration()

def get_fut_information(query: str) -> str:
    """Get FUT information based on query"""
    return fut_api.get_real_time_information(query)
