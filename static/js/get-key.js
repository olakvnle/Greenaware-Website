


 const GenerateKey = document.querySelector('.generate_api_key');
const apikey = document.querySelector('.api-key');
const created_date = document.querySelector('.created-date');
const used_date = document.querySelector('.used-date');

// Create a new Date object
const currentDate = new Date();

// Get the current date
const day = currentDate.getDate(); // Day of the month (1-31)
const month = currentDate.getMonth() + 1; // Month (0-11, add 1 to get the actual month)
const year = currentDate.getFullYear();

GenerateKey.addEventListener('click', (e) => {
    e.preventDefault();

     check_token();
 const jwtToken=localStorage.getItem('access')
    apikey.textContent= jwtToken;
    created_date.textContent= ` ${day}/${month}/${year}`
    used_date.textContent= `${day}/${month}/${year}`



});
