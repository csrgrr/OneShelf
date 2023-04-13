import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { GenreService } from 'src/app/services/genre.service';
import { Genre } from 'src/app/models/genre';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-genremodifyconfirm',
  templateUrl: './genremodifyconfirm.component.html',
  styleUrls: ['./genremodifyconfirm.component.css']
})
export class GenremodifyconfirmComponent implements OnInit {
  genre:Genre = new Genre;

  constructor( private genreService:GenreService, private router:Router, private activatedRoute:ActivatedRoute) { }

  ngOnInit(): void {
    this.loadGenre()
  }
  loadGenre(){
    this.activatedRoute.params.subscribe(
      params =>{
        let id = params['id']
        if(id){
          this.genreService.findGenre(id).subscribe(
            res=>{
              this.genre.id = res.id
              this.genre.genre = res.genre
              this.genre.color = res.color
            }
          )
        }
      }
    )
  }
  modify(){
    this.genreService.modifyGenre(this.genre).subscribe(
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
  }

  }


