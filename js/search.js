// search.js
document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.querySelector('.search-form');
    const searchInput = document.getElementById('search-input');

    searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const searchTerm = searchInput.value.toLowerCase().trim();
        
        // List of available athlete pages
        const athletes = [
            'bruno', 'enshu', 'dylan', 'gustaf', 'alex', 'garrett', 'emmett', 'ethan', 'cole', 'amir',
            'irie', 'alison', 'adrienne', 'elin', 'emily', 'alexandra', 'calla', 'ann', 'elsa', 'arabella'
        ];

        // Check if the search term matches any athlete
        const matchedAthlete = athletes.find(athlete => athlete.includes(searchTerm));

        if (matchedAthlete) {
            window.location.href = `athlete-${matchedAthlete}.html`;
        } else {
            alert('Athlete not found. Please try again.');
        }
    });
});