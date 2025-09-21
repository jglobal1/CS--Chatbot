# 🚀 Deployment Guide for Vercel

## Quick Fix for 404 Error

The 404 error occurs because Vercel needs proper configuration to deploy Python/FastAPI applications.

## Files Created for Deployment

1. **`vercel.json`** - Vercel configuration
2. **`main.py`** - Main entry point combining API and static files
3. **`requirements.txt`** - Python dependencies
4. **`backend/config.py`** - Configuration for API keys

## Deployment Steps

### 1. Commit and Push Changes
```bash
git add .
git commit -m "Add Vercel deployment configuration"
git push origin main
```

### 2. Redeploy on Vercel
- Go to your Vercel dashboard
- Click "Redeploy" on your project
- Or trigger a new deployment by pushing to GitHub

### 3. Set Environment Variables in Vercel
In your Vercel dashboard, go to Settings → Environment Variables and add:

```
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
GROQ_API_KEY=your_groq_key_here
HUGGINGFACE_API_KEY=your_hf_key_here
```

### 4. Test the Deployment
After redeployment, your app should be accessible at:
- `https://cs-chatbotfut.vercel.app/` - Main interface
- `https://cs-chatbotfut.vercel.app/health` - Health check
- `https://cs-chatbotfut.vercel.app/api/` - API endpoints

## Troubleshooting

### If still getting 404:
1. Check Vercel build logs in the dashboard
2. Ensure all files are committed and pushed
3. Verify environment variables are set
4. Check that `main.py` is in the root directory

### If API keys not working:
1. Verify environment variables in Vercel dashboard
2. Check that keys are valid and active
3. Test locally first with `python main.py`

## Local Testing
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python main.py

# Test endpoints
curl http://localhost:8000/health
curl http://localhost:8000/
```

## File Structure
```
fut_qa_assistant/
├── main.py              # Main entry point
├── vercel.json          # Vercel configuration
├── requirements.txt     # Python dependencies
├── backend/
│   ├── app.py          # FastAPI application
│   └── config.py       # Configuration
├── frontend/
│   ├── index.html      # Main interface
│   ├── style.css       # Styles
│   └── script.js       # JavaScript
└── .env                # Local environment (not in git)
```
