import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {EventService} from "../event.service";
import {Location} from "../../models/location.model";
import {User} from "../../models/user.model";

@Component({
  selector: 'app-event-view',
  templateUrl: './event-view.component.html',
  styleUrls: ['./event-view.component.sass']
})
export class EventViewComponent implements OnInit {
  private data:any;
  event: any;
  event_id: any;
  games: any;
  participants: User[];
  location: Location;
  ratings: any;
  showrating: boolean=false

  constructor(private es: EventService,
              private route: ActivatedRoute,
              private router: Router) { }

  ngOnInit() {
    this.route.params.subscribe((res) => {
      this.event_id = res['event_id'];
      this.es.get_event(this.event_id).subscribe((res)=>{
        this.data = res;
        this.event = res['event'];
        this.games = res['games'];
        this.participants = res['participants'];
        this.location = res['location'];
        this.ratings = res['ratings'];
      });
    });
  }

}
