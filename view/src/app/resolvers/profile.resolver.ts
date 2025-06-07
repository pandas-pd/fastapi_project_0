import { ResolveFn } from '@angular/router';
import { ApiUsersService } from '../services/api-users.service';
import { inject } from '@angular/core';

export const profileResolver: ResolveFn<any> = (route, state) => {

    const apiUserService = inject(ApiUsersService);
    const profileKey : number = Number(route.paramMap.get('key'));

    return apiUserService.getUser(profileKey);
};
