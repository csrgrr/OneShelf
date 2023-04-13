import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from 'src/app/models/User';
import { UserService } from 'src/app/services/user.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {

  username: string = "";
  email: string = "";
  password: string = "";

  user: User = new User();

  constructor(private userService: UserService, private router: Router) {}

  ngOnInit(): void {
  }

  save() {
    this.user.user = this.username;
    this.user.email = this.email;
    this.user.password = this.password;

    console.log(this.user);

    this.userService.saveUser(this.user).subscribe(
      res => {
        Swal.fire({
          position: 'top',
          icon: 'success',
          title: 'User registered',
          showConfirmButton: false,
          timer: 1000
        })
        this.router.navigate(['/librarian'])
      },
      error => {
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'User or password already existing!'
        })
        console.log(error);
      }
    );
  }
}
