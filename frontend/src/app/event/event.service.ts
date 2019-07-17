import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class EventService {

  constructor(private http: HttpClient) { }

  all_events(){
    console.log("EventService.all_events");
    return this.http.get('api/event');
  }

  get_event(event_id){
    return this.http.get('api/event/'+event_id);
  }

  send_invite(event_id, receiver){
    return this.http.post('api/event/invite',{
      'event_id': event_id,
      'receiver': receiver
    })
  }

  get_my_invites(){
    return this.http.get('api/event/invite')
  }

  change_invite_status(event_id, status){
    return this.http.put('api/event/invite',
                        {'event_id': event_id,
                        'status': status});
  }

}
