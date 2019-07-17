import { Component, OnInit } from '@angular/core';
import {LocationsService} from "../services/locations.service";
import {GameServiceService} from "../game/game-service.service"
import {EventService} from "../event/event.service";
import {NewsService} from "../news/news.service";
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.sass']
})
export class DashboardComponent implements OnInit {
  private locations:any;
  private games:any;
  private events:any;
  private news: any;

  constructor(private ls: LocationsService,
              private gs: GameServiceService,
              private es: EventService,
              private ns: NewsService) { }

  ngOnInit() {
    this.ls.get_public_locations().subscribe((res)=>{
      console.log(res);
      this.locations = res;
    });
    this.gs.get_games().subscribe((res) => {
      this.games = res;
    });
    this.es.all_events().subscribe((res)=>{
      this.events = res;
    })

    this.ns.get_news().subscribe((res)=>{
      this.news = res;
    })
  }

}
