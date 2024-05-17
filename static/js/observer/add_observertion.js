
 const form = document.querySelector('.add_observation');
//
 const date = document.querySelector('#date');
const time = document.querySelector('#time');
const timeZoneOffset = document.querySelector('#timeZoneOffset');
const what3words = document.querySelector('#what3words');
const temperatureLandSurface = document.querySelector('#temperatureLandSurface');
const temperatureSeaSurface = document.querySelector('#temperatureSeaSurface');
const humidity = document.querySelector('#humidity');
const windSpeed = document.querySelector('#windSpeed');
const windDirection = document.querySelector('#windDirection');
const precipitation = document.querySelector('#precipitation');
const haze = document.querySelector('#haze');
const notes = document.querySelector('#notes');

 const csrfTokenElement = document.getElementsByName('csrfmiddlewaretoken')[0]



form.addEventListener('submit', (e) => {
    e.preventDefault();

     check_token();

    const formData = {
    "date": date.value,
    "time": time.value,
    "timeZoneOffset": timeZoneOffset.value,
    "location": what3words.value,
    "temperatureLandSurface": temperatureLandSurface.value,
    "temperatureSeaSurface": temperatureSeaSurface.value,
    "humidity": humidity.value,
    "windSpeed": windSpeed.value,
    "windDirection": windDirection.value,
    "precipitation": precipitation.value,
    "haze": haze.value,
    "notes": notes.textContent
};

    const jwtToken=localStorage.getItem('access')
    fetch(apiURL + 'observations/', {
        method: 'POST',
        body: JSON.stringify(formData), // Set the body to the FormData object
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${jwtToken}`,
            'X-CSRFToken': csrfTokenElement.value // Include CSRF token if CSRF protection is enabled

        }
    })
    .then((res) => res.json())
    .then((data) => {

        if (data.detail ) {
            toast(data.detail);
        } else if (data.message) {
           toast(data.message);
        }else if (data.id) {
           toast("Observation created Successfully");
        }else if (data && Object.keys(data).length > 0) {
            // Handle validation errors
            for (const field in data) {
                if (data.hasOwnProperty(field)) {
                   const errors = data[field];
                    const errorMessage = errors.join(', '); // Concatenate error message
                // Display error message next to the input field
                    const errorElement = document.getElementById(`${field}Error`);
                    errorElement.textContent = errorMessage;
                }
            }
        }

    })
    .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
    });
});


function toast(msg,type='success'){
    if(type === 'warning')
        type='#dc3545'
    else if (type === 'success')
        type ='#198754'

         Toastify({text: msg, style: {background: type,}}).showToast();

    }


