import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { ApiUsersService } from '../../services/api-users.service';
import { SpinnerService } from '../../services/spinner.service';
import { PopupService } from '../../services/popup.service';
import { Router } from '@angular/router';

@Component({
    selector: 'app-reset-password',
    standalone: true,
    imports: [],
    templateUrl: './reset-password.component.html',
    styleUrl: './reset-password.component.css'
})
export class ResetPasswordComponent implements OnInit{

    private usernameField: HTMLInputElement | null = null;


    constructor(
        private apiUserService:ApiUsersService,
        private popupService:PopupService,
        private spinnerService:SpinnerService,
        private router:Router,
    ){}


    ngOnInit(): void {
        this.usernameField = document.getElementById('username') as HTMLInputElement;
    }


    async resetPassword(): Promise<void> {

        //get field values
        const username: any = this.usernameField?.value;

        //validate and run transaction
        this.spinnerService.show()
        const result : any = await this.apiUserService.resetPassword(username);
        this.spinnerService.hide()


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
