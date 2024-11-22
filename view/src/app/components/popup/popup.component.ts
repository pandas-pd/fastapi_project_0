import { Component } from '@angular/core';

@Component({
    selector: 'app-popup',
    standalone: true,
    imports: [],
    templateUrl: './popup.component.html',
    styleUrl: './popup.component.css'
})
export class PopupComponent {

    visible: boolean        = false;
    displayTimeMS: number   = 5000;

    showPopup():void{
        this.visible = true;
    }

    hidePopup():void{
        this.visible = false
    }

    displayMessage():void{}

}
