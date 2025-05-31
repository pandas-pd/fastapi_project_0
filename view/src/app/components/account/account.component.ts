import { Component, inject, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink, Router, RouterLinkActive} from '@angular/router';
import { CommonModule } from '@angular/common';
import { ApiUsersService } from '../../services/api-users.service';
import { EnumParserService } from '../../services/enum-parser.service';

@Component({
    selector: 'app-account',
    standalone: true,
    imports: [
        CommonModule,
        RouterLink,
        RouterLinkActive,
    ],
    templateUrl: './account.component.html',
    styleUrl: './account.component.css'
})

export class AccountComponent implements OnInit{

    accountData: object | any;
    roleData: Array<object> | any;

    constructor(
        private route: ActivatedRoute,
        private apiUserService: ApiUsersService,
        private enumParser: EnumParserService
    ){}

    async ngOnInit(): Promise<void> {

        //bind resolved data
        this.accountData            = this.route.snapshot.data['accountData']['user']['response'];
        const roleEnum : object     = this.route.snapshot.data['accountData']['roles']['response'];

        //parse role data
        this.roleData               = this.enumParser.roleParser(this.accountData.roles, roleEnum);
        return;
    }

}
