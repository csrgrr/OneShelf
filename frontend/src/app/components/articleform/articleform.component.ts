import { Component, OnInit } from '@angular/core';
import { Article } from 'src/app/models/article';
import { ArticleService } from 'src/app/services/article.service';
import Swal from 'sweetalert2';
import {Router} from "@angular/router";
import { GenreService } from 'src/app/services/genre.service';

@Component({
  selector: 'app-articleform',
  templateUrl: './articleform.component.html',
  styleUrls: ['./articleform.component.css']
})
export class ArticleformComponent implements OnInit {

  authors: string = ""
  year: number = 0
  title: string = ""
  journal: string = ""
  issue: number = 0
  place: string = ""
  doi: string = ""
  genreId: number = 0
  pdf: string = ""

  genres:any = []
  article:Article = new Article();


  constructor(private articleService:ArticleService, private genreService:GenreService, private router:Router) { }

  ngOnInit(): void {
    this.loadGenres()
  }
  loadGenres(){
    this.genreService.listGenres().subscribe(
      res=>{
        console.log(res)
        this.genres = res
      }
    )
  }


  save(){
   this.article.authors = this.authors
   this.article.year = this.year
   this.article.title = this.title
   this.article.journal = this.journal
   this.article.issue = this.issue
   this.article.place = this.place
   this.article.doi = this.doi
   this.article.genreId = this.genreId
   this.article.pdf = this.pdf
   

   this.articleService.saveArticle(this.article).subscribe(
    res => {
   Swal.fire({
     position: 'top',
     icon: 'success',
     title: 'Genre registered',
     showConfirmButton: false,
     timer: 1000
   })
   this.router.navigate(['/shelf'])
  }
   )
  }
}
