'use strict'

const Base_url = 'http://127.0.0.1:8090/';

const email = document.querySelector('#email');
const first_name = document.querySelector('#first_name');
const last_name = document.querySelector('#last_name');
const password = document.querySelector('#password');
const re_password = document.querySelector('#re_password');
const Register = document.querySelector('.register_observer');
const csrfTokenElement = document.getElementsByName('csrfmiddlewaretoken')[0]






// Register

Register.addEventListener('submit',(e)=>{

    e.preventDefault();

        if (email.value === ""){
            toast('Email address field may not be blank','warning')
            return
        }

        else  if (first_name.value === ""){
            toast('First name field may not be blank','warning')
            return
        }

        else  if (last_name.value === ""){
             toast('Last name field may not be blank','warning')
            return
        }

        else  if (password.value === ""){
             toast('Password field may not be blank','warning')
            return
        }
        else  if (re_password.value === ""){
            toast('Confirm password field may not be blank','warning')
            return;
        }


    // if (email.value.length > 0) {
        fetch(Base_url+'observer/', {
             method: 'POST',
             headers: {
                 'Content-Type': 'application/json',
                 'X-CSRFToken': csrfTokenElement.value // Include CSRF token if CSRF protection is enabled
             },
            body: JSON.stringify({
                'email': email.value,
                'first_name': first_name.value,
                'last_name': last_name.value,
                'password': password.value,
                're_password': re_password.value
            }),

        })
            .then(response =>  response.json())
            .then((data) => {
                if(data.success)
                    toast('Please check your Email to activate your account')
                else if (data.email_error && data.email_error.length > 0){
                     toast(data.email_error,'warning')
                }
                else if (data.password_error && data.password_error.length > 0){
                     toast(data.password_error,'warning')
                }
                else if (data.re_password_error && data.re_password_error.length > 0){
                     toast(data.re_password_error,'warning')
                }
                console.log(data)
            })
    // }
})





function toast(msg,type='success'){
    if(type === 'warning')
        type='#dc3545'
    else if (type === 'success')
        type ='#198754'

         Toastify({text: msg, style: {background: type,}}).showToast();

    }


