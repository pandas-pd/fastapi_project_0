import { Injectable } from '@angular/core';
import { PopupComponent } from '../components/popup/popup.component';

@Injectable({
    providedIn: 'root'
})
export class PopupService {

    private popupComponent!: PopupComponent;

    constructor(){};

    //register instance for eas of use and best practice as dependency injection
    registerPopupComponent( component: PopupComponent): void {
        this.popupComponent = component;
    }


    //used for showing message
    show(message: string, isSuccess: boolean, displayTime: number | null): void {

        if (this.popupComponent){
            this.popupComponent.showPopup(message, isSuccess, displayTime);

        } else {
            console.error("PopupComponent is not registered");
        }
    }

}
