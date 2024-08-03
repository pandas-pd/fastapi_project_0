import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { SkillsComponent } from './components/skills/skills.component';

export const routes: Routes = [

    {
        path: 'home',
        component: HomeComponent,
    },

    {
        path: 'skills',
        loadComponent: () =>
            import('./components/skills/skills.component').then((c) => c.SkillsComponent),
        //component: SkillsComponent,
    }

];
