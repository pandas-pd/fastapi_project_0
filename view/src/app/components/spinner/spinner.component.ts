import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-spinner',
    standalone: true,
    imports: [CommonModule],
    templateUrl: './spinner.component.html',
    styleUrl: './spinner.component.css'
})
export class SpinnerComponent{
    public isLoading : boolean = false;
}
