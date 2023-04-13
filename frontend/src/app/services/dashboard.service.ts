import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { UsersDashboard } from '../models/Dashboard';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  URL:string = "http://localhost:5000"

  constructor(private http:HttpClient) { }

  getUsers() : Observable<UsersDashboard>{
    return this.http.get<UsersDashboard>(this.URL+'/dashboard')
  }
}
