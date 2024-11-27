import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-popup',
    standalone: true,
    imports: [CommonModule],
    templateUrl: './popup.component.html',
    styleUrl: './popup.component.css'
})
export class PopupComponent implements OnInit{

    isVisible = false;  // Control visibility of the popup
    message = '';       // Message to display
    isSuccess = true;   // Success or failure state

    constructor(){}

    ngOnInit(): void {}

    async showPopup(message: string, isSuccess: boolean, displayTime: number){

        // update values to acess by service
        this.message        = message;
        this.isSuccess      = isSuccess;
        this.isVisible      = true;

        setTimeout(() => {
            this.isVisible = false;
        }, displayTime);
    }
}
