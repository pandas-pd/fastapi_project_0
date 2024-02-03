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
        var messageElement = document.getElementById("infoMessage");

        const response =  await User.resetPassword(username);
        console.log(response);

        if (response.status == 200){

        } else if (response.status == 400){
            
        }

    }

}