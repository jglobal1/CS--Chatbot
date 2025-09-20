"""
Simplified FUT QA Assistant - FastAPI Backend
This version works without heavy ML dependencies for testing
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="FUT QA Assistant API",
    description="Question-Answering API for Federal University of Technology students",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class QuestionRequest(BaseModel):
    question: str
    context: Optional[str] = None

class QuestionResponse(BaseModel):
    answer: str
    confidence: float
    model_used: str

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    model_name: str

# Simple mock responses for testing
MOCK_RESPONSES = {
    "what is fut": "Federal University of Technology (FUT) is a Nigerian university focused on technology and engineering education.",
    "programs": "FUT offers various programs in engineering, technology, and applied sciences including Computer Science, Electrical Engineering, and Mechanical Engineering.",
    "admission": "FUT admission requirements include a minimum of 5 credits in relevant subjects including Mathematics and English.",
    "computer science": "The Computer Science department at FUT offers programs in software engineering, artificial intelligence, and data science.",
    "engineering": "FUT is known for its comprehensive engineering programs including Electrical, Mechanical, Civil, and Computer Engineering."
}

def get_mock_answer(question: str) -> tuple:
    """Get a mock answer based on question keywords"""
    question_lower = question.lower()
    
    for keyword, answer in MOCK_RESPONSES.items():
        if keyword in question_lower:
            return answer, 0.85
    
    # Default response
    return "I'm a FUT QA Assistant. I can help you with information about Federal University of Technology programs, admission requirements, and academic departments. Please ask me a specific question about FUT!", 0.7

@app.get("/", response_model=dict)
async def root():
    """Root endpoint"""
    return {
        "message": "FUT QA Assistant API",
        "status": "running",
        "model_loaded": True
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        model_loaded=True,
        model_name="mock-demo"
    )

@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """Main question-answering endpoint"""
    try:
        # Get mock answer
        answer, confidence = get_mock_answer(request.question)
        
        return QuestionResponse(
            answer=answer,
            confidence=confidence,
            model_used="mock-demo"
        )
        
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")

@app.post("/reload-model")
async def reload_model():
    """Reload the model (useful after training)"""
    return {"message": "Mock model is always ready", "model_loaded": True}

if __name__ == "__main__":
    # Run the application
    uvicorn.run(
        "simple_app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
