#!/usr/bin/env python3
"""
Setup script for FUT QA Assistant
Automates the initial setup process
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def create_virtual_environment():
    """Create virtual environment if it doesn't exist"""
    venv_path = Path("backend/.venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    print("🔄 Creating virtual environment...")
    return run_command("cd backend && python -m venv .venv", "Creating virtual environment")

def install_dependencies():
    """Install required dependencies"""
    if os.name == 'nt':  # Windows
        activate_cmd = "backend\\.venv\\Scripts\\activate"
        pip_cmd = f"{activate_cmd} && pip install -r backend/requirements.txt"
    else:  # Unix/Linux/Mac
        activate_cmd = "backend/.venv/bin/activate"
        pip_cmd = f"source {activate_cmd} && pip install -r backend/requirements.txt"
    
    return run_command(pip_cmd, "Installing dependencies")

def create_directories():
    """Create necessary directories"""
    directories = [
        "data/models",
        "data/processed",
        "docs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("✅ Directories created")

def generate_sample_data():
    """Generate sample training data"""
    try:
        from training.data_preparation import main as generate_data
        generate_data()
        print("✅ Sample training data generated")
        return True
    except Exception as e:
        print(f"⚠️  Could not generate sample data: {e}")
        return False

def create_config_file():
    """Create configuration file if it doesn't exist"""
    config_path = Path("backend/config.py")
    if config_path.exists():
        print("✅ Configuration file already exists")
        return True
    
    config_content = '''"""
Configuration file for FUT QA Assistant
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Model settings
MODEL_PATH = BASE_DIR / "data" / "models" / "fut_qa_model"
DEFAULT_MODEL = "distilbert/distilbert-base-cased-distilled-squad"

# API settings
API_HOST = "0.0.0.0"
API_PORT = 8000
DEBUG = True

# CORS settings
ALLOWED_ORIGINS = ["*"]  # Change this in production

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
'''
    
    try:
        with open(config_path, 'w') as f:
            f.write(config_content)
        print("✅ Configuration file created")
        return True
    except Exception as e:
        print(f"❌ Failed to create config file: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up FUT QA Assistant...")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Create virtual environment
    if not create_virtual_environment():
        print("❌ Setup failed at virtual environment creation")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed at dependency installation")
        sys.exit(1)
    
    # Create config file
    if not create_config_file():
        print("❌ Setup failed at config file creation")
        sys.exit(1)
    
    # Generate sample data
    generate_sample_data()
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate your virtual environment:")
    if os.name == 'nt':  # Windows
        print("   backend\\.venv\\Scripts\\activate")
    else:
        print("   source backend/.venv/bin/activate")
    
    print("2. Start the backend server:")
    print("   cd backend && python app.py")
    
    print("3. Open frontend/index.html in your browser")
    print("4. Train your model using training/train_model.ipynb in Google Colab")
    
    print("\n📚 For more information, check the README.md file")

if __name__ == "__main__":
    main()
