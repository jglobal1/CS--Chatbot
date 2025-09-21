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
if os.path.exists("frontend"):
    app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def read_index():
    """Serve the main HTML file"""
    if os.path.exists("frontend/index.html"):
        return FileResponse("frontend/index.html")
    return {"message": "FUT QA Assistant API", "status": "running"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "FUT QA Assistant is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)