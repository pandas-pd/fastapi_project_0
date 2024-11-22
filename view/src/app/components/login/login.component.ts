import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { PopupComponent } from '../popup/popup.component';

@Component({
    selector: 'app-login',
    standalone: true,
    imports: [],
    templateUrl: './login.component.html',
    styleUrl: './login.component.css'
})

export class LoginComponent implements OnInit {

    private usernameFiled: HTMLInputElement | null = null;
    private passwordField: HTMLInputElement | null = null;

    constructor(private authService:AuthService, private router:Router){}

    ngOnInit(): void {
        this.usernameFiled = document.getElementById('username') as HTMLInputElement;
        this.passwordField = document.getElementById('password') as HTMLInputElement;
    }


    async login(): Promise<void> {

        //get field contents
        const username: any = this.usernameFiled?.value;
        const password: any = this.passwordField?.value;

        const result : any = await this.authService.login(username, password);
        console.log("this is result:");
        console.log(result);

        //handle login
        if (result.success == false){
        }
        else if (result.success == true){
            this.router.navigate(['/'])
        }

        return;

    }

}
