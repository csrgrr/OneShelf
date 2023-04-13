import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../models/User';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private httpHeaders:HttpHeaders = new HttpHeaders({'Context-type':'application/json'})

  URL:string = "http://localhost:5000"

  constructor(private http:HttpClient) { }


  //Save User
  saveUser(user:User) : Observable<User>{
    return this.http.post<User>(this.URL +'/add-user', user, {headers: this.httpHeaders})
  }
}