import { Routes } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { SkillsComponent } from './components/skills/skills.component';
import { ProjectsComponent } from './components/projects/projects.component';
import { UsersComponent } from './components/users/users.component';
import { LoginComponent } from './components/login/login.component';
import { ResetPasswordComponent } from './components/reset-password/reset-password.component';



export const routes: Routes = [

    {
        path: '',
        component: HomeComponent,
    },

    {
        path: 'skills',
        loadComponent: () =>
            import('./components/skills/skills.component').then((c) => c.SkillsComponent),
        //component: SkillsComponent,
    },

    {
        path: 'projects',
        loadComponent: () =>
            import('./components/projects/projects.component').then((c) => c.ProjectsComponent),
    },

    {
        path: 'users',
        loadComponent: () =>
            import('./components/users/users.component').then((c) => c.UsersComponent),
    },

    {
        path: 'login',
        loadComponent: () =>
            import('./components/login/login.component').then((c) => c.LoginComponent),
    },

    {
        path: 'reset-password',
        loadComponent: () =>
            import('./components/reset-password/reset-password.component').then((c) => c.ResetPasswordComponent),
    }

];
