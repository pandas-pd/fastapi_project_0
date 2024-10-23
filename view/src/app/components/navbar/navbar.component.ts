import { Component, OnDestroy, OnInit } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { Router, ActivatedRoute } from '@angular/router';
import { NavigationEnd } from '@angular/router';
import { Subscription } from 'rxjs';
import { filter } from 'rxjs';
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


export class NavbarComponent implements OnInit, OnDestroy{

    private navbarDefaultColor: any;
    private navbarHighlightColor: any;
    private routerSubscription!: Subscription;
    private urlTabMap: any;

    constructor(private styleService: StyleService, private router: Router) {}

    ngOnInit(): void {

        //init the mapping
        interface StringMap{
            [key: string]: string;
        }

        //map the urls from routes.ts to navbar.component.html
        let urlTabMap: StringMap = {
            '/':                'navbarHome',
            '/skills':          'navbarSkills',
            '/projects':        'navbarProjects',
            '/users':           'navbarUsers',
            '/login':           'navbarLogin',
        };
        this.urlTabMap = urlTabMap;

        //fetch styles needed for highlight
        this.navbarDefaultColor    = this.styleService.getCSSVariableValue('--font-color-1');
        this.navbarHighlightColor  = this.styleService.getCSSVariableValue('--font-color-3');

        //subscribe to NavigationEnd events
        this.routerSubscription = this.router.events

        .pipe(filter((event): event is NavigationEnd => event instanceof NavigationEnd)) // Type guard here
        .subscribe((event: NavigationEnd) => {

            const currentUrl : string = event.urlAfterRedirects;
            //console.log('URL changed to:', currentUrl);
            this.markTab(currentUrl);
            });
        }

    ngOnDestroy(): void {
        //unsubscribe to avoid memory leaks
        if (this.routerSubscription) {
          this.routerSubscription.unsubscribe();
        }
      }

    markTab(currentUrl:string) : void{

        //fetch id
        let aId : string = this.urlTabMap[currentUrl];

        //restet style
        const ulElement = document.getElementById('navbarUl');

        if (ulElement){

            const aElements = ulElement.getElementsByTagName('a');
            const aArray: HTMLElement[] = Array.from(aElements) as HTMLElement[];

            //reset color
            aArray.forEach(a => a.style.color = this.navbarDefaultColor);
        };

        //set new color
        let currentTab: any         = document.getElementById(aId);
        currentTab.style.color      = this.navbarHighlightColor;
    }

}
