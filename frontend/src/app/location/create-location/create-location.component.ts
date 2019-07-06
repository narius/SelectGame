import { Component, OnInit } from '@angular/core';
import {LocationsService} from "../../services/locations.service";

@Component({
  selector: 'app-create-location',
  templateUrl: './create-location.component.html',
  styleUrls: ['./create-location.component.sass']
})
export class CreateLocationComponent implements OnInit {

  constructor(private ls: LocationsService) { }

  ngOnInit() {
  }

  create_location(name,ispublic,street, postalcode,city){
    console.log("create_location");
    console.log(name);
    console.log(ispublic);
    console.log(street);
    console.log(postalcode);
    console.log(city);
    this.ls.create_location(name,ispublic,street, postalcode,city).subscribe()
  }
}
