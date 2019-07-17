import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {HttpClient} from "@angular/common/http";
import {AppComponent} from "../app.component";
import {Router} from '@angular/router';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.sass']
})
export class RegistrationComponent implements OnInit {
  require_registrationcode: boolean;
  username: string;
  password: string;
  queryForm: FormGroup;
  data: any
  loginForm: FormGroup;

  constructor(private formBuilder: FormBuilder,
              private http: HttpClient,
              private ac: AppComponent,
              private router: Router) {
  }

  ngOnInit() {
    this.queryForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });
    this.require_registrationcode = true;
  }

  register() {
    console.log("register");
    console.log(this.queryForm.value['username']);
    console.log(this.queryForm.value['password']);
  }

  login() {
    console.log("login()")
    this.username = this.loginForm.value['username'];
    this.password = this.loginForm.value['password'];

    this.data = {
      "username": this.username,
      "password": this.password
    }

    this.http.post("/api/login", this.data).subscribe(
      res => {
        console.log("login().post.bra")
        console.log(res.toString());
        localStorage.setItem('access_token', res.toString());
        window.location.href = "/";
      },
      error => {
        console.log(error)
      }
    )

  }
}
