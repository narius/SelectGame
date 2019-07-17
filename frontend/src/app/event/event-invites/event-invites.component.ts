import { Component, OnInit } from '@angular/core';
import {EventService} from "../event.service";

@Component({
  selector: 'app-event-invites',
  templateUrl: './event-invites.component.html',
  styleUrls: ['./event-invites.component.sass']
})
export class EventInvitesComponent implements OnInit {
  invites: any;

  constructor(private es: EventService) { }

  ngOnInit() {
    this.es.get_my_invites().subscribe((res)=>{
      console.log("EventInvitesComponent");
      console.log(res)
      this.invites = res;
    })

  }

}
