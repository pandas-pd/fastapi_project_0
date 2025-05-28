import { ResolveFn } from '@angular/router';
import { inject } from '@angular/core';
import { forkJoin } from 'rxjs';
import { ApiUsersService } from '../services/api-users.service';
import { ApiEnumService } from '../services/api-enum.service';

export const accountResolver: ResolveFn<any> = () => {

    const apiUserService = inject(ApiUsersService);
    const apiEnumService = inject(ApiEnumService);

    return forkJoin({
        user: apiUserService.getUser(),
        roles: apiEnumService.getUserRoles()
    })
};
