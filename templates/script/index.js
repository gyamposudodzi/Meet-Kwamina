const form = document.querySelector('.chat-input');
const button = document.querySelector('#button');

form.addEventListener('submit', function(event) {
  event.preventDefault(); // prevent default form submission behavior

  // Call function to handle form submission
  handleFormSubmit();
});

// Add click event listener to button (optional, to handle button clicks)
button.addEventListener('click', handleFormSubmit);

function handleFormSubmit() {
  // Code to handle form submission goes here
}
