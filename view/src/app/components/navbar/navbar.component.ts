import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { Router, ActivatedRoute } from '@angular/router';


@Component({
    selector: 'app-navbar',
    standalone: true,
    imports: [
        RouterLink,
        RouterLinkActive,
  ],
    templateUrl: './navbar.component.html',
    styleUrl: './navbar.component.css'
})


export class NavbarComponent {

    highlightTab(event: Event): void{

        //fetch all element of UL
        const ulElement = document.getElementById('navbarUl');

        if (ulElement){

            const aElements = ulElement.getElementsByTagName('a');
            const aArray: HTMLElement[] = Array.from(aElements) as HTMLElement[];

            //reset color
            aArray.forEach(a => a.style.color = 'white');
        }

        //fetch caller element
        const clickedElement    = event.target as HTMLElement;
        clickedElement.style.color = 'red';
    }
}
