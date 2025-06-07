import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { ApiUsersService } from '../../services/api-users.service';
import { Router, RouterLink, RouterLinkActive } from '@angular/router';
import { PopupService } from '../../services/popup.service';
import { Location } from '@angular/common';

@Component({
    selector: 'app-change-password',
    standalone: true,
    imports: [
        RouterLink,
        RouterLinkActive,
    ],
    templateUrl: './change-password.component.html',
    styleUrl: './change-password.component.css'
})

export class ChangePasswordComponent implements OnInit{

    private passwordCurrentField:HTMLElement | any;
    private passwordNewField:HTMLElement | any;
    private passwordRepeatField:HTMLElement | any;


    constructor(
        private apiUserService:ApiUsersService,
        private popupService:PopupService,
        private router:Router,
        private location:Location,
    ){}


    ngOnInit(): void {
        this.passwordCurrentField       = document.getElementById('current-password') as HTMLInputElement;
        this.passwordNewField           = document.getElementById('new-password') as HTMLInputElement;
        this.passwordRepeatField        = document.getElementById('repeat-password') as HTMLInputElement;
    }


    private validatePasswordMatch(password:string, passwordRepeat:string): boolean {

        if (password != passwordRepeat){
            this.popupService.show("Passwords do not match", false, null);
            return false
        }
        return true;
    }

    async changePassword(): Promise<void> {

        //get field contents
        const passwordCurrent: any          = this.passwordCurrentField?.value;
        const passwordNew: any              = this.passwordNewField?.value;
        const passwordRepeat: any           = this.passwordRepeatField?.value;

        //validations
        if (this.validatePasswordMatch(passwordNew, passwordRepeat) === false){
            return;
        };

        //ws calls
        const userData: any = await this.apiUserService.getOwnUser();
        const result: any = await this.apiUserService.updatePassword(userData.response.key, passwordCurrent, passwordNew, 'password change over GUI');

        //handle response
        if (!result.success && result["message"] == null){
            this.popupService.show("Password change failed", false, null);
        }
        else if (result.success){
            this.popupService.show("New password set", true, null);
            this.back();
        }
        return;

        return;
    }


    back(): void {
        this.location.back();
    }
}
