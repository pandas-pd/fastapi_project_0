import {User} from "./apiServices.js";

var currentPath = window.location.pathname;

export class NavBar{

    static async renderUserDropDown(){
        //open user pop up when user is clicked
        console.log("clicked user icon, yey");
        return;
    }

    static async renderUserIcon(){

        var userIcon = document.getElementById("userIcon");
        var loginLink = document.getElementById("loginNavBar");

        //access local storage to retrieve info
        var userData = JSON.parse(sessionStorage.getItem('userData'));

        //hide icon when no data is found
        if (userData == null){
            userIcon.style.display = "none";
            loginLink.style.display = "block";
            return;
        }

        //add eventlistener to render data when clicked
        userIcon.addEventListener("click", NavBar.renderUserDropDown);

        //hide Login when already logged in
        userIcon.style.display = "block";
        loginLink.style.display = "none";

        return;
    }

    static async renderUsersTab(){

        var usersTab = document.getElementById("usersNavBar");
        var userData = JSON.parse(sessionStorage.getItem("userData"));

        if (userData == null){
            usersTab.style.display = "none";

        } else if (userData.roleKeys.includes(0) == false){
            usersTab.style.display = "none";

        } else {
            usersTab.style.display = "block";

        }
    }
}

//add triggers to render nav bar element
//user icon --> only render when logged in (check local storage)
if (
    currentPath == "/view/index.html" ||
    currentPath == "/view/skills/skills.html" ||
    currentPath == "/view/projects/projects.html" ||
    currentPath == "/view/users/users.html"
){
    await NavBar.renderUserIcon();
    await NavBar.renderUsersTab();
}

