// Code pour la validation du mot de passe
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');
const passwordErrorMessage = document.getElementById('password-error');
const submitButton = document.getElementById('submit-btn');

function validatePassword() {
  if (passwordInput.value !== confirmPasswordInput.value) {
    passwordErrorMessage.textContent = 'The passwords do not match.';
    submitButton.disabled = true;
  } else {
    passwordErrorMessage.textContent = '';
    submitButton.disabled = false;
  }
}

passwordInput.addEventListener('input', validatePassword);
confirmPasswordInput.addEventListener('input', validatePassword);

// Code pour la validation du numéro de téléphone
const phoneInput = document.getElementById('phone');
const phoneErrorMessage = document.getElementById('phone-error');

function validatePhone() {
  const phonePattern = /^\(\d{3}\)\s\d{3}-\d{4}$/;
  if (!phonePattern.test(phoneInput.value)) {
    phoneErrorMessage.textContent = 'Please enter a valid phone number in the format (123) 456-7890.';
    phoneInput.setCustomValidity('Invalid phone number');
  } else {
    phoneErrorMessage.textContent = '';
    phoneInput.setCustomValidity('');
  }
}

phoneInput.addEventListener('input', validatePhone);
