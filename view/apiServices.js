class API{

    static endpoint = "";
    static cookiePath = "";
    static header = {'Content-Type': 'application/json'}

    constructor(method, call, body){
        this.method = method;
        this.url = API.endpoint + call;
        this.body = body;
    }

    callPublic(){

        try{

            const response = await fetch( this.url,{
                method: this.method,
                headers: API.header,
                body : JSON.stringify(this.body)
            });

            if (response.ok) {
                const data = await response.json();
            }
        }
    };

    callPrivat(call, method, body){
        //some
    }

}

class Authentication{

    static login(){

        //get items
        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;

        //create call instance
        const api = new API(
            method = "POST",
            call = "/login",
            body = {"username" : username, "password" : password},
        )

        await api.callPublic();

        //redirect to home

        return null;

    }
}

