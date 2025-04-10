const questionElement = document.getElementById("question");
const trueButton = document.getElementById("true-button");
const falseButton = document.getElementById("false-button");
const timerText = document.getElementById("timer");
const scoreElement = document.getElementById("score");
const startButton = document.getElementById("start-button");
const categorySelect = document.getElementById("category-select");
const leaderboardButton = document.getElementById("view-leaderboard-button");
const missesElement = document.getElementById("misses");

let currentQuestion;
let questions = [];
let timerInterval;
let timeLeft = 18;
let incorrectAnswers = 0;
let askedQuestions = new Set();

function startGame() {
    document.getElementById("game-elements").style.display = "block";
    loadQuestionsByCategory();
    playBackgroundMusic();
    resetTimer();
    getNextQuestion();
}

function playBackgroundMusic() {
    const backgroundMusic = document.getElementById("background-music");
    backgroundMusic.play().catch(error => {
        console.error("Error playing background music:", error);
    });
}

function loadQuestionsByCategory() {
    const category = categorySelect.value;
    const askedQuestionsArray = Array.from(askedQuestions);

    // Get questions and reset flag
    const result = getRandomQuestions(category, askedQuestionsArray, 5);
    questions = result.questions;

    // If we need to reset tracking (all questions were asked), clear the Set
    if (result.resetTracking) {
        // Show a notification to the user
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = 'All questions in this category have been asked. Starting over with shuffled questions!';
        document.querySelector('.container').appendChild(notification);

        // Remove the notification after 3 seconds
        setTimeout(() => {
            notification.remove();
        }, 3000);

        // Clear the tracking Set
        askedQuestions.clear();
    }

    getNextQuestion();
}

function getNextQuestion() {
    if (questions.length > 0) {
        currentQuestion = questions.shift();
        askedQuestions.add(currentQuestion.question);
        questionElement.textContent = currentQuestion.question;
    } else {
        let currentScore = parseInt(scoreElement.textContent.split(":")[1].trim());
        if (currentScore === 30) {
            endGame("Congratulations, you answered 30 questions correctly. You may not be very attractive, but YOU WIN!");
        } else {
            loadQuestionsByCategory();
        }
    }
}

function checkAnswer(userAnswer) {
    if (userAnswer === currentQuestion.correct_answer) {
        updateScore();
        timeLeft += 3;
        updateTimer();
        getNextQuestion();
    } else {
        incorrectAnswers++;
        updateMisses();
        if (incorrectAnswers === 5) {
            playGameOverSound();
            endGame("You have reached 5 incorrect answers, you lose!");
            return;
        } else {
            getNextQuestion();
        }
    }
}

function updateMisses() {
    missesElement.textContent = `Misses: ${incorrectAnswers}`;
}

function updateScore() {
    let currentScore = parseInt(scoreElement.textContent.split(":")[1].trim());
    currentScore++;
    scoreElement.textContent = `Score: ${currentScore}`;
}

function playGameOverSound() {
    stopBackgroundMusic();
    const gameOverSound = document.getElementById("game-over-sound");
    gameOverSound.volume = 1.0;
    gameOverSound.play().catch(error => {
        console.error("Error playing game-over sound:", error);
    });
}

function resetTimer() {
    clearInterval(timerInterval);
    timerInterval = setInterval(updateTimer, 1000);
    timeLeft = 18;
    updateTimer();
}

function updateTimer() {
    if (timeLeft > 0) {
        timerText.textContent = `Time Left: ${timeLeft}`;
        timeLeft--;
    } else {
        playGameOverSound();
        endGame(`Out of time! You answered ${parseInt(scoreElement.textContent.split(":")[1].trim())} questions correctly.`);
    }
}

function endGame(message) {
    playGameOverSound();
    clearInterval(timerInterval);
    alert(message);

    let currentScore = parseInt(scoreElement.textContent.split(":")[1].trim());
    let category = categorySelect.value;

    let playerName = prompt("Enter your name:");
    if(playerName) {
        // Update leaderboard in localStorage
        updateLeaderboard(playerName, currentScore, category);
        alert("Leaderboard updated!");
    }

    window.location.reload();
}

function stopBackgroundMusic() {
    const backgroundMusic = document.getElementById("background-music");
    backgroundMusic.pause();
    backgroundMusic.currentTime = 0;
}

trueButton.addEventListener("click", () => checkAnswer("True"));
falseButton.addEventListener("click", () => checkAnswer("False"));
startButton.addEventListener("click", startGame);
leaderboardButton.addEventListener("click", function() {
    stopBackgroundMusic();
    // Check if we're running on GitHub Pages or locally
    const isGitHubPages = window.location.hostname.includes('github.io');
    window.location.href = isGitHubPages ? "leaderboard.html" : "/leaderboard";
});
