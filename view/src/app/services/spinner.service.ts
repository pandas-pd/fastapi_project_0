import { Injectable, OnInit } from '@angular/core';
import { SpinnerComponent } from '../components/spinner/spinner.component';
import { timeout } from 'rxjs';

@Injectable({
    providedIn: 'root'
})

export class SpinnerService {

    private spinnerComponent!: SpinnerComponent;
    constructor() { }

    registerSpinnerComponent(component:SpinnerComponent): void {
        this.spinnerComponent = component;
    }

    show(){
        this.spinnerComponent.isLoading = true;
    }

    hide(){
        this.spinnerComponent.isLoading = false;
    }

}

