import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { ApiAuthService } from '../../services/api-auth.service';
import { Router, RouterLink, RouterLinkActive } from '@angular/router';
import { PopupService } from '../../services/popup.service';

@Component({
    selector: 'app-login',
    standalone: true,
    imports: [
        RouterLink,
        RouterLinkActive,
    ],
    templateUrl: './login.component.html',
    styleUrl: './login.component.css'
})

export class LoginComponent implements OnInit {

    private usernameFiled: HTMLInputElement | null = null;
    private passwordField: HTMLInputElement | null = null;

    constructor(
        private apiAuthService:ApiAuthService,
        private popupService:PopupService,
        private router:Router
    ){}

    ngOnInit(): void {
        this.usernameFiled = document.getElementById('username') as HTMLInputElement;
        this.passwordField = document.getElementById('password') as HTMLInputElement;
    }


    async login(): Promise<void> {

        //get field contents
        const username: any = this.usernameFiled?.value;
        const password: any = this.passwordField?.value;

        const result : any = await this.apiAuthService.login(username, password);

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
