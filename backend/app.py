"""
FUT QA Assistant - FastAPI Backend
Main application file for the question-answering API
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import uvicorn
import os
from typing import Optional
import logging
import requests as http_requests
from unified_intelligence import unified_intelligence
from config import ExternalAPIConfig

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

# Global variables for model and pipeline
qa_pipeline = None
model_loaded = False

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

def get_external_llm_response(question: str) -> Optional[str]:
    """Get response from external LLMs (Google, OpenAI, etc.)"""
    try:
        # Try multiple external APIs in order of preference
        
        # 1. Try Google's Gemini API (if available)
        gemini_response = try_gemini_api(question)
        if gemini_response:
            return gemini_response
        
        # 2. Try OpenAI API (if available)
        openai_response = try_openai_api(question)
        if openai_response:
            return openai_response
        
        # 3. Try Hugging Face Inference API
        huggingface_response = try_huggingface_api(question)
        if huggingface_response:
            return huggingface_response
        
        # 4. Try Groq API (FREE)
        groq_response = try_groq_api(question)
        if groq_response:
            return groq_response
        
        # 5. Fallback to web search + basic processing
        web_response = try_web_search(question)
        if web_response:
            return web_response
        
        return None
        
    except Exception as e:
        logger.error(f"Error getting external LLM response: {str(e)}")
        return None

def try_gemini_api(question: str) -> Optional[str]:
    """Try Google's Gemini API"""
    try:
        if not ExternalAPIConfig.is_gemini_configured():
            return None
        
        # Implement Gemini API call here
        # This would require google-generativeai package
        # For now, return None to indicate not implemented
        return None
    except Exception as e:
        logger.error(f"Gemini API error: {str(e)}")
        return None

def try_openai_api(question: str) -> Optional[str]:
    """Try OpenAI API"""
    try:
        if not ExternalAPIConfig.is_openai_configured():
            return None
        
        # Make actual OpenAI API call
        api_key = ExternalAPIConfig.OPENAI_API_KEY
        if not api_key or api_key == "your_openai_key_here":
            return None
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": ExternalAPIConfig.OPENAI_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Provide clear, informative answers to user questions."
                },
                {
                    "role": "user", 
                    "content": question
                }
            ],
            "max_tokens": 500,
            "temperature": 0.7
        }
        
        response = http_requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content'].strip()
        
        logger.error(f"OpenAI API error: {response.status_code} - {response.text}")
        return None
        
    except Exception as e:
        logger.error(f"OpenAI API error: {str(e)}")
        return None

def try_huggingface_api(question: str) -> Optional[str]:
    """Try Hugging Face Inference API (Free)"""
    try:
        # Use Hugging Face's free inference API (no key required for some models)
        api_url = f"https://api-inference.huggingface.co/models/{ExternalAPIConfig.HUGGINGFACE_MODEL}"
        
        # Try without authentication first (free tier)
        headers = {"Content-Type": "application/json"}
        
        payload = {
            "inputs": question,
            "parameters": {
                "max_length": 200,
                "temperature": 0.7,
                "do_sample": True
            }
        }
        
        response = http_requests.post(api_url, headers=headers, json=payload, timeout=15)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                generated_text = result[0].get('generated_text', '')
                # Clean up the response
                if generated_text:
                    # Remove the original question from the response
                    if question.lower() in generated_text.lower():
                        generated_text = generated_text.replace(question, '').strip()
                    return generated_text[:300]  # Limit length
        
        # If that fails, try with a different free model
        alternative_models = [
            "microsoft/DialoGPT-small",
            "distilbert-base-uncased",
            "gpt2"
        ]
        
        for model in alternative_models:
            try:
                alt_url = f"https://api-inference.huggingface.co/models/{model}"
                response = http_requests.post(alt_url, headers=headers, json=payload, timeout=10)
                
                if response.status_code == 200:
                    result = response.json()
                    if isinstance(result, list) and len(result) > 0:
                        generated_text = result[0].get('generated_text', '')
                        if generated_text:
                            return generated_text[:300]
            except:
                continue
        
        return None
        
    except Exception as e:
        logger.error(f"Hugging Face API error: {str(e)}")
        return None

def try_groq_api(question: str) -> Optional[str]:
    """Try Groq API (FREE)"""
    try:
        if not ExternalAPIConfig.is_groq_configured():
            return None
        
        api_key = ExternalAPIConfig.GROQ_API_KEY
        if not api_key or api_key == "your_groq_key_here":
            return None
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Provide clear, informative answers to user questions."
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            "model": ExternalAPIConfig.GROQ_MODEL,
            "max_tokens": 500,
            "temperature": 0.7
        }
        
        response = http_requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content'].strip()
        
        logger.error(f"Groq API error: {response.status_code} - {response.text}")
        return None
        
    except Exception as e:
        logger.error(f"Groq API error: {str(e)}")
        return None

def try_web_search(question: str) -> Optional[str]:
    """Try web search for general information"""
    try:
        # Use a simple web search approach
        # This is a basic implementation - you can enhance with actual search APIs
        
        question_lower = question.lower()
        
        # Handle common general questions
        if any(word in question_lower for word in ['fut', 'university', 'minna']):
            return get_fut_basic_info(question)
        
        if any(word in question_lower for word in ['weather', 'temperature', 'climate']):
            return "I can't provide real-time weather information. Please check a weather service for current conditions."
        
        if any(word in question_lower for word in ['news', 'current', 'recent']):
            return "I can't provide real-time news. Please check news websites for the latest updates."
        
        # Provide more helpful responses for common questions
        if 'technology' in question_lower or 'tech' in question_lower:
            return "**🚀 Latest Technology Trends:**\n\n• **Artificial Intelligence**: ChatGPT, GPT-4, and AI assistants are revolutionizing how we work\n• **Machine Learning**: Advanced algorithms for data analysis and prediction\n• **Blockchain**: Cryptocurrency, NFTs, and decentralized applications\n• **Cloud Computing**: AWS, Azure, and Google Cloud platforms\n• **Cybersecurity**: Advanced threat protection and data security\n• **IoT**: Internet of Things connecting everyday devices\n\nFor the most current information, I recommend checking tech news websites like TechCrunch, Wired, or The Verge."
        
        if 'artificial intelligence' in question_lower or 'ai' in question_lower:
            return "**🤖 Artificial Intelligence (AI):**\n\nAI is the simulation of human intelligence in machines. Key areas include:\n\n• **Machine Learning**: Algorithms that learn from data\n• **Deep Learning**: Neural networks with multiple layers\n• **Natural Language Processing**: Understanding and generating human language\n• **Computer Vision**: Teaching machines to 'see' and interpret images\n• **Robotics**: Combining AI with physical machines\n\nAI is transforming industries from healthcare to finance, making processes more efficient and enabling new capabilities."
        
        if 'machine learning' in question_lower or 'ml' in question_lower:
            return "**📊 Machine Learning:**\n\nMachine Learning is a subset of AI that enables computers to learn and improve from experience without being explicitly programmed.\n\n**Types:**\n• **Supervised Learning**: Learning from labeled examples\n• **Unsupervised Learning**: Finding patterns in unlabeled data\n• **Reinforcement Learning**: Learning through trial and error\n\n**Applications:**\n• Recommendation systems (Netflix, Amazon)\n• Image recognition (medical diagnosis)\n• Natural language processing (chatbots)\n• Predictive analytics (stock market, weather)\n\nIt's a powerful tool for data analysis and automation."
        
        # Add responses for education/university questions
        if any(word in question_lower for word in ['school', 'university', 'college', 'education', 'africa', 'nigeria', 'harvard', 'mit', 'stanford']):
            return "**🎓 Top Universities and Schools:**\n\n**Global Rankings:**\n• **Harvard University** (USA) - World-renowned for business, medicine, law\n• **MIT** (USA) - Leading in technology and engineering\n• **Stanford University** (USA) - Excellence in computer science and innovation\n• **Oxford University** (UK) - Prestigious research institution\n• **Cambridge University** (UK) - Historic academic excellence\n\n**Top African Universities:**\n• **University of Cape Town** (South Africa) - Leading African university\n• **University of Witwatersrand** (South Africa) - Strong research focus\n• **University of Ibadan** (Nigeria) - Nigeria's premier university\n• **Cairo University** (Egypt) - Leading in North Africa\n• **University of Ghana** (Ghana) - West African excellence\n\n**Nigerian Universities:**\n• **University of Ibadan** - Nigeria's oldest and most prestigious\n• **University of Lagos** - Strong in engineering and business\n• **Ahmadu Bello University** - Northern Nigeria's leading institution\n• **Federal University of Technology, Minna** - Technology and engineering focus\n\nFor detailed rankings, check QS World University Rankings or Times Higher Education."
        
        # Generic response for other questions
        return f"I understand you're asking about '{question}'. This question is outside my specialized domain of Computer Science at FUT. For general information, I recommend consulting relevant websites or asking a general AI assistant."
        
    except Exception as e:
        logger.error(f"Web search error: {str(e)}")
        return None

def get_fut_basic_info(question: str) -> str:
    """Get basic FUT information"""
    fut_info = {
        "general": "Federal University of Technology, Minna is a Nigerian federal university focused on technology and engineering education.",
        "location": "Minna, Niger State, Nigeria",
        "established": "1983",
        "type": "Federal University",
        "focus": "Technology, Engineering, and Applied Sciences",
        "website": "https://futminna.edu.ng",
        "departments": "Computer Science, Engineering, Agriculture, Sciences",
        "admission": "Admission requirements vary by program. Check the official website for details."
    }
    
    question_lower = question.lower()
    
    if 'location' in question_lower or 'where' in question_lower:
        return f"FUT is located in {fut_info['location']}"
    elif 'when' in question_lower or 'established' in question_lower:
        return f"FUT was established in {fut_info['established']}"
    elif 'website' in question_lower or 'url' in question_lower:
        return f"FUT's official website is {fut_info['website']}"
    elif 'admission' in question_lower or 'apply' in question_lower:
        return f"{fut_info['admission']} Visit {fut_info['website']} for more information."
    elif 'departments' in question_lower or 'programs' in question_lower:
        return f"FUT offers programs in {fut_info['departments']}. Check {fut_info['website']} for complete details."
    else:
        return f"{fut_info['general']} It was established in {fut_info['established']} and is located in {fut_info['location']}. Visit {fut_info['website']} for more information."

def load_model():
    """Load the QA model and create pipeline"""
    global qa_pipeline, model_loaded
    
    try:
        # Try to load ultimate model first, then fallback to final model
        model_path = "../data/models/fut_qa_model_ultimate"
        if not os.path.exists(model_path):
            model_path = "../data/models/fut_qa_model_final"
        if os.path.exists(model_path):
            logger.info(f"Loading fine-tuned model from: {model_path}")
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            model = AutoModelForQuestionAnswering.from_pretrained(model_path)
            qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
            model_loaded = True
            logger.info("Fine-tuned model loaded successfully")
        else:
            # Fallback to pre-trained model
            logger.info("Fine-tuned model not found, using pre-trained model")
            model_name = "distilbert/distilbert-base-cased-distilled-squad"
            qa_pipeline = pipeline("question-answering", model=model_name)
            model_loaded = True
            logger.info("Pre-trained model loaded successfully")
            
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        model_loaded = False
        raise e

@app.on_event("startup")
async def startup_event():
    """Load model on startup"""
    try:
        load_model()
    except Exception as e:
        logger.error(f"Failed to load model on startup: {str(e)}")

@app.get("/", response_model=dict)
async def root():
    """Root endpoint"""
    return {
        "message": "FUT QA Assistant API",
        "status": "running",
        "model_loaded": model_loaded
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy" if model_loaded else "unhealthy",
        model_loaded=model_loaded,
        model_name="Johnson's Training Model"
    )

@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """Main question-answering endpoint with external API integration"""
    if not model_loaded:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # First, check if this is a general FUT question that should use external API
        question_lower = request.question.lower()
        
        # Check for general FUT questions (not domain-specific CS questions)
        general_fut_keywords = ['fut', 'university', 'minna', 'federal', 'technology', 'campus', 'admission', 'facilities']
        cs_domain_keywords = ['course', 'lecturer', 'programming', 'computer', 'software', 'hardware', 'materials', 'study', 'cos', 'cst', 'mat', 'phy', 'cpt']
        
        is_general_fut = any(word in question_lower for word in general_fut_keywords)
        is_cs_domain = any(word in question_lower for word in cs_domain_keywords)
        
        # Enhanced CS domain detection - more comprehensive course codes
        cs_course_codes = [
            'cos101', 'cos102', 'cos103', 'cos104', 'cos105', 'cos106', 'cos107', 'cos108', 'cos109', 'cos110',
            'cst111', 'cst112', 'cst113', 'cst114', 'cst115', 'cst116', 'cst117', 'cst118', 'cst119', 'cst120',
            'mat121', 'mat122', 'mat123', 'mat124', 'mat125', 'mat126', 'mat127', 'mat128', 'mat129', 'mat130',
            'phy101', 'phy102', 'phy103', 'phy104', 'phy105', 'phy106', 'phy107', 'phy108', 'phy109', 'phy110',
            'cpt111', 'cpt112', 'cpt113', 'cpt114', 'cpt115', 'cpt116', 'cpt117', 'cpt118', 'cpt119', 'cpt120',
            'cpt192', 'cpt193', 'cpt194', 'cpt195', 'cpt196', 'cpt197', 'cpt198', 'cpt199', 'cpt200'
        ]
        has_cs_course = any(code in question_lower for code in cs_course_codes)
        
        # Also check for course name variations
        course_name_variations = [
            'computer science', 'computer studies', 'programming', 'software engineering',
            'data structures', 'algorithms', 'database', 'networking', 'cybersecurity',
            'artificial intelligence', 'machine learning', 'web development'
        ]
        has_cs_course_name = any(variation in question_lower for variation in course_name_variations)
        
        if has_cs_course or has_cs_course_name:
            is_cs_domain = True
        
        # PRIORITY 1: Always use Unified Intelligence for CS domain questions
        # This ensures your specific dataset (COS101, COS102, etc.) is used first
        if is_cs_domain or has_cs_course or has_cs_course_name:
            # Use Unified Intelligence System for domain-specific CS questions
            unified_response = unified_intelligence.get_unified_response(request.question, request.context or "")
            
            if unified_response and unified_response.get('answer'):
                # Check if the response is too generic or low confidence
                if (unified_response.get('confidence', 0) < 0.7 or 
                    'FUT CS Assistant - How Can I Help?' in unified_response.get('answer', '') or
                    len(unified_response.get('answer', '')) < 50):
                    
                    # For low confidence CS responses, still return them but mark as low confidence
                    return QuestionResponse(
                        answer=unified_response['answer'],
                        confidence=unified_response['confidence'],
                        model_used="Johnson's Training Model"
                    )
                
                # Return the unified response for CS questions
                return QuestionResponse(
                    answer=unified_response['answer'],
                    confidence=unified_response['confidence'],
                    model_used="Johnson's Training Model"
                )
        
        # PRIORITY 2: Use Groq with PDF data for CS questions, external APIs for general questions
        if is_cs_domain or has_cs_course or has_cs_course_name:
            # For CS questions, try Groq with PDF data first
            groq_pdf_response = call_groq_with_context(
                request.question, 
                f"You are a specialized assistant for Federal University of Technology, Minna Computer Science Department.\n\n{get_comprehensive_fut_cs_context()}\n\nProvide detailed, accurate information based on the FUT Computer Science context above. Be specific about lecturers, courses, career paths, and academic information."
            )
            if groq_pdf_response:
                return QuestionResponse(
                    answer=groq_pdf_response,
                    confidence=0.95,
                    model_used="Johnson's Training Model"
                )
        else:
            # For general questions, use external APIs
            external_response = get_external_llm_response(request.question)
            if external_response and "I understand you're asking about" not in external_response:
                return QuestionResponse(
                    answer=external_response,
                    confidence=0.85,
                    model_used="Johnson's Training Model"
                )
        
        # PRIORITY 3: Fallback to Unified Intelligence for any remaining questions
        unified_response = unified_intelligence.get_unified_response(request.question, request.context or "")
        
        if unified_response and unified_response.get('answer'):
            return QuestionResponse(
                answer=unified_response['answer'],
                confidence=unified_response['confidence'],
                model_used="Johnson's Training Model"
            )
        
        # Prepare the input for QA model
        if request.context:
            # Use provided context
            result = qa_pipeline(question=request.question, context=request.context)
        else:
            # Use default FUT context for academic questions
            default_context = """
            Federal University of Technology (FUT) is a Nigerian university focused on technology and engineering education. 
            The university offers various programs in engineering, technology, and applied sciences. 
            Students can access academic resources, course materials, and institutional information through various channels.
            """
            result = qa_pipeline(question=request.question, context=default_context)
        
        # Use Johnson's Training Model name
        return QuestionResponse(
            answer=result["answer"],
            confidence=result["score"],
            model_used="Johnson's Training Model"
        )
        
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")

@app.post("/reload-model")
async def reload_model():
    """Reload the model (useful after training)"""
    try:
        load_model()
        return {"message": "Model reloaded successfully", "model_loaded": model_loaded}
    except Exception as e:
        logger.error(f"Error reloading model: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error reloading model: {str(e)}")

@app.get("/conversation-summary")
async def get_conversation_summary():
    """Get conversation summary from unified intelligence"""
    try:
        summary = unified_intelligence.get_conversation_summary()
        return {"conversation_summary": summary}
    except Exception as e:
        logger.error(f"Error getting conversation summary: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error getting conversation summary: {str(e)}")

@app.post("/learn")
async def learn_from_interaction(question: str, response: str, feedback: Optional[str] = None):
    """Learn from user interactions"""
    try:
        unified_intelligence.learn_from_interaction(question, response, feedback)
        return {"message": "Learning data recorded successfully"}
    except Exception as e:
        logger.error(f"Error recording learning data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error recording learning data: {str(e)}")

@app.get("/intelligence-status")
async def get_intelligence_status():
    """Get unified intelligence system status"""
    try:
        return unified_intelligence.get_system_status()
    except Exception as e:
        logger.error(f"Error getting intelligence status: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error getting intelligence status: {str(e)}")

@app.get("/external-api-status")
async def get_external_api_status():
    """Get the status of external API integrations"""
    try:
        available_apis = ExternalAPIConfig.get_available_apis()
        return {
            "status": "success",
            "available_apis": available_apis,
            "total_configured": len(available_apis),
            "openai_configured": ExternalAPIConfig.is_openai_configured(),
            "gemini_configured": ExternalAPIConfig.is_gemini_configured(),
            "huggingface_configured": ExternalAPIConfig.is_huggingface_configured(),
            "groq_configured": ExternalAPIConfig.is_groq_configured(),
            "message": f"External APIs configured: {', '.join(available_apis) if available_apis else 'None'}"
        }
    except Exception as e:
        logger.error(f"Error getting external API status: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error getting external API status: {str(e)}")

@app.post("/ask-groq")
async def ask_groq_direct(request: QuestionRequest):
    """Direct Groq API endpoint for enhanced responses"""
    try:
        groq_response = try_groq_api(request.question)
        if groq_response:
            return QuestionResponse(
                answer=groq_response,
                confidence=0.9,
                model_used="Johnson's Training Model"
            )
        else:
            raise HTTPException(status_code=503, detail="Groq API not available")
    except Exception as e:
        logger.error(f"Groq direct error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Groq error: {str(e)}")

@app.post("/ask-groq-pdf")
async def ask_groq_pdf_trained(request: QuestionRequest):
    """Groq endpoint trained on your PDF data"""
    try:
        question_lower = request.question.lower()
        
        # Enhanced course detection
        course_codes = ["COS101", "COS102", "COS103", "COS104", "COS105", "COS106", "COS107", "COS108", "COS109", "COS110",
                       "CST111", "CST112", "CST113", "CST114", "CST115", "CST116", "CST117", "CST118", "CST119", "CST120",
                       "MAT121", "MAT122", "MAT123", "MAT124", "MAT125", "MAT126", "MAT127", "MAT128", "MAT129", "MAT130",
                       "PHY101", "PHY102", "PHY103", "PHY104", "PHY105", "PHY106", "PHY107", "PHY108", "PHY109", "PHY110",
                       "CPT111", "CPT112", "CPT113", "CPT114", "CPT115", "CPT116", "CPT117", "CPT118", "CPT119", "CPT120",
                       "CPT192", "CPT193", "CPT194", "CPT195", "CPT196", "CPT197", "CPT198", "CPT199", "CPT200",
                       "GST112", "STA111"]
        
        # Check for specific course questions
        course_context = None
        for course in course_codes:
            if course.lower() in question_lower:
                course_context = course
                break
        
        # Check for lecturer-related questions
        lecturer_keywords = ['lecturer', 'lecturers', 'teacher', 'teachers', 'instructor', 'instructors', 'professor', 'professors', 'dr.', 'dr', 'who teaches', 'who is teaching']
        is_lecturer_question = any(keyword in question_lower for keyword in lecturer_keywords)
        
        # Check for general CS questions about FUT
        fut_cs_keywords = ['fut', 'futminna', 'computer science', 'cs department', 'department', 'university', 'minna']
        is_fut_cs_question = any(keyword in question_lower for keyword in fut_cs_keywords)
        
        # Check for career/academic questions
        career_keywords = ['career', 'careers', 'job', 'jobs', 'work', 'employment', 'industry', 'industries', 'path', 'paths']
        is_career_question = any(keyword in question_lower for keyword in career_keywords)
        
        # Check for skills questions
        skills_keywords = ['skills', 'skill', 'learn', 'learning', 'study', 'studying', 'essential', 'important', 'required']
        is_skills_question = any(keyword in question_lower for keyword in skills_keywords)
        
        # Determine the best context to provide
        if course_context:
            # Specific course question
            pdf_content = get_course_pdf_content(course_context)
            system_prompt = f"""
            You are a specialized assistant for Federal University of Technology, Minna Computer Science courses.
            
            Course Content for {course_context}:
            {pdf_content}
            
            Provide detailed, accurate information about {course_context} based on the course content.
            Be specific about course details, learning objectives, and assessment methods.
            Include information about lecturers, materials, and practical sessions when available.
            If asked about lecturers, provide the exact names from the course content.
            """
        elif is_lecturer_question or is_fut_cs_question or is_career_question or is_skills_question:
            # General FUT CS question - use comprehensive context
            fut_context = get_comprehensive_fut_cs_context()
            system_prompt = f"""
            You are a specialized assistant for Federal University of Technology, Minna Computer Science Department.
            
            {fut_context}
            
            Provide detailed, accurate information based on the FUT Computer Science context above.
            Be specific about lecturers, courses, career paths, and academic information.
            If asked about lecturers, provide the exact names and courses they teach.
            If asked about career paths, provide the comprehensive list from the context.
            If asked about skills, provide the essential skills list from the context.
            """
        else:
            # General CS question
            system_prompt = "You are a computer science expert. Provide detailed, educational explanations suitable for university students."
        
        groq_response = call_groq_with_context(request.question, system_prompt)
        
        if groq_response:
            return QuestionResponse(
                answer=groq_response,
                confidence=0.95,
                model_used="Johnson's Training Model"
            )
        else:
            raise HTTPException(status_code=503, detail="Groq PDF-trained API not available")
            
    except Exception as e:
        logger.error(f"Groq PDF-trained error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Groq PDF error: {str(e)}")

@app.get("/download/{course_code}")
async def download_course_materials(course_code: str):
    """Download course materials for a specific course"""
    try:
        # Check for existing PDF materials first
        materials_dir = f"../data/course_materials/{course_code.upper()}"
        
        if os.path.exists(materials_dir):
            # Look for existing PDF files first
            pdf_files = [f for f in os.listdir(materials_dir) if f.endswith('.pdf')]
            if pdf_files:
                file_path = os.path.join(materials_dir, pdf_files[0])
                return FileResponse(
                    path=file_path,
                    filename=pdf_files[0],
                    media_type='application/pdf'
                )
            
            # Look for HTML files as fallback
            html_files = [f for f in os.listdir(materials_dir) if f.endswith('.html')]
            if html_files:
                file_path = os.path.join(materials_dir, html_files[0])
                return FileResponse(
                    path=file_path,
                    filename=html_files[0],
                    media_type='text/html'
                )
        
        # If no existing materials, create new ones
        os.makedirs(materials_dir, exist_ok=True)
        
        # Create sample materials for the course
        sample_files = {
            f"{course_code.upper()}_syllabus.html": f"Course syllabus for {course_code.upper()}",
            f"{course_code.upper()}_lecture_notes.html": f"Lecture notes for {course_code.upper()}",
            f"{course_code.upper()}_past_questions.html": f"Past questions for {course_code.upper()}",
            f"{course_code.upper()}_study_guide.html": f"Study guide for {course_code.upper()}"
        }
        
        for filename, content in sample_files.items():
            file_path = os.path.join(materials_dir, filename)
            # Create HTML content that browsers can display
            html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{content}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }}
        .header {{
            background-color: #667eea;
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        .content {{
            margin: 20px 0;
        }}
        .section {{
            margin: 20px 0;
            padding: 15px;
            border-left: 4px solid #667eea;
            background-color: #f8f9fa;
        }}
        .download-info {{
            background-color: #e8f4fd;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{content}</h1>
        <p>Course: {course_code.upper()}</p>
        <p>Generated by FUT CS Assistant</p>
    </div>
    
    <div class="content">
        <div class="section">
            <h2>📚 Course Information</h2>
            <p>This is a sample {content.lower()} for {course_code.upper()}.</p>
            <p>This material contains essential information for students taking this course.</p>
        </div>
        
        <div class="section">
            <h2>📖 Content Overview</h2>
            <ul>
                <li>Course objectives and learning outcomes</li>
                <li>Detailed syllabus and topics</li>
                <li>Assessment methods and grading criteria</li>
                <li>Recommended textbooks and resources</li>
                <li>Important dates and deadlines</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>🎯 Study Tips</h2>
            <ul>
                <li>Review materials regularly</li>
                <li>Attend all lectures and practical sessions</li>
                <li>Complete assignments on time</li>
                <li>Form study groups with classmates</li>
                <li>Seek help from lecturers when needed</li>
            </ul>
        </div>
        
        <div class="download-info">
            <h3>📥 Download Information</h3>
            <p><strong>File:</strong> {filename}</p>
            <p><strong>Course:</strong> {course_code.upper()}</p>
            <p><strong>Generated:</strong> {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>Source:</strong> FUT CS Assistant</p>
        </div>
    </div>
</body>
</html>"""
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
        
        # Return the first available file
        files = [f for f in os.listdir(materials_dir) if f.endswith(('.pdf', '.html'))]
        if files:
            file_path = os.path.join(materials_dir, files[0])
            media_type = 'application/pdf' if files[0].endswith('.pdf') else 'text/html'
            return FileResponse(
                path=file_path,
                filename=files[0],
                media_type=media_type
            )
        else:
            raise HTTPException(status_code=404, detail=f"No materials found for {course_code}")
            
    except Exception as e:
        logger.error(f"Error downloading materials for {course_code}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error downloading materials: {str(e)}")

def get_course_pdf_content(course_code):
    """Get PDF content for a specific course"""
    
    # Enhanced content based on your actual PDF data
    course_content = {
        "COS101": """
        COS101 - Introduction to Computer Science
        
        Course Overview:
        This course introduces students to the fundamental concepts of computer science including:
        - History of computing and computer evolution
        - Computer hardware components (CPU, RAM, Storage, Input/Output devices)
        - Software systems and operating systems
        - Programming basics and syntax
        - Problem-solving techniques and algorithms
        - Introduction to data structures and programming logic
        
        Learning Objectives:
        1. Understand the evolution of computers from abacus to modern systems
        2. Learn basic computer hardware components and their functions
        3. Introduction to programming concepts and syntax
        4. Develop logical thinking and problem-solving skills
        5. Understand the role of algorithms in computing
        
        Assessment Structure:
        - Continuous Assessment: 30% (Assignments, Quizzes, Lab work)
        - Mid-term Examination: 20% (Theory and Practical)
        - Final Examination: 50% (Comprehensive)
        
        Lecturers: Umar Alkali, O. Ojerinde O, Abisoye O. A, Lawal Olamilekan Lawal, Bashir Suleiman
        
        Course Materials:
        - Introduction to Computer Science textbook
        - Programming exercises and assignments
        - Lab manuals and practical guides
        - Past examination questions
        """,
        "COS102": """
        COS102 - Introduction to Problem Solving
        
        Course Overview:
        This course focuses on problem-solving techniques and programming fundamentals:
        - Algorithm design and analysis
        - Flowchart creation and documentation
        - Programming logic and control structures
        - Debugging techniques and error handling
        - Code optimization and best practices
        
        Programming Languages Covered:
        - Python programming basics
        - Control structures (if-else, loops)
        - Functions and modular programming
        - Data types and variable manipulation
        - Input/output operations
        
        Practical Sessions:
        - Weekly programming laboratories
        - Group programming projects
        - Code review and peer assessment
        - Debugging and testing exercises
        
        Lecturers: Sadiu Ahmed Abubakar, Shuaibu M Badeggi, Ibrahim Shehi Shehu, Abubakar Suleiman T, Lasotte Yakubu
        
        Assessment:
        - Lab Assignments: 40%
        - Programming Projects: 30%
        - Final Examination: 30%
        """,
        "PHY101": """
        PHY101 - General Physics I
        
        Course Content:
        - Mechanics and motion
        - Forces and energy
        - Waves and oscillations
        - Thermodynamics basics
        - Laboratory experiments
        
        Lecturers: Aku Ibrahim
        
        Assessment:
        - Laboratory Work: 30%
        - Continuous Assessment: 20%
        - Final Examination: 50%
        """,
        "PHY102": """
        PHY102 - General Physics II
        
        Course Content:
        - Advanced mechanics and motion
        - Electromagnetism
        - Optics and wave phenomena
        - Modern physics concepts
        - Laboratory experiments
        
        Lecturers: Dr. Julia Elchie
        
        Assessment:
        - Laboratory Work: 30%
        - Continuous Assessment: 20%
        - Final Examination: 50%
        """,
        "CST111": """
        CST111 - Communication in English
        
        Course Content:
        - English language skills
        - Technical writing
        - Presentation skills
        - Communication in academic settings
        
        Lecturers: Okeli Chike, Amina Gogo Tafida, Halima Shehu
        
        Assessment:
        - Written Assignments: 40%
        - Oral Presentations: 30%
        - Final Examination: 30%
        """,
        "CPT111": """
        FTM-CPT111 - Probability for Computer Science
        
        Course Content:
        - Probability theory and applications
        - Statistical methods for computer science
        - Data analysis techniques
        - Mathematical foundations for CS
        
        Lecturers: Saliu Adam Muhammad, Saidu Ahmed Abubakar
        
        Assessment:
        - Assignments: 30%
        - Mid-term Test: 20%
        - Final Examination: 50%
        """,
        "CPT112": """
        FTM-CPT112 - Front End Web Development
        
        Course Content:
        - HTML, CSS, JavaScript fundamentals
        - Responsive web design
        - Front-end frameworks
        - User interface design
        - Web development best practices
        
        Lecturers: Benjamin Alenoghen, Lawal Olamilekan Lawal, Lasotte Yakubu, Benjamin Alenoghena
        
        Assessment:
        - Web Development Projects: 40%
        - Practical Assignments: 30%
        - Final Examination: 30%
        """,
        "CPT192": """
        FTM-CPT192 - Introduction to Computer Hardware
        
        Course Content:
        - Computer hardware components
        - System architecture
        - Hardware troubleshooting
        - Assembly and maintenance
        - Hardware-software interaction
        
        Lecturers: Benjamin Alenoghen
        
        Assessment:
        - Hardware Labs: 40%
        - Practical Projects: 30%
        - Final Examination: 30%
        """
    }
    
    return course_content.get(course_code, f"{course_code} - Course content not available")

def get_comprehensive_fut_cs_context():
    """Get comprehensive FUT Computer Science context for Groq"""
    
    return """
    FEDERAL UNIVERSITY OF TECHNOLOGY, MINNA - COMPUTER SCIENCE DEPARTMENT
    
    CURRENT LECTURERS AND COURSES:
    
    PHYSICS COURSES:
    - PHY 101 - General Physics I: Aku Ibrahim
    - PHY 102 - General Physics II: Dr. Julia Elchie
    
    COMPUTER SCIENCE CORE COURSES:
    - COS 101 - Introduction to Computer Science:
      Lecturers: Umar Alkali, O. Ojerinde O, Abisoye O. A, Lawal Olamilekan Lawal, Bashir Suleiman
      
    - COS 102 - Introduction to Problem Solving:
      Lecturers: Sadiu Ahmed Abubakar, Shuaibu M Badeggi, Ibrahim Shehi Shehu, Abubakar Suleiman T, Lasotte Yakubu
    
    COMMUNICATION COURSES:
    - CST 111 - Communication in English:
      Lecturers: Okeli Chike, Amina Gogo Tafida, Halima Shehu
    
    GENERAL STUDIES:
    - GST 112 - Nigerian Peoples and Culture: Isah Usman
    
    COMPUTER SCIENCE SPECIALIZED COURSES:
    - FTM-CPT111 - Probability for Computer Science:
      Lecturers: Saliu Adam Muhammad, Saidu Ahmed Abubakar
      
    - FTM-CPT112 - Front End Web Development:
      Lecturers: Benjamin Alenoghen, Lawal Olamilekan Lawal, Lasotte Yakubu, Benjamin Alenoghena
      
    - FTM-CPT192 - Introduction to Computer Hardware:
      Lecturers: Benjamin Alenoghen
    
    STATISTICS:
    - STA111 - Descriptive Statistics: Olayiwola Adelutu
    
    PHYSICS PRACTICAL:
    - PHY 101 - General Practical Physics I: Moses AS
    
    CAREER PATHS IN COMPUTER SCIENCE:
    1. Software Development
    2. Web Development
    3. Mobile App Development
    4. Data Science and Analytics
    5. Cybersecurity
    6. Artificial Intelligence and Machine Learning
    7. Database Administration
    8. Network Administration
    9. System Administration
    10. IT Consulting
    
    ESSENTIAL SKILLS FOR COMPUTER SCIENCE STUDENTS:
    - Programming Languages (Python, Java, C++, JavaScript)
    - Problem-solving and logical thinking
    - Data structures and algorithms
    - Database management
    - Web development
    - Software engineering principles
    - Mathematics and statistics
    - Communication skills
    - Project management
    - Continuous learning
    
    INDUSTRIES WHERE COMPUTER SCIENCE GRADUATES CAN WORK:
    - Technology companies (Google, Microsoft, Apple, etc.)
    - Financial services and banking
    - Healthcare and medical technology
    - E-commerce and retail
    - Gaming and entertainment
    - Government and public sector
    - Education and research
    - Consulting firms
    - Startups and entrepreneurship
    - Telecommunications
    
    COMPUTER SCIENCE CONTRIBUTION TO SOCIETY (Next 15 years):
    - Artificial Intelligence and automation
    - Smart cities and IoT
    - Healthcare technology and telemedicine
    - Environmental monitoring and sustainability
    - Education technology and e-learning
    - Financial technology and digital banking
    - Cybersecurity and data protection
    - Space technology and exploration
    - Biotechnology and bioinformatics
    - Renewable energy optimization
    """

def call_groq_with_context(question, system_prompt):
    """Call Groq API with specific context"""
    
    try:
        if not ExternalAPIConfig.is_groq_configured():
            return None
        
        headers = {
            "Authorization": f"Bearer {ExternalAPIConfig.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            "model": ExternalAPIConfig.GROQ_MODEL,
            "max_tokens": 500,
            "temperature": 0.3
        }
        
        response = http_requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content']
        
        return None
        
    except Exception as e:
        logger.error(f"Groq context API error: {e}")
        return None

@app.get("/materials/{course_code}")
async def get_course_materials(course_code: str):
    """Get available course materials for a specific course"""
    try:
        materials_dir = f"../data/course_materials/{course_code.upper()}"
        
        if not os.path.exists(materials_dir):
            return {
                "course_code": course_code.upper(),
                "materials": [],
                "message": "No materials available yet. Contact your lecturer for course materials."
            }
        
        files = [f for f in os.listdir(materials_dir) if f.endswith(('.pdf', '.html'))]
        
        return {
            "course_code": course_code.upper(),
            "materials": [
                {
                    "filename": f,
                    "download_url": f"/download/{course_code.upper()}/{f}",
                    "type": "PDF" if f.endswith('.pdf') else "HTML"
                } for f in files
            ],
            "total_files": len(files)
        }
        
    except Exception as e:
        logger.error(f"Error getting materials for {course_code}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error getting materials: {str(e)}")

if __name__ == "__main__":
    # Run the application
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
