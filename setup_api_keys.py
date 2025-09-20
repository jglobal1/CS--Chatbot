#!/usr/bin/env python3
"""
Setup script for API keys
"""

import os

def setup_api_keys():
    """Interactive setup for API keys"""
    print("🔑 API Key Setup for External LLM Integration")
    print("=" * 50)
    print("This script will help you configure API keys for external LLMs.")
    print("You can get API keys from:")
    print("• OpenAI: https://platform.openai.com/api-keys")
    print("• Google Gemini: https://makersuite.google.com/app/apikey")
    print("• Hugging Face: https://huggingface.co/settings/tokens")
    print()
    
    # Get API keys from user
    openai_key = input("Enter your OpenAI API key (or press Enter to skip): ").strip()
    gemini_key = input("Enter your Google Gemini API key (or press Enter to skip): ").strip()
    hf_key = input("Enter your Hugging Face API key (or press Enter to skip): ").strip()
    
    # Create environment variables
    if openai_key:
        os.environ['OPENAI_API_KEY'] = openai_key
        print("✅ OpenAI API key set!")
    
    if gemini_key:
        os.environ['GEMINI_API_KEY'] = gemini_key
        print("✅ Google Gemini API key set!")
    
    if hf_key:
        os.environ['HUGGINGFACE_API_KEY'] = hf_key
        print("✅ Hugging Face API key set!")
    
    # Update config file
    config_path = "backend/config.py"
    if os.path.exists(config_path):
        print(f"\n📝 Updating {config_path}...")
        
        # Read current config
        with open(config_path, 'r') as f:
            content = f.read()
        
        # Update API keys
        if openai_key:
            content = content.replace('"your_openai_key_here"', f'"{openai_key}"')
        if gemini_key:
            content = content.replace('"your_gemini_key_here"', f'"{gemini_key}"')
        if hf_key:
            content = content.replace('"your_hf_key_here"', f'"{hf_key}"')
        
        # Write updated config
        with open(config_path, 'w') as f:
            f.write(content)
        
        print("✅ Config file updated!")
    
    print("\n🎉 Setup complete!")
    print("You can now start your backend with:")
    print("cd backend && python app.py")
    
    # Test the configuration
    print("\n🧪 Testing configuration...")
    try:
        from backend.config import ExternalAPIConfig
        available_apis = ExternalAPIConfig.get_available_apis()
        print(f"✅ Available APIs: {', '.join(available_apis) if available_apis else 'None'}")
    except Exception as e:
        print(f"❌ Error testing config: {e}")

if __name__ == "__main__":
    setup_api_keys()
