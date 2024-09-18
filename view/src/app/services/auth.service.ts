import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
//import { getCookie } from '../utils/cookie';



@Injectable({
    providedIn: 'root'
})

export class AuthService {

    //class variabel
    private cookieName : string     = 'fastapi_project0_token';
    private endpoint : string       = "http://127.0.0.1:8080";
    private cookiePath : string     = "";

    private header : object = {
        "Content-Type": "application/json",
        "Cache-Control": "max-age=7200", // Cache for 1 hour;
    };


    constructor() {}

    //funcitonality

        /*
    isLoggedIn(): Observable<boolean> {

        const cookieValues : any = getCookie(this.cookieName);
        return of(cookieValues !== null);
    }
        */

    async login(username:string, password:string){
        console.log("hello from auth services");
    }
}
