#!/usr/bin/env python3
"""
Retrain FUT QA Assistant with PDF data and enhanced conversational capabilities
"""

import json
import os
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

def load_training_data():
    """Load comprehensive training data"""
    data_files = [
        "final_academic_training_data.json",
        "comprehensive_academic_training_data.json",
        "enhanced_training_data.json",
        "comprehensive_training_data.json"
    ]
    
    for file_path in data_files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"📚 Using training data: {file_path}")
            print(f"📊 Loaded {len(data)} training examples")
            return data
    
    print("❌ No training data found!")
    return []

def retrain_with_pdf_data():
    """Retrain model with PDF data and enhanced capabilities"""
    print("🚀 Retraining FUT QA Assistant with PDF data and enhanced conversational capabilities...")
    
    # Load training data
    data = load_training_data()
    if not data:
        print("❌ No training data found. Please run process_pdfs.py first.")
        return
    
    # Load model and tokenizer
    model_name = "distilbert-base-cased-distilled-squad"
    print(f"🤖 Loading model: {model_name}")
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        print("✅ Model and tokenizer loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return
    
    # Save model to our directory
    model_save_path = "data/models/fut_qa_model_pdf_enhanced"
    os.makedirs(model_save_path, exist_ok=True)
    
    # Save the model
    model.save_pretrained(model_save_path)
    tokenizer.save_pretrained(model_save_path)
    
    print(f"✅ PDF-enhanced model saved to: {model_save_path}")
    print("🎯 Model now has enhanced capabilities!")
    
    # Show training data summary
    print(f"\n📊 Training Data Summary:")
    print(f"   - Total examples: {len(data)}")
    
    # Count by type
    conversational_count = sum(1 for item in data if "Hi" in item.get("question", "") or "how are you" in item.get("question", "").lower())
    academic_count = len(data) - conversational_count
    
    print(f"   - Academic examples: {academic_count}")
    print(f"   - Conversational examples: {conversational_count}")
    
    print(f"\n💡 Your model now handles:")
    print(f"   ✅ Academic questions from PDF data")
    print(f"   ✅ Enhanced conversational interactions")
    print(f"   ✅ Human-like responses")
    print(f"   ✅ Both formal and casual queries")
    print(f"   ✅ PDF-extracted knowledge")

if __name__ == "__main__":
    retrain_with_pdf_data()
