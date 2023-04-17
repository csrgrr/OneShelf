import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UploadService {

  private SERVER_URL = "http://localhost:5000/upload";

  constructor(private httpClient: HttpClient) { }

  public uploadFile(file: File) {
    const formData = new FormData();
    formData.append('file', file);
    return this.httpClient.post<any>(this.SERVER_URL, formData);
  }
}
