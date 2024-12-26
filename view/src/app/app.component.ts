import { AfterViewInit, Component, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

//components
import { NavbarComponent } from './components/navbar/navbar.component';
import { PopupComponent } from "./components/popup/popup.component";
import { PopupService } from './services/popup.service';
import { SpinnerComponent } from './components/spinner/spinner.component';
import { SpinnerService } from './services/spinner.service';

@Component({
    selector: 'app-root',
    standalone: true,
    imports: [

        //router stuff
        CommonModule,
        RouterOutlet,

        //component imports not included in router
        NavbarComponent,
        PopupComponent,
        SpinnerComponent
],

    templateUrl: './app.component.html',
    styleUrl: './app.component.css'
})

export class AppComponent implements AfterViewInit{
    title = 'view';

    @ViewChild(PopupComponent) popupComponent!: PopupComponent;
    @ViewChild(SpinnerComponent) spinnerComponent!: SpinnerComponent;

    constructor(private popupService: PopupService, private spinnerService: SpinnerService){}

    ngAfterViewInit(): void {
        this.popupService.registerPopupComponent(this.popupComponent);
        this.spinnerService.registerSpinnerComponent(this.spinnerComponent);
    }
}
