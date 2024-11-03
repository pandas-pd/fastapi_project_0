# Notes on Angualr app

## Usefull commands:

- ng build --configuration=development; ng serve --configuration=development --open
    - builds for the dev env
    - uses the environment variables from src\environments\environment.development.ts
    - servers the application on the given port

- ng build; ng serve --open
    - builds for production environment
    - uses the environment variables from src\environments\environment.ts
    - servers the application on the given port
