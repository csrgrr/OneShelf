import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms'
import { Router } from '@angular/router';
import { UserLogin } from 'src/app/models/UserLogin';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  form:FormGroup

  constructor(private formBuilder:FormBuilder, private loginService:LoginService, private router:Router){
    this.form = formBuilder.group({
      username : [],
      password : []
    })

  }


  getData(){
    let username = this.form.get('username')?.value
    let password = this.form.get('password')?.value

    let userLogin = new UserLogin(username, password)

    this.loginService.login(userLogin).subscribe(
      res => {
        console.log(res)
        sessionStorage.setItem('token', res.token)
        this.router.navigate(['/shelf'])
      }
    )
  }

}
