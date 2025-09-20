#!/usr/bin/env python3
"""
Script to help upload training data to Google Colab
This script creates a downloadable file with your training data
"""

import json
import os
from pathlib import Path

def create_colab_upload_file():
    """Create a file that can be easily uploaded to Google Colab"""
    
    # Read the comprehensive training data
    data_file = Path("data/raw/fut_comprehensive_training_data.json")
    
    if not data_file.exists():
        print("❌ Training data file not found!")
        return False
    
    with open(data_file, 'r', encoding='utf-8') as f:
        training_data = json.load(f)
    
    # Create a simple upload file
    upload_file = Path("fut_training_data_for_colab.json")
    
    with open(upload_file, 'w', encoding='utf-8') as f:
        json.dump(training_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Created upload file: {upload_file}")
    print(f"📊 Training data contains {len(training_data)} examples")
    
    # Show sample data
    print("\n📋 Sample training data:")
    for i, example in enumerate(training_data[:3]):
        print(f"\nExample {i+1}:")
        print(f"  Question: {example['question']}")
        print(f"  Answer: {example['answers']['text'][0]}")
        print(f"  Context: {example['context'][:100]}...")
    
    print(f"\n🚀 UPLOAD METHODS:")
    print(f"\n📁 Method 1 - Direct to Google Drive:")
    print(f"1. Go to drive.google.com")
    print(f"2. Click 'New' → 'File upload'")
    print(f"3. Select '{upload_file}' from your computer")
    print(f"4. Make sure it goes to Drive root (not in any folder)")
    
    print(f"\n💻 Method 2 - From Google Colab:")
    print(f"1. Open colab.research.google.com")
    print(f"2. Create new notebook")
    print(f"3. Run this code in a cell:")
    print(f"   from google.colab import files")
    print(f"   uploaded = files.upload()")
    print(f"4. Click 'Choose Files' and select '{upload_file}'")
    print(f"5. Then run this to copy to Drive:")
    print(f"   from google.colab import drive")
    print(f"   drive.mount('/content/drive')")
    print(f"   import shutil")
    print(f"   shutil.copy('{upload_file}', '/content/drive/MyDrive/')")
    
    print(f"\n📋 After uploading:")
    print(f"1. Open the training notebook in Google Colab")
    print(f"2. The notebook will automatically find your data")
    print(f"3. Run all training cells")
    
    return True

if __name__ == "__main__":
    create_colab_upload_file()
