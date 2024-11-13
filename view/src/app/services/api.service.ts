import { Injectable, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { environment } from '../../environments/environment';


@Injectable({
    providedIn: 'root'
})


export class ApiService {

    private header : object = {
        'Content-Type': 'application/json',
        'Cache-Control': 'max-age=7200', // Cache for 1 hour;
    };


    constructor(private http:HttpClient) {}

    private sendRequest(method:string, endpoint:string,body?:object, includeCredentials?:boolean): Observable<any>{

        let httpMethod: any;

        switch(method){

            case 'get':
                httpMethod = this.http.get;
                break;

            case 'post':
                httpMethod = this.http.post;
                break;

            case 'put':
                httpMethod = this.http.put;
                break;

            case 'patch':
                httpMethod = this.http.patch;
                break;

            case 'delete':
                httpMethod = this.http.delete;
                break;
        }

        const url = environment.apiUrl.concat(endpoint);

        const response = httpMethod(
            url,
            body,
            
        )
    }


    /**
     * Sends a rest api request to the defined backend, based on the currnet build env
     * 
     * @param method ['get', 'post', 'put', 'patch', 'delete']
     * @param endpoint /endpoint
     * @param body /{'param' : 'value', ...}
     * @param includeCredentials 
     * @retruns {'status': httpStatus, 'response' : responseObject}
     */
    request(method:string, endpoint:string,body?:object, includeCredentials:boolean = true): object{



        const url = environment.apiUrl.concat('/login');

    }


}
