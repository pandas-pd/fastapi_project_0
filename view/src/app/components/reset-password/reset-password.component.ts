import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { ApiUsersService } from '../../services/api-users.service';
import { PopupService } from '../../services/popup.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';


@Component({
    selector: 'app-reset-password',
    standalone: true,
    imports: [FormsModule],
    templateUrl: './reset-password.component.html',
    styleUrl: './reset-password.component.css'
})


export class ResetPasswordComponent{

    username! : string;

    constructor(
        private apiUserService:ApiUsersService,
        private popupService:PopupService,
        private router:Router,
    ){}


    async resetPassword(): Promise<void> {

        //validate and run transaction
        const result : any = await this.apiUserService.resetPassword(this.username);

        //feedback
        if (result.success){
            this.popupService.show('Password reset successfull. Please check your e-mail.', result['success'], null);
            this.router.navigate(['/login'])
        }
        else if (!result.success){
            this.popupService.show('Password reset not successfull. The username is either invalid or does not exists.', result['success'], null);
        }
        else{
            this.popupService.show('Someting went wrong', false, null);
        }
        return;
    }
}
