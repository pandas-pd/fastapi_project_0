import { Injectable, signal } from '@angular/core';
import { Observable, of } from 'rxjs';
import { environment } from '../../environments/environment';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class ApiAuthService {


    constructor(private api: ApiService) {} //inject the http client


    async login(username:string, password:string) : Promise<object> {

        const result : object =  await this.api.request(
            'post',
            '/login',
            {'username': username, 'password': password},
        );

        return result;
    }
}
