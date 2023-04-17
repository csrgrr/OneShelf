import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ArticleformComponent } from './components/articleform/articleform.component';
import { ShelfComponent } from './components/shelf/shelf.component';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { GenreformComponent } from './components/genreform/genreform.component';
import { ArticlemodifyComponent } from './components/articlemodify/articlemodify.component';
import { GenremodifyComponent } from './components/genremodify/genremodify.component';
import { GenremodifyconfirmComponent } from './components/genremodifyconfirm/genremodifyconfirm.component';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { LibrarianComponent } from './components/librarian/librarian.component';
import { ArticleDetailsComponent } from './components/article-details/article-details.component';
import { LoginComponent } from './components/login/login.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { DashboardGuard } from './guards/dashboard.guard';
import { TokenInterceptor } from './interceptors/token.interceptor';
import { SigninComponent } from './components/signin/signin.component';
import { PdfComponent } from './components/pdf/pdf.component';

//ROUTES
const routes: Routes = [
  {path: '', redirectTo: '/login', pathMatch: 'full' },
  {path: 'shelf', component: ShelfComponent},
  {path: 'librarian', component: LibrarianComponent},
  {path: 'form/article', component: ArticleformComponent},
  {path: 'form/genre', component: GenreformComponent},
  {path: 'modify/article/:id', component: ArticlemodifyComponent},
  {path: 'modify/genre', component: GenremodifyComponent},
  {path: 'modify/genre/:id', component: GenremodifyconfirmComponent},
  {path: 'shelf/details', component:ArticleDetailsComponent},
  {path: 'login', component:LoginComponent},
  {path: 'dashboard', component:DashboardComponent, canActivate: [DashboardGuard]},
  {path: 'sign-in', component:SigninComponent},
  {path: 'pdf', component:PdfComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    ArticleformComponent,
    ShelfComponent,
    GenreformComponent,
    ArticlemodifyComponent,
    GenremodifyComponent,
    GenremodifyconfirmComponent,
    NavBarComponent,
    LibrarianComponent,
    ArticleDetailsComponent,
    LoginComponent,
    DashboardComponent,
    SigninComponent,
    PdfComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes),
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass:TokenInterceptor, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
