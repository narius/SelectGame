import { Component, OnInit } from '@angular/core';
import {GameServiceService} from "../game-service.service";

@Component({
  selector: 'app-game-library',
  templateUrl: './game-library.component.html',
  styleUrls: ['./game-library.component.sass']
})
export class GameLibraryComponent implements OnInit {
  games: any;
  constructor(private gs: GameServiceService) { }

  ngOnInit() {
    this.gs.get_library().subscribe((res)=>{
      this.games=res;
    });
  }

}
