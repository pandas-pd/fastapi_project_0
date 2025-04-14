import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class ApiUsersService {


    constructor(private api:ApiService) {} // injecting the service


    //users

    async validateUsername(username:string) : Promise<object> {

        const result : object = await this.api.request(
            'post',
            '/users/validate_username',
            {'username': username}
        );

        return result;
    }


    async addUser(username:string, eMail:string, password:string, comment:string | null) : Promise<object> {

        const result : object = await this.api.request(
            'post',
            '/users/user',
            {'username': username, 'e_mail': eMail, 'password': password, 'comment': comment,}
        );

        return result;
    }


    async getUser() : Promise<object> {

        const result : object = await this.api.request(
            'get',
            '/users/user',
            null
        );

        return result;
    }


    async getAllUsers() : Promise<object> {

        const result : object = await this.api.request(
            'get',
            '/users/all_users',
            null
        );
        return result;
    }


    async updateUser(keyUser:number, username:string, eMail:string, comment:string | null) : Promise<object> {

        const result : object = await this.api.request(
            'put',
            '/users/user',
            {'key': keyUser, 'username': username, 'e_mail': eMail, 'comment': comment}
        );

        return result;
    }


    async deleteUser(keyUser:number) : Promise<object> {

        const result : object = await this.api.request(
            'delete',
            `/users/user?key=${keyUser}`,
            null
        );
        return result;
    }


    //role

    async addRole(keyUser:number, keyRole:number, comment:string | null) : Promise<object> {

        const result : object = await this.api.request(
            'post',
            '/users/role',
            {'key_user': keyUser, 'key_role': keyRole, 'comment': comment}
        );
        return result;
    }


    async deletRole(keyRole:number) : Promise<object> {

        const result : object = await this.api.request(
            'delete',
            `/users/role?key=${keyRole}`,
            null
        );
        return result;
    }


    async getRoles(keyUser:number) : Promise<object> {

        const result : object = await this.api.request(
            'get',
            `/users/roles?key_user=${keyUser}`,
            null
        );
        return result;
    }


    //password


    async updatePassword(keyUser:number, passwordOld:string, passwordNew:string, comment:string | null) : Promise<object> {

        const result : object = await this.api.request(
            'put',
            '/users/password',
            {'key_user': keyUser, 'password_old': passwordOld, 'password_new': passwordNew, 'comment': comment}
        );
        return result;
    }


    async resetPassword(username:string) : Promise<object> {

        const result : object = await this.api.request(
            'post',
            '/users/reset_password',
            {'username': username}
        );
        return result;
    }
}
