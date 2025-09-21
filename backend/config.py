"""
Configuration for external API integrations
"""

import os
from typing import Optional

class ExternalAPIConfig:
    """Configuration for external API services"""
    
    # API Keys from environment variables
    OPENAI_API_KEY: Optional[str] = os.getenv('OPENAI_API_KEY')
    GEMINI_API_KEY: Optional[str] = os.getenv('GEMINI_API_KEY')
    HUGGINGFACE_API_KEY: Optional[str] = os.getenv('HUGGINGFACE_API_KEY')
    SEARCH_API_KEY: Optional[str] = os.getenv('SEARCH_API_KEY')
    GROQ_API_KEY: Optional[str] = os.getenv('GROQ_API_KEY')
    
    @classmethod
    def has_openai_key(cls) -> bool:
        """Check if OpenAI API key is configured"""
        return cls.OPENAI_API_KEY is not None and cls.OPENAI_API_KEY != "your_openai_key_here"
    
    @classmethod
    def has_gemini_key(cls) -> bool:
        """Check if Gemini API key is configured"""
        return cls.GEMINI_API_KEY is not None and cls.GEMINI_API_KEY != "your_gemini_key_here"
    
    @classmethod
    def has_huggingface_key(cls) -> bool:
        """Check if Hugging Face API key is configured"""
        return cls.HUGGINGFACE_API_KEY is not None and cls.HUGGINGFACE_API_KEY != "your_hf_key_here"
    
    @classmethod
    def has_groq_key(cls) -> bool:
        """Check if Groq API key is configured"""
        return cls.GROQ_API_KEY is not None and cls.GROQ_API_KEY != "your_groq_key_here"