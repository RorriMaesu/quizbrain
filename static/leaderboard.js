// Leaderboard.js - Handles the leaderboard display with modern styling

document.addEventListener('DOMContentLoaded', function() {
    // Hide loader after a short delay to show animation
    setTimeout(() => {
        const loader = document.getElementById('leaderboard-loader');
        if (loader) {
            loader.style.display = 'none';
        }
        displayLeaderboard();
    }, 800);
});

function displayLeaderboard() {
    const leaderboard = getLeaderboard();
    const leaderboardContainer = document.getElementById('leaderboard-container');

    // Clear any existing content except the loader
    const loader = document.getElementById('leaderboard-loader');
    leaderboardContainer.innerHTML = '';
    if (loader) {
        leaderboardContainer.appendChild(loader);
    }

    // Display top 9 scores
    const topScores = leaderboard.scores.slice(0, 9);

    // Create a wrapper for the leaderboard entries
    const entriesWrapper = document.createElement('div');
    entriesWrapper.className = 'leaderboard-entries';

    topScores.forEach((score, index) => {
        const rankIndex = index + 1;

        // Create rank image container with animation delay
        const rankImageDiv = document.createElement('div');
        rankImageDiv.className = 'rank-image fade-in';
        rankImageDiv.style.animationDelay = `${index * 0.1}s`;
        rankImageDiv.setAttribute('data-category', score.category);

        // Create rank container
        const rankContainer = document.createElement('div');
        rankContainer.className = 'rank-container';

        // Create rank number
        const rankNumber = document.createElement('div');
        rankNumber.className = 'rank-number';
        rankNumber.innerHTML = `<span>${rankIndex}</span>`;

        // Create medal for top 3
        if (rankIndex <= 3) {
            const medalClass = rankIndex === 1 ? 'gold' : rankIndex === 2 ? 'silver' : 'bronze';
            rankNumber.classList.add(medalClass);
            rankNumber.innerHTML = `<i class="fas fa-medal"></i>`;
        }

        // Create player info container
        const playerInfo = document.createElement('div');
        playerInfo.className = 'player-info';

        // Create player name
        const playerName = document.createElement('div');
        playerName.className = 'player-name';
        playerName.innerHTML = `<i class="fas fa-user"></i> <span>${score.name}</span>`;

        // Create category
        const category = document.createElement('div');
        category.className = 'player-category';
        // Convert "Movies and TV Shows" to "TV" for display
        const displayCategory = score.category === "Movies and TV Shows" ? "TV & Movies" : score.category;
        category.innerHTML = `<i class="fas fa-tag"></i> <span>${displayCategory}</span>`;

        // Create score
        const scoreElement = document.createElement('div');
        scoreElement.className = 'score-text';
        scoreElement.innerHTML = `<i class="fas fa-star"></i> <span>${score.score}</span>`;

        // Append elements to player info
        playerInfo.appendChild(playerName);
        playerInfo.appendChild(category);

        // Append elements to rank container
        rankContainer.appendChild(rankNumber);
        rankContainer.appendChild(playerInfo);
        rankContainer.appendChild(scoreElement);

        // Append rank container to rank image div
        rankImageDiv.appendChild(rankContainer);

        // Append to entries wrapper
        entriesWrapper.appendChild(rankImageDiv);
    });

    // Append entries wrapper to leaderboard container
    leaderboardContainer.appendChild(entriesWrapper);

    // If no scores, show a message
    if (topScores.length === 0) {
        const noScores = document.createElement('div');
        noScores.className = 'no-scores';
        noScores.innerHTML = '<i class="fas fa-exclamation-circle"></i> No scores yet. Be the first to play!';
        leaderboardContainer.appendChild(noScores);
    }
}
