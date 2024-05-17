'use strict'



const emailField = document.querySelector('#email');
const passwordField = document.querySelector('#password');
const Login = document.querySelector('.login');
const btnSubmit = document.querySelector('#login-check');
const csrfTokenElement = document.getElementsByName('csrfmiddlewaretoken')[0]
 const checkbox = document.querySelector("#login-check");
const api_url =  'http://127.0.0.1:3000/api/v1/';


// Login

Login.addEventListener('submit',(e)=>{

    e.preventDefault();

     // btnSubmit.disabled= true;

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

                login(email, password, `/login/`)
                     .then((res => res.json()))
                     .then((data) => {

                 if (data.msg ) {
                     generateToken(email, password,data.msg);
                     console.log(data)
                     //window.location.href = data.msg;
                 } else if (data.activate_error) {
                     toast(data.activate_error, 'warning');
                 }else if (data.error) {
                     toast(data.error, 'warning');
                 }

                 // btnSubmit.disabled= false;
 })






});

function generateToken(email, password,uri){
     login(email, password, `${api_url}jwt/create/`)
             .then((res => res.json()))
             .then((data) => {
                 localStorage.setItem('refresh',data.refresh)
                 localStorage.setItem('access',data.access)
                 if (data.access) {
                     auth(data.access, data.refresh,uri)
                     //window.location.href = '/observer/dashboard';

                 } else if (data.password) {
                     toast(data.password, 'warning');
                 }
                 console.log(data)
          })
}


function login(email, password, url) {
    return fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfTokenElement.value // Include CSRF token if CSRF protection is enabled
        },
        body: JSON.stringify({
            email,
            password,
        }),
    });
}


function auth(access,refresh,url=''){
    fetch('/store-tokens/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
         'X-CSRFToken': csrfTokenElement.value // Include CSRF token if CSRF protection is enabled
    },
    body: JSON.stringify({
        'access':access,
        'refresh':refresh,
    }),
})
.then(response => response.json())
.then((data) => {
    window.location.href = url;
    console.log(data)
    })
}


function toast(msg,type='success'){
    if(type === 'warning')
        type='#dc3545'
    else if (type === 'success')
        type ='#198754'

         Toastify({text: msg, style: {background: type,}}).showToast();

    }


