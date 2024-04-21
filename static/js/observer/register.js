'use strict'

const API_URL = 'http://127.0.0.1:8000/api/v1/';

const email = document.querySelector('#email');
const first_name = document.querySelector('#first_name');
const last_name = document.querySelector('#last_name');
const password = document.querySelector('#password');
const re_password = document.querySelector('#re_password');
const Register = document.querySelector('.register_observer');






// Register

Register.addEventListener('submit',(e)=>{

    e.preventDefault();

        if (email.value === "")
            toast('Email address field may not be blank','warning')
        else  if (first_name.value === "")
            toast('First name field may not be blank','warning')
        else  if (last_name.value === "")
            toast('Last name field may not be blank','warning')
        else  if (password.value === "")
            toast('Password field may not be blank','warning')
        else  if (re_password.value === "")
            toast('Confirm password field may not be blank','warning')

    if (email.value.length > 0) {
        fetch(API_URL + 'users/', {
            body: JSON.stringify({
                'email': email.value,
                'first_name': first_name.value,
                'last_name': last_name.value,
                'password': password.value,
                're_password': re_password.value
            }),
            headers: {
                'Content-Type': 'application/json'
            },
            method: 'POST'
        })
            .then((res) => res.json())
            .then((data) => {

                if(data.status==="success")
                    toast('Please check your Email to activate your account')
                else if (data.password){

                }

                console.log(data)
            })

    }
})





function toast(msg,type='success'){
    if(type === 'warning')
        type='#dc3545'
    else if (type === 'success')
        type ='#198754'

         Toastify({text: msg, style: {background: type,}}).showToast();

    }


