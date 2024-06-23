// function togglePasswordVisibility() {
//     const passwordInput = document.getElementById("password");
//     if (passwordInput.type === "password") {
//       passwordInput.type = "text";
//     } else {
//       passwordInput.type = "password";
//     }
//   }

const togglePassword = document.getElementById('togglePassword');
const password = document.getElementById('password');

togglePassword.addEventListener('click', function () {
  if (password.type === 'password') {
    password.type = 'text';
    togglePassword.classList.remove('fa-eye-slash');
    togglePassword.classList.add('fa-eye'); // Change class for open eye icon
  } else {
    password.type = 'password';
    togglePassword.classList.remove('fa-eye');
    togglePassword.classList.add('fa-eye-slash');
  }
});
