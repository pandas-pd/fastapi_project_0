import { CanMatchFn } from '@angular/router';
import { CookieService } from '../services/cookie.service';
import { inject } from '@angular/core';

export const authGuard: CanMatchFn = (route, segments) => {
    const cookieService = inject(CookieService);

    if (cookieService.isLoggedIn()){
        return true;
    } else {
        return false;
    }
};
