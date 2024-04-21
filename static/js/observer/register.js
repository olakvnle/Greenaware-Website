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
            .then(response =>  response.json())
            .then((data) => {
                if(data.status==="success")
                    toast('Please check your Email to activate your account')
                else if (data.non_field_errors && data.non_field_errors.length > 0){
                     toast(data.non_field_errors[0],'warning')
                }
                else if (data.password && data.password.length > 0){
                     toast(data.password[0],'warning')
                }
                else if (data.email && data.email.length > 0){
                     toast(data.email[0],'warning')
                }
                //console.log(data)
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


