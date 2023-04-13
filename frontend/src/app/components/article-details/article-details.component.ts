import { Component, OnInit, Input } from '@angular/core';
import {Router} from "@angular/router";
import { ShelfComponent } from '../shelf/shelf.component';
import { ArticleService } from 'src/app/services/article.service';
@Component({
  selector: 'app-article-details',
  templateUrl: './article-details.component.html',
  styleUrls: ['./article-details.component.css']
})
export class ArticleDetailsComponent implements OnInit {

  @Input() id: number = 0;
  @Input() article:any = '';
  constructor(private router:Router, private shelf:ShelfComponent, private articleService:ArticleService) { }

  ngOnInit(): void {
  }
  loadId(){
      console.log(this.id)

    this.id = this.shelf.id
    this.article = this.shelf.article
    const book = document.getElementsByTagName("book")[0]!
      book.classList.add("bookDetails");

  }

 

}
