import { Component, OnInit } from '@angular/core';
import { Genre } from 'src/app/models/genre';
import { GenreService } from 'src/app/services/genre.service';
import Swal from 'sweetalert2';
import {Router} from "@angular/router";

@Component({
  selector: 'app-genreform',
  templateUrl: './genreform.component.html',
  styleUrls: ['./genreform.component.css']
})
export class GenreformComponent implements OnInit {
  genre: string = ""
  color: string = ""

  genreClass:Genre = new Genre();

  constructor(private genreService:GenreService, private router:Router) { }

  ngOnInit(): void {
  }
  save(){
    this.genreClass.genre = this.genre
    this.genreClass.color = this.color
    
    
 
    this.genreService.saveGenre(this.genreClass).subscribe(
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
