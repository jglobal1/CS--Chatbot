#!/usr/bin/env python3
"""
Process Raw Data for FUT QA Assistant Training
Handles PDFs, text files, and other raw data sources
"""

import os
import json
import re
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    try:
        import PyPDF2
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except ImportError:
        print("❌ PyPDF2 not installed. Install with: pip install PyPDF2")
        return None
    except Exception as e:
        print(f"❌ Error reading PDF {pdf_path}: {e}")
        return None

def extract_text_from_txt(txt_path):
    """Extract text from text file"""
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"❌ Error reading text file {txt_path}: {e}")
        return None

def clean_text(text):
    """Clean and preprocess text"""
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)]', '', text)
    
    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    
    # Filter out very short sentences
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    
    return sentences

def create_training_examples_from_text(text, source_name):
    """Create training examples from extracted text"""
    sentences = clean_text(text)
    examples = []
    
    # Create question-answer pairs from sentences
    for i, sentence in enumerate(sentences[:50]):  # Limit to first 50 sentences
        if len(sentence) > 30:  # Only use substantial sentences
            # Create a simple question
            question = f"What information is available about {source_name}?"
            
            # Use the sentence as context and answer
            context = sentence
            answer = sentence[:100] + "..." if len(sentence) > 100 else sentence
            
            examples.append({
                "context": context,
                "question": question,
                "answers": {
                    "text": [answer],
                    "answer_start": [0]
                }
            })
    
    return examples

def process_raw_data_directory(data_dir="raw_data"):
    """Process all raw data files in a directory"""
    if not os.path.exists(data_dir):
        print(f"❌ Directory {data_dir} not found. Creating it...")
        os.makedirs(data_dir, exist_ok=True)
        print(f"📁 Please put your PDFs, text files, etc. in the {data_dir} directory")
        return []
    
    all_examples = []
    
    # Process PDF files
    for pdf_file in Path(data_dir).glob("*.pdf"):
        print(f"📄 Processing PDF: {pdf_file.name}")
        text = extract_text_from_pdf(str(pdf_file))
        if text:
            examples = create_training_examples_from_text(text, pdf_file.stem)
            all_examples.extend(examples)
            print(f"✅ Extracted {len(examples)} examples from {pdf_file.name}")
    
    # Process text files
    for txt_file in Path(data_dir).glob("*.txt"):
        print(f"📄 Processing text file: {txt_file.name}")
        text = extract_text_from_txt(str(txt_file))
        if text:
            examples = create_training_examples_from_text(text, txt_file.stem)
            all_examples.extend(examples)
            print(f"✅ Extracted {len(examples)} examples from {txt_file.name}")
    
    return all_examples

def create_conversational_examples():
    """Create conversational training examples for human-like responses"""
    conversational_examples = [
        {
            "context": "Hello! I'm the FUT QA Assistant. I can help you with questions about Federal University of Technology, including academic programs, admission requirements, campus information, and student services.",
            "question": "Hi, how are you?",
            "answers": {
                "text": ["Hello! I'm doing great, thank you for asking! I'm here to help you with any questions about FUT. How can I assist you today?"],
                "answer_start": [0]
            }
        },
        {
            "context": "The FUT QA Assistant is designed to help students, prospective students, and visitors with information about Federal University of Technology. I can provide details about programs, admissions, campus life, and academic resources.",
            "question": "What's up?",
            "answers": {
                "text": ["Hey there! I'm here and ready to help you with any questions about FUT. What would you like to know?"],
                "answer_start": [0]
            }
        },
        {
            "context": "I'm the FUT QA Assistant, your friendly guide to all things Federal University of Technology. Whether you're a current student, prospective student, or just curious about the university, I'm here to help!",
            "question": "How are you doing?",
            "answers": {
                "text": ["I'm doing fantastic, thank you! I'm excited to help you learn more about FUT. What questions do you have for me today?"],
                "answer_start": [0]
            }
        },
        {
            "context": "The FUT QA Assistant is always ready to help with questions about Federal University of Technology. I can provide information about academic programs, campus facilities, student life, and much more.",
            "question": "What can you help me with?",
            "answers": {
                "text": ["I can help you with information about FUT's academic programs, admission requirements, campus facilities, student services, and much more! What specific information are you looking for?"],
                "answer_start": [0]
            }
        },
        {
            "context": "Federal University of Technology offers various programs in engineering, technology, and applied sciences. The university provides excellent academic resources and student support services.",
            "question": "Tell me about FUT",
            "answers": {
                "text": ["Federal University of Technology (FUT) is a Nigerian university focused on technology and engineering education. We offer various programs in engineering, technology, and applied sciences with excellent academic resources and student support services."],
                "answer_start": [0]
            }
        }
    ]
    
    return conversational_examples

def main():
    """Main processing function"""
    print("🚀 Processing raw data for FUT QA Assistant training...")
    
    # Process raw data files
    raw_examples = process_raw_data_directory()
    print(f"📊 Extracted {len(raw_examples)} examples from raw data")
    
    # Create conversational examples
    conversational_examples = create_conversational_examples()
    print(f"💬 Created {len(conversational_examples)} conversational examples")
    
    # Load existing training data
    existing_data = []
    if os.path.exists("combined_training_data.json"):
        with open("combined_training_data.json", "r") as f:
            existing_data = json.load(f)
        print(f"📚 Loaded {len(existing_data)} existing examples")
    
    # Combine all data
    all_examples = existing_data + raw_examples + conversational_examples
    
    # Save comprehensive training data
    with open("comprehensive_training_data.json", "w") as f:
        json.dump(all_examples, f, indent=2)
    
    print(f"✅ Created comprehensive training data with {len(all_examples)} examples")
    print(f"📁 Saved to: comprehensive_training_data.json")
    print("\n🎯 Next steps:")
    print("1. Put your PDFs and text files in the 'raw_data' directory")
    print("2. Run this script again to process them")
    print("3. Use the comprehensive_training_data.json for training")

if __name__ == "__main__":
    main()
