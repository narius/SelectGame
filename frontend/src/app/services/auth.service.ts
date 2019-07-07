import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {HttpEvent, HttpInterceptor, HttpHandler, HttpRequest} from '@angular/common/http';
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private httpclient: HttpClient) {
  }

  is_loggedin() {
    return this.httpclient.get('/api/login');
  }

  logout(){
    return this.httpclient.delete('/api/login');
  }

}


@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  private token: string
  constructor() {

  }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    console.log("intercept setheaders")
    console.log(localStorage.getItem("access_token"));
    this.token = localStorage.getItem("access_token");
    if (this.token == null){
      this.token = '';
    }
    req = req.clone({
      setHeaders: {
        "Authorization": this.token,}
      }
    );

    return next.handle(req);
  }
}
