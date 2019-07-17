import {Component} from '@angular/core';
import {TranslateService} from '@ngx-translate/core';
import {AuthGuard} from "./auth-guard.guard";
import {AuthService} from "./services/auth.service";
import {HttpClient} from "@angular/common/http";
import { timer } from 'rxjs';
import { concatMap, map, tap } from 'rxjs/operators';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass',
    './header.component.scss',
    './sidebar.component.scss',
    './layout.component.scss']
})
export class AppComponent {
  public pushRightClass: string;
  title = 'frontend';
  invites: any;
  number_of_invites: any;

  items = [
    {
      title: 'Home',
      icon: 'home-outline',
      link: [''],
    },
    {
      title: 'Game',
      expanded: false,
      children: [
        {
          title: 'Create game',
          link: ['game/create'], // goes into angular `routerLink`
        },
        {
          title: 'Rate game',
          ulr: '#', // goes directly into `href` attribute
        },
      ],
    },
  ];

  constructor(private translate: TranslateService,
              private auth: AuthGuard,
              private as: AuthService,
              private http: HttpClient) {
    translate.setDefaultLang('en');
  }

  ngOnInit() {
    console.log("AppComponent.ngOnInit");
    console.log(this.translate.instant("friendship.status"));
    // console.log(this.translate.get("friendship.status"));
    this.translate.get("friendship.status").subscribe((res) => {
      console.log(res);
    });
    const log = this.http.get('api/event/invite');

    this.invites = timer(0, 1000).pipe(
        concatMap(_ => log),
        map((response) => this.test(response)),
      );
    console.log(this.invites.valueOf())
  }

  toggleSidebar() {
    const dom: any = document.querySelector('body');
    dom.classList.toggle(this.pushRightClass);
  }

  logout(){
    this.as.logout().subscribe((res)=>{
      console.log("logout");
      console.log(res);
      localStorage.removeItem("access_token")
      window.location.href = "/login";
    })

  }

  test(re){
    console.log("test");
    console.log(re);
    this.number_of_invites=re.length;
  }



}
