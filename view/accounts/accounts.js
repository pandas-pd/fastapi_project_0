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