// Leaderboard.js - Handles the leaderboard display

document.addEventListener('DOMContentLoaded', function() {
    displayLeaderboard();
});

function displayLeaderboard() {
    const leaderboard = getLeaderboard();
    const leaderboardContainer = document.getElementById('leaderboard-container');

    // Clear any existing content
    leaderboardContainer.innerHTML = '';

    // Display top 9 scores
    const topScores = leaderboard.scores.slice(0, 9);

    topScores.forEach((score, index) => {
        const rankIndex = index + 1;

        // Create rank image container
        const rankImageDiv = document.createElement('div');
        rankImageDiv.className = 'rank-image';

        // Create rank image
        const rankImage = document.createElement('img');
        rankImage.src = `leaderboard_${rankIndex}.png`;
        rankImage.alt = `Rank ${rankIndex}`;

        // Add special styling for first place
        if (rankIndex === 1) {
            rankImage.style.position = 'relative';
            rankImage.style.top = '-10px';
        }

        // Create score overlay
        const scoreOverlay = document.createElement('div');
        scoreOverlay.className = 'score-overlay';

        // Create player name span
        const playerNameSpan = document.createElement('span');
        playerNameSpan.className = 'player-name';
        playerNameSpan.textContent = score.name;

        // Create category span
        const categorySpan = document.createElement('span');
        categorySpan.className = 'player-category';
        // Convert "Movies and TV Shows" to "TV" for display
        const displayCategory = score.category === "Movies and TV Shows" ? "TV" : score.category;
        categorySpan.textContent = displayCategory;

        // Create score span
        const scoreSpan = document.createElement('span');
        scoreSpan.className = 'score-text';
        scoreSpan.textContent = score.score;

        // Append all elements
        scoreOverlay.appendChild(playerNameSpan);
        scoreOverlay.appendChild(categorySpan);
        scoreOverlay.appendChild(scoreSpan);

        rankImageDiv.appendChild(rankImage);
        rankImageDiv.appendChild(scoreOverlay);

        leaderboardContainer.appendChild(rankImageDiv);
    });
}
