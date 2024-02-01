import {API} from "../apiServices.js";

export class LoginView {

    static async login(){

        //get items
        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;

        console.log("this is bullshit");

        //get response
        const response = await API.login(username, password);

        if (response.status == 200){
            window.location.href = "../index.html";

        } else if (response.status == 401){
            return;
        } else {
            return;
        }
    }
}