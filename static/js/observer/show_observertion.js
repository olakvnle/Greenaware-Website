


 load_observation();




function load_observation(){
    check_token();
    const tableBody = document.getElementById('observationTableBody'); // Assuming you have a tbody element with id="observationTableBody" in your HTML
     const jwtToken=localStorage.getItem('access')
    fetch(apiURL + 'observations/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${jwtToken}`,

        }
    })
    .then((res) => res.json())
    .then((data) => {
        // Clear existing table rows
        tableBody.innerHTML = '';

        // Iterate over the data and create table rows
        data.forEach((observation) => {
            const row = document.createElement('tr');

            // Iterate over each property of the observation object and create table cells
            for (const key in observation) {
                if (observation.hasOwnProperty(key) && key !== 'user') {
                    const cell = document.createElement('td');
                    cell.textContent = observation[key];
                    row.appendChild(cell);
                }
            }
            tableBody.appendChild(row);
        // console.log( data);
    })
    })
    .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
    });
}


// function verifyToken(jwtToken) {
//     const url = `${apiURL}jwt/verify/`;
//     const requestData = {
//         token: jwtToken
//     };
//
//     return fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             // You may need to include the CSRF token here if CSRF protection is enabled
//         },
//         body: JSON.stringify(requestData)
//     })
//     .then(response => {
//         if (response.ok) {
//             return response.json();
//         } else {
//             throw new Error('Token verification failed');
//         }
//     });
// }
//
// function RefreshToken(refreshToken) {
//     const url = `${apiURL}jwt/refresh/`;
//     const requestData = {
//         refresh: refreshToken
//     };
//
//     return fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             // You may need to include the CSRF token here if CSRF protection is enabled
//         },
//         body: JSON.stringify(requestData)
//     })
//     .then(response => {
//         if (response.ok) {
//             return response.json();
//         } else {
//             throw new Error('Token refresh failed');
//         }
//     });
// }
//
//
// function check_token(){
//     const jwtToken = localStorage.getItem('access')
// verifyToken(jwtToken)
//     .then(data => {
//         console.log('Token verification successful:', data);
//         // Proceed with authenticated actions
//     })
//     .catch(error => {
//         console.error('Token verification failed:', error);
//         // Token is invalid or expired, attempt to refresh it
//         const refreshToken = localStorage.getItem('refresh');
//         RefreshToken(refreshToken)
//             .then(data => {
//                 console.log('Token refresh successful:', data);
//                  localStorage.setItem('refresh',data.refresh)
//                  localStorage.setItem('access',data.access)
//                 storeToken(data.access,data.refresh)
//             })
//             .catch(error => {
//                 console.error('Token refresh failed:', error);
//                 // Handle refresh token failure (e.g., redirect to login page)
//             });
//     });
//
// }
//
// function storeToken(access,refresh){
//     fetch('/store-tokens/', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json',
//         // 'X-CSRFToken': csrfTokenElement.value // Include CSRF token if CSRF protection is enabled
//     },
//     body: JSON.stringify({
//         'access':access,
//         'refresh':refresh,
//     }),
// })
// .then(response => response.json())
// .then((data) => {
//     console.log(data)
//     })
// }