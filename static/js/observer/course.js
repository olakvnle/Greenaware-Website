

const Submit = document.querySelector('#course-form')
  const checkbox = document.querySelector("#course-check");
const csrfTokenElement = document.getElementsByName('csrfmiddlewaretoken')[0]
Submit.addEventListener('submit',(e)=>{

    e.preventDefault();

    // Check if the checkbox is checked
        if (checkbox.checked) {

             fetch('/submit-course/', {
                 method: 'POST',
                  headers: {
                 'Content-Type': 'application/json',
                 'X-CSRFToken': csrfTokenElement.value // Include CSRF token if CSRF protection is enabled
             },

    })
    .then((res) => {
        console.log(res)
        if (!res.ok) {
            throw new Error('Failed to Submit');
        }
        return res.json();
    })
    .then((data) => {
        if (data.success ) {
            toast('Congratulations! You have successfully completed the weather course. ' +
                'You are now qualified to provide weather data. Thank you for your participation!', );
        } else{
            toast(data.error, 'warning');
        }
console.log(data)
    })


        } else {
            toast('Checkbox is not checked', 'warning');

        }

    // Make a POST request to the login endpoint

});






function toast(msg,type='success'){
    if(type === 'warning')
        type='#dc3545'
    else if (type === 'success')
        type ='#198754'

         Toastify({text: msg, style: {background: type,}}).showToast();

    }


