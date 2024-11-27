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

    isVisible : boolean | null = false;  // Control visibility of the popup
    message = '';       // Message to display
    isSuccess = true;   // Success or failure state

    constructor(){}

    ngOnInit(): void {}

    showPopup(message: string, isSuccess: boolean, displayTime: number | null){

        // set a standard display time for consitance
        if (displayTime == null){
            displayTime = 3000;
        }

        // update values to acess by service
        this.message        = message;
        this.isSuccess      = isSuccess;
        this.isVisible      = true;

        setTimeout(() => {
            this.hidePopup();
        }, displayTime);
    }


    hidePopup(): void {
        this.isVisible = false;
    }

}
