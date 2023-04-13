import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ArticleformComponent } from './components/articleform/articleform.component';
import { ShelfComponent } from './components/shelf/shelf.component';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { GenreformComponent } from './components/genreform/genreform.component';
import { ArticlemodifyComponent } from './components/articlemodify/articlemodify.component';
import { GenremodifyComponent } from './components/genremodify/genremodify.component';
import { GenremodifyconfirmComponent } from './components/genremodifyconfirm/genremodifyconfirm.component';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { LibrarianComponent } from './components/librarian/librarian.component';
import { BrowseComponent } from './components/browse/browse.component';
import { ArticleDetailsComponent } from './components/article-details/article-details.component';

//ROUTES
const routes: Routes = [
  {path: '', redirectTo: '/shelf', pathMatch: 'full' },
  {path: 'shelf', component: ShelfComponent},
  {path: 'librarian', component: LibrarianComponent},
  {path: 'form/article', component: ArticleformComponent},
  {path: 'form/genre', component: GenreformComponent},
  {path: 'modify/article/:id', component: ArticlemodifyComponent},
  {path: 'modify/genre', component: GenremodifyComponent},
  {path: 'modify/genre/:id', component: GenremodifyconfirmComponent},
  {path: 'shelf/details', component:ArticleDetailsComponent}
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
    BrowseComponent,
    ArticleDetailsComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes),
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
