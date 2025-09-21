# 🔒 Security Setup Guide

## API Keys Removed from Code

All hardcoded API keys have been removed from the codebase for security. You now need to set up your API keys using environment variables.

## Quick Setup

### Option 1: Automated Setup (Recommended)
```bash
python setup_environment.py
```

### Option 2: Manual Setup
1. Copy the template: `cp env_template.txt .env`
2. Edit `.env` with your actual API keys
3. Never commit the `.env` file to git

## Required API Keys

| Service | Purpose | Get Key From |
|---------|---------|--------------|
| **OpenAI** | Primary AI responses | https://platform.openai.com/api-keys |
| **Google Gemini** | Alternative AI provider | https://makersuite.google.com/app/apikey |
| **Groq** | Fast AI responses | https://console.groq.com/keys |
| **Hugging Face** | Model hosting | https://huggingface.co/settings/tokens |

## Security Features

✅ **Environment Variables**: All API keys now use `os.getenv()`  
✅ **Git Ignore**: `.env` files are automatically ignored  
✅ **Error Handling**: Graceful failure when keys are missing  
✅ **Template System**: Easy setup with `env_template.txt`  

## Testing Your Setup

```bash
# Test all API connections
python test_external_api.py

# Test individual services
python test_openai_direct.py
python test_groq_direct.py
```

## Troubleshooting

### "API key not set" errors
- Make sure your `.env` file is in the project root
- Check that your API keys are valid and active
- Ensure no extra spaces in your `.env` file

### Still getting blocked by GitHub?
- Run `git status` to see if any sensitive files are staged
- Use `git reset` to unstage any `.env` files
- Check for any remaining hardcoded keys with: `grep -r "sk-\|gsk_\|AIza" .`

## File Structure
```
fut_qa_assistant/
├── .env                    # Your API keys (not in git)
├── .env.example           # Template for others
├── setup_environment.py   # Automated setup script
└── SECURITY_SETUP.md      # This guide
```
