// Get an HTML element in JavaScript code
const signup = document.querySelector(".signup");
const signupModal = document.querySelector(".signup-modal-wrapper");
const closeButton = document.querySelector(".close-modal");

// function which shows the modal by changing the style of signupModal to "block"
const showModal = () => {
  signupModal.style.display = "block";
};

// function which hides the modal by changing the style of signupModal to "none"
const closeModal = () => {
  signupModal.style.display = "none";
};

// Call the showModal function when signup button is clicked
signup.addEventListener("click", () => {
  showModal();
});

// Call the closeModal function when close button on the modal is clicked
closeButton.addEventListener("click", () => {
  closeModal();
});

// Call the closeModal function when anywhere outside of the modal is clicked
window.addEventListener("click", () => {
  if (event.target === modal) {
    closeModal();
  }
});


var color = ["#222f3e" , "#f368e0" , "#ee5253" , "#0abde3" , "#222f3e" , "#5f27cd"];
var i = 0;
document.querySelector("button").addEventListener("click" , 
  function(){
  i = i < color.length ? ++i : 0;
document.querySelector("body").style.background = color[i]
})
