import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})

export class StyleService {

    getCSSVariableValue(variable: string): string {
        return getComputedStyle(document.documentElement).getPropertyValue(variable).trim();
    }
}
