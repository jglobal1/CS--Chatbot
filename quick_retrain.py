#!/usr/bin/env python3
"""
Quick Retraining Script for FUT QA Assistant
Run this to quickly retrain your model with new data before defense
"""

import json
import torch
from transformers import (
    AutoTokenizer, 
    AutoModelForQuestionAnswering, 
    TrainingArguments, 
    Trainer,
    DefaultDataCollator
)
from datasets import Dataset
import os

def load_training_data(data_path):
    """Load training data from JSON file"""
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def prepare_dataset(data):
    """Convert data to HuggingFace dataset format"""
    contexts = []
    questions = []
    answers = []
    
    for item in data:
        contexts.append(item['context'])
        questions.append(item['question'])
        
        # Handle both answer formats
        if 'answers' in item:
            if isinstance(item['answers'], dict):
                answers.append({
                    'text': item['answers']['text'],
                    'answer_start': item['answers']['answer_start']
                })
            else:
                answers.append(item['answers'])
        else:
            # Create dummy answer if not provided
            answers.append({
                'text': [item['context'][:50] + "..."],
                'answer_start': [0]
            })
    
    return Dataset.from_dict({
        'context': contexts,
        'question': questions,
        'answers': answers
    })

def tokenize_function(examples, tokenizer):
    """Tokenize the examples"""
    questions = [q.strip() for q in examples["question"]]
    contexts = [c.strip() for c in examples["context"]]
    
    tokenized = tokenizer(
        questions,
        contexts,
        truncation="only_second",
        max_length=512,
        stride=128,
        return_overflowing_tokens=True,
        return_offsets_mapping=True,
        padding="max_length",
    )
    
    # Find answer positions
    offset_mapping = tokenized.pop("offset_mapping")
    sample_map = tokenized.pop("overflow_to_sample_mapping")
    answers = examples["answers"]
    start_positions = []
    end_positions = []
    
    for i, offset in enumerate(offset_mapping):
        sample_idx = sample_map[i]
        answer = answers[sample_idx]
        start_char = answer["answer_start"][0] if answer["answer_start"] else 0
        end_char = start_char + len(answer["text"][0]) if answer["text"] else 1
        
        # Find token positions
        start_token = None
        end_token = None
        for token_idx, (token_start, token_end) in enumerate(offset):
            if token_start <= start_char < token_end:
                start_token = token_idx
            if token_start < end_char <= token_end:
                end_token = token_idx
                break
        
        start_positions.append(start_token if start_token is not None else 0)
        end_positions.append(end_token if end_token is not None else 1)
    
    tokenized["start_positions"] = start_positions
    tokenized["end_positions"] = end_positions
    return tokenized

def quick_retrain():
    """Quick retraining function"""
    print("🚀 Starting quick retraining for your defense...")
    
    # Check for training data
    training_files = [
        "combined_training_data.json",
        "sict_training_data_for_colab.json",
        "fut_training_data_for_colab.json",
        "data/raw/fut_comprehensive_training_data.json"
    ]
    
    training_data_path = None
    for file_path in training_files:
        if os.path.exists(file_path):
            training_data_path = file_path
            break
    
    if not training_data_path:
        print("❌ No training data found! Please add your training data.")
        return
    
    print(f"📚 Using training data: {training_data_path}")
    
    # Load data
    data = load_training_data(training_data_path)
    print(f"📊 Loaded {len(data)} training examples")
    
    # Load model and tokenizer
    model_name = "distilbert-base-cased-distilled-squad"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    
    # Prepare dataset
    dataset = prepare_dataset(data)
    tokenized_dataset = dataset.map(
        lambda examples: tokenize_function(examples, tokenizer),
        batched=True,
        remove_columns=dataset.column_names,
    )
    
    # Split dataset
    train_size = int(0.8 * len(tokenized_dataset))
    train_dataset = tokenized_dataset.select(range(train_size))
    eval_dataset = tokenized_dataset.select(range(train_size, len(tokenized_dataset)))
    
    # Training arguments
    training_args = TrainingArguments(
        output_dir="./fut_qa_model_quick",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        num_train_epochs=3,  # Quick training for defense
        weight_decay=0.01,
        save_strategy="epoch",
        load_best_model_at_end=True,
        report_to=None,  # Disable wandb
    )
    
    # Data collator
    data_collator = DefaultDataCollator()
    
    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )
    
    # Train
    print("🔥 Starting training...")
    trainer.train()
    
    # Save model
    model_save_path = "data/models/fut_qa_model_quick"
    os.makedirs(model_save_path, exist_ok=True)
    trainer.save_model(model_save_path)
    tokenizer.save_pretrained(model_save_path)
    
    print(f"✅ Model saved to: {model_save_path}")
    print("🎯 Ready for your defense!")

if __name__ == "__main__":
    quick_retrain()
