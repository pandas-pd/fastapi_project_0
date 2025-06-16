import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { ApiUsersService } from '../../services/api-users.service';
import { Router, RouterLink, RouterLinkActive } from '@angular/router';
import { PopupService } from '../../services/popup.service';
import { Location } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-change-password',
    standalone: true,
    imports: [
        RouterLink,
        RouterLinkActive,
        FormsModule,
    ],
    templateUrl: './change-password.component.html',
    styleUrl: './change-password.component.css'
})

export class ChangePasswordComponent{

    passwordCurrent!: string;
    passwordNew!: string;
    passwordRepeat! :string;


    constructor(
        private apiUserService:ApiUsersService,
        private popupService:PopupService,
        private router:Router,
        private location:Location,
    ){}


    private validatePasswordMatch(password:string, passwordRepeat:string): boolean {

        if (password != passwordRepeat){
            this.popupService.show('Passwords do not match', false, null);
            return false
        }
        return true;
    }

    async changePassword(): Promise<void> {

        //validations
        if (this.validatePasswordMatch(this.passwordNew, this.passwordRepeat) === false){
            return;
        };

        //ws calls
        const userData: any = await this.apiUserService.getOwnUser();
        const result: any = await this.apiUserService.updatePassword(userData.response.key, this.passwordCurrent, this.passwordNew, 'password change over GUI');

        //handle response
        if (!result.success && result['message'] == null){
            this.popupService.show('Password change failed', false, null);
        }
        else if (result.success){
            this.popupService.show('New password set', true, null);
            this.back();
        }
        return;
    }


    back(): void {
        this.router.navigate(['/account']);
    }
}
