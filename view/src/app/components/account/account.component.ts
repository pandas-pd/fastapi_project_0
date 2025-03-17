import { Component } from '@angular/core';
import { ApiUsersService } from '../../services/api-users.service';

@Component({
    selector: 'app-account',
    standalone: true,
    imports: [],
    templateUrl: './account.component.html',
    styleUrl: './account.component.css'
})

export class AccountComponent {

    constructor(private apiUserService:ApiUsersService){}

}
