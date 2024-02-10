import {User} from "../apiServices.js";

export class LoginView {

    static async login(){

        //get items
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        var messageElement = document.getElementById('login-message');

        //get response
        const response = await User.login(username, password);

        if (response.status == 200){
            window.location.href = "../index.html";
            messageElement.style.display = 'none';

        } else if (response.status == 401){
            messageElement.textContent = response.data.message;
            messageElement.style.display = 'block';

        } else {
            messageElement.textContent = "Something went wrong. Error " + response.data.status;
            messageElement.style.display = 'block';
        }
    }
}

export class ResetPasswordView {

    static async resetPassword(){

        //get item
        const username = document.getElementById("username").value;
        var successElement = document.getElementById("successMessage");
        var errorElement = document.getElementById("errorMessage");

        const response = await User.resetPassword(username);
        console.log(response);

        //reset boxes
        successElement.style.display = 'none';
        errorElement.style.display = 'none';

        if (response.status == 200 || response.status == "error"){ //strange fucking bug, when requesting a reset over fetch, fastAPI backend does not reply. (Swagger works)
            successElement.textContent = "Reset successfull."; // https://stackoverflow.com/questions/67451129/express-and-fetch-typeerror-networkerror-when-attempting-to-fetch-resource
            successElement.style.display = 'block';
            //await new Promise(r => setTimeout(r, 2000));
            window.location.href = "./login.html";

        } else if (response.status == 400){
            errorElement.textContent = response.data.message;
            errorElement.style.display = 'block';

        } else {
            errorElement.textContent = "Something went wrong. Error " + response.data.status;
            errorElement.style.display = 'block';
        }
    }
}

export class CreateAccountView {

    static async setErrorMessage(message){

        //retrieve element
        var errorElement = document.getElementById("errorMessage");

        //set properties and message
        errorElement.textContent = message;
        errorElement.style.display = 'block';
    }

    static async resetErrorMessage(){

        //retrieve element
        var errorElement = document.getElementById("errorMessage");

        //set elemt
        errorElement.style.display = 'none';
    }

    static async validateUseranme(){

        //reset to default
        CreateAccountView.resetErrorMessage();

        //wait for ui to finish processing
        await new Promise(r => setTimeout(r, 1));

        //get item
        const username = document.getElementById("username").value;
        var usernameLabel = document.getElementById("usernameLabel");

        //handle empty input
        if (username.length == 0){
            usernameLabel.style.color = CssProperties.fontColors.fontColorDefault;
            return;
        }

        //verify username
        const response = await User.validateUsername(username);

        //handle response
        if (response.status == 200){
            usernameLabel.style.color = CssProperties.fontColors.fontColorSuccess;
        } else if (response.status == 400){
            usernameLabel.style.color = CssProperties.fontColors.fontColorFailure;
            CreateAccountView.setErrorMessage("Username already exists or is invalid");
        }
    }

    static async validateEmail(){
        console.log("email trigger");
    }

    static async validateEmailConfirm(){
        console.log("emailConfirm trigger");
    }

    static async createAccount(){

        //get items
        const username          = document.getElementById("username").value;
        const email             = document.getElementById("email").value;
        const emailConfirm      = document.getElementById("emailConfirm").value;
        const password          = document.getElementById("password").value;

        //stuff
    }
}

export class CssProperties{

    static fontColors = undefined;

    static async setFontColor(){

        // Get the computed style of the hidden div
        const rootStyles = getComputedStyle(document.documentElement);

        // Retrieve the values of CSS variables
        const fontColorDefault = rootStyles.getPropertyValue("--font-color-1");
        const fontColorSuccess = rootStyles.getPropertyValue("--success-color");
        const fontColorFailure = rootStyles.getPropertyValue("--failure-color");

        CssProperties.fontColors = {"fontColorDefault" : fontColorDefault, "fontColorSuccess" : fontColorSuccess, "fontColorFailure" : fontColorFailure};
        return;
    }

}