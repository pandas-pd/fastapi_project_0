export class API{

    static endpoint = "http://127.0.0.1:8080";
    static cookiePath = "";
    static header = {
        "Content-Type": "application/json",
        "Cache-Control": "max-age=3600", // Cache for 1 hour;
    }

    static async callEndpoint(method, call, body){

        //handle timeouts
        const controller = new AbortController();
        const signal = controller.signal;

        //prep data for a clean call
        const url = API.endpoint + call;
        const strBody = JSON.stringify(body);

        //call api and catch errors
        try{
            const response = await fetch(url,{
                method: method, //POST, GET, UPDATE, DELETE
                headers: API.header,
                body : strBody,
                signal: signal, // Pass the AbortSignal to the fetch options
                credentials : "include", //includes cookies if existing
            })

            const data = await response.json();
            return {"status" : response.status, "data" : data};

        }catch(error){
            console.log(error);
            return {"status" : "error", "data" : ""};
        }
    }
}

export class User{

    static async login(username, password){

        const response = await API.callEndpoint(
            "POST",
            "/login",
            {"username" : username, "password" : password},
        );
        return response;
    }

    static async resetPassword(username){

        const response = await API.callEndpoint(
            "POST",
            "/users/reset_password",
            {"username" : username},
        );
        return response;
    }

    static async validateUsername(username){

        const response = await API.callEndpoint(
            "POST",
            "/users/validate_username",
            {"username": username},
        );
        return response;
    }

}