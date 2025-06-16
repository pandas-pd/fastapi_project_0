import { Component } from '@angular/core';
import { Router, RouterLink, ActivatedRoute, RouterLinkActive } from '@angular/router';
import { ApiUsersService } from '../../services/api-users.service';
import { OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Location } from '@angular/common';
import { PopupService } from '../../services/popup.service';

@Component({
    selector: 'app-edit-profile',
    standalone: true,
    imports: [
        FormsModule,
        RouterLink,
        RouterLinkActive,
    ],
    templateUrl: './edit-profile.component.html',
    styleUrl: './edit-profile.component.css'
})


export class EditProfileComponent implements OnInit{

    profileData: object | any;

    constructor(
        private route:ActivatedRoute,
        private location:Location,
        private apiUserService:ApiUsersService,
        private popupService:PopupService,
        private router:Router,
    ){}

    ngOnInit(): void {
        this.profileData = this.route.snapshot.data['profileData']['response'];
        console.log(this.profileData);
    }

    async updateProfile (): Promise<void>{

        //get data to backend
        const result : any = await this.apiUserService.updateUser(
            this.profileData.key,
            this.profileData.username,
            this.profileData.e_mail,
            this.profileData.comment
        );

        //handle response
        if (!result.success && result["message"] == null){
            this.popupService.show("Something went wrong while saving", false, null);
        }
        else if (result.success){
            this.popupService.show("Profile data saved", true, null);
            this.back();
        }

        this.back();
        return;

    }

    back(): void {
        this.router.navigate(['/account']);
    }

}
