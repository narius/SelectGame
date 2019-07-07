import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class GameServiceService {

  constructor(private http: HttpClient) { }

  create_game(name: string){
    return this.http.post("api/games",{'name':name});
  }

  get_games(){
    return this.http.get("api/games");
  }

  get_game(id){
    return this.http.get("/api/game/"+id);
  }

  rate_gate(game,rating){
    return this.http.put('api/game/rate/'+game,{'rate':rating});
  }
}
