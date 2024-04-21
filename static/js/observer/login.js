'use strict'

const API_URL = 'http://127.0.0.1:8000/api/v1/';

const emailField = document.querySelector('#email');
const passwordField = document.querySelector('#password');
const Login = document.querySelector('.login_observer');






// Register

Login.addEventListener('submit',(e)=>{

    e.preventDefault();

    const email = emailField.value.trim();
    const password = passwordField.value.trim();

    // Basic validation for email and password fields
    if (!email) {
        toast('Email address field may not be blank', 'warning');
        return;
    }
    if (!password) {
        toast('Password field may not be blank', 'warning');
        return;
    }

    // Make a POST request to the login endpoint
    fetch(API_URL + 'jwt/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email,
            password,
        }),
    })
    .then((res) => {
        if (!res.ok) {
            throw new Error('Failed to authenticate');
        }
        return res.json();
    })
    .then((data) => {
        // Check if the response contains both access and refresh tokens
        if (data.access && data.refresh) {
            // Store the tokens securely, for example, in local storage
            localStorage.setItem('accessToken', data.access);
            localStorage.setItem('refreshToken', data.refresh);

            // Redirect the user to another page, such as the dashboard
            window.location.href = '/dashboard';
        } else {
            // Handle the case where tokens are missing in the response
            toast('Invalid response from the server', 'error');
        }
    })
    .catch((error) => {
        // Handle errors, such as network errors or server errors
        console.error('Error:', error);
        toast('An error occurred during login', 'error');
    });
});





function toast(msg,type='success'){
    if(type === 'warning')
        type='#dc3545'
    else if (type === 'success')
        type ='#198754'

         Toastify({text: msg, style: {background: type,}}).showToast();

    }


