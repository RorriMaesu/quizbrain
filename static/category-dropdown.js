// Category Dropdown for Leaderboard
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the dropdown
    initCategoryDropdown();
});

function initCategoryDropdown() {
    const dropdownButton = document.querySelector('.dropdown-button');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    const dropdownItems = document.querySelectorAll('.dropdown-item');

    if (!dropdownButton || !dropdownMenu) {
        return;
    }

    // Toggle dropdown when button is clicked
    dropdownButton.addEventListener('click', function() {
        dropdownButton.classList.toggle('active');
        dropdownMenu.classList.toggle('show');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function(event) {
        if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownButton.classList.remove('active');
            dropdownMenu.classList.remove('show');
        }
    });

    // Handle dropdown item selection
    dropdownItems.forEach(item => {
        item.addEventListener('click', function() {
            // Update button text - get the text from the span element
            const categoryName = this.querySelector('span').textContent.trim();
            const buttonText = dropdownButton.querySelector('span');
            buttonText.textContent = categoryName;

            // Update active state
            dropdownItems.forEach(i => i.classList.remove('active'));
            this.classList.add('active');

            // Close dropdown
            dropdownButton.classList.remove('active');
            dropdownMenu.classList.remove('show');

            // Filter leaderboard
            const filter = this.getAttribute('data-filter');
            filterLeaderboard(filter);
        });
    });
}

// This function is already defined in the leaderboard.html script section
// We're keeping it here for reference
/*
function filterLeaderboard(filter) {
    const entries = document.querySelectorAll('.rank-image');

    entries.forEach(entry => {
        const category = entry.getAttribute('data-category');

        if (filter === 'all' || category === filter) {
            entry.style.display = 'block';
        } else {
            entry.style.display = 'none';
        }
    });
}
*/
