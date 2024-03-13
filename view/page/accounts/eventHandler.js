import {CreateAccountView, CssProperties, LoginView, ResetPasswordView} from './accounts.js';
var currentPath = window.location.pathname;
console.log(currentPath);

if (currentPath == "/page/accounts/login.html"){

    document.getElementById("loginForm").addEventListener("submit", LoginView.login);
}

else if (currentPath == "/page/accounts/resetPassword.html"){

    document.getElementById("passwordResetForm").addEventListener("submit", ResetPasswordView.resetPassword);
}

else if (currentPath == "/page/accounts/createAccount.html"){

    //set css colors
    CssProperties.setFontColor();

    //valiation on key strokes
    document.getElementById("username").addEventListener("keydown", CreateAccountView.validateUseranme);
    document.getElementById("email").addEventListener("keydown", CreateAccountView.validateEmail);
    document.getElementById("emailConfirm").addEventListener("keydown", CreateAccountView.validateEmailConfirm);
    document.getElementById("password").addEventListener("keydown", CreateAccountView.validatePassword);

    //form submit
    document.getElementById("createAccountForm").addEventListener("submit", CreateAccountView.createAccount);

}
