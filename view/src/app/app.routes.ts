import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { SkillsComponent } from './components/skills/skills.component';
import { ProjectsComponent } from './components/projects/projects.component';
import { UsersComponent } from './components/users/users.component';
import { LoginComponent } from './components/login/login.component';
import { AccountComponent } from './components/account/account.component';
import { ResetPasswordComponent } from './components/reset-password/reset-password.component';
import { ChangePasswordComponent } from './components/change-password/change-password.component';
import { authGuard } from './guards/auth.guard';
import { accountResolver } from './resolvers/account.resolver';


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
            canMatch: [authGuard]
    },

    {
        path: 'login',
        loadComponent: () =>
            import('./components/login/login.component').then((c) => c.LoginComponent),
    },

    {
        path: 'account',
        loadComponent: () =>
            import('./components/account/account.component').then((c) => c.AccountComponent),
            canMatch: [authGuard],
            resolve: {accountData: accountResolver}
    },

    {
        path: 'reset-password',
        loadComponent: () =>
            import('./components/reset-password/reset-password.component').then((c) => c.ResetPasswordComponent),
    },

    {
        path: 'account/change-password',
        loadComponent: () =>
            import('./components/change-password/change-password.component').then((c) => c.ChangePasswordComponent),
    }

];
