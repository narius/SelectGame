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

  add_to_library(game_id){
    return this.http.post('api/library',{'game_id':game_id});
  }

  remove_from_library(game_id){
    return this.http.delete('api/library/'+game_id);
  }

  get_library(){
    return this.http.get('api/library');
  }
}
