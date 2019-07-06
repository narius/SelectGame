import {HTTP_INTERCEPTORS} from '@angular/common/http';
import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {Observable} from "rxjs";
import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';

// import ngx-translate and the http loader
import {TranslateLoader, TranslateModule} from '@ngx-translate/core';
import {TranslateHttpLoader} from '@ngx-translate/http-loader';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import {LekComponent} from './lek/lek.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {
  NbThemeModule,
  NbLayoutModule,
  NbCardModule,
  NbSidebarModule,
  NbButtonModule,
  NbMenuModule
} from '@nebular/theme';
import {NbEvaIconsModule} from '@nebular/eva-icons';
//https://www.codeandweb.com/babeledit/tutorials/how-to-t
import {ToastrModule} from 'ngx-toastr';
import {RegistrationComponent} from './registration/registration.component';
import {DashboardComponent} from './dashboard/dashboard.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {LoginComponent} from './login/login.component';
import {CdkTableModule} from "@angular/cdk/table";
import {CreateGameComponent} from './game/create-game/create-game.component';
import {RateGameComponent} from './game/rate-game/rate-game.component';
import {ViewGameComponent} from './game/view-game/view-game.component';
import {CreateLocationComponent} from './location/create-location/create-location.component';
import {ViewMyLocationsComponent} from './location/view-my-locations/view-my-locations.component';
import {ButtonsModule} from 'ngx-bootstrap/buttons';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {HeaderComponent} from './layout/header/header.component';
import {FontAwesomeModule} from '@fortawesome/angular-fontawesome';
import {library} from '@fortawesome/fontawesome-svg-core';
import {fas} from '@fortawesome/free-solid-svg-icons';
import {AuthInterceptor} from "./services/auth.service";

// ranslate-your-angular8-app-with-ngx-translate

@NgModule({
  declarations: [
    AppComponent,
    LekComponent,
    RegistrationComponent,
    DashboardComponent,
    LoginComponent,
    CreateGameComponent,
    RateGameComponent,
    ViewGameComponent,
    CreateLocationComponent,
    ViewMyLocationsComponent,
    HeaderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: HttpLoaderFactory,
        deps: [HttpClient]
      }
    }),
    BrowserAnimationsModule,
    NbThemeModule.forRoot({name: 'default'}),
    NbLayoutModule,
    NbEvaIconsModule,
    NbCardModule,
    NbSidebarModule,
    NbSidebarModule.forRoot(),
    NbButtonModule,
    NbMenuModule.forRoot(),
    FormsModule,
    ReactiveFormsModule,
    CdkTableModule,
    ButtonsModule.forRoot(),
    NgbModule,
    BrowserModule,
    FontAwesomeModule,
    ToastrModule.forRoot()
  ],
  providers: [
    {provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true}, ,
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor() {
    library.add(fas);
  }
}

// required for AOT compilation
export function HttpLoaderFactory(http: HttpClient) {
  return new TranslateHttpLoader(http);
}
