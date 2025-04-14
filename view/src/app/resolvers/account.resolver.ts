import { ResolveFn } from '@angular/router';
import { inject } from '@angular/core';
import { ApiUsersService } from '../services/api-users.service';

export const accountResolver: ResolveFn<any> = () => {

    const apiUserService = inject(ApiUsersService);
    //console.log(apiUserService.getUser());
    return apiUserService.getUser();

};
