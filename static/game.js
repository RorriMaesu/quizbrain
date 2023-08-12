const questionElement = document.getElementById("question");
const trueButton = document.getElementById("true-button");
const falseButton = document.getElementById("false-button");
const timerText = document.getElementById("timer");
const scoreElement = document.getElementById("score");
const startButton = document.getElementById("start-button");
const categorySelect = document.getElementById("category-select");
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
    
    // Always reset the timer after starting a new game
    resetTimer();
    getNextQuestion();  // Fetch the first question
}

function playBackgroundMusic() {
    const backgroundMusic = document.getElementById("background-music");
    backgroundMusic.play();
}

async function loadQuestionsByCategory() {
    const category = categorySelect.value;
    const askedQuestionsArray = Array.from(askedQuestions);
    const response = await fetch(`/get_questions?category=${category}&askedQuestions=${JSON.stringify(askedQuestionsArray)}`);
    const data = await response.json();
    questions = data.questions;
    getNextQuestion();
}

function getNextQuestion() {
    if (questions.length > 0) {
        currentQuestion = questions.shift();
        askedQuestions.add(currentQuestion.question);
        questionElement.textContent = currentQuestion.question;
        // Remove the resetTimer call from here
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
        // Add 3 seconds to the timer for correct answers
        timeLeft += 3; 
        updateTimer(); // Update the timer display after adding time
        getNextQuestion();  // Fetch the next question for correct answers
    } else {
        incorrectAnswers++;
        console.log("Incorrect answer count:", incorrectAnswers);
        updateMisses();  // Update the missed tally for incorrect answers
        if (incorrectAnswers === 5) {
            console.log("Incorrect answers reached 5. Game over condition met.");
            playGameOverSound();
            endGame("You have reached 5 incorrect answers, you lose!");
            return;
        } else {
            getNextQuestion();  // Fetch the next question for incorrect answers without resetting the timer
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
    console.log("Attempting to play game-over sound.");

    stopBackgroundMusic();

    const gameOverSound = document.getElementById("game-over-sound");
    gameOverSound.volume = 1.0;
    gameOverSound.play().then(() => {
        console.log("Game-over sound played successfully.");
    }).catch(error => {
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
        console.log("Time left:", timeLeft);
    } else {
        console.log("Time ran out. Game over condition met.");
        playGameOverSound();
        endGame(`Out of time! You answered ${parseInt(scoreElement.textContent.split(":")[1].trim())} questions correctly.`);
    }
}

function endGame(message) {
    playGameOverSound(); // Play game over sound at the beginning of the endGame function
    clearInterval(timerInterval);
    alert(message);
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
