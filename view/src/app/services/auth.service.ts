import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { getCookie } from '../utils/cookie';



@Injectable({
    providedIn: 'root'
})

export class AuthService {

    //class variabel
    private cookieName : string = 'fastapi_project0_token';

    constructor(private http: HttpClient) {}

    //funcitonality

    isLoggedIn(): Observable<boolean> {

        const cookieValues : any = getCookie(this.cookieName);
        return of(cookieValues !== null);
    }
}
