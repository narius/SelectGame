import {Component} from '@angular/core';
import {TranslateService} from '@ngx-translate/core';
import {AuthGuard} from "./auth-guard.guard";
import {AuthService} from "./services/auth.service";

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
              private as: AuthService) {
    translate.setDefaultLang('en');
  }

  ngOnInit() {
    console.log("AppComponent.ngOnInit");
    console.log(this.translate.instant("friendship.status"));
    // console.log(this.translate.get("friendship.status"));
    this.translate.get("friendship.status").subscribe((res) => {
      console.log(res);
    });
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



}
