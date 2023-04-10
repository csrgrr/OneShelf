import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import { GenreService } from 'src/app/services/genre.service';
import { Genre } from 'src/app/models/genre';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-genremodify',
  templateUrl: './genremodify.component.html',
  styleUrls: ['./genremodify.component.css']
  
})
export class GenremodifyComponent implements OnInit {
  genreId: number = 0
  genres:any = []



  constructor(private genreService:GenreService, private router:Router) { }

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

  modify(){

    this.router.navigate(['modify/genre/', this.genreId])
  
   }
   delete(id:number){
    this.genreService.deleteGenre(id).subscribe(
      res =>{
        Swal.fire({
          position: 'top',
          icon: 'success',
          title: 'Article deleted',
          showConfirmButton: false,
          timer: 1000
        })
        this.router.navigate(['shelf'])
       }
    )

  }

}
