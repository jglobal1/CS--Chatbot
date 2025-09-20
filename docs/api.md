# API Documentation

This document describes the REST API endpoints for the FUT QA Assistant.

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, no authentication is required. In production, implement proper authentication.

## Endpoints

### 1. Root Endpoint

**GET** `/`

Returns basic information about the API.

**Response:**
```json
{
    "message": "FUT QA Assistant API",
    "status": "running",
    "model_loaded": true
}
```

### 2. Health Check

**GET** `/health`

Returns the health status of the API and model.

**Response:**
```json
{
    "status": "healthy",
    "model_loaded": true,
    "model_name": "fine-tuned"
}
```

**Status Codes:**
- `200`: API is healthy
- `503`: Model not loaded

### 3. Ask Question

**POST** `/ask`

Main endpoint for asking questions.

**Request Body:**
```json
{
    "question": "What is FUT known for?",
    "context": "Optional context text..."
}
```

**Parameters:**
- `question` (string, required): The question to ask
- `context` (string, optional): Additional context for the question

**Response:**
```json
{
    "answer": "technology and engineering education",
    "confidence": 0.95,
    "model_used": "fine-tuned"
}
```

**Response Fields:**
- `answer` (string): The generated answer
- `confidence` (float): Confidence score (0-1)
- `model_used` (string): Which model was used ("fine-tuned" or "pre-trained")

**Status Codes:**
- `200`: Question answered successfully
- `503`: Model not loaded
- `500`: Internal server error

### 4. Reload Model

**POST** `/reload-model`

Reloads the model (useful after training a new model).

**Response:**
```json
{
    "message": "Model reloaded successfully",
    "model_loaded": true
}
```

**Status Codes:**
- `200`: Model reloaded successfully
- `500`: Error reloading model

## Error Responses

All error responses follow this format:

```json
{
    "detail": "Error message description"
}
```

## Example Usage

### Using curl

```bash
# Health check
curl http://localhost:8000/health

# Ask a question
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What programming languages are taught at FUT?",
    "context": "The Computer Science department offers courses in various programming languages."
  }'
```

### Using Python

```python
import requests

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())

# Ask a question
response = requests.post(
    "http://localhost:8000/ask",
    json={
        "question": "What is FUT known for?",
        "context": "Federal University of Technology is a Nigerian university."
    }
)
print(response.json())
```

### Using JavaScript

```javascript
// Health check
fetch('http://localhost:8000/health')
  .then(response => response.json())
  .then(data => console.log(data));

// Ask a question
fetch('http://localhost:8000/ask', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    question: 'What programs does FUT offer?',
    context: 'FUT offers various academic programs.'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Rate Limiting

Currently, no rate limiting is implemented. In production, implement appropriate rate limiting.

## CORS

CORS is enabled for all origins in development. In production, configure CORS to allow only your frontend domain.

## Model Information

### Fine-tuned Model

When a fine-tuned model is available, it will be used automatically. The model should be located at:
```
data/models/fut_qa_model/
```

### Pre-trained Model

If no fine-tuned model is found, the system falls back to:
```
distilbert/distilbert-base-cased-distilled-squad
```

## Performance Considerations

- Model loading time: ~2-5 seconds on first request
- Response time: ~100-500ms per question
- Memory usage: ~1-2GB for the model
- Concurrent requests: Limited by available memory

## Monitoring

Monitor the following metrics:
- Response times
- Error rates
- Model confidence scores
- Memory usage
- CPU usage
