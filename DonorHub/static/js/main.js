function onSignIn(googleUser) {
    // Get user profile information
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail());

    // The ID token you need to pass to your backend:
    var id_token = googleUser.getAuthResponse().id_token;
    console.log("ID Token: " + id_token);

    // Here, you would handle the sign-in process, like sending the token to your server
}

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
});