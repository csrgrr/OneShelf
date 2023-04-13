import { Injectable } from '@angular/core';
import { Observable } from 'rxjs'
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { UserLogin } from '../models/UserLogin';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  URL:string = "http://localhost:5000"
  httpHeaders:HttpHeaders = new HttpHeaders({'Content-Type':'application/json'})

  constructor(private http:HttpClient) { }

  login(userLogin:UserLogin) : Observable<UserLogin>{
    return this.http.post<UserLogin>(this.URL+'/login', userLogin, {headers:this.httpHeaders})

  }
}
