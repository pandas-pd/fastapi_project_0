import {CreateAccountView, CssProperties, LoginView, ResetPasswordView} from './accounts.js';
var currentPath = window.location.pathname;


if (currentPath == "/view/accounts/login.html"){

    document.getElementById("loginForm").addEventListener("submit", LoginView.login);
}

else if (currentPath == "/view/accounts/resetPassword.html"){

    document.getElementById("passwordResetForm").addEventListener("submit", ResetPasswordView.resetPassword);
}

else if (currentPath == "/view/accounts/createAccount.html"){

    //set css colors
    CssProperties.setFontColor();

    //valiation on key strokes
    document.getElementById("username").addEventListener("keydown", CreateAccountView.validateUseranme);
    document.getElementById("email").addEventListener("keydown", CreateAccountView.validateEmail);
    document.getElementById("emailConfirm").addEventListener("keydown", CreateAccountView.validateEmailConfirm);

    //form submit
    document.getElementById("email").addEventListener("submit", CreateAccountView.createAccount);

}


