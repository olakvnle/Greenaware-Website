'use strict'

const Base_URL = 'http://127.0.0.1:8090/';

const emailField = document.querySelector('#email');
const passwordField = document.querySelector('#password');
const Login = document.querySelector('.login');
const csrfTokenElement = document.getElementsByName('csrfmiddlewaretoken')[0]





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
    fetch(Base_URL + 'login/', {
        method: 'POST',
        headers: {
                 'Content-Type': 'application/json',
                 'X-CSRFToken': csrfTokenElement.value // Include CSRF token if CSRF protection is enabled
             },
        body: JSON.stringify({
            email,
            password,
        }),
    })
    .then((res) => {
        console.log(res)
        if (!res.ok) {
            throw new Error('Failed to authenticate');
        }
        return res.json();
    })
    .then((data) => {
        if (data.msg ) {
            window.location.href = data.msg;
        } else if (data.activate_error) {
            toast(data.activate_error, 'warning');
        }else if (data.error) {
            toast(data.error, 'warning');
        }

    })
    .catch((error) => {
        // Handle errors, such as network errors or server errors
        console.error('Error:', error);
        toast('No active account found with the given credentials');
    });
});





function toast(msg,type='success'){
    if(type === 'warning')
        type='#dc3545'
    else if (type === 'success')
        type ='#198754'

         Toastify({text: msg, style: {background: type,}}).showToast();

    }


