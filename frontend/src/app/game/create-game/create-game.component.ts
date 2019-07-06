import { Component, OnInit } from '@angular/core';
import {GameServiceService} from "../game-service.service";
import {ToastrService} from "ngx-toastr";
@Component({
  selector: 'app-create-game',
  templateUrl: './create-game.component.html',
  styleUrls: ['./create-game.component.sass']
})
export class CreateGameComponent implements OnInit {
  public game_name: string;
  constructor(private gs: GameServiceService,
              private toastr: ToastrService) { }

  ngOnInit() {
  }

  create_game(name){
    console.log("Create_game()");
    console.log(name);
    this.gs.create_game(name).subscribe((res) => {
      console.log("gs.create_game");
      console.log(res);
      this.toastr.success("Sucess");

    },(error1) => {
      console.log("gs.create_game error");
      console.log(error1)
    })
  }

}
