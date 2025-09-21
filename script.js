// FUT QA Assistant Frontend JavaScript

// Configuration
const API_BASE_URL = window.location.origin; // Use the same domain as the frontend

// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const questionInput = document.getElementById('questionInput');
const askButton = document.getElementById('askButton');
const buttonText = document.getElementById('buttonText');
const loadingSpinner = document.getElementById('loadingSpinner');
const apiStatus = document.getElementById('apiStatus');
const modelStatus = document.getElementById('modelStatus');

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    checkAPIHealth();
    setupEventListeners();
});

// Setup event listeners
function setupEventListeners() {
    // Enter key to send message
    questionInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            askQuestion();
        }
    });
    
    // Auto-resize textarea
    questionInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });
    
}

// Check API health
async function checkAPIHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        const data = await response.json();
        
        if (response.ok) {
            apiStatus.textContent = 'Connected';
            apiStatus.className = 'status-value healthy';
            modelStatus.textContent = data.model_loaded ? data.model_name : 'Not loaded';
            modelStatus.className = `status-value ${data.model_loaded ? 'healthy' : 'unhealthy'}`;
        } else {
            throw new Error('API not responding');
        }
    } catch (error) {
        console.error('Health check failed:', error);
        apiStatus.textContent = 'Disconnected';
        apiStatus.className = 'status-value unhealthy';
        modelStatus.textContent = 'Unknown';
        modelStatus.className = 'status-value unhealthy';
    }
}

// Ask a question
async function askQuestion() {
    const question = questionInput.value.trim();
    
    if (!question) {
        showNotification('Please enter a question!', 'error');
        return;
    }
    
    // Add user message to chat
    addMessageToChat(question, 'user');
    
    // Clear input
    questionInput.value = '';
    questionInput.style.height = 'auto';
    
    // Show loading state
    setLoadingState(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/ask`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: question
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            // Add bot response to chat
            addMessageToChat(data.answer, 'bot', data.confidence, data.model_used);
        } else {
            throw new Error(data.detail || 'Failed to get answer');
        }
    } catch (error) {
        console.error('Error asking question:', error);
        addMessageToChat(
            'Sorry, I encountered an error while processing your question. Please try again later.',
            'bot',
            0,
            'error'
        );
    } finally {
        setLoadingState(false);
    }
}

// Add message to chat
function addMessageToChat(message, sender, confidence = null, modelUsed = null) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    // Add message text
    const messageText = document.createElement('p');
    messageText.textContent = message;
    contentDiv.appendChild(messageText);
    
    // Add confidence score and model info if available
    if (confidence !== null && sender === 'bot') {
        const infoDiv = document.createElement('div');
        infoDiv.className = 'confidence-score';
        
        let confidenceClass = 'confidence-low';
        if (confidence > 0.7) confidenceClass = 'confidence-high';
        else if (confidence > 0.4) confidenceClass = 'confidence-medium';
        
        infoDiv.innerHTML = `
            <span class="${confidenceClass}">Confidence: ${(confidence * 100).toFixed(1)}%</span>
            ${modelUsed ? ` • Model: ${modelUsed}` : ''}
        `;
        contentDiv.appendChild(infoDiv);
    }
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Set loading state
function setLoadingState(loading) {
    askButton.disabled = loading;
    questionInput.disabled = loading;
    
    if (loading) {
        buttonText.style.display = 'none';
        loadingSpinner.style.display = 'inline';
    } else {
        buttonText.style.display = 'inline';
        loadingSpinner.style.display = 'none';
    }
}

// Show notification
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    // Style the notification
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        z-index: 1000;
        animation: slideIn 0.3s ease;
        max-width: 300px;
    `;
    
    // Set background color based on type
    switch (type) {
        case 'error':
            notification.style.background = '#dc3545';
            break;
        case 'success':
            notification.style.background = '#28a745';
            break;
        default:
            notification.style.background = '#17a2b8';
    }
    
    // Add to page
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

// Add CSS animations for notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Periodic health check
setInterval(checkAPIHealth, 30000); // Check every 30 seconds
