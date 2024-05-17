'use strict'




const Activate = document.querySelector('.activate_account');
const csrfTokenElement = document.getElementsByName('csrfmiddlewaretoken')[0]
const uidField = document.querySelector('#uid');
const tokenField = document.querySelector('#token');

const API_URL = 'http://127.0.0.1:3000/api/v1/';


// Register

Activate.addEventListener('click',(e)=>{

    e.preventDefault();
     const uid= uidField.value.trim()
      const token= tokenField.value.trim()

           fetch(API_URL + 'users/activation/', {
               headers: {
                'Content-Type': 'application/json'
            },
            method: 'POST',
            body: JSON.stringify({
                'uid': uid,
                'token': token,

            }),

        })
            .then((res) => res.json())
            .then((data) => {

                if(data.uid)
                    toast(data.uid[0],'warning')
                else if (data.token){
                    toast(data.token[0],'warning')
                }
                 else if (data.non_field_errors){
                    toast(data.non_field_errors[0])
                }
                  else if (data.detail){
                    toast('Account has Already been activated')
                }else {
                       toast('Account has been activated Successful')
                }

                console.log(data)
            })


})





function toast(msg,type='success'){
    if(type === 'warning')
        type='#dc3545'
    else if (type === 'success')
        type ='#198754'

         Toastify({text: msg, style: {background: type,}}).showToast();

    }


