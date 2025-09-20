#!/usr/bin/env python3
"""
Data Preparation Script for FUT QA Assistant
Converts various data formats to the required training format
"""

import json
import csv
import os
from typing import List, Dict, Any
import re

def create_qa_pairs_from_text(text: str, questions: List[str]) -> List[Dict[str, Any]]:
    """
    Create QA pairs from a text and a list of questions
    
    Args:
        text: The context text
        questions: List of questions to ask about the text
        
    Returns:
        List of QA pairs in the required format
    """
    qa_pairs = []
    
    for question in questions:
        # Simple answer extraction (you can improve this)
        # For now, we'll create a basic structure
        qa_pair = {
            "context": text,
            "question": question,
            "answers": {
                "text": ["[Answer to be filled manually]"],
                "answer_start": [0]
            }
        }
        qa_pairs.append(qa_pair)
    
    return qa_pairs

def convert_csv_to_qa(csv_file: str, context_column: str, question_column: str, answer_column: str) -> List[Dict[str, Any]]:
    """
    Convert CSV file to QA format
    
    Args:
        csv_file: Path to CSV file
        context_column: Name of column containing context
        question_column: Name of column containing questions
        answer_column: Name of column containing answers
        
    Returns:
        List of QA pairs
    """
    qa_pairs = []
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Find answer position in context
            context = row[context_column]
            answer = row[answer_column]
            answer_start = context.find(answer)
            
            if answer_start == -1:
                answer_start = 0
            
            qa_pair = {
                "context": context,
                "question": row[question_column],
                "answers": {
                    "text": [answer],
                    "answer_start": [answer_start]
                }
            }
            qa_pairs.append(qa_pair)
    
    return qa_pairs

def save_qa_data(qa_pairs: List[Dict[str, Any]], output_file: str):
    """
    Save QA pairs to JSON file
    
    Args:
        qa_pairs: List of QA pairs
        output_file: Output file path
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(qa_pairs, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(qa_pairs)} QA pairs to {output_file}")

def create_sample_fut_data():
    """
    Create sample FUT-specific training data
    """
    sample_data = [
        {
            "context": "The Federal University of Technology (FUT) was established in 1981 by the Federal Government of Nigeria. It was created to provide high-quality technical education and produce graduates with practical skills in engineering, technology, and applied sciences.",
            "question": "When was FUT established and by whom?",
            "answers": {
                "text": ["1981 by the Federal Government of Nigeria"],
                "answer_start": [52]
            }
        },
        {
            "context": "FUT offers Bachelor of Technology (B.Tech) degrees in various engineering disciplines. The university also offers Master of Technology (M.Tech) and Doctor of Philosophy (Ph.D.) programs for postgraduate students. All programs are accredited by the National Universities Commission (NUC).",
            "question": "What degree programs does FUT offer?",
            "answers": {
                "text": ["Bachelor of Technology (B.Tech), Master of Technology (M.Tech), and Doctor of Philosophy (Ph.D.) programs"],
                "answer_start": [0]
            }
        },
        {
            "context": "The university campus features modern laboratories, workshops, computer centers, and research facilities. Students have access to industry-standard equipment for practical training. The campus also includes student housing, sports facilities, and a health center.",
            "question": "What facilities are available on the FUT campus?",
            "answers": {
                "text": ["modern laboratories, workshops, computer centers, research facilities, industry-standard equipment, student housing, sports facilities, and a health center"],
                "answer_start": [47]
            }
        }
    ]
    
    return sample_data

def main():
    """Main function to demonstrate data preparation"""
    
    # Create sample data
    print("Creating sample FUT training data...")
    sample_data = create_sample_fut_data()
    
    # Save sample data
    output_dir = "../data/raw"
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, "fut_training_data.json")
    save_qa_data(sample_data, output_file)
    
    print("\nData preparation complete!")
    print(f"Sample data saved to: {output_file}")
    print("\nNext steps:")
    print("1. Review and edit the generated data")
    print("2. Add more FUT-specific questions and answers")
    print("3. Use the data to train your model in Google Colab")
    print("4. Download the trained model to data/models/")

if __name__ == "__main__":
    main()
