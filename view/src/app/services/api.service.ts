import { Injectable, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { firstValueFrom, Observable, of } from 'rxjs';
import { environment } from '../../environments/environment';


@Injectable({
    providedIn: 'root'
})


export class ApiService {

    private header : any = {
        'Content-Type': 'application/json',
        'Cache-Control': 'max-age=7200', // Cache for 1 hour;
    };


    constructor(private http:HttpClient) {}

    private sendRequest(method:string, endpoint:string,body:object | null, includeCredentials?:boolean): Observable<any>{

        const url = environment.apiUrl.concat(endpoint);

        switch(method){

            case 'get':
                return this.http.get(url, {withCredentials: includeCredentials, headers:this.header});
                break;

            case 'post':
                return this.http.post(url, body, {withCredentials: includeCredentials, headers:this.header});
                break;

            case 'put':
                return this.http.put(url, body, {withCredentials: includeCredentials, headers:this.header});
                break;

            case 'patch':
                return this.http.patch(url, body, {withCredentials: includeCredentials, headers:this.header});
                break;

            case 'delete':
                return this.http.delete(url, {withCredentials: includeCredentials, headers:this.header});
                break;

            default:
                throw new Error(`Unsupported HTTP method: ${method}`);
        }
    }


    /**
     * Sends a rest api request to the defined backend, based on the currnet build env
     * 
     * @param method ['get', 'post', 'put', 'patch', 'delete']
     * @param endpoint /endpoint
     * @param body /{'param' : 'value', ...}
     * @param includeCredentials 
     * @retruns {'success' : success, 'status' : httpStatusCode, 'response' : response}
     */
    async request(method:string, endpoint:string, body:object | null, includeCredentials:boolean = true): Promise<object>{

        let result: Record<string, any> = {
            success : null,
            response : null
        };

        try {
            const response = await firstValueFrom(
                this.sendRequest(method,endpoint,body,includeCredentials)
            );
            result['success']   = true;
            result['response']  = response;

        } catch (error) {

            result['success']   = false;
            console.log('error while contacting backend: ', error);
        }

        return result;
    }
}