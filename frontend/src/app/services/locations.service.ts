import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class LocationsService {

  constructor(private httpClient: HttpClient) { }

  get_public_locations()
  {
    return this.httpClient.get("/api/locations")
  }

  create_location(name,ispublic,street, postalcode,city){
    return this.httpClient.post("/api/locations",{
      "name": name,
      "ispublic": ispublic,
      "street": street,
      "postalcode": postalcode,
      "city": city
    })
  }
}
