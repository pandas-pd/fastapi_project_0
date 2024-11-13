import { Injectable, signal } from '@angular/core';
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


    constructor(private http: HttpClient) {} //inject the http client


    loginCall(username:string, password:string): Observable<any>{

        let url = environment.apiUrl.concat("/login");
        const header = {
            "Content-Type": "application/json",
            "Cache-Control": "max-age=7200", // Cache for 1 hour;
        }

        const body = {
            "username": username,
            "password": password,
          };

        const result = this.http.post(url, body, {withCredentials: true, headers:header});
        return result;
    }

    login(username:string, password:string): any{

        //call api
        this.loginCall(username, password).subscribe({
            next: (response) => {
                console.log(response);
            },
            error: (error) => {
                console.log(error);
            }
        })
    }
}
