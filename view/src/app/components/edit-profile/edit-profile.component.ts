import { Component } from '@angular/core';
import { Router, RouterLink, ActivatedRoute } from '@angular/router';
import { ApiUsersService } from '../../services/api-users.service';
import { OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-edit-profile',
    standalone: true,
    imports: [
        FormsModule
    ],
    templateUrl: './edit-profile.component.html',
    styleUrl: './edit-profile.component.css'
})
export class EditProfileComponent implements OnInit{

    profileData: object | any;

    constructor(
        private route: ActivatedRoute,
    ){}

    ngOnInit(): void {
        this.profileData = this.route.snapshot.data['profileData']['response'];
        console.log(this.profileData);
    }

    async updateProfile (): Promise<void>{
        console.log(this.profileData.username);
    }

}
