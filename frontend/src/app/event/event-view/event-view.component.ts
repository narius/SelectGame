import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {EventService} from "../event.service";
import {Location} from "../../models/location.model";
import {User} from "../../models/user.model";
import {FriendsService} from "../../friends/friends.service";

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
  sent: User[]
  rejected: User[];
  location: Location;
  ratings: any;
  showrating: boolean=false
  friends: any;

  constructor(private es: EventService,
              private route: ActivatedRoute,
              private router: Router,
              private fs: FriendsService) { }

  ngOnInit() {
    this.route.params.subscribe((res) => {
      this.event_id = res['event_id'];
      this.es.get_event(this.event_id).subscribe((res)=>{
        this.data = res;
        this.event = res['event'];
        this.games = res['games'];
        this.participants = res['participants'];
        this.sent = res['sent'];
        this.rejected = res['rejected'];
        this.location = res['location'];
        this.ratings = res['ratings'];
      });
    });
    this.fs.get_friends(this.event_id).subscribe((res)=>{
      console.log("event view,get_friends");
      console.log(res)
      this.friends = res;
    })
  }

  send_invite(receiver){
    this.es.send_invite(this.event_id,receiver).subscribe((res)=>{
      console.log("send_invite");
      console.log(res)
    })
  }

}
