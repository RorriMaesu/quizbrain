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
let timeLeft = 10;
let incorrectAnswers = 0;
let askedQuestions = new Set();

function startGame() {
    document.getElementById("game-elements").style.display = "block";
    loadQuestionsByCategory();
    playBackgroundMusic();
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
        resetTimer();
    } else {
        let currentScore = parseInt(scoreElement.textContent.split(":")[1].trim());
        if (currentScore === 10) {
            endGame("Congratulations, you answered 10 questions correctly. You win!");
        } else {
            loadQuestionsByCategory();
        }
    }
}

function checkAnswer(userAnswer) {
    if (userAnswer === currentQuestion.correct_answer) {
        updateScore();
    } else {
        incorrectAnswers++;
        updateMisses();
        if (incorrectAnswers === 5) {
            playGameOverSound();
            setTimeout(() => {
                endGame("You have reached 5 incorrect answers, you lose!");
            }, 500); // Delay the game over message by half a second to ensure the sound plays.
            return;
        }
    }
    getNextQuestion();
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
    timeLeft = 10;
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
        endGame(`You ran out of time after answering ${parseInt(scoreElement.textContent.split(":")[1].trim())} questions correctly. You lose!`);
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
