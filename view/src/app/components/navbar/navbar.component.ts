import { Component, OnInit } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { Router, ActivatedRoute } from '@angular/router';
import { StyleService } from '../../services/style.service';


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


export class NavbarComponent implements OnInit{

    private navbarDefaultColor: any;
    private navbarHighlightColor: any;

    constructor(private styleService: StyleService) {}

    ngOnInit(): void {
        this.navbarDefaultColor    = this.styleService.getCSSVariableValue('--font-color-1');
        this.navbarHighlightColor  = this.styleService.getCSSVariableValue('--font-color-3');
    }

    highlightTab(event: Event): void{

        //fetch all element of UL
        const ulElement = document.getElementById('navbarUl');

        if (ulElement){

            const aElements = ulElement.getElementsByTagName('a');
            const aArray: HTMLElement[] = Array.from(aElements) as HTMLElement[];

            //reset color
            aArray.forEach(a => a.style.color = this.navbarDefaultColor);
        }

        //fetch caller element
        const clickedElement            = event.target as HTMLElement;
        clickedElement.style.color      = this.navbarHighlightColor;
    }
}
