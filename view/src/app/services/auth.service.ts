import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { environment } from '../../environments/environment';
//import { getCookie } from '../utils/cookie';



@Injectable({
    providedIn: 'root'
})

export class AuthService {


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
        console.log(username, password);
        
    }
}
