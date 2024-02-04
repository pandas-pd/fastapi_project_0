import {LoginView, ResetPasswordView} from './accounts.js';
var currentPath = window.location.pathname;

if (currentPath == "/view/accounts/login.html"){

    document.getElementById("loginForm").addEventListener("submit", LoginView.login);
}


if (currentPath == "/view/accounts/resetPassword.html"){

    document.getElementById("PasswordResetForm").addEventListener("submit", ResetPasswordView.resetPassword);
}