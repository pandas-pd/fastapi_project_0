import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { OnInit } from '@angular/core';

@Component({
    selector: 'app-login',
    standalone: true,
    imports: [],
    templateUrl: './login.component.html',
    styleUrl: './login.component.css'
})

export class LoginComponent implements OnInit {

    private usernameFiled: HTMLElement | undefined | null;
    private passwordField: HTMLElement | undefined | null;

    constructor(private authService:AuthService) {
    }

    ngOnInit(): void {
        this.usernameFiled = document.getElementById('username');
        this.passwordField = document.getElementById('password');
    }

    async login() {

        //get field contents
        const username: any = this.usernameFiled?.textContent;
        const password: any = this.passwordField?.textContent;

        var response = await this.authService.login(username, password);
    }

}
