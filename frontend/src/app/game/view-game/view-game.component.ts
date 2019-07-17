import { Component, OnInit } from '@angular/core';
import {GameServiceService} from "../game-service.service";
import { Router, ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-view-game',
  templateUrl: './view-game.component.html',
  styleUrls: ['./view-game.component.sass']
})
export class ViewGameComponent implements OnInit {
  games: any;

  constructor(private gs: GameServiceService,
              private route: ActivatedRoute,
              private router: Router) { }

  ngOnInit() {
    console.log("ViewGameComponent");
    this.gs.get_games().subscribe((res)=>{
      console.log("ViewGameComponent.ngOnInit.gs.get_games");
      this.games = res;
    })
  }

}
