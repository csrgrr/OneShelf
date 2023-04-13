import { Component, OnInit } from '@angular/core';
import { UsersDashboard } from 'src/app/models/Dashboard';
import { DashboardService } from 'src/app/services/dashboard.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  userDashboard:UsersDashboard = new UsersDashboard()

  ngOnInit():void {
    this.getDataFromDashboard()
  }

  constructor(private dashboardService:DashboardService){

  }
  getDataFromDashboard(){
    this.dashboardService.getUsers().subscribe(
      res => {
        console.log(res)
        this.userDashboard = res
      }
    )
  }

}
