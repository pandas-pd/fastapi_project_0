import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { DOCUMENT } from '@angular/common';
import { Inject } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class CookieService {

    constructor(@Inject(DOCUMENT) private document:Document) {}

    isLoggedIn():boolean{

        const cookies = this.document.cookie.split(';');

        for (let cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            console.log('cookie: ', name, value);
        }

        return false;
    }

}
