import { Component, OnInit } from '@angular/core';
import {LocationsService} from "../services/locations.service";
import {GameServiceService} from "../game/game-service.service"
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.sass']
})
export class DashboardComponent implements OnInit {
  private locations:any;
  private games:any;

  constructor(private ls: LocationsService,
              private gs: GameServiceService) { }

  ngOnInit() {
    this.ls.get_public_locations().subscribe((res)=>{
      console.log(res);
      this.locations = res;
    });
    this.gs.get_games().subscribe((res) => {
      this.games = res;
    });
  }

}
