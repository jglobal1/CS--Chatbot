"""
Main entry point for the FUT QA Assistant
Simplified version for Vercel deployment
"""

import os
import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from typing import Optional

# Create main app
app = FastAPI(
    title="FUT QA Assistant",
    description="AI-powered question answering system for FUT students",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    confidence: float
    source: str

# Simple QA function that works without heavy ML dependencies
def get_simple_answer(question: str) -> dict:
    """Simple question answering without ML models"""
    
    # Basic FUT information
    fut_info = {
        "what is fut": "Federal University of Technology, Minna (FUT) is a Nigerian federal university focused on technology and engineering education.",
        "where is fut": "FUT is located in Minna, Niger State, Nigeria.",
        "when was fut established": "FUT was established in 1983.",
        "fut website": "FUT's official website is https://futminna.edu.ng",
        "fut departments": "FUT offers programs in Computer Science, Engineering, Agriculture, Sciences, and more.",
        "how to apply to fut": "Admission requirements vary by program. Check the official website for details."
    }
    
    question_lower = question.lower()
    
    # Simple keyword matching
    for key, answer in fut_info.items():
        if any(word in question_lower for word in key.split()):
            return {
                "answer": answer,
                "confidence": 0.9,
                "source": "FUT Knowledge Base"
            }
    
    # Default response
    return {
        "answer": "I'm the FUT QA Assistant. I can help with questions about Federal University of Technology, Minna. Please ask about FUT programs, admission, or general information.",
        "confidence": 0.7,
        "source": "FUT Assistant"
    }

# API Routes
@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """Ask a question to the FUT QA Assistant"""
    try:
        result = get_simple_answer(request.question)
        return AnswerResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ask")
async def ask_question_get(question: str):
    """Ask a question via GET request"""
    try:
        result = get_simple_answer(question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mount static files
frontend_path = "frontend"
if not os.path.exists(frontend_path):
    frontend_path = "."

if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
async def read_index():
    """Serve the main HTML file"""
    # Try different possible locations for the HTML file
    possible_paths = [
        "index.html",
        "frontend/index.html"
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return FileResponse(path)
    
    # Fallback: return a simple HTML page
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FUT QA Assistant</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 15px; color: #333; }
            .header { text-align: center; margin-bottom: 30px; }
            .logo { width: 60px; height: 60px; background: #2c3e50; border-radius: 10px; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; }
            h1 { color: #2c3e50; margin-bottom: 10px; }
            .subtitle { color: #666; margin-bottom: 30px; }
            .input-group { margin-bottom: 20px; }
            input[type="text"] { width: 100%; padding: 15px; border: 2px solid #ddd; border-radius: 8px; font-size: 16px; }
            button { background: #667eea; color: white; padding: 15px 30px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; }
            button:hover { background: #5a6fd8; }
            .status { margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 8px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="logo">FUT</div>
                <h1>FUT QA Assistant</h1>
                <p class="subtitle">Ask questions about Federal University of Technology</p>
            </div>
            
            <div class="input-group">
                <input type="text" id="questionInput" placeholder="Ask your question about FUT..." />
                <button onclick="askQuestion()">Ask Question</button>
            </div>
            
            <div class="status">
                <p><strong>API Status:</strong> <span id="apiStatus">Connected</span></p>
                <p><strong>Model:</strong> <span id="modelStatus">Johnson's Training Model</span></p>
            </div>
            
            <div id="response" style="margin-top: 20px; padding: 15px; background: #e9ecef; border-radius: 8px; display: none;"></div>
        </div>
        
        <script>
            async function askQuestion() {
                const question = document.getElementById('questionInput').value;
                const responseDiv = document.getElementById('response');
                
                if (!question) {
                    alert('Please enter a question!');
                    return;
                }
                
                try {
                    const response = await fetch('/ask?question=' + encodeURIComponent(question));
                    const data = await response.json();
                    
                    responseDiv.innerHTML = '<strong>Answer:</strong> ' + data.answer;
                    responseDiv.style.display = 'block';
                } catch (error) {
                    responseDiv.innerHTML = '<strong>Error:</strong> ' + error.message;
                    responseDiv.style.display = 'block';
                }
            }
            
            document.getElementById('questionInput').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    askQuestion();
                }
            });
        </script>
    </body>
    </html>
    """

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "FUT QA Assistant is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)