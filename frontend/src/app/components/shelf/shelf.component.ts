import { Component, OnInit } from '@angular/core';
import { ArticleService } from 'src/app/services/article.service';
import { Genre } from 'src/app/models/genre';
import Swal from 'sweetalert2';
import { NavBarComponent } from '../nav-bar/nav-bar.component';
import { ArticleDetailsComponent } from '../article-details/article-details.component';

@Component({
  selector: 'app-shelf',
  templateUrl: './shelf.component.html',
  styleUrls: ['./shelf.component.css']
})
export class ShelfComponent implements OnInit {

  search:string='';
  articlesRepo:any = []
  articles:any = []

  filterRepo:any = []
 


  constructor(private articleService:ArticleService) { 
    
  }

  

  ngOnInit(): void {
    this.list()
  }

  inputWrite(){
    this.articles = []
    for (const article of this.articlesRepo) {
      
      let search = this.search.toLowerCase()

      let authors = article.authors.toLowerCase()
      let doi = article.doi
      let color = article.genre.color.toLowerCase()
      let genre = article.genre.genre.toLowerCase()
      let issue = String(article.issue)
      let journal = article.journal.toLowerCase()
      let pdf = article.pdf.toLowerCase()
      let place = article.place.toLowerCase()
      let title = article.title.toLowerCase()
      let year = String(article.year)

      if(
        authors.includes(search) ||
        doi.includes(search) ||
        color.includes(search) ||
        genre.includes(search) ||
        issue.includes(search) ||
        journal.includes(search) ||
        pdf.includes(search) ||
        place.includes(search) ||
        title.includes(search) ||
        year.includes(search) 
      )
      this.articles.push(article)
      
    }
  }

  clicked = false;
showFilter() {
  const filterForm = document.getElementById("filterForm")!;
  if(this.clicked == false) {
    filterForm.classList.add("show");
    filterForm.classList.remove("hide"); 
    this.clicked = true;
  } else{
    filterForm.classList.add("hide");
    filterForm.classList.remove("show");
    this.clicked = false;
  }
}
  

authors:String = '';
title:String = '';
year:String = '';
journal:String = '';
issue:String = '';
place:String = '';
genre:String = '';
doi:String = '';



filter(){
  this.articles = []
   for (const article of this.filterRepo) {
   let authorsSearch = this.authors.toLowerCase()
   let titleSearch = this.title.toLowerCase()
   let yearSearch = this.year.toLowerCase()
   let journalSearch = this.journal.toLowerCase()
   let issueSearch = this.issue.toLowerCase()
   let placeSearch = this.place.toLowerCase()
   let genreSearch = this.genre.toLowerCase()
   let doiSearch = this.doi.toLowerCase()

   let authors = article.authors.toLowerCase()
   let doi = article.doi
   let genre = article.genre.genre.toLowerCase()
   let issue = String(article.issue)
   let journal = article.journal.toLowerCase()
   let place = article.place.toLowerCase()
   let title = article.title.toLowerCase()
   let year = String(article.year)

      console.log(authorsSearch)
     if(
       (authors.includes(authorsSearch) || authorsSearch == '') &&
       (title.includes(titleSearch)|| titleSearch == '')  &&
       (year.includes(yearSearch)|| yearSearch == '')  &&
       (journal.includes(journalSearch)|| journalSearch == '')  &&
       (issue.includes(issueSearch)|| issueSearch == '')  &&
       (place.includes(placeSearch)|| placeSearch == '')  &&
       (genre.includes(genreSearch)|| genreSearch == '')  &&
       (doi.includes(doiSearch)|| doiSearch == '') 
      )
      this.articles.push(article)
      
    }

}



  list(){
    this.articleService.listArticles().subscribe(
      res=>{
        console.log(res)
        this.articlesRepo = res
        this.articles = this.articlesRepo
        this.filterRepo = this.articlesRepo
      }
    )
  }

  id:number = 0
  article:any = '';
  details(id:number){
    // console.log(id)
    this.id = id;
    console.log(this.id)
    const details = document.getElementsByTagName("app-article-details")[0]!
    // if(this.clicked == false) {
    //   details.classList.add("showDetails");
    //   details.classList.remove("hideDetails"); 
    //   this.clicked = true;
    // } else{
    //   details.classList.add("hideDetails");
    //   details.classList.remove("showDetails");
    //   this.clicked = false;
    // }

      this.articleService.findArticle(this.id).subscribe(
        res=>{
          this.article = res
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

  //---------------------





}

