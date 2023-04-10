import { Component, OnInit } from '@angular/core';
import { ArticleService } from 'src/app/services/article.service';
import { Genre } from 'src/app/models/genre';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-librarian',
  templateUrl: './librarian.component.html',
  styleUrls: ['./librarian.component.css']
})
export class LibrarianComponent implements OnInit {

  articles:any = []

  constructor(private articleService:ArticleService) { }

  ngOnInit(): void {
    this.list()
  }

  list(){
    this.articleService.listArticles().subscribe(
      res=>{
        console.log(res)
        this.articles = res
      }
    )
  }
  delete(id:number){
    this.articleService.deleteArticle(id).subscribe(
      res =>{
        Swal.fire({
          position: 'top',
          icon: 'success',
          title: 'Article deleted',
          showConfirmButton: false,
          timer: 1000
        })
        this.list();
       }
    )

  }

}
