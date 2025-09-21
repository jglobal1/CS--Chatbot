"""
Vercel serverless function entry point
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app import app

# Export the FastAPI app for Vercel
handler = app
