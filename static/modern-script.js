// Modern script for enhanced functionality

document.addEventListener('DOMContentLoaded', function() {
    // Initialize theme toggle
    initThemeToggle();
    
    // Add animation class to game elements when they appear
    const gameElements = document.getElementById('game-elements');
    if (gameElements) {
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'style' && 
                    gameElements.style.display !== 'none') {
                    gameElements.classList.add('active');
                }
            });
        });
        
        observer.observe(gameElements, { attributes: true });
    }
    
    // Add sound effects for correct/wrong answers
    enhanceGameWithSoundEffects();
    
    // Add confetti effect for winning
    setupConfettiEffect();
});

// Theme toggle functionality
function initThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    const icon = themeToggle.querySelector('i');
    
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('quizBrainTheme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    }
    
    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-theme');
        
        if (document.body.classList.contains('dark-theme')) {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
            localStorage.setItem('quizBrainTheme', 'dark');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
            localStorage.setItem('quizBrainTheme', 'light');
        }
    });
}

// Add sound effects for correct/wrong answers
function enhanceGameWithSoundEffects() {
    // Only run this on the game page
    if (!document.getElementById('true-button')) return;
    
    const trueButton = document.getElementById('true-button');
    const falseButton = document.getElementById('false-button');
    const correctSound = document.getElementById('correct-sound');
    const wrongSound = document.getElementById('wrong-sound');
    
    // Store the original checkAnswer function
    const originalCheckAnswer = window.checkAnswer;
    
    // Override the checkAnswer function to add sound effects
    window.checkAnswer = function(userAnswer) {
        const isCorrect = userAnswer === currentQuestion.correct_answer;
        
        if (isCorrect) {
            correctSound.currentTime = 0;
            correctSound.play().catch(error => {
                console.error("Error playing correct sound:", error);
            });
            
            // Add visual feedback
            document.getElementById('question').classList.add('correct-answer');
            setTimeout(() => {
                document.getElementById('question').classList.remove('correct-answer');
            }, 500);
        } else {
            wrongSound.currentTime = 0;
            wrongSound.play().catch(error => {
                console.error("Error playing wrong sound:", error);
            });
            
            // Add visual feedback
            document.getElementById('question').classList.add('wrong-answer');
            setTimeout(() => {
                document.getElementById('question').classList.remove('wrong-answer');
            }, 500);
        }
        
        // Call the original function
        originalCheckAnswer(userAnswer);
    };
}

// Setup confetti effect for winning
function setupConfettiEffect() {
    // Store the original endGame function
    if (typeof endGame !== 'function') return;
    
    const originalEndGame = window.endGame;
    
    // Override the endGame function to add confetti for winners
    window.endGame = function(message) {
        if (message.includes('WIN')) {
            createConfetti();
        }
        
        // Call the original function
        originalEndGame(message);
    };
}

// Create confetti effect
function createConfetti() {
    const confettiCount = 200;
    const container = document.body;
    
    const colors = ['#6c5ce7', '#00cec9', '#fd79a8', '#00b894', '#fdcb6e', '#e17055'];
    
    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        
        // Random properties
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.animationDuration = (Math.random() * 3 + 2) + 's';
        confetti.style.animationDelay = Math.random() * 5 + 's';
        
        // Add to container
        container.appendChild(confetti);
        
        // Remove after animation
        setTimeout(() => {
            confetti.remove();
        }, 8000);
    }
}

// Add CSS for dark theme
const darkThemeCSS = `
    body.dark-theme {
        background: linear-gradient(135deg, #2d3436, #636e72, #2d3436);
    }
    
    body.dark-theme .container {
        background: rgba(45, 52, 54, 0.9);
        color: #f8f9fa;
    }
    
    body.dark-theme .header {
        color: #a29bfe;
    }
    
    body.dark-theme select {
        background-color: #2d3436;
        border-color: #636e72;
        color: #f8f9fa;
    }
    
    body.dark-theme #game-elements {
        background: rgba(45, 52, 54, 0.8);
    }
    
    body.dark-theme #question {
        background: #2d3436;
        color: #f8f9fa;
    }
    
    body.dark-theme #misses, 
    body.dark-theme #timer, 
    body.dark-theme #score {
        background: #2d3436;
        color: #f8f9fa;
    }
    
    body.dark-theme .score-overlay span {
        background: rgba(45, 52, 54, 0.9);
        color: #f8f9fa;
    }
`;

// Add the dark theme CSS to the document
const styleElement = document.createElement('style');
styleElement.textContent = darkThemeCSS;
document.head.appendChild(styleElement);

// Add CSS classes for correct/wrong answer feedback
const feedbackCSS = `
    .correct-answer {
        animation: correct-pulse 0.5s;
        background: rgba(0, 184, 148, 0.2) !important;
    }
    
    .wrong-answer {
        animation: wrong-pulse 0.5s;
        background: rgba(214, 48, 49, 0.2) !important;
    }
    
    @keyframes correct-pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    @keyframes wrong-pulse {
        0% { transform: scale(1); }
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }
    
    .rank-container {
        display: flex;
        align-items: center;
        background: white;
        border-radius: var(--border-radius-md);
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: var(--shadow-md);
        transition: transform 0.3s ease;
    }
    
    .rank-container:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-lg);
    }
    
    .rank-number {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: var(--neutral-200);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-right: 1rem;
    }
    
    .rank-number.gold {
        background: linear-gradient(135deg, #f9ca24, #f0932b);
        color: white;
    }
    
    .rank-number.silver {
        background: linear-gradient(135deg, #dfe6e9, #b2bec3);
        color: white;
    }
    
    .rank-number.bronze {
        background: linear-gradient(135deg, #e17055, #d63031);
        color: white;
    }
    
    .player-info {
        flex: 1;
        text-align: left;
        display: flex;
        flex-direction: column;
        gap: 0.25rem;
    }
    
    .leaderboard-tabs {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin: 1rem 0;
        justify-content: center;
    }
    
    .tab-button {
        padding: 0.5rem 1rem;
        background: var(--neutral-200);
        border: none;
        border-radius: var(--border-radius-sm);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .tab-button.active {
        background: var(--primary);
        color: white;
    }
    
    .no-scores {
        padding: 2rem;
        text-align: center;
        color: var(--neutral-600);
        font-size: 1.2rem;
    }
    
    body.dark-theme .rank-container {
        background: #2d3436;
        color: #f8f9fa;
    }
    
    body.dark-theme .tab-button {
        background: #2d3436;
        color: #f8f9fa;
    }
    
    body.dark-theme .tab-button.active {
        background: var(--primary);
    }
`;

// Add the feedback CSS to the document
const feedbackStyleElement = document.createElement('style');
feedbackStyleElement.textContent = feedbackCSS;
document.head.appendChild(feedbackStyleElement);
