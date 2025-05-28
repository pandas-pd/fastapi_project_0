import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

@Injectable({
    providedIn: 'root'
})
export class ApiEnumService {

    constructor(private api:ApiService) { } //injecting the service


    async getSkillLevels () : Promise<object> {

        const result : object = await this.api.request(
            'get',
            '/enum/skill_levels',
            null
        );

        return result;
    }


    async getProjectStatus () : Promise<object> {

        const result = this.api.request(
            'get',
            '/enum/project_status',
            null
        );

        return result;
    }


    async getUserRoles () : Promise<object> {

        const result = this.api.request(
            'get',
            '/enum/user_roles',
            null
        )

        return result;
    }
}
