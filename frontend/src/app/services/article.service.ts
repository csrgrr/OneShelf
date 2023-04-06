import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Article } from '../models/article';

@Injectable({
  providedIn: 'root'
})
export class ArticleService {
  
  private httpHeaders:HttpHeaders = new HttpHeaders({'Context-type':'application/json'})

  URL:string = "https://localhost:7064"

  constructor(private http:HttpClient) { }


  //Save Article
  saveArticle(article:Article) : Observable<Article>{
    return this.http.post<Article>(this.URL +'/api/article/save', article, {headers: this.httpHeaders})
  }

  //List Articles
  listArticles() : Observable<Article>{
    return this.http.get<Article>(this.URL+'/api/article/list')
  }

  //Modify - find by id
  findArticle(id:number) : Observable<Article>{
    return this.http.get<Article>(this.URL+'/api/article/'+id)
  }

  //Modify - confirm
  modifyArticle(article:Article) :Observable<Article>{
    let modifyParams:any = {
      Authors: article.authors, 
      Year: article.year,
      Title: article.title,
      Journal: article.journal,
      Issue: article.issue,
      Place: article.place,
      Doi: article.doi,
      GenreId: article.genreId,
      Pdf: article.pdf
    }
    return this.http.put<Article>(this.URL+'/updateArticle/'+article.id, article, {headers: this.httpHeaders , params: modifyParams})
  }


  //DELETE Article
  deleteArticle(id:number): Observable<Article>{
    return this.http.delete<Article>(this.URL+'/deleteArticle/'+id)
  }




}
