document.addEventListener('DOMContentLoaded', function() {
    var redirectHomeElement = document.getElementById('redirectHome');
    if (redirectHomeElement) {
        redirectHomeElement.addEventListener('click', function() {
            window.location.href = 'http://localhost:5500/homepage.html';
        });
    }

    var homeLoginElement = document.getElementById('homeLogin');
    if (homeLoginElement) {
        homeLoginElement.addEventListener('click', function() {
            window.location.href = 'http://localhost:5500/login.html';
        });
    }

    // Code to refresh the page when the home logo and title are clicked
    var homeLogoAndTitle = document.querySelector('.home-logo-and-title');
    if (homeLogoAndTitle) {
        homeLogoAndTitle.addEventListener('click', function() {
            location.reload();
        });
    }

    var aboutLogoAndTitle = document.querySelector('.about-logo-and-title');
    if (aboutLogoAndTitle) {
        aboutLogoAndTitle.addEventListener('click', function() {
            window.location.href = 'http://localhost:5500/homepage.html';
        });
    }

    var contactLogoAndTitle = document.querySelector('.contact-logo-and-title');
    if (contactLogoAndTitle) {
        contactLogoAndTitle.addEventListener('click', function() {
            window.location.href = 'http://localhost:5500/homepage.html';
        });
    }

    var homeLogoAndTitle = document.querySelector('.land-logo-and-title');
    if (homeLogoAndTitle) {
        homeLogoAndTitle.addEventListener('click', function() {
            location.reload();
        });
    }
    var googleSignInButton = document.querySelector('.g-signin2');
    if (googleSignInButton) {
        googleSignInButton.addEventListener('click', function() {
            window.location.href = '/accounts/google/login/'; // URL for Django Allauth Google login
        });
    }
});