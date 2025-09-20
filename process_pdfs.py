#!/usr/bin/env python3
"""
Process PDF documents for FUT QA Assistant Academic Training
Extracts text from PDFs and creates training examples
"""

import os
import json
import re
from pathlib import Path
import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file with better error handling"""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num, page in enumerate(reader.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += f"Page {page_num + 1}: {page_text}\n"
                except Exception as e:
                    print(f"Warning: Could not extract text from page {page_num + 1} of {pdf_path}: {e}")
                    continue
        return text
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
        return None

def clean_and_process_text(text):
    """Clean and process extracted text"""
    if not text:
        return []
    
    # Remove extra whitespace and clean text
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)]', '', text)
    
    # Split into paragraphs
    paragraphs = [p.strip() for p in text.split('\n') if len(p.strip()) > 50]
    
    # Filter out very short or very long paragraphs
    paragraphs = [p for p in paragraphs if 50 <= len(p) <= 1000]
    
    return paragraphs

def create_training_examples_from_text(text, source_name):
    """Create training examples from extracted text"""
    paragraphs = clean_and_process_text(text)
    examples = []
    
    for i, paragraph in enumerate(paragraphs[:20]):  # Limit to first 20 paragraphs
        if len(paragraph) > 50:
            # Create different types of questions
            questions = [
                f"What information is available about {source_name}?",
                f"What does {source_name} cover?",
                f"What are the details about {source_name}?",
                f"What can you tell me about {source_name}?",
                f"What is mentioned about {source_name}?"
            ]
            
            # Use the paragraph as context and create a summary as answer
            context = paragraph
            answer = paragraph[:150] + "..." if len(paragraph) > 150 else paragraph
            
            for question in questions:
                examples.append({
                    "context": context,
                    "question": question,
                    "answers": {
                        "text": [answer],
                        "answer_start": [0]
                    }
                })
    
    return examples

def process_pdf_directory(pdf_dir="pdf_data"):
    """Process all PDF files in a directory"""
    if not os.path.exists(pdf_dir):
        print(f"❌ Directory {pdf_dir} not found. Creating it...")
        os.makedirs(pdf_dir, exist_ok=True)
        print(f"📁 Please put your PDF files in the {pdf_dir} directory")
        return []
    
    all_examples = []
    pdf_files = list(Path(pdf_dir).glob("*.pdf"))
    
    if not pdf_files:
        print(f"📁 No PDF files found in {pdf_dir} directory")
        print(f"💡 Please add your PDF files to the {pdf_dir} directory and run this script again")
        return []
    
    print(f"📚 Found {len(pdf_files)} PDF files to process...")
    
    for pdf_file in pdf_files:
        print(f"📄 Processing PDF: {pdf_file.name}")
        text = extract_text_from_pdf(str(pdf_file))
        
        if text:
            examples = create_training_examples_from_text(text, pdf_file.stem)
            all_examples.extend(examples)
            print(f"✅ Extracted {len(examples)} examples from {pdf_file.name}")
        else:
            print(f"❌ Could not extract text from {pdf_file.name}")
    
    return all_examples

def create_academic_training_data():
    """Create comprehensive academic training data"""
    
    # Process PDFs
    pdf_examples = process_pdf_directory()
    print(f"📊 Extracted {len(pdf_examples)} examples from PDFs")
    
    # Load existing training data
    existing_data = []
    if os.path.exists("enhanced_training_data.json"):
        with open("enhanced_training_data.json", "r") as f:
            existing_data = json.load(f)
        print(f"📚 Loaded {len(existing_data)} existing examples")
    
    # Create additional academic examples
    additional_academic_examples = [
        {
            "context": "Federal University of Technology (FUT) is a Nigerian university focused on technology and engineering education. The university offers various programs in engineering, technology, and applied sciences.",
            "question": "What is Federal University of Technology?",
            "answers": {
                "text": ["Federal University of Technology (FUT) is a Nigerian university focused on technology and engineering education"],
                "answer_start": [0]
            }
        },
        {
            "context": "FUT offers undergraduate and postgraduate programs in various fields including Computer Science, Electrical Engineering, Mechanical Engineering, Civil Engineering, and Information Technology.",
            "question": "What programs does FUT offer?",
            "answers": {
                "text": ["undergraduate and postgraduate programs in various fields including Computer Science, Electrical Engineering, Mechanical Engineering, Civil Engineering, and Information Technology"],
                "answer_start": [0]
            }
        },
        {
            "context": "The admission requirements for FUT include a minimum of five credits in relevant subjects including Mathematics and English, and a good score in the Unified Tertiary Matriculation Examination (UTME).",
            "question": "What are the admission requirements for FUT?",
            "answers": {
                "text": ["minimum of five credits in relevant subjects including Mathematics and English, and a good score in the Unified Tertiary Matriculation Examination (UTME)"],
                "answer_start": [0]
            }
        }
    ]
    
    # Combine all data
    all_examples = existing_data + pdf_examples + additional_academic_examples
    
    # Save comprehensive training data
    with open("comprehensive_academic_training_data.json", "w") as f:
        json.dump(all_examples, f, indent=2)
    
    print(f"✅ Created comprehensive academic training data with {len(all_examples)} examples")
    print(f"📊 Breakdown:")
    print(f"   - Existing examples: {len(existing_data)}")
    print(f"   - PDF examples: {len(pdf_examples)}")
    print(f"   - Additional academic: {len(additional_academic_examples)}")
    print(f"   - Total: {len(all_examples)}")
    
    return "comprehensive_academic_training_data.json"

def main():
    """Main processing function"""
    print("🚀 Processing PDF documents for FUT QA Assistant academic training...")
    
    # Create academic training data
    data_file = create_academic_training_data()
    
    print(f"✅ Academic training data ready: {data_file}")
    print("\n🎯 Next steps:")
    print("1. Add your PDF files to the 'pdf_data' directory")
    print("2. Run this script again to process them")
    print("3. Use the comprehensive_academic_training_data.json for training")

if __name__ == "__main__":
    main()
