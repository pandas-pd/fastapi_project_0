import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class EnumParserService {


    constructor() {}


    roleParser (userRoles : Array<object>, enumRoles : any) : Array<object> {

        const mapper = (userRole:any) => {
            return {
                ...userRole,
                role : enumRoles[userRole.role]
            };
        };
        const parsedRoles : Array<object> = userRoles.map(mapper);
        return parsedRoles;
    }

}
