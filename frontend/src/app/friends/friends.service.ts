import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class FriendsService {

  constructor(private http: HttpClient) { }

  get_friends(event_id){
    return this.http.patch('api/event/invite',{'event_id': event_id})
  }
}
