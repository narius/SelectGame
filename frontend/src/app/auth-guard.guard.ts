import {Injectable} from '@angular/core';
import {CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router} from '@angular/router';
import {Observable} from 'rxjs';
import { first } from 'rxjs/operators';
//import {AuthenticationService} from "./services/authentication.service";
import {HttpClient} from "@angular/common/http";
import {AuthService} from "./services/auth.service";

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  is_anonymous: any;
  asyncResult: any;
  roles: any;
  ia: boolean;


  constructor(private httpClient: HttpClient,
              private router: Router,
              private as: AuthService) {
  }

  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    console.log('canActivate');
    /*this.as.loggedIn().subscribe((res)=>{
      console.log(res)
      this.is_anonymous=res['user']['is_anonymous'];
      console.log(this.is_anonymous)
    })*/


    console.log("efter async anrop");
    return this.get_is_logged_in();
    //return !this.is_anonymous;

  }


  async get_is_logged_in() {
    console.log("get_is_logged_in");
    await this.httpClient.get('/api/login').pipe(first()).toPromise().then(data => {
      console.log(data);
    }, error => {
      console.log("error");
      console.log(error);
      window.location.href = "/login";
    });
    console.log("after await");
    console.log(this.asyncResult);
    return true
  }

  public get loggedIn(): boolean {
    return localStorage.getItem('access_token') !== null;
  }

}
