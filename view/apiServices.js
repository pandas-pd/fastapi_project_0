class API{

    static endpoint = "http://127.0.0.1:8080";
    static cookiePath = "";
    static header = {"Content-Type": "application/json"};

    constructor(method, call, body){
        this.method = method;
        this.call = call; //dubugging
        this.url = API.endpoint + call;
        this.body = JSON.stringify(body);
    }

    async callPublic(){

        try{
            const response = await fetch(this.url,{
                method: this.method,
                headers: API.header,
                body : this.body,
                credentials : "include",
            });

            const data = response.json();
            const status = response.status;

            return {"data" : data, "status" : status};

        } catch (error){
            throw new Error("Unable to contact backend: \n" + error);
        }
    }

    callPrivat(call, method, body){
        //some
    }
}

class ExecptionHandler{
}

class Authentication{

    static async login(){

        //get items
        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;

        //create call instance
        const api = new API(
            "POST",
            "/login",
            {"username" : username, "password" : password},
        );

        //fetch data
        let response = await api.callPublic();
        console.log("REPONSE CODE: " + response.status + response.data);

        //redirect to home
        Enum.skillLevels();

        if (response.status == 200){

        } if (response.status == 401){

        } else {

        }
    }
}

class Enum{

    static async skillLevels(){

        const api = new API(
            "GET",
            "/users/user",
        );

        let response = await api.callPublic();
        console.log("THIS IS RESPONSE: " + response.data);
        return
    }

}

/*
// Function to perform login and save the received cookie
async function loginAndSaveCookie(username, password) {
    try {
        const response = await fetch('http://your-fastapi-backend.com/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const cookies = response.headers.get('Set-Cookie'); // Retrieve the cookie from the response headers
            document.cookie = cookies; // Save the received cookie
            console.log('Login successful!');
        } else {
            console.error('Login failed!');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Function to make a request to a FastAPI endpoint and pass the saved cookie
async function makeRequestWithCookie() {
    try {
        const response = await fetch('http://your-fastapi-backend.com/get_projects', {
            method: 'GET',
            headers: {
                'Cookie': document.cookie // Pass the saved cookie with the request
            }
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Projects:', data);
        } else {
            console.error('Failed to fetch projects:', response.status);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Example usage:
loginAndSaveCookie('your_username', 'your_password')
    .then(() => makeRequestWithCookie());
*/