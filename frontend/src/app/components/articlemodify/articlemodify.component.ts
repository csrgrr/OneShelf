import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Article } from 'src/app/models/article';
import { ArticleService } from 'src/app/services/article.service';
import { GenreService } from 'src/app/services/genre.service';
import { UploadService } from 'src/app/services/upload.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-articlemodify',
  templateUrl: './articlemodify.component.html',
  styleUrls: ['./articlemodify.component.css']
})
export class ArticlemodifyComponent implements OnInit {

  article:Article = new Article;
  genres:any = []
  selectedFiles: File[] = [];


  constructor(private articleService:ArticleService, private genreService:GenreService, private router:Router,  private uploadService: UploadService, private activatedRoute:ActivatedRoute) { }

  ngOnInit(): void {
    this.loadGenres()
    this.loadArticle()
  }
  loadGenres(){
    this.genreService.listGenres().subscribe(
      res=>{
        // console.log(res)
        this.genres = res
      }
    )
  }

  loadArticle(){
    this.activatedRoute.params.subscribe(
      params =>{
        let id = params['id']
        if(id){
          this.articleService.findArticle(id).subscribe(
            res=>{
              this.article.id = res.id
              this.article.authors = res.authors
              this.article.year = res.year
              this.article.title = res.title
              this.article.journal = res.journal
              this.article.issue = res.issue
              this.article.place = res.place
              this.article.doi = res.doi
              this.article.genreId = res.genreId
              this.article.pdf = res.pdf
              
              console.log(res)
              
            }
            
          )
        }
      }
    )
  }


  file: any = undefined;
  // PDFS
onFileSelected(event: any) {
  this.selectedFiles = event.target.files;
  const file = this.selectedFiles[0];
  this.file = file;

  this.article.pdf = file.name
  
}



  modify(){
    this.articleService.modifyArticle(this.article).subscribe(
      res => {
        Swal.fire({
          position: 'top',
          icon: 'success',
          title: 'Article modified',
          showConfirmButton: false,
          timer: 1000
        })
        this.router.navigate(['/librarian'])
      }
    )
    this.uploadService.uploadFile(this.file).subscribe(
      (response) => console.log(response),
      (error) => console.log(error)
    );
    
  }
  

}
