import {Component, OnInit} from '@angular/core';
import {GameServiceService} from "../game-service.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-game-details',
  templateUrl: './game-details.component.html',
  styleUrls: ['./game-details.component.sass']
})
export class GameDetailsComponent implements OnInit {
  game: any;
  rate: any;
  id: any;
  constructor(private gs: GameServiceService,
              private route: ActivatedRoute,
              private router: Router) {
  }

  ngOnInit() {
    this.rate=0;
    console.log('ViewGameComponent');
    console.log(this.router);
    console.log(this.route);
    this.route.params.subscribe((res) => {
      this.id = res['id'];
      this.gs.get_game(this.id).subscribe((res) => {
        console.log("ViewGameComponent.ngOnInit.gs.get_game");
        console.log(res)
        this.game = res['game'];
        this.rate=res['my_rating']['rating'];
        console.log(this.game);
      });
    });
  }

  rate_game(rating){
    this.gs.rate_gate(this.id,rating).subscribe((res)=>{
      console.log(res);
      location.reload();
    })
  }

}
