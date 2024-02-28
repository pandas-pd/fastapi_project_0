import {User, Enum} from "../apiServices.js";

export class LoginView {

    static async login(){

        //get items
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        var messageElement = document.getElementById("login-message");

        //get response
        const response = await User.login(username, password);

        if (response.status == 200){
            await LoginView.storeUserDate();
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

    static async storeUserDate(){ //stores the user data form the logged in user to local storage to render to user button in header

        //get user infromation and set object format
        const responseUser = await User.getUser();
        const responseEnum = await Enum.userRoles();

        //parse user data
        const username      = responseUser.data.username;
        const email         = responseUser.data.e_mail;
        var userRoles       = [];
        var userRoleKeys    = [];

        //parse role data

        for (var i = 0; i < responseUser.data.roles.length; i++){

            let roleKey = responseUser.data.roles[i].role;
            const role = responseEnum.data[roleKey];
            userRoles.push(role);
            userRoleKeys.push(roleKey);
        }

        var userData = {
            "username" : username,
            "email" : email,
            "roles" : userRoles,
            "roleKeys" : userRoleKeys,
        };

        //save to local storage
        sessionStorage.setItem("userData", JSON.stringify(userData));
        console.log("successfully cached username");
        return;

        // Retrieve object from local storage
        //var retrievedObj = JSON.parse(localStorage.getItem('user'));
        //console.log(retrievedObj); // { name: 'John', age: 30 }

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

    static async setMessage(message, color){

        //retrieve element
        var messageElement = document.getElementById("message");

        //set properties and message
        messageElement.textContent = message;
        messageElement.style.color = color;
        messageElement.style.display = 'block';
    }

    static async resetMessage(){

        //retrieve element
        var messageElement = document.getElementById("message");

        //set elemt
        messageElement.style.display = 'none';
    }

    static async validateUseranme(){

        //reset to default
        CreateAccountView.resetMessage();

        //wait for ui to finish processing
        await new Promise(r => setTimeout(r, 1));

        //get item
        const username = document.getElementById("username").value;
        var usernameLabel = document.getElementById("usernameLabel");

        //handle empty input
        if (username.length == 0){
            usernameLabel.style.color = CssProperties.fontColors.fontColorDefault;
            return false;
        }

        //verify username
        const response = await User.validateUsername(username);

        //handle response
        if (response.status == 200){
            usernameLabel.style.color = CssProperties.fontColors.fontColorSuccess;
            return true;

        } else if (response.status == 400){
            usernameLabel.style.color = CssProperties.fontColors.fontColorFailure;
            CreateAccountView.setMessage("Username already exists or is invalid", CssProperties.fontColors.fontColorFailure);
            return false;

        }
    }

    static async validateEmail(){
        //has some flaws but works good enough

        //reset to default
        await new Promise(r => setTimeout(r, 1));

        //fetch elements
        const email = document.getElementById("email").value;
        var emailLabel = document.getElementById("emailLabel");

        //handle empty input
        if (email.length == 0){
            emailLabel.style.color = CssProperties.fontColors.fontColorDefault;
            return false;
        }

        //@ verification
        let atIndex = email.indexOf("@");
        let providerSuffix = email.slice(atIndex);

        if (atIndex == -1){
            emailLabel.style.color = CssProperties.fontColors.fontColorFailure;
            return false;
        }

        //dot verification
        let dotIndex = providerSuffix.indexOf(".");
        let invertedDotIndex = dotIndex - (providerSuffix.length);

        if (dotIndex == -1 || invertedDotIndex > -3){
            emailLabel.style.color = CssProperties.fontColors.fontColorFailure;
            return false;

        } else {
            emailLabel.style.color = CssProperties.fontColors.fontColorSuccess;
            return true;
        }
    }

    static async validateEmailConfirm(){

        //await last input to load
        await new Promise(r => setTimeout(r, 1));

        //get items
        const email = document.getElementById("email").value;
        const emailConfirm = document.getElementById("emailConfirm").value;
        var emailConfirmLabel = document.getElementById("emailConfirmLabel");

        if (emailConfirm.length == 0){
            emailConfirmLabel.style.color = CssProperties.fontColors.fontColorDefault;
            return false;

        } else if (email != emailConfirm){
             emailConfirmLabel.style.color = CssProperties.fontColors.fontColorFailure;
             return false;

        } else if (email == emailConfirm) {
            emailConfirmLabel.style.color = CssProperties.fontColors.fontColorSuccess;
            return true;
        }
    }

    static async validatePassword(){

        //await last input to load
        CreateAccountView.resetMessage()
        await new Promise(r => setTimeout(r, 1));

        //get elemts
        const password = document.getElementById("password").value;
        var passwordLabel = document.getElementById("passwordLabel");
        const dumbPasswords = ["password", "1234"];

        if (password.length == 0){
            passwordLabel.style.color = CssProperties.fontColors.fontColorDefault;
            return false;

        } else if (dumbPasswords.includes(password)){
            passwordLabel.style.color = CssProperties.fontColors.fontColorFailure;
            CreateAccountView.setMessage("Really, that is your password?", CssProperties.fontColors.fontColorFailure);
            return false;

        } else if (password.length < 6){
            passwordLabel.style.color = CssProperties.fontColors.fontColorFailure;
            CreateAccountView.setMessage("Password must be at least 6 characters long", CssProperties.fontColors.fontColorFailure);
            return false;

        } else {
            passwordLabel.style.color = CssProperties.fontColors.fontColorSuccess;
            return true;
        }
    }

    static async createAccount(){

        //reset to default
        CreateAccountView.resetMessage();

        //get items
        const username          = document.getElementById("username").value;
        const email             = document.getElementById("email").value;
        const password          = document.getElementById("password").value;

        //check frontend validations
        if (    await CreateAccountView.validateUseranme() == false ||
                await CreateAccountView.validateEmail() == false ||
                await CreateAccountView.validateEmailConfirm() == false ||
                await CreateAccountView.validatePassword() == false
        ){
            CreateAccountView.setMessage("Validation failed. Check input fields.", CssProperties.fontColors.fontColorFailure);
            return;
        }

        //debug
        console.log("all checks passed");
        const response = await User.createAccount(username, email, password);

        //debug
        console.log(response, response.data);

        if (response.status == 200){
            CreateAccountView.setMessage("Account created. Redirecting to login page.", CssProperties.fontColors.fontColorSuccess);
            //await new Promise(r => setTimeout(r, 2000));
            window.location.href = "./login.html";

        } else if (response.status == 400){
            CreateAccountView.setMessage(response.data.message, CssProperties.fontColors.fontColorFailure);

        } else {
            CreateAccountView.setMessage("Something went wrong", CssProperties.fontColors.fontColorFailure);
        }
        //return;
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