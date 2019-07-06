import { Component, OnInit } from '@angular/core';
import {TranslateService} from '@ngx-translate/core';
@Component({
  selector: 'app-lek',
  templateUrl: './lek.component.html',
  styleUrls: ['./lek.component.sass']
})
export class LekComponent implements OnInit {
  status: string;
  fromjson: string;

  constructor(private translate: TranslateService) { }

  ngOnInit() {
    this.fromjson = 'friendship.status.sent';
    this.translate.get(this.fromjson).subscribe((res: string) => {
    console.log(res);
    this.status = res;
});
  }

}

