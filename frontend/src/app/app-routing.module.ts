import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {RegistrationComponent} from "./registration/registration.component";
import {DashboardComponent} from "./dashboard/dashboard.component";
import {CreateGameComponent} from "./game/create-game/create-game.component";
import {AuthGuard} from "./auth-guard.guard";

import {CreateLocationComponent} from "./location/create-location/create-location.component";
import {ViewGameComponent} from "./game/view-game/view-game.component";
import {GameDetailsComponent} from "./game/game-details/game-details.component";
import {GameLibraryComponent} from "./game/game-library/game-library.component";
import {EventViewComponent} from "./event/event-view/event-view.component";


const routes: Routes = [
  {path: '', component: DashboardComponent, canActivate: [AuthGuard]},
  {path: 'login', component: RegistrationComponent},
  {path: 'game/create', component: CreateGameComponent, canActivate: [AuthGuard]},
  {path: 'game/view', component: ViewGameComponent, canActivate: [AuthGuard]},
  {path: 'game/view/:id', component: GameDetailsComponent, canActivate: [AuthGuard]},
  {path: 'location/new', component: CreateLocationComponent, canActivate: [AuthGuard]},
  {path: 'event/:event_id', component: EventViewComponent, canActivate: [AuthGuard]},
  {path: 'library', component: GameLibraryComponent, canActivate: [AuthGuard]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
