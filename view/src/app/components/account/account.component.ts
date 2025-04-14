import { Component, inject, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ApiUsersService } from '../../services/api-users.service';

@Component({
    selector: 'app-account',
    standalone: true,
    imports: [CommonModule],
    templateUrl: './account.component.html',
    styleUrl: './account.component.css'
})

export class AccountComponent implements OnInit{

    accountData: any;
    roleData: any;
    constructor(private route: ActivatedRoute, private apiUserService: ApiUsersService){}

    async ngOnInit(): Promise<void> {

        //bind resolved data
        this.accountData = this.route.snapshot.data['accountData'];
        console.log(this.accountData);

        //fetch role data
        this.roleData = await this.apiUserService.getRoles(this.accountData.response.key);
        console.log(this.roleData);

    }

}
