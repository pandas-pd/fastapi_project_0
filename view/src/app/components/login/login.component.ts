import { Component } from '@angular/core';
import { ApiAuthService } from '../../services/api-auth.service';
import { Router, RouterLink, RouterLinkActive } from '@angular/router';
import { PopupService } from '../../services/popup.service';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-login',
    standalone: true,
    imports: [
        RouterLink,
        RouterLinkActive,
        FormsModule
    ],
    templateUrl: './login.component.html',
    styleUrl: './login.component.css'
})

export class LoginComponent {

    username!: string;
    password!: string;

    constructor(
        private apiAuthService:ApiAuthService,
        private popupService:PopupService,
        private router:Router
    ){}


    async login(): Promise<void> {

        //get field contents
        console.log(this.username, this.password);
        const result : any = await this.apiAuthService.login(this.username, this.password);

        //handle login
        if (!result.success && result["message"] == null){
            this.popupService.show("Login failed", false, null);
        }
        else if (result.success){
            this.popupService.show("Login successful", true, null);
            this.router.navigate(['/'])
        }
        return;
    }

}
