import { Component, OnInit } from '@angular/core';
import { ShelfComponent } from '../shelf/shelf.component';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent implements OnInit {

  searcher = false;

  constructor() { 
  }

  ngOnInit(): void {
  }

  browse(){
    if(this.searcher == false)
    this.searcher = true
    else 
    this.searcher = false
    
  }


}
