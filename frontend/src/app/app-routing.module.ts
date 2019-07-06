import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {RegistrationComponent} from "./registration/registration.component";
import {DashboardComponent} from "./dashboard/dashboard.component";
import {CreateGameComponent} from "./game/create-game/create-game.component";
import {AuthGuard} from "./auth-guard.guard";
import {CreateLocationComponent} from "./location/create-location/create-location.component";

const routes: Routes = [
  {path: '', component: DashboardComponent,canActivate: [AuthGuard]},
  {path: 'login', component: RegistrationComponent},
  {path: 'game/create', component: CreateGameComponent},
  {path: 'location/new', component: CreateLocationComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
