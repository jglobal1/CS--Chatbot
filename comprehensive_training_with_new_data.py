#!/usr/bin/env python3
"""
Comprehensive Training Script with New Course Data and Lecturer Information
Includes all 100-level CS courses, lecturers, and the new questions
"""

import json
import os
from datetime import datetime

def create_comprehensive_training_data():
    """Create comprehensive training data with all new information"""
    
    print("🚀 Creating Comprehensive Training Data with New Course Information...")
    
    # Comprehensive training data with all new courses and lecturers
    training_data = [
        # Course-specific questions with lecturer information
        {
            "context": "COS101 - Introduction to Computer Science is taught by Umar alkali, O. Ojerinde O, Abisoye O. A, Lawal OLamilekan Lawal, and Bashir Suleiman. It covers fundamental concepts of computer science, history, and applications.",
            "question": "Who teaches COS101?",
            "answers": {"text": ["Umar alkali", "O. Ojerinde O", "Abisoye O. A", "Lawal OLamilekan Lawal", "Bashir Suleiman"], "answer_start": [0]}
        },
        {
            "context": "COS102 - Introduction to Problem Solving is taught by Sadiu Admed Abubakar, Shuaibu M Badeggi, Ibrahim Shehi Shehu, Abubakar Suleiman T, and Lasotte yakubu. It covers basic programming concepts and problem-solving techniques using Python.",
            "question": "Who are the lecturers for COS102?",
            "answers": {"text": ["Sadiu Admed Abubakar", "Shuaibu M Badeggi", "Ibrahim Shehi Shehu", "Abubakar Suleiman T", "Lasotte yakubu"], "answer_start": [0]}
        },
        {
            "context": "PHY101 - General Physics I is taught by Aku Ibrahim. It covers fundamental concepts of physics including mechanics, waves, and thermodynamics.",
            "question": "Who teaches PHY101?",
            "answers": {"text": ["Aku Ibrahim"], "answer_start": [0]}
        },
        {
            "context": "PHY102 - General Physics II is taught by Dr. Julia Elchie. It covers advanced physics concepts including electricity, magnetism, and modern physics.",
            "question": "Who is the lecturer for PHY102?",
            "answers": {"text": ["Dr. Julia Elchie"], "answer_start": [0]}
        },
        {
            "context": "CST111 - Communication in English is taught by Okeli Chike, Amina Gogo Tafida, and Halima Shehu. It covers English language skills for academic and professional communication.",
            "question": "Who teaches CST111?",
            "answers": {"text": ["Okeli Chike", "Amina Gogo Tafida", "Halima Shehu"], "answer_start": [0]}
        },
        {
            "context": "GST112 - Nigerian Peoples and Culture is taught by Isah Usman. It covers Nigerian cultural diversity, traditions, and social structures.",
            "question": "Who is the lecturer for GST112?",
            "answers": {"text": ["Isah Usman"], "answer_start": [0]}
        },
        {
            "context": "STA111 - Descriptive Statistics is taught by Olayiwola Adelutu. It covers statistical methods, data analysis, and probability.",
            "question": "Who teaches STA111?",
            "answers": {"text": ["Olayiwola Adelutu"], "answer_start": [0]}
        },
        {
            "context": "FTM-CPT111 - Probability for Computer Science is taught by Saliu adam muhammad and Saidu Ahmed Abubakar. It covers probability theory and its applications in computer science.",
            "question": "Who are the lecturers for FTM-CPT111?",
            "answers": {"text": ["Saliu adam muhammad", "Saidu Ahmed Abubakar"], "answer_start": [0]}
        },
        {
            "context": "FTM-CPT112 - Front End Web Development is taught by Benjamin Alenoghen, Lawal Olamilekan Lawal, Iosotte Yakubu, and Benjamin Alenoghena. It covers web development using HTML, CSS, and JavaScript.",
            "question": "Who teaches FTM-CPT112?",
            "answers": {"text": ["Benjamin Alenoghen", "Lawal Olamilekan Lawal", "Iosotte Yakubu", "Benjamin Alenoghena"], "answer_start": [0]}
        },
        {
            "context": "FTM-CPT192 - Introduction to Computer Hardware is taught by Benjamin Alenoghen. It covers fundamental concepts of computer hardware components and systems.",
            "question": "Who is the lecturer for FTM-CPT192?",
            "answers": {"text": ["Benjamin Alenoghen"], "answer_start": [0]}
        },
        
        # New comprehensive questions with detailed answers
        {
            "context": "Computer Science offers diverse career paths including Software Development (Full-stack, Mobile, Game development), Data Science & Analytics, Cybersecurity, Artificial Intelligence & Machine Learning, Web Development, System Administration, Database Administration, Network Engineering, Cloud Computing, DevOps, IT Consulting, Research & Academia, and Entrepreneurship in tech startups.",
            "question": "What career paths are available in Computer Science?",
            "answers": {"text": ["Software Development", "Data Science & Analytics", "Cybersecurity", "Artificial Intelligence & Machine Learning", "Web Development", "System Administration", "Database Administration", "Network Engineering", "Cloud Computing", "DevOps", "IT Consulting", "Research & Academia", "Entrepreneurship in tech startups"], "answer_start": [0]}
        },
        {
            "context": "To balance academics with other responsibilities, create a structured schedule with dedicated study time, prioritize tasks using the Eisenhower Matrix, use time-blocking techniques, set realistic goals, learn to say no to non-essential activities, maintain a healthy work-life balance, use productivity tools and apps, join study groups for efficiency, communicate with lecturers about challenges, and remember that quality study time is more important than quantity.",
            "question": "How do I balance academics with other responsibilities?",
            "answers": {"text": ["Create a structured schedule", "Prioritize tasks using the Eisenhower Matrix", "Use time-blocking techniques", "Set realistic goals", "Learn to say no to non-essential activities", "Maintain a healthy work-life balance", "Use productivity tools and apps", "Join study groups for efficiency", "Communicate with lecturers about challenges"], "answer_start": [0]}
        },
        {
            "context": "To get access to associations or organizations for Computer Science Students, join the Computer Science Students Association (CSSA) at FUT, participate in ACM (Association for Computing Machinery) student chapter, join IEEE Computer Society, attend tech meetups and conferences, participate in hackathons and coding competitions, join online communities like Stack Overflow, GitHub, and LinkedIn groups, volunteer for tech events, and network with industry professionals through these organizations.",
            "question": "How do I get access to associations or organizations for Computer Science Students?",
            "answers": {"text": ["Join the Computer Science Students Association (CSSA) at FUT", "Participate in ACM (Association for Computing Machinery) student chapter", "Join IEEE Computer Society", "Attend tech meetups and conferences", "Participate in hackathons and coding competitions", "Join online communities like Stack Overflow, GitHub, and LinkedIn groups", "Volunteer for tech events", "Network with industry professionals"], "answer_start": [0]}
        },
        {
            "context": "Computer Science provides a strong foundation in algorithms, data structures, and computational thinking that applies across all ICT fields. CS graduates have deeper understanding of software development, system design, and problem-solving methodologies. The mathematical and theoretical foundation in CS provides better analytical skills, while the programming expertise gives CS students an advantage in automation, AI, and emerging technologies. CS also offers more diverse career opportunities and higher earning potential.",
            "question": "What edge does Computer Science have over other departments in ICT?",
            "answers": {"text": ["Strong foundation in algorithms, data structures, and computational thinking", "Deeper understanding of software development, system design, and problem-solving methodologies", "Better analytical skills from mathematical and theoretical foundation", "Advantage in automation, AI, and emerging technologies", "More diverse career opportunities and higher earning potential"], "answer_start": [0]}
        },
        {
            "context": "FUT has well-equipped computer laboratories for CS students including the SICT Computer Laboratory with modern workstations, Network Laboratory for networking courses, Software Development Lab with programming environments, Hardware Maintenance Lab for hands-on hardware training, Research Laboratory for advanced projects, and 24/7 access labs for student use. These labs are equipped with the latest software, development tools, and high-speed internet connectivity.",
            "question": "Are there any Computer labs for Computer Science Students?",
            "answers": {"text": ["SICT Computer Laboratory with modern workstations", "Network Laboratory for networking courses", "Software Development Lab with programming environments", "Hardware Maintenance Lab for hands-on hardware training", "Research Laboratory for advanced projects", "24/7 access labs for student use"], "answer_start": [0]}
        },
        {
            "context": "Essential skills for Computer Science students include Programming (Python, Java, C++, JavaScript), Problem-solving and Algorithmic thinking, Data Structures and Algorithms, Database Management (SQL, NoSQL), Version Control (Git), Web Development (HTML, CSS, JavaScript), Software Engineering principles, Mathematics and Statistics, Communication skills, Teamwork and collaboration, Continuous learning mindset, Debugging and testing skills, and Project management abilities.",
            "question": "What are the essential skills for a Computer Science Student?",
            "answers": {"text": ["Programming (Python, Java, C++, JavaScript)", "Problem-solving and Algorithmic thinking", "Data Structures and Algorithms", "Database Management (SQL, NoSQL)", "Version Control (Git)", "Web Development (HTML, CSS, JavaScript)", "Software Engineering principles", "Mathematics and Statistics", "Communication skills", "Teamwork and collaboration", "Continuous learning mindset", "Debugging and testing skills", "Project management abilities"], "answer_start": [0]}
        },
        {
            "context": "CS graduates can work in Technology (Google, Microsoft, Apple), Finance (Banks, Fintech), Healthcare (Medical software, Health tech), E-commerce (Amazon, Shopify), Gaming (Game development studios), Education (EdTech companies), Government (Digital services), Manufacturing (Automation, IoT), Entertainment (Streaming platforms), Transportation (Uber, Tesla), Energy (Smart grids), and virtually any industry that uses technology.",
            "question": "What industries can a Computer Science Student work in?",
            "answers": {"text": ["Technology (Google, Microsoft, Apple)", "Finance (Banks, Fintech)", "Healthcare (Medical software, Health tech)", "E-commerce (Amazon, Shopify)", "Gaming (Game development studios)", "Education (EdTech companies)", "Government (Digital services)", "Manufacturing (Automation, IoT)", "Entertainment (Streaming platforms)", "Transportation (Uber, Tesla)", "Energy (Smart grids)", "Virtually any industry that uses technology"], "answer_start": [0]}
        },
        {
            "context": "Computer Science will drive AI and Machine Learning advancements, revolutionize healthcare with telemedicine and AI diagnostics, enable smart cities with IoT and data analytics, transform education through personalized learning, advance climate solutions with green tech, improve transportation with autonomous vehicles, enhance cybersecurity for digital safety, democratize access to information and services, create new job opportunities, and solve complex global challenges through computational solutions in the next 15 years.",
            "question": "What can Computer Science contribute to society in the next 15 years?",
            "answers": {"text": ["Drive AI and Machine Learning advancements", "Revolutionize healthcare with telemedicine and AI diagnostics", "Enable smart cities with IoT and data analytics", "Transform education through personalized learning", "Advance climate solutions with green tech", "Improve transportation with autonomous vehicles", "Enhance cybersecurity for digital safety", "Democratize access to information and services", "Create new job opportunities", "Solve complex global challenges through computational solutions"], "answer_start": [0]}
        },
        {
            "context": "To achieve excellence in Computer Science, set clear academic and career goals, maintain high GPA through consistent study, build a strong portfolio of projects, participate in coding competitions and hackathons, contribute to open-source projects, network with professionals and alumni, pursue internships and practical experience, stay updated with technology trends, develop soft skills like communication and leadership, seek mentorship from experienced professionals, and maintain a growth mindset throughout your journey.",
            "question": "How can I achieve excellence on this path?",
            "answers": {"text": ["Set clear academic and career goals", "Maintain high GPA through consistent study", "Build a strong portfolio of projects", "Participate in coding competitions and hackathons", "Contribute to open-source projects", "Network with professionals and alumni", "Pursue internships and practical experience", "Stay updated with technology trends", "Develop soft skills like communication and leadership", "Seek mentorship from experienced professionals", "Maintain a growth mindset throughout your journey"], "answer_start": [0]}
        },
        {
            "context": "While there are no true shortcuts to mastering Computer Science, you can optimize your learning by focusing on fundamentals first, using online resources and tutorials for faster learning, joining study groups for collaborative learning, practicing coding daily for muscle memory, building projects to apply knowledge immediately, seeking help from lecturers and peers when stuck, using spaced repetition for memorization, and maintaining consistency rather than cramming. Remember, solid understanding is better than quick fixes.",
            "question": "Are there any shortcuts?",
            "answers": {"text": ["Focus on fundamentals first", "Use online resources and tutorials for faster learning", "Join study groups for collaborative learning", "Practice coding daily for muscle memory", "Build projects to apply knowledge immediately", "Seek help from lecturers and peers when stuck", "Use spaced repetition for memorization", "Maintain consistency rather than cramming", "Solid understanding is better than quick fixes"], "answer_start": [0]}
        },
        
        # PDF content access questions
        {
            "context": "PDF materials are available for all courses including MAT121 Differential and Integral Calculus, COS102 Introduction to Programming, CPT121 Computer Hardware, and CPT122 Hardware Systems. These PDFs contain comprehensive course content, lecture notes, practice problems, and detailed explanations.",
            "question": "How can I access PDF materials for my courses?",
            "answers": {"text": ["PDF materials are stored in the pdf_data directory", "Download the relevant course PDFs for offline study", "Use PDF readers like Adobe Reader or browser viewers", "Combine PDF content with Q&A system for better learning"], "answer_start": [0]}
        },
        {
            "context": "MAT121 Differential and Integral Calculus PDF covers topics including Limits and Continuity, Derivatives and Differentiation Rules, Applications of Derivatives, Integration Techniques, Applications of Integration, and Differential Equations. Key concepts include Chain rule and product rule, Implicit differentiation, Related rates problems, Optimization problems, Integration by parts, Partial fractions, and Area and volume calculations.",
            "question": "What topics are covered in the MAT121 PDF?",
            "answers": {"text": ["Limits and Continuity", "Derivatives and Differentiation Rules", "Applications of Derivatives", "Integration Techniques", "Applications of Integration", "Differential Equations"], "answer_start": [0]}
        },
        
        # Past questions and examples
        {
            "context": "Past questions are available for all courses including MAT121, COS102, CPT121, and CPT122. These include questions with different difficulty levels (Basic, Intermediate, Advanced) and cover various topics within each course. Students can use these for exam preparation and practice.",
            "question": "How can I access past questions for exam preparation?",
            "answers": {"text": ["Ask specifically for a course (e.g., 'MAT121 past questions')", "Each course has questions with different difficulty levels", "Questions include answers and topic classifications", "Use these for exam preparation and practice"], "answer_start": [0]}
        },
        {
            "context": "Example MAT121 questions include: 'What is the derivative of x² + 3x + 2?' (Answer: 2x + 3), 'How do you solve integration by parts?' (Answer: Use formula ∫u dv = uv - ∫v du), and 'What are the applications of derivatives in optimization?' (Answer: Find maximum and minimum values by setting f'(x) = 0).",
            "question": "What are some example MAT121 questions?",
            "answers": {"text": ["What is the derivative of x² + 3x + 2? (Answer: 2x + 3)", "How do you solve integration by parts? (Answer: Use formula ∫u dv = uv - ∫v du)", "What are the applications of derivatives in optimization? (Answer: Find maximum and minimum values by setting f'(x) = 0)"], "answer_start": [0]}
        }
    ]
    
    # Save the comprehensive training data
    output_file = "comprehensive_training_with_new_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(training_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Created comprehensive training data with {len(training_data)} examples")
    print(f"📁 Saved to: {output_file}")
    
    # Summary of data
    course_questions = len([ex for ex in training_data if "COS" in ex["context"] or "PHY" in ex["context"] or "CST" in ex["context"] or "GST" in ex["context"] or "STA" in ex["context"] or "FTM-CPT" in ex["context"]])
    career_questions = len([ex for ex in training_data if "career" in ex["context"].lower() or "industry" in ex["context"].lower()])
    pdf_questions = len([ex for ex in training_data if "PDF" in ex["context"] or "pdf" in ex["context"]])
    past_questions = len([ex for ex in training_data if "past questions" in ex["context"].lower() or "example" in ex["context"].lower()])
    
    print(f"\n📊 Training Data Summary:")
    print(f"   - Course-specific questions: {course_questions}")
    print(f"   - Career guidance questions: {career_questions}")
    print(f"   - PDF content questions: {pdf_questions}")
    print(f"   - Past questions examples: {past_questions}")
    print(f"   - Total examples: {len(training_data)}")
    
    print(f"\n🎯 New Features Included:")
    print(f"   ✅ All 100-level CS courses with lecturers")
    print(f"   ✅ Comprehensive career guidance")
    print(f"   ✅ PDF content access information")
    print(f"   ✅ Past questions and examples")
    print(f"   ✅ Academic success strategies")
    print(f"   ✅ Professional development guidance")
    
    return output_file

def create_lecturer_database():
    """Create a comprehensive lecturer database"""
    
    lecturer_database = {
        "COS101": {
            "course": "Introduction to Computer Science",
            "lecturers": [
                {"name": "Umar alkali", "role": "Lead Lecturer"},
                {"name": "O. Ojerinde O", "role": "Co-Lecturer"},
                {"name": "Abisoye O. A", "role": "Co-Lecturer"},
                {"name": "Lawal OLamilekan Lawal", "role": "Co-Lecturer"},
                {"name": "Bashir Suleiman", "role": "Co-Lecturer"}
            ]
        },
        "COS102": {
            "course": "Introduction to Problem Solving",
            "lecturers": [
                {"name": "Sadiu Admed Abubakar", "role": "Lead Lecturer"},
                {"name": "Shuaibu M Badeggi", "role": "Co-Lecturer"},
                {"name": "Ibrahim Shehi Shehu", "role": "Co-Lecturer"},
                {"name": "Abubakar Suleiman T", "role": "Co-Lecturer"},
                {"name": "Lasotte yakubu", "role": "Co-Lecturer"}
            ]
        },
        "PHY101": {
            "course": "General Physics I",
            "lecturers": [
                {"name": "Aku Ibrahim", "role": "Lecturer"}
            ]
        },
        "PHY102": {
            "course": "General Physics II",
            "lecturers": [
                {"name": "Dr. Julia Elchie", "role": "Lecturer"}
            ]
        },
        "CST111": {
            "course": "Communication in English",
            "lecturers": [
                {"name": "Okeli Chike", "role": "Lead Lecturer"},
                {"name": "Amina Gogo Tafida", "role": "Co-Lecturer"},
                {"name": "Halima Shehu", "role": "Co-Lecturer"}
            ]
        },
        "GST112": {
            "course": "Nigerian Peoples and Culture",
            "lecturers": [
                {"name": "Isah Usman", "role": "Lecturer"}
            ]
        },
        "STA111": {
            "course": "Descriptive Statistics",
            "lecturers": [
                {"name": "Olayiwola Adelutu", "role": "Lecturer"}
            ]
        },
        "FTM-CPT111": {
            "course": "Probability for Computer Science",
            "lecturers": [
                {"name": "Saliu adam muhammad", "role": "Lead Lecturer"},
                {"name": "Saidu Ahmed Abubakar", "role": "Co-Lecturer"}
            ]
        },
        "FTM-CPT112": {
            "course": "Front End Web Development",
            "lecturers": [
                {"name": "Benjamin Alenoghen", "role": "Lead Lecturer"},
                {"name": "Lawal Olamilekan Lawal", "role": "Co-Lecturer"},
                {"name": "Iosotte Yakubu", "role": "Co-Lecturer"},
                {"name": "Benjamin Alenoghena", "role": "Co-Lecturer"}
            ]
        },
        "FTM-CPT192": {
            "course": "Introduction to Computer Hardware",
            "lecturers": [
                {"name": "Benjamin Alenoghen", "role": "Lecturer"}
            ]
        }
    }
    
    # Save lecturer database
    with open("lecturer_database.json", "w", encoding="utf-8") as f:
        json.dump(lecturer_database, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Created lecturer database with {len(lecturer_database)} courses")
    return "lecturer_database.json"

if __name__ == "__main__":
    print("=" * 80)
    print("🚀 COMPREHENSIVE TRAINING DATA CREATION")
    print("=" * 80)
    
    # Create comprehensive training data
    training_file = create_comprehensive_training_data()
    
    # Create lecturer database
    lecturer_file = create_lecturer_database()
    
    print("\n" + "=" * 80)
    print("🎉 COMPREHENSIVE TRAINING DATA CREATION COMPLETE!")
    print("=" * 80)
    print(f"✅ Training data: {training_file}")
    print(f"✅ Lecturer database: {lecturer_file}")
    print(f"✅ All 100-level CS courses included")
    print(f"✅ All lecturers and course information added")
    print(f"✅ Comprehensive Q&A database created")
    print(f"✅ Ready for model training!")
    print("\n🚀 Next steps:")
    print("1. Train the model with the new comprehensive data")
    print("2. Test the system with course and lecturer questions")
    print("3. Verify PDF content access functionality")
    print("4. Test past questions and examples")
    print("5. Deploy the enhanced system")
