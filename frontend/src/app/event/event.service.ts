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

}
