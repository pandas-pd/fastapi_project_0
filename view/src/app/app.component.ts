import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

//components
import { NavbarComponent } from './components/navbar/navbar.component';

@Component({
    selector: 'app-root',
    standalone: true,
    imports: [

        //router stuff
        CommonModule,
        RouterOutlet,

        //component imports not included in router
        NavbarComponent
    ],

    templateUrl: './app.component.html',
    styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'view';
}
