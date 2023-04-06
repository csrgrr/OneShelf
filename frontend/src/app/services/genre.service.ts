import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Genre } from '../models/genre';

@Injectable({
  providedIn: 'root'
})
export class GenreService {
  private httpHeaders:HttpHeaders = new HttpHeaders({'Context-type':'application/json'})

  URL:string = "https://localhost:7064"

  constructor(private http:HttpClient) { }


  //Save Genres
  saveGenre(genre:Genre) : Observable<Genre>{
    return this.http.post<Genre>(this.URL +'/api/genre/save', genre, {headers: this.httpHeaders})
  }

    //List Genres
    listGenres() : Observable<Genre>{
      return this.http.get<Genre>(this.URL+'/api/genre/list')
    }
  
  //Modify - find by id
  findGenre(id:number) : Observable<Genre>{
    return this.http.get<Genre>(this.URL+'/api/genre/'+id)
  }
  //Modify - confirm
  modifyGenre(genre:Genre) :Observable<Genre>{
    let modifyParams:any = {
      Genre: genre.genre, 
      Color: genre.color
    }
    return this.http.put<Genre>(this.URL+'/updateGenre/'+genre.id, genre, {headers: this.httpHeaders, params: modifyParams})
  }

    //DELETE Genres
    deleteGenre(id:number): Observable<Genre>{
      return this.http.delete<Genre>(this.URL+'/deleteGenre/'+id)
    }

}
